using System;
using System.Globalization;
using Microsoft.ML;
using Microsoft.ML.Data;

namespace RainForecast
{
    public class WeatherData
    {
        [LoadColumn(0)] public float TemperatureC { get; set; }
        [LoadColumn(1)] public float HumidityPct { get; set; }
        [LoadColumn(2)] public float WindSpeedKmh { get; set; }
        [LoadColumn(3)] public float PressureHpa { get; set; }
        [LoadColumn(4), ColumnName("Label")] public bool Label { get; set; }
    }

    public class WeatherPrediction
    {
        [ColumnName("PredictedLabel")] public bool WillRain { get; set; }
        public float Probability { get; set; }
        public float Score { get; set; }
    }

    public class Program
    {
        private const string DataPath = "/workspace/rain_forecast_model_cs/Data/weather_samples.csv";
        private const string ModelPath = "/workspace/rain_forecast_model_cs/Models/model.zip";

        public static void Main(string[] args)
        {
            var mlContext = new MLContext(seed: 42);

            // Load data
            var data = mlContext.Data.LoadFromTextFile<WeatherData>(
                path: DataPath,
                hasHeader: true,
                separatorChar: ',');

            // Build pipeline
            var pipeline = mlContext.Transforms.Concatenate(
                    "Features",
                    nameof(WeatherData.TemperatureC),
                    nameof(WeatherData.HumidityPct),
                    nameof(WeatherData.WindSpeedKmh),
                    nameof(WeatherData.PressureHpa))
                .Append(mlContext.BinaryClassification.Trainers.FastForest());

            // Train
            Console.WriteLine("Training model...");
            var model = pipeline.Fit(data);

            // Evaluate on training (small sample)
            var predictions = model.Transform(data);
            var metrics = mlContext.BinaryClassification.Evaluate(predictions);
            Console.WriteLine($"Accuracy: {metrics.Accuracy:P2}, AUC: {metrics.AreaUnderRocCurve:P2}");

            // Save model
            mlContext.Model.Save(model, data.Schema, ModelPath);
            Console.WriteLine($"Model saved to: {ModelPath}");

            // Parse CLI args for a prediction
            float temp = GetArg(args, "--temperature", 23f);
            float humidity = GetArg(args, "--humidity", 82f);
            float wind = GetArg(args, "--wind", 22f);
            float pressure = GetArg(args, "--pressure", 1003f);

            var engine = mlContext.Model.CreatePredictionEngine<WeatherData, WeatherPrediction>(model);
            var sample = new WeatherData
            {
                TemperatureC = temp,
                HumidityPct = humidity,
                WindSpeedKmh = wind,
                PressureHpa = pressure
            };
            var result = engine.Predict(sample);
            Console.WriteLine($"Prediction: {(result.WillRain ? "Yes" : "No")}, Probability: {result.Probability:F4}");
        }

        private static float GetArg(string[] args, string name, float defaultValue)
        {
            for (int i = 0; i < args.Length - 1; i++)
            {
                if (string.Equals(args[i], name, StringComparison.OrdinalIgnoreCase))
                {
                    if (float.TryParse(args[i + 1], NumberStyles.Float, CultureInfo.InvariantCulture, out var value))
                    {
                        return value;
                    }
                }
            }
            return defaultValue;
        }
    }
}