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
    sums = 0
    for i in range(0,len(y_true)):
        squared_difference = (y_true[i] - y_pred[i]) ** 2
        sums = sums + squared_difference
    
    mean_squared_error = sums / len(y_true)
    return mean_squared_error
   

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
    sums = 0
    for i in range(0,len(y_true)):
        squared_difference = (y_true[i] - y_pred[i]) ** 2
        sums = sums + squared_difference
        
    mean_squared_error = sums / len(y_true)
    return mean_squared_error ** 0.5
