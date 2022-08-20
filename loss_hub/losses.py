def Mse(y_true, y_pred):
    """
    Mean Squared Error (MSE) is the mean of the squared errors.
    Math: MSE = 1/n * sum( (y_true - y_pred)^2 )
    Args:
        y_true: ground truth values [numpy array]
        y_pred: predicted values [numpy array]
    Returns:

    """
    sums = 0
    for i in range(0,len(y_true)):
        squared_difference = (y_true[i] - y_pred[i]) ** 2
        sums = sums + squared_difference
    
    mean_squared_error = sums / len(y_true)
    return mean_squared_error
