from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution1D, Flatten, MaxPooling1D, Dropout, GlobalAveragePooling1D

# Create an empty model
testModel = Sequential()

# Adding layers
testModel.add(Convolution1D(100, 20, activation='relu', input_shape=(200, 6)))
testModel.add(Convolution1D(100, 20, activation='relu'))
testModel.add(MaxPooling1D(6))
testModel.add(Convolution1D(160, 13, activation='relu'))
testModel.add(Convolution1D(160, 13, activation='relu'))
testModel.add(GlobalAveragePooling1D())
testModel.add(Dropout(0.5))
testModel.add(Dense(10, activation='softmax'))
print(testModel.summary())

