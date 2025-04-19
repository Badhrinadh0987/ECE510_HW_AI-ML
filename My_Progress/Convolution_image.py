from tensorflow.keras.models import Model  # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input  # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
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

print(f"🟢 Found {train_generator.samples} images.")
print(f"📂 Class indices: {train_generator.class_indices}")
print(f"📦 Number of batches per epoch: {len(train_generator)}")

# Load one batch
batch = next(train_generator)
X_batch = batch[0]
Y_batch = batch[1]

print(f"✅ Batch X shape: {X_batch.shape}")
print(f"✅ Batch Y labels: {Y_batch}")

# ✅ Model using Functional API
input_tensor = Input(shape=(64, 64, 3))
x = Conv2D(32, (3, 3), activation='relu')(input_tensor)
x = MaxPooling2D(2, 2)(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = MaxPooling2D(2, 2)(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)
output_tensor = Dense(1, activation='sigmoid')(x)

model = Model(inputs=input_tensor, outputs=output_tensor)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_generator, epochs=5)

# ✅ Now model.input and model.output are guaranteed to exist
conv_layer_output_model = Model(inputs=model.input, outputs=model.layers[1].output)
activations = conv_layer_output_model.predict(X_batch)

print(f"🔍 Activation shape from Conv2D layer: {activations.shape}")

# 🖼️ Visualize first 6 feature maps of the first image
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 6, figsize=(20, 5))
for i in range(6):
    axes[i].imshow(activations[0, :, :, i], cmap='viridis')
    axes[i].axis('off')
    axes[i].set_title(f'Filter {i}')
plt.tight_layout()
plt.show()
