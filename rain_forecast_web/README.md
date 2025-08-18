### Rain Forecasting: HTML/JS Demo

Open `index.html` in your browser. No build step required.

#### What it does
- Input features: Temperature (°C), Humidity (%), Wind Speed (km/h), Pressure (hPa)
- Predicts Rain = Yes/No using a simple rule-based model derived from your sample patterns:
  - High humidity (≥70%) + low pressure (<1005) → Rain likely
  - Low humidity (≤55%) + high pressure (>1015) → No Rain likely
  - Stronger winds can increase rain likelihood
  - Temperature provides a small adjustment

#### Files
- `index.html`: UI for inputs and results
- `assets/styles.css`: Layout and styling
- `assets/app.js`: Prediction logic and rendering of the sample dataset
- `Data/weather_samples.csv`: Sample dataset mirrored in app.js for display

You can expand the rules or replace them with a small on-device ML model later (e.g., TensorFlow.js) if needed.