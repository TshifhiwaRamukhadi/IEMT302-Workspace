### Rain Forecasting: Predicting Rain

**Goal**: Predict whether it will rain today based on current weather conditions.

#### Project Structure
- `data/weather_samples.csv`: Sample training data
- `src/config.py`: Feature/label definitions and model path
- `src/train.py`: Train and save the model
- `src/predict.py`: Use the trained model for predictions
- `models/`: Trained model artifacts
- `PROFILE.md`: Model profile (features, label, data, observations, usage)
- `requirements.txt`: Python dependencies

#### Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

#### Train
```bash
python -m src.train --data data/weather_samples.csv --out models/model.joblib
```

#### Predict (example)
```bash
python -m src.predict --temperature 23 --humidity 82 --wind_speed 22 --pressure 1003
```

Expected output (example):
```bash
{'prediction': 'Yes', 'confidence': 0.9, 'features': {'TemperatureC': 23.0, 'HumidityPct': 82.0, 'WindSpeedKmh': 22.0, 'PressureHpa': 1003.0}}
```

#### Notes
- Labels in the CSV are `Yes/No`; the training script maps them to 1/0 internally.
- The simple dataset is illustrative; for real use, expand with more historical records.