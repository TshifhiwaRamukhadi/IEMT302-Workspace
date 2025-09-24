Minimal Machine Learning Example (NumPy Linear Regression)

Overview
This folder contains the simplest useful example of machine learning: fitting a straight line to data using ordinary least squares (closed-form linear regression). We learn parameters weight w and bias b such that y ≈ w·x + b.

What the code does
- Generates synthetic points with a known rule y = 3x + 2 plus small Gaussian noise
- Builds a design matrix X = [1, x] and solves the normal equation theta = (X^T X)^{-1} X^T y
- Reports learned parameters, mean squared error, and makes predictions for a few new inputs

Why this is ML
We do not hard-code w and b. The algorithm infers them from examples (x, y). This is supervised learning because we provide both inputs and target outputs.

Files
- linear_regression_numpy.py: Self-contained script implementing the above steps
- requirements.txt: Python packages required to run the example
- .gitignore: Standard Python ignores for cleanliness

Setup
1) Create and activate a virtual environment (recommended)
   Windows (PowerShell):
   python -m venv .venv; .\.venv\Scripts\Activate.ps1

2) Install dependencies
   pip install -r requirements.txt

Run the example
python ml_minimal/linear_regression_numpy.py

Expected output (example)
Learned parameters:
  weight w = ~3.0
  bias   b = ~2.0

Training MSE: small positive value

Predictions for new inputs:
  x =  -2.0 -> y_hat ≈ -4
  x =   0.0 -> y_hat ≈  2
  x =   2.0 -> y_hat ≈  8

How to explain it in plain English
- We start with points scattered around an unknown straight line
- We choose w (slope) and b (intercept) to minimize the average squared vertical distance to those points
- The normal equation gives a direct formula for w and b that achieves this minimum under standard assumptions
- After learning w and b, we can predict y for any new x using y_hat = w·x + b

Troubleshooting
- If NumPy is missing: run pip install -r requirements.txt
- If the command python is not found on Windows, try py instead of python

