import numpy as np
import matplotlib.pyplot as plt
screen_time = np.array([
    3.6, 7.7, 6.1, 5.2, 2.1, 2.1, 1.4, 7.1, 5.2, 6.0,
    1.1, 7.8, 6.8, 2.5, 2.3, 2.3, 3.1, 4.7, 4.0, 3.0
])

battery_used = np.array([
    43.0, 94.0, 72.0, 61.0, 34.0, 28.0, 21.0, 82.0, 63.0, 74.0,
    14.0, 96.0, 81.0, 33.0, 30.0, 37.0, 41.0, 56.0, 53.0, 36.0
])

w = 0 
b = 0 
n = len(screen_time)
learning_rate = 0.01
epochs = 500
mse_history = []

for epoch in range(epochs):
    indices =np.arange(n)
    np.random.shuffle(indices)

    for i in indices:
        x_i = screen_time[i]
        y_i = battery_used[i]

        y_pred_i = w * x_i + b

        dw = -2 * x_i * (y_i - y_pred_i)
        db = -2 * (y_i - y_pred_i)

        w -= learning_rate * dw
        b -= learning_rate * db

    Y_pred = w * screen_time + b
    mse = np.mean((battery_used - Y_pred) ** 2)
    mse_history.append(mse)

    if(epoch + 1) % 50 == 0:
       print(
            f"Epoch: {epoch + 1} | "
            f"MSE: {mse:.4f} | "
            f"w: {w:.4f} | "
            f"b: {b:.4f} | "
            f"Predicted value: {Y_pred}"
        )
       
prediction = w * 10 + b
plt.plot(mse_history)
plt.title("Error minimization")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid(True)
print(prediction)
plt.show()
