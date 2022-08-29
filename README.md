<p align="center">
<img src="doc/logo.png" width="350">
</p>

<div align="center">
    <a href="https://badge.fury.io/for/py/losshub"><img src="https://badge.fury.io/py/losshub.svg" alt="pypi version"></a>
</div>

<p align="center">
    Classification Loss Function Library.
</p>

## Loss Functions for Image Classification

Rmse: $$\sqrt{(1/n) \sum_{i=1}^n (y_i - y')^2}$$
Mse: $$\frac{1}{n} \sum_{i=1}^n (y_i - y')^2$$

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