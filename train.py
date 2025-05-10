import tensorflow as tf
from tensorflow.keras import layers, callbacks
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Configuration
BASE_DIR = 'dataset'
TRAIN_DIR = os.path.join(BASE_DIR, 'train')
TEST_DIR = os.path.join(BASE_DIR, 'test')
IMG_SIZE = (128, 128)  # Reduced from 224x224
BATCH_SIZE = 16        # Reduced from 32
EPOCHS = 30

def create_generators():
    """Memory-efficient data pipeline"""
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        rotation_range=15,  # Reduced augmentation
        horizontal_flip=True
    )

    return train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='binary',
        classes=['REAL', 'FAKE'],
        subset='training',
        seed=42
    )

def build_model():
    """Simplified architecture"""
    model = tf.keras.Sequential([
        layers.Conv2D(16, (3,3), activation='relu', input_shape=(*IMG_SIZE, 3)),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(32, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

def train():
    """Memory-optimized training"""
    # Suppress warnings
    tf.get_logger().setLevel('ERROR')
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    
    train_gen = create_generators()
    model = build_model()
    
    model.fit(
        train_gen,
        steps_per_epoch=100,  # Process 100 batches per epoch
        epochs=EPOCHS,
        callbacks=[
            callbacks.EarlyStopping(patience=3),
            callbacks.ModelCheckpoint('optimized_model.h5')
        ]
    )

if __name__ == '__main__':
    train()