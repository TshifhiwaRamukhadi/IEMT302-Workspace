### Rain Forecasting in C# (ML.NET)

#### Prerequisites
- .NET SDK 8.0+ installed

#### Setup
```bash
cd rain_forecast_model_cs
 dotnet new console -n RainForecast -o .
 dotnet add package Microsoft.ML --version 3.0.1
 dotnet add package Microsoft.ML.FastTree --version 3.0.1
```

#### Run training and prediction
- Build and run the console app (includes training and a sample prediction).
```bash
 dotnet build
 dotnet run -- --temperature 23 --humidity 82 --wind 22 --pressure 1003
```

Data is read from `Data/weather_samples.csv`, model saved to `Models/model.zip`.