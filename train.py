from model_mucuri import MucuriModel
from read_data import X_train, Y_train, test_data

model = MucuriModel()
model.train(X_train.values, Y_train.values)
print(Y_train.values[0])
print(X_train.values[0])
print(model.predict(X_train.values))
# for value in train_data.values:
#    print(value)
