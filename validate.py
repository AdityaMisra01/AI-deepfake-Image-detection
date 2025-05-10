import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load model and threshold
model = tf.keras.models.load_model('ai_image_detector.h5')
threshold = np.load('model_threshold.npy').item()

# Load validation data
val_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory(
    'dataset/val',
    target_size=(64, 64),
    batch_size=64,
    class_mode='binary',
    shuffle=False
)

# Predictions
y_true = val_generator.classes
y_pred = model.predict(val_generator) > threshold

# Detailed report
print(classification_report(y_true, y_pred, target_names=['Real', 'AI Generated']))

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Real', 'AI Generated'],
            yticklabels=['Real', 'AI Generated'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()