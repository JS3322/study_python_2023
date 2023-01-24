import tensorflow as tf
import tensorflow.keras.layers as layers

# docker build -t keras-model:0.1 .
# docker run -it keras-model:0.1 model.py


class ClassificationModel:
    def __init__(self, image_size, num_classes):
        self.input_shape = image_size + (3,)
        self.num_classes = num_classes

    def build_model(self):
        def data_augmentation(inputs):
            data_augmentation = tf.keras.Sequential(
                [
                    layers.experimental.preprocessing.RandomFlip("horizontal"),
                    layers.experimental.preprocessing.RandomRotation(0.1),
                ]
            )
            return data_augmentation(inputs)

        inputs = tf.keras.Input(self.input_shape)

        x = data_augmentation(inputs)
        x = layers.experimental.preprocessing.Rescaling(1.0 / 255)(x)
        x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)

        x = layers.Conv2D(64, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)

        previous_block_activation = x  # Set aside residual

        for size in [128, 256, 512, 728]:
            x = layers.Activation("relu")(x)
            x = layers.SeparableConv2D(size, 3, padding="same")(x)
            x = layers.BatchNormalization()(x)

            x = layers.Activation("relu")(x)
            x = layers.SeparableConv2D(size, 3, padding="same")(x)
            x = layers.BatchNormalization()(x)

            x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

            # Project residual
            residual = layers.Conv2D(size, 1, strides=2, padding="same")(
                previous_block_activation
            )
            x = layers.add([x, residual])  # Add back residual
            previous_block_activation = x  # Set aside next residual

        x = layers.SeparableConv2D(1024, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)

        x = layers.GlobalAveragePooling2D()(x)
        if self.num_classes == 2:
            activation = "sigmoid"
            units = 1
        else:
            activation = "softmax"
            units = self.num_classes

        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(units, activation=activation)(x)
        return tf.keras.Model(inputs, outputs)


if __name__ == "__main__":
    image_size = (180, 180)
    num_classes = 2

    model = ClassificationModel(image_size=image_size, num_classes=num_classes)
    model = model.build_model()
    print(model.summary())
