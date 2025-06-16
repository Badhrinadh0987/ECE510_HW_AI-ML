from tensorflow.keras.models import Model # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
import matplotlib.pyplot as plt # type: ignore
import os

# Dataset path
dataset_path = 'dataset'

# Preprocessing
datagen = ImageDataGenerator(rescale=1./255)

train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(64, 64),
    batch_size=2,
    class_mode='binary'
)

# Build model
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
model.fit(train_generator, epochs=5)

# Visualize activations
batch = next(train_generator)
X_batch = batch[0]

conv_output_model = Model(inputs=model.input, outputs=model.layers[1].output)
activations = conv_output_model.predict(X_batch)

fig, axes = plt.subplots(1, 6, figsize=(20, 5))
for i in range(6):
    axes[i].imshow(activations[0, :, :, i], cmap='viridis')
    axes[i].axis('off')
    axes[i].set_title(f'Filter {i}')
plt.tight_layout()
plt.show()