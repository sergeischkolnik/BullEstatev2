import tensorflow as tf
import cv2
import numpy as np
import os

class yapo_ocr():
    """ Clase para leer digitos de yapo usando CNN entrenada con TF"""
    def __init__(self,checkpoint_path = "CNN_distilation/training_1/cp.ckpt"):

        self.checkpoint_path=checkpoint_path
        try:
            self.cnn=self.load_cnn()
        except:
            raise FileNotFoundError("Revisar direccion de archivos de pesos de red")

    def load_cnn(self):
      IMAGE_SHAPE = [28, 28, 1]

      inputs = tf.keras.Input(shape=(*IMAGE_SHAPE,))
      x = tf.keras.layers.Conv2D(32, kernel_size=5, padding='SAME', activation=tf.nn.relu)(inputs)
      x = tf.keras.layers.MaxPooling2D(
          pool_size=[2, 2], strides=[2, 2], padding="SAME")(x)
      x = tf.keras.layers.Conv2D(64, kernel_size=5, padding='SAME', activation=tf.nn.relu)(x)
      x = tf.keras.layers.MaxPooling2D(
          pool_size=[2, 2], strides=[2, 2], padding="SAME")(x)
      x = tf.keras.layers.Conv2D(128, kernel_size=5, padding='SAME', activation=tf.nn.relu)(x)
      x = tf.keras.layers.Flatten()(x)
      x = tf.keras.layers.Dense(
          84, activation=tf.nn.relu)(x)
      x = tf.keras.layers.Dropout(0.4)(x)
      predictions = tf.keras.layers.Dense(10,activation=tf.nn.softmax)(x)

      cnn = tf.keras.Model(inputs=inputs, outputs=predictions)



      checkpoint_dir = os.path.dirname(self.checkpoint_path)

      # Create checkpoint callback
      cp_callback = tf.keras.callbacks.ModelCheckpoint(self.checkpoint_path,
                                                       save_weights_only=True,
                                                       verbose=1)

      cnn.compile(optimizer='adam',
                    loss=tf.keras.losses.categorical_crossentropy,
                    metrics=['accuracy'])

      cnn.load_weights(self.checkpoint_path)
      return cnn

    def prepros(self, frame):
        x_proj = np.sum(frame[:, :, 0], axis=0) > 7300

        edges = np.where(np.diff(x_proj) == 1)[0]
        boxes = [(edges[2 * i], edges[(2 * i) + 1]) for i in range(5, 14)]
        digits = [frame[:24, p[0] + -1:p[1] + 2, 0] for p in boxes]

        centered = []
        for dig in digits:
            base = np.zeros((28, 28), dtype=np.uint8)

            x_ini = int((28 - dig.shape[1]) / 2)
            x_fin = int(x_ini + dig.shape[1])
            base[3:27, x_ini:x_fin] = 255 - dig
            centered.append(base)

        return np.array(centered).reshape((9, 28, 28, 1))

    def read_image(self, path):
        gif = cv2.VideoCapture(path)
        okay, frame = gif.read()
        if not okay:
            print("problem")
        digits = self.prepros(frame)
        pred = self.cnn.predict(digits)
        gif.release()
        return [np.argmax(i) for i in pred]

    def __call__(self, path):
        """ Retorna numero con parentesis"""
        num = self.read_image(path)

        return "+56"+"".join([str(i) for i in num])