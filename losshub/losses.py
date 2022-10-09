import numpy as np

def mse(y_true, y_pred):
    """
    Mean Squared Error (MSE) is the mean of the squared errors.
    Math: MSE = 1/n * sum( (y_true - y_pred)^2 )
    Args:
        y_true: ground truth values [numpy array]
        y_pred: predicted values [numpy array]
    Returns:
        y_true : [0.1, 0.2, 0.3, 0.4, 0.5]
        y_pred : [0.1, 0.3, 0.3, 0.4, 0.2]
        mse : 1.25
    """
    return np.mean((y_true - y_pred)**2)

def rmse(y_true, y_pred):
    """
    Root Mean Squared Error (RMSE) is the square root of the mean of the squared errors.
    Math: RMSE = sqrt(1/n * sum( (y_true - y_pred)^2 ))
    Args:
        y_true: ground truth values [numpy array]
        y_pred: predicted values [numpy array]
    Returns:
        y_true : [0.1, 0.2, 0.3, 0.4, 0.5]
        y_pred : [0.1, 0.3, 0.3, 0.4, 0.2]
        rmse : 0.6
    """
    return np.sqrt(np.mean((y_true - y_pred)**2))
