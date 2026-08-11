import pandas as pd

from linear_regression import LinearRegression


df = pd.read_csv("shinobi.csv")

X = df[["Training_Hours", "Chakra"]].values
y = df["Missions"].values


model = LinearRegression(
    learning_rate=0.0001,
    epochs=10000
)

model.fit(X, y)


print("Weights:", model.weights)
print("Bias:", model.bias)

print("\nPredictions:")
print(model.predict(X))

print("\nActual:")
print(y)

print("\nFinal Cost:")
print(model.cost_history[-1])