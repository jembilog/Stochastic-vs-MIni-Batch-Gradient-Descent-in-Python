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
learning_rate = 0.005
epochs = 1000
batch_size = 5
mse_history = []

for epoch in range(epochs):
    indices = np.arange(n)
    np.random.shuffle(indices)

    X_shuffled = screen_time[indices]
    Y_shuffled = battery_used[indices]

    for i in range(0,n,batch_size):
        X_batch = X_shuffled[i:i+batch_size]
        Y_batch = Y_shuffled[i:i+batch_size]

        Y_pred_batch = w * X_batch + b

        dw = (-2/ len(X_batch)) * np.sum(X_batch * (Y_batch - Y_pred_batch))
        db = (-2/len(X_batch)) * np.sum(Y_batch - Y_pred_batch)

        w -= learning_rate * dw
        b -= learning_rate * db

    Y_pred_all = w * screen_time + b
    mse = np.mean((battery_used - Y_pred_all) ** 2)
    mse_history.append(mse)

    if(epoch + 1) % 50 == 0:
        print(mse)

Y_prediction = w * 10 + b
print(Y_prediction)
plt.plot(mse_history)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid(True)
plt.show()
