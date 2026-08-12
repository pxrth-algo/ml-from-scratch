# Multiple Linear Regression with Haikyuu Dataset

A simple machine learning project implementing **Multiple Linear Regression using Scikit-learn**.

The model predicts a Haikyuu player's **Overall rating** based on four player attributes:

* Attack
* Defense
* Speed
* Jump

## Project Structure

```text
multiple-linear-regression/
├── haikyu_players.csv
└── multiple_linear_regression.ipynb
```

## Dataset

The dataset contains fictional/example ratings for Haikyuu players.

| Feature | Description             |
| ------- | ----------------------- |
| Attack  | Player's attack rating  |
| Defense | Player's defense rating |
| Speed   | Player's speed rating   |
| Jump    | Player's jump rating    |
| Overall | Target rating           |

## Workflow

The notebook follows a standard regression workflow:

1. Load the dataset using Pandas
2. Separate features (`X`) and target (`y`)
3. Split the dataset into training and testing sets
4. Create a `LinearRegression` model using Scikit-learn
5. Train the model
6. Generate predictions
7. Evaluate the model using:

   * Mean Squared Error (MSE)
   * R² Score
8. Inspect learned coefficients and intercept
9. Predict the Overall rating of a new player
10. Visualize actual vs predicted values

## Model

The model learns the relationship:

```text
Overall = β₀ + β₁(Attack) + β₂(Defense) + β₃(Speed) + β₄(Jump)
```

where the coefficients are learned automatically during training.

## Libraries Used

```text
Python
Pandas
NumPy
Scikit-learn
Matplotlib
```

## Purpose

This project is part of my **ML from Scratch / Machine Learning learning journey**.

The goal is to understand the complete machine learning workflow by building models, understanding the mathematics behind them, and then implementing the same algorithms using established libraries such as Scikit-learn.

## Next Steps

* Expand the dataset
* Compare predictions with the actual values
* Experiment with feature scaling
* Try Polynomial Regression
* Explore Ridge and Lasso Regression
* Compare the Scikit-learn implementation with a from-scratch implementation
* Experiment with cross-validation

## Note

The Haikyuu player ratings are fictional and are used only for learning and experimentation.
