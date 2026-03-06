import json
import sys
import time
from pathlib import Path
import tempfile
import joblib

import pandas as pd


EVAL_SETS = ["test", "private_test"]


def evaluate_model(model, X_test):
    y_pred = model.predict(X_test)
    return pd.DataFrame(y_pred)


def get_train_data(data_dir):
    data_dir = Path(data_dir)
    training_dir = data_dir / "train"
    X_train = pd.read_csv(training_dir / "train_features.csv")
    y_train = pd.read_csv(training_dir / "train_labels.csv")
    return X_train, y_train

def get_model_size_mb(model):
    """measure model size in MB."""
    with tempfile.NamedTemporaryFile(suffix=".joblib", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    joblib.dump(model, tmp_path)
    size_mb = tmp_path.stat().st_size / (1024 * 1024)
    tmp_path.unlink()
    return size_mb

def main(data_dir, output_dir):
    # Here, you can import info from the submission module, to evaluate the
    # submission
    from submission import get_model

    X_train, y_train = get_train_data(data_dir)

    print("Training the model")
    model = get_model()
    start = time.time()
    X_train = X_train.select_dtypes(include=["number"])
    model.fit(X_train, y_train)
    train_time = time.time() - start

    print("Measuring model size")
    model_size_mb = get_model_size_mb(model)
    print(f"Model size: {model_size_mb:.2f} MB")
    print("-" * 10)
    print("Evaluate the model")
    start = time.time()

    res = {}
    prediction_times = {}
    for eval_set in EVAL_SETS:
        X_test = pd.read_csv(data_dir / eval_set / f"{eval_set}_features.csv")
        start = time.time()
        res[eval_set] = evaluate_model(model, X_test)
        prediction_times[eval_set] = time.time() - start
    test_time = time.time() - start
    print("-" * 10)
    total_duration = train_time + sum(prediction_times.values())
    print(f"Completed Prediction. Total duration: {total_duration}")

    # Write output files
    output_dir.mkdir(parents=True, exist_ok=True)
    metadata = dict(
        train_time=train_time,
        model_size_mb=model_size_mb,
        **{f"{eval_set}_prediction_time": t for eval_set, t in prediction_times.items()}
    )
    with open(output_dir / "metadata.json", "w+") as f:
        json.dump(metadata, f)
    for eval_set in EVAL_SETS:
        filepath = output_dir / f"{eval_set}_predictions.csv"
        res[eval_set].to_csv(filepath, index=False)
    print()
    print("Ingestion Program finished. Moving on to scoring")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Ingestion program for codabench"
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default="/app/input_data",
        help="",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="/app/output",
        help="",
    )
    parser.add_argument(
        "--submission-dir",
        type=str,
        default="/app/ingested_program",
        help="",
    )

    args = parser.parse_args()
    sys.path.append(args.submission_dir)
    sys.path.append(Path(__file__).parent.resolve())

    main(Path(args.data_dir), Path(args.output_dir))
