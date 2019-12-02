from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

model = Sequential()
model.add(Dense(9, input_shape=(9,)))
model.add(Dense(9, activation="tanh"))
model.add(Dense(6, activation="tanh"))
model.add(Dense(1, activation="linear"))

model.compile(loss="mean_squared_error", optimizer="adam")

checkpoint = ModelCheckpoint(filepath="weights.hdf5", save_best_only=True)
model.fit(X, Y, epochs=30, validation_data=(X_test, Y_test), callbacks=[checkpoint])
