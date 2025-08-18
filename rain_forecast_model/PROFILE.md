## Rain Prediction Model Profile

- **Goal**: Predict whether it will rain today based on current weather conditions.

- **Features (Inputs)**:
  - TemperatureC (°C)
  - HumidityPct (%)
  - WindSpeedKmh (km/h)
  - PressureHpa (hPa)

- **Label (Output)**:
  - Rain (Binary): Yes = 1, No = 0 (stored as Yes/No in data)

- **Training Data**:
  - Located at `data/weather_samples.csv`
  - Columns: TemperatureC, HumidityPct, WindSpeedKmh, PressureHpa, Rain

- **Observations**:
  - High humidity (≥70%) + low pressure (<1005 hPa) → Likely Rain
  - Low humidity (≤55%) + high pressure (>1015 hPa) → Likely No Rain
  - Stronger winds can accompany rainy conditions

- **Model**:
  - Logistic Regression in a `scikit-learn` pipeline with `StandardScaler`
  - Saved to `models/model.joblib`

- **Usage**:
  - Train: `python -m src.train --data data/weather_samples.csv`
  - Predict: `python -m src.predict --temperature 23 --humidity 82 --wind_speed 22 --pressure 1003`