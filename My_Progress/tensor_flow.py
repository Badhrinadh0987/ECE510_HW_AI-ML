from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras import Input # type: ignore
import os

# Dataset path
dataset_path = r'C:\Users\Student\Videos\COURSES\AI-ML\DDDS_Final_Pro\dataset'

# Preprocessing
datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(64, 64),
    batch_size=2,
    class_mode='binary'
)

# Debug info
print(f"🟢 Found {train_generator.samples} images.")
print(f"📂 Class indices: {train_generator.class_indices}")
print(f"📦 Number of batches per epoch: {len(train_generator)}")

# ✅ 🔍 Try loading one batch manually before training
batch = next(train_generator)
print(f"✅ Batch X shape: {batch[0].shape}")
print(f"✅ Batch Y labels: {batch[1]}")

# Model
model = Sequential([
    Input(shape=(64, 64, 3)),
    Conv2D(32, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 👇 Now we run training only if batch loads successfully
model.fit(train_generator, epochs=5)
