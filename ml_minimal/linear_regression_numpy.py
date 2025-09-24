import numpy as np


def generate_synthetic_linear_data(num_samples: int = 100, noise_std: float = 1.0, random_seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate synthetic linear data following y = 3x + 2 + noise.

    Returns:
        features_x: shape (num_samples,)
        targets_y: shape (num_samples,)
    """
    rng = np.random.default_rng(random_seed)
    features_x = rng.uniform(low=-5.0, high=5.0, size=num_samples)
    noise = rng.normal(loc=0.0, scale=noise_std, size=num_samples)
    targets_y = 3.0 * features_x + 2.0 + noise
    return features_x, targets_y


def fit_simple_linear_regression_closed_form(features_x: np.ndarray, targets_y: np.ndarray) -> tuple[float, float]:
    """
    Fit y = w * x + b using the closed-form least squares solution.

    We solve for theta = [b, w]^T using normal equation:
        theta = (X^T X)^{-1} X^T y
    where X = [[1, x_i] for each sample].

    Returns:
        bias_b, weight_w
    """
    # Ensure shapes are correct
    x_column = features_x.reshape(-1, 1)
    ones_column = np.ones_like(x_column)
    design_matrix = np.hstack([ones_column, x_column])  # shape: (n, 2)

    # Normal equation
    xtx = design_matrix.T @ design_matrix
    xty = design_matrix.T @ targets_y
    theta = np.linalg.inv(xtx) @ xty  # shape: (2,)

    bias_b = float(theta[0])
    weight_w = float(theta[1])
    return bias_b, weight_w


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


def main() -> None:
    # 1) Create a tiny dataset with a known underlying rule
    x, y = generate_synthetic_linear_data(num_samples=80, noise_std=0.8, random_seed=7)

    # 2) Fit a linear model y ≈ w*x + b using least squares (a fundamental ML method)
    b, w = fit_simple_linear_regression_closed_form(x, y)

    # 3) Evaluate fit quality via Mean Squared Error
    y_hat = w * x + b
    mse = mean_squared_error(y, y_hat)

    # 4) Make a simple prediction
    new_x = np.array([-2.0, 0.0, 2.0])
    new_y_hat = w * new_x + b

    print("Learned parameters:")
    print(f"  weight w = {w:.4f}")
    print(f"  bias   b = {b:.4f}")
    print()
    print(f"Training MSE: {mse:.4f}")
    print()
    print("Predictions for new inputs:")
    for value, pred in zip(new_x, new_y_hat):
        print(f"  x = {value:>5.1f} -> y_hat = {pred:>7.3f}")


if __name__ == "__main__":
    main()


