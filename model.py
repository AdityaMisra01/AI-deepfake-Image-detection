from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Update paths to match your structure
train_dir = 'train/'  # Contains FAKE/ and REAL/
test_dir = 'test/'    # Contains FAKE/ and REAL/

# Fix class names to match directory casing
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(32, 32),
    batch_size=64,
    class_mode='binary',
    classes=['REAL', 'FAKE'],  # Match exact folder names
    subset='training'
)

val_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(32, 32),
    batch_size=64,
    class_mode='binary',
    classes=['REAL', 'FAKE'],
    subset='validation'
)