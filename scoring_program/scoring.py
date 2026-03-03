import json
from pathlib import Path
from sklearn.metrics import recall_score

import pandas as pd

EVAL_SETS = ["test", "private_test"]

# --- Scoring constants ---
MODEL_SIZE_THRESHOLD_MB = 20.0   # Models at or below this score 1.0; above score 0.0
TIME_THRESHOLD_SECONDS = 60.0    # Reference time cap 

# Within each performance third: 50% time, 50% recall
TIME_WEIGHT = 0.5
METRIC_WEIGHT = 0.5

# Final score weights (each third = 1/3)
SIZE_WEIGHT = 1 / 3
TRAIN_WEIGHT = 1 / 3
PRIVATE_WEIGHT = 1 / 3


def compute_recall(predictions, targets):
    # Make sure there is no NaN, as pandas ignores them in mean computation
    predictions = predictions.replace({-1: 0}).fillna(0).values
    targets = targets.replace({-1: 0}).values.ravel()
    return float(recall_score(targets, predictions, zero_division=0))

def score_model_size(size_mb):
    """
    Score model size between 0 and 1.
    Models <= threshold get 1.0; larger models are penalised linearly,
    hitting 0.0 at double the threshold.
    """
    if size_mb <= MODEL_SIZE_THRESHOLD_MB:
        return 1.0
    elif size_mb >= 2 * MODEL_SIZE_THRESHOLD_MB:
        return 0.0
    else:
        return 1.0 - (size_mb - MODEL_SIZE_THRESHOLD_MB) / MODEL_SIZE_THRESHOLD_MB

def score_time(elapsed_seconds):
    return max(0.0, 1.0 - elapsed_seconds / TIME_THRESHOLD_SECONDS)

def score_performance_third(recall, elapsed_seconds):
    """Combine time score and recall into a single third (50/50)."""
    return TIME_WEIGHT * score_time(elapsed_seconds) + METRIC_WEIGHT * recall


def main(reference_dir, prediction_dir, output_dir):
    scores = {}
    durations = json.loads((prediction_dir / "metadata.json").read_text())
    model_size_mb = durations["model_size_mb"]

       # --- Third 1: Model size ---
    size_score = score_model_size(model_size_mb)
    scores["size_score"] = size_score
    scores["model_size_mb"] = model_size_mb
    print(f"Model size: {model_size_mb:.2f} MB  →  size_score: {size_score:.4f}")

    # --- Thirds 2 & 3: Performance on train eval set and private test ---
    eval_scores = {}
    for eval_set in EVAL_SETS:
        print(f"Scoring {eval_set}")
        predictions = pd.read_csv(prediction_dir / f"{eval_set}_predictions.csv")
        targets = pd.read_csv(reference_dir / f"{eval_set}_labels.csv")

        recall = compute_recall(predictions, targets)
        elapsed = durations.get(f"{eval_set}_prediction_time", 0.0)
        perf_score = score_performance_third(recall, elapsed)

        scores[f"{eval_set}_recall"] = recall
        scores[f"{eval_set}_prediction_time"] = elapsed
        scores[f"{eval_set}_score"] = perf_score
        eval_scores[eval_set] = perf_score

        print(f"  recall={recall:.4f}, time={elapsed:.2f}s  →  {eval_set}_score: {perf_score:.4f}")

    # --- Final combined score ---
    final_score = (
        SIZE_WEIGHT * size_score
        + TRAIN_WEIGHT * eval_scores["test"]
        + PRIVATE_WEIGHT * eval_scores["private_test"]
    )
    scores["final_score"] = final_score
    print(f"\nFinal score: {final_score:.4f}")

    # Write output scores
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / 'scores.json').write_text(json.dumps(scores, indent=2))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Scoring program for codabench"
    )
    parser.add_argument(
        "--reference-dir",
        type=str,
        default="/app/input/ref",
        help="",
    )
    parser.add_argument(
        "--prediction-dir",
        type=str,
        default="/app/input/res",
        help="",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="/app/output",
        help="",
    )

    args = parser.parse_args()

    main(
        Path(args.reference_dir),
        Path(args.prediction_dir),
        Path(args.output_dir)
    )
