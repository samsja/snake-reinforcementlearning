import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import prime

print("youpi")

n = 2

base = 10

targets_prime = np.array(prime.crible(base**n -1))
number_inputs = np.zeros((len(targets_prime),n))

print(len(targets_prime))
print(len(number_inputs))

for i in range(len(targets_prime)):
     decompo = prime.decompoNbaseB(i) #invert
     for j in range(len(decompo)):
         number_inputs[i-1,j] = decompo[j]

print(number_inputs)



# Flatten
model = tf.keras.models.Sequential()

# Add the layers
model.add(tf.keras.layers.Dense(30, activation="sigmoid"))
model.add(tf.keras.layers.Dense(30, activation="sigmoid"))
model.add(tf.keras.layers.Dense(2, activation="softmax"))

model.predict(number_inputs[0:1])

model.summary()

# Compile the model
model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer="sgd",
    metrics=["accuracy"]
)

history = model.fit(number_inputs, targets_prime, epochs=50, validation_split=0)

#test

input = number_inputs[3:4]
model_output = model.predict(input)

print(input)
print(model_output)


#show

loss_curve = history.history["loss"]
acc_curve = history.history["accuracy"]

#loss_val_curve = history.history["val_loss"]
#acc_val_curve = history.history["val_accuracy"]


plt.subplot(2, 1, 1)
plt.plot(loss_curve, label="Train")
#plt.plot(loss_val_curve, label="Val")
plt.legend(loc='upper left')
plt.title("Loss")

plt.subplot(2, 1, 2)
plt.plot(acc_curve, label="Train")
#plt.plot(acc_val_curve, label="Val")
plt.legend(loc='upper left')
plt.title("Accuracy")
plt.show()
