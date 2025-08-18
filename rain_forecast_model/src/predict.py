import argparse
import joblib
import numpy as np
from config import FEATURE_COLUMNS, MODEL_PATH, CLASS_LABELS


def predict_rain(
    temperature_c: float,
    humidity_pct: float,
    wind_speed_kmh: float,
    pressure_hpa: float,
    model_path: str = MODEL_PATH,
):
    pipeline = joblib.load(model_path)
    features = np.array([[temperature_c, humidity_pct, wind_speed_kmh, pressure_hpa]])
    probabilities = pipeline.predict_proba(features)[0]
    prediction = int(np.argmax(probabilities))
    label = CLASS_LABELS[prediction]
    confidence = float(probabilities[prediction])
    return label, confidence


def main():
    parser = argparse.ArgumentParser(
        description="Predict whether it will rain today based on current weather conditions"
    )
    parser.add_argument("--temperature", type=float, required=True, help="Temperature in °C")
    parser.add_argument("--humidity", type=float, required=True, help="Humidity in %")
    parser.add_argument("--wind_speed", type=float, required=True, help="Wind speed in km/h")
    parser.add_argument("--pressure", type=float, required=True, help="Pressure in hPa")
    parser.add_argument(
        "--model", type=str, default=MODEL_PATH, help="Path to the trained model (.joblib)"
    )
    args = parser.parse_args()

    label, confidence = predict_rain(
        temperature_c=args.temperature,
        humidity_pct=args.humidity,
        wind_speed_kmh=args.wind_speed,
        pressure_hpa=args.pressure,
        model_path=args.model,
    )
    print(
        {
            "prediction": label,
            "confidence": round(confidence, 4),
            "features": {
                "TemperatureC": args.temperature,
                "HumidityPct": args.humidity,
                "WindSpeedKmh": args.wind_speed,
                "PressureHpa": args.pressure,
            },
        }
    )


if __name__ == "__main__":
    main()