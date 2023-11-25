# import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
train_images = train_images / 255.0
test_images = test_images / 255.0
class_names = ['Ankle boot', 'T-shirt/top', 'T-shirt/top', 'Dress', 'T-shirt/top', 'Pullover', 'Sneaker',
               'Pullover', 'Sandal', 'Sandal', 'T-shirt/top', 'Ankle boot', 'Ankle boot', 'Ankle boot',
               'Ankle boot', 'Ankle boot', 'Ankle boot', 'Ankle boot', 'Ankle boot', 'Ankle boot', 'Ankle boot',
               'Ankle boot', 'Ankle boot', 'Ankle boot', 'Ankle boot', 'Ankle boot']
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i])
    plt.xlabel(class_names[train_labels[i]])
plt.show()
