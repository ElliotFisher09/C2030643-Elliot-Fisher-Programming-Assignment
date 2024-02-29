import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import random

# Load the Olivetti people dataset
olivetti_faces = datasets.fetch_olivetti_faces()
data = olivetti_faces.data  
images = olivetti_faces.images  
target = olivetti_faces.target  

# Split the data into training and testing sets
train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

# Display a grid of sample images from the training data and their labels
def display_sample_images(data, target, num_samples=9):
    plt.figure(figsize=(10, 10))
    random_indices = np.random.choice(len(train_data), size=min(num_samples, len(train_data)), replace=False)
    for i, idx in enumerate(random_indices):
        plt.subplot(3, 3, i + 1)
        plt.imshow(train_data[idx].reshape((64, 64)), cmap=plt.cm.gray)
        plt.title(f"Label: {target[idx]}")
        plt.axis('off')
    plt.suptitle("Training Images with Label")
    plt.show()

# Train a Multi-layer Perceptron classifier
scaler = StandardScaler()
train_data_scaled = scaler.fit_transform(train_data)
model = MLPClassifier(hidden_layer_sizes=(1000, 1000))
model.fit(train_data_scaled, train_target)

# Display a grid of sample images from the testing data along with their true labels and predictions
def display_sample_predictions(test_data, test_target, model, scaler, num_samples=10):
    plt.figure(figsize=(12, 8))
    test_random_indices = random.sample(range(len(test_data)), min(num_samples, len(test_data)))
    for i, idx in enumerate(test_random_indices):
        plt.subplot(2, 5, i + 1)
        plt.imshow(test_data[idx].reshape((64, 64)), cmap=plt.cm.gray)
        test_data_scaled = scaler.transform([test_data[idx]])
        prediction = model.predict(test_data_scaled)[0]
        plt.title(f"Prediction: {prediction}\nActual Label: {test_target[idx]}")
        plt.axis('off')
    plt.suptitle("Images with Label Predictions")
    plt.show()

# Display the confusion matrix for the testing data
def display_confusion_matrix(test_target, predictions):
    cm = ConfusionMatrixDisplay.from_predictions(test_target, predictions, xticks_rotation='vertical', cmap='Blues')
    cm.ax_.set_title('Confusion Matrix')
    plt.show()

# Get predictions for the testing data
test_data_scaled = scaler.transform(test_data)
predictions = model.predict(test_data_scaled)

# Display sample images, predictions, and confusion matrix
display_sample_images(train_data, train_target)
display_sample_predictions(test_data, test_target, model, scaler)
display_confusion_matrix(test_target, predictions)
