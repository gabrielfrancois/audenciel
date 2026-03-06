# Script to download the data from a given source and create the splits
# This is a mock version that generate fake problems
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Directory configuration
PHASE = "dev_phase"
DATA_DIR = Path(PHASE) / "input_data"
REF_DIR = Path(PHASE) / "reference_data"

RAW_DATA_PATH = Path("dev_phase") / "raw_data"


def clean_time_string(time_str):
    """Standardize timestamp strings."""
    if pd.isna(time_str):
        return time_str
    if time_str.endswith(":"):
        return time_str + "00"
    if len(time_str) == 13:
        return time_str + ":00:00"
    if len(time_str) == 16:
        return time_str + ":00"
    return time_str


def load_and_prepare(name, filename, house_id):
    """Load, clean and prepare features from raw house data."""
    print(f"Loading {name}...")
    df = pd.read_csv(RAW_DATA_PATH / filename)

    # Datetime conversion
    df["time"] = df["time"].apply(clean_time_string)
    df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
    if df["time"].isnull().any() and "unix" in df.columns:
        df["time"] = pd.to_datetime(df["unix"], unit="s")

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["dayofweek"] = df["date"].dt.dayofweek
    
    df = df.drop(columns=["date"])

    df["house_id"] = house_id

    # Anomaly type column naming normalization
    type_col = (
        "type_defaut_fridge_freezzer"
        if "type_defaut_fridge_freezzer" in df.columns
        else "type_defaut_Fridge_Freezer"
    )
    if type_col in df.columns:
        df = df.rename(columns={type_col: "anomaly_type"})
    else:
        df["anomaly_type"] = 0

    if "anomaly" not in df.columns:
        df["anomaly"] = 0

    # Calculate energy gap baseline for Task 2
    normal_mask = df["anomaly"] == 0
    baseline = df.loc[normal_mask, "fridge freezer"].mean() if normal_mask.any() else 0
    df["energy_gap"] = df["fridge freezer"] - baseline

    return df[["unix", "time", "aggregate", "house_id", "anomaly"]]


def make_csv(data, filepath):
    """Helper to save CSV and create parent directories."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(filepath, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup competition data splits")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    # Raw files configuration
    files = [
        ("H2", "df_H2_fridge_freezer_normal.csv", 2),
        ("H3_N", "df_H3_fridge_freezer_normal.csv", 3),
        ("H9_N", "df_h9_fridge_freezer_normal.csv", 9),
        ("H15", "df_H15_fridge_freezer_normal.csv", 15),
        ("H3_A", "house3_anotated.csv", 3),
        ("H9_A", "house9_anotated_corrrige.csv", 9),
    ]

    all_data = [load_and_prepare(n, f, i) for n, f, i in files]
    full_df = pd.concat(all_data).sort_values("unix")

    # Split Normal / Anomalies
    normal_df = full_df[full_df["anomaly"] == 0]
    anom_df = full_df[full_df["anomaly"] == 1]

    # Split Normal: 80% Train / 20% Pool for Tests
    train_normal, test_pool_normal = train_test_split(
        normal_df, train_size=0.8, random_state=args.seed, shuffle=False
    )

    # Create the full evaluation pool (remaining normal + all anomalies)
    full_eval_pool = pd.concat([test_pool_normal, anom_df]).sort_values("unix")

    # Split the pool into Public Test and Private Test (50/50)
    test_df, private_test_df = train_test_split(
        full_eval_pool, test_size=0.5, random_state=args.seed
    )

    # Export mapping
    splits = [
        ("train", train_normal),
        ("test", test_df),
        ("private_test", private_test_df),
    ]

    features_cols = ["unix", "time", "aggregate", "house_id"]
    labels_cols = ["anomaly"]

    for name, df in splits:
        split_dir = DATA_DIR / name
        # Export Features
        make_csv(df[features_cols], split_dir / f"{name}_features.csv")

        # Export Labels (Train is public, Test/Private are hidden in reference_data)
        label_dir = split_dir if name == "train" else REF_DIR
        make_csv(df[labels_cols], label_dir / f"{name}_labels.csv")

    print(
        f"Preparation complete: Train={len(train_normal)}, Test={len(test_df)}, Private={len(private_test_df)}"
    )
