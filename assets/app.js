const SAMPLE_DATA = [
  { TemperatureC: 30, HumidityPct: 45, WindSpeedKmh: 10, PressureHpa: 1015, Rain: "No" },
  { TemperatureC: 24, HumidityPct: 70, WindSpeedKmh: 18, PressureHpa: 1005, Rain: "Yes" },
  { TemperatureC: 28, HumidityPct: 55, WindSpeedKmh: 12, PressureHpa: 1010, Rain: "No" },
  { TemperatureC: 22, HumidityPct: 85, WindSpeedKmh: 20, PressureHpa: 1002, Rain: "Yes" },
  { TemperatureC: 35, HumidityPct: 40, WindSpeedKmh: 15, PressureHpa: 1018, Rain: "No" },
  { TemperatureC: 19, HumidityPct: 90, WindSpeedKmh: 25, PressureHpa: 999,  Rain: "Yes" },
];

function renderTable() {
  const tbody = document.getElementById('data-table');
  tbody.innerHTML = '';
  for (const row of SAMPLE_DATA) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${row.TemperatureC}</td>
      <td>${row.HumidityPct}</td>
      <td>${row.WindSpeedKmh}</td>
      <td>${row.PressureHpa}</td>
      <td>${row.Rain}</td>
    `;
    tbody.appendChild(tr);
  }
}

// Rule-based predictor derived from the patterns provided
function predictRain({ temperature, humidity, wind, pressure }) {
  let score = 0;
  // High humidity + low pressure -> Rain
  if (humidity >= 70) score += 1;
  if (pressure < 1005) score += 1.2;

  // Low humidity + high pressure -> No Rain
  if (humidity <= 55) score -= 1;
  if (pressure > 1015) score -= 1.2;

  // Stronger wind can indicate rain
  if (wind >= 20) score += 0.5;

  // Temperature slight influence
  if (temperature <= 22) score += 0.2; // cooler -> a bit more likely
  if (temperature >= 32) score -= 0.2; // hotter -> a bit less likely

  const willRain = score >= 0.5; // decision threshold
  // map score to a pseudo-confidence (bounded 0.5..0.99)
  const confidence = Math.max(0.5, Math.min(0.99, 0.5 + Math.abs(score) / 3));
  return { label: willRain ? 'Yes' : 'No', confidence: Number(confidence.toFixed(3)) };
}

function handleFormSubmit(event) {
  event.preventDefault();
  const temperature = parseFloat(document.getElementById('temperature').value);
  const humidity = parseFloat(document.getElementById('humidity').value);
  const wind = parseFloat(document.getElementById('wind').value);
  const pressure = parseFloat(document.getElementById('pressure').value);

  const { label, confidence } = predictRain({ temperature, humidity, wind, pressure });
  const result = document.getElementById('result');
  result.textContent = `Prediction: ${label} (confidence: ${confidence})`;
}

window.addEventListener('DOMContentLoaded', () => {
  renderTable();
  document.getElementById('predict-form').addEventListener('submit', handleFormSubmit);
});