<p align="center">
<img src="doc/logo.png" width="450">
</p>
<p align="center"> LossHub: Loss Functions Library for Image Classification and Detection</p>
<div align="center">
    <a href="https://badge.fury.io/for/py/losshub"><img src="https://badge.fury.io/py/losshub.svg" alt="pypi version"></a>
    <a href="[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/kadirnar)"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue.svg" alt="hugging face spaces"></a>
    <a href="[![Medium](https://img.shields.io/badge/Medium-Blog-red)](https://medium.com/@kadir.nar)"><img src="https://img.shields.io/badge/%20Medium%20-Blog-blue.svg" alt="medium"></a>

</div>

## Loss Functions for Image Classification

Rmse: It is a frequently used measure of the differences between values (sample or population values) predicted by a model or an estimator and the values observed. 
### $$\text{rmse}(x,y) = \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i - y_i)^2}$$
Mse: In statistics, the mean squared error or mean squared deviation of an estimator (of a procedure for estimating an unobserved quantity) measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value. 
### $$\text{mse}(x,y) = \frac{1}{n} \sum_{i=1}^n (x_i - y_i)^2$$


## Installation
```bash
pip install losshub
```

## Usage
```python
from losshub.losses import mse, rmse
# outputs and labels
y_true = [1, 2, 3, 4, 5]
y_pred = [1, 2, 3, 4, 5]
# mse
mse(y_true, y_pred)
# rmse
rmse(y_true, y_pred)
```

## References
- [Balanced-Loss](https://github.com/fcakyon/balanced-loss/)
- [Rmse](https://en.wikipedia.org/wiki/Root_mean_squared_error)
- [Mse](https://en.wikipedia.org/wiki/Mean_squared_error)
