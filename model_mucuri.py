from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint


class MucuriModel:
    def __init__(self):

        self.model = None
        self._build_model()

    def _build_model(self):

        if self.model is None:
            self.model = Sequential()
            self.model.add(Dense(9, input_dim=9))
            self.model.add(Dense(9, activation="tanh"))
            self.model.add(Dense(6, activation="tanh"))
            self.model.add(Dense(1, activation="linear"))
            self.model.compile(loss="mean_squared_error", optimizer="adam")

    def train(self, X, Y, X_test=None, Y_test=None):

        assert self.model is not None

        checkpoint = ModelCheckpoint(filepath="./weights.hdf5", save_best_only=True)
        self.model.fit(
            X,
            Y,
            verbose=1,
            epochs=30,
            validation_data=(X_test, Y_test)
            if X_test is not None and Y_test is not None
            else None,
            callbacks=[checkpoint],
        )

    def predict(self, data):

        assert self.model is not None

        return self.model.predict(data)
