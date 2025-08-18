FEATURE_COLUMNS = [
    "TemperatureC",
    "HumidityPct",
    "WindSpeedKmh",
    "PressureHpa",
]

LABEL_COLUMN = "Rain"

MODEL_PATH = "/workspace/rain_forecast_model/models/model.joblib"

CLASS_LABELS = {0: "No", 1: "Yes"}