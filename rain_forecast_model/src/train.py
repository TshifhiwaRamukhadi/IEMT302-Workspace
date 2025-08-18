import argparse
import pathlib
from typing import Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from config import FEATURE_COLUMNS, LABEL_COLUMN, MODEL_PATH


def load_dataset(csv_path: str) -> pd.DataFrame:
    dataframe = pd.read_csv(csv_path)
    if LABEL_COLUMN not in dataframe.columns:
        raise ValueError(f"Label column '{LABEL_COLUMN}' not found in dataset")
    missing_features = [c for c in FEATURE_COLUMNS if c not in dataframe.columns]
    if missing_features:
        raise ValueError(f"Missing feature columns: {missing_features}")
    return dataframe


def prepare_features_and_labels(dataframe: pd.DataFrame) -> Tuple[pd.DataFrame, np.ndarray]:
    label_series = (
        dataframe[LABEL_COLUMN]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"yes": 1, "no": 0})
    )
    if label_series.isna().any():
        raise ValueError("Label values must be 'Yes' or 'No' (case-insensitive). Found others.")
    X = dataframe[FEATURE_COLUMNS]
    y = label_series.values.astype(int)
    return X, y


def build_pipeline() -> Pipeline:
    preprocess = ColumnTransformer(
        transformers=[
            ("scale", StandardScaler(), FEATURE_COLUMNS),
        ],
        remainder="drop",
    )
    model = LogisticRegression(max_iter=1000, solver="lbfgs")
    pipeline = Pipeline(
        steps=[
            ("preprocess", preprocess),
            ("model", model),
        ]
    )
    return pipeline


def train_and_save_model(csv_path: str, out_path: str) -> None:
    dataframe = load_dataset(csv_path)
    X, y = prepare_features_and_labels(dataframe)
    pipeline = build_pipeline()
    pipeline.fit(X, y)

    predictions = pipeline.predict(X)
    print("Training set classification report:\n")
    print(classification_report(y, predictions, target_names=["No", "Yes"]))

    pathlib.Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, out_path)
    print(f"Model saved to: {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Train a rain prediction model")
    parser.add_argument(
        "--data",
        default="/workspace/rain_forecast_model/data/weather_samples.csv",
        help="Path to CSV dataset",
    )
    parser.add_argument("--out", default=MODEL_PATH, help="Path to save trained model (.joblib)")
    args = parser.parse_args()

    train_and_save_model(args.data, args.out)


if __name__ == "__main__":
    main()