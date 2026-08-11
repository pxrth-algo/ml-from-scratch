# Linear Regression From Scratch

A from-scratch implementation of Linear Regression using Python, NumPy, and Pandas. The goal of this project is to understand the mathematics and implementation of Linear Regression instead of using a library such as Scikit-learn.

## Dataset

A small Naruto-themed dataset is used for experimentation.

Features:
- Training Hours
- Chakra

Target:
- Missions Completed

Example:

| Shinobi | Training Hours | Chakra | Missions |
|---|---:|---:|---:|
| Naruto | 1 | 40 | 5 |
| Sasuke | 2 | 50 | 7 |
| Sakura | 3 | 35 | 8 |
| Kakashi | 4 | 80 | 10 |
| Rock Lee | 5 | 70 | 12 |

## Model

For multiple features, Linear Regression predicts:

\[
\hat{y} = w_1x_1 + w_2x_2 + b
\]

In matrix form:

\[
\hat{y} = Xw + b
\]

The model learns the weights and bias from the training data.

## Cost Function

The model uses Mean Squared Error with a factor of \(1/2\):

\[
J(w,b)=\frac{1}{2m}\sum_{i=1}^{m}(\hat{y}_i-y_i)^2
\]

The objective is to minimize this cost.

## Gradient Descent

The model is trained using Gradient Descent.

Weight gradient:

\[
\frac{\partial J}{\partial w}
=
\frac{1}{m}X^T(\hat{y}-y)
\]

Bias gradient:

\[
\frac{\partial J}{\partial b}
=
\frac{1}{m}\sum(\hat{y}-y)
\]

Parameter updates:

\[
w \leftarrow w-\alpha\frac{\partial J}{\partial w}
\]

\[
b \leftarrow b-\alpha\frac{\partial J}{\partial b}
\]

where \(\alpha\) is the learning rate.

The process is repeated for a fixed number of epochs.

## Vectorized Implementation

NumPy is used to perform calculations on the complete dataset at once.

Prediction:
<img width="527" height="241" alt="image" src="https://github.com/user-attachments/assets/efb623e3-db1b-4425-be0a-8dafbaed16ad" />


```python
y_pred = np.dot(X, self.weights) + self.bias
