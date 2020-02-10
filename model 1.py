from keras.layers import Dense, Conv1D, Flatten
from keras.models import Sequential
from getData import trainData
from getData import dataReader
from getData import normalization, getData, getLabel
from keras.utils import to_categorical
import tensorflow as tf
import matplotlib.pyplot as plt

# Model Init
testModel = Sequential()

# Collect Data
trainSignals, trainLabels = normalization(getData(1, 5, 10)), getLabel(0, 10)
# trainLabels = to_categorical(trainLabels, 2)
testSignals, testLabels = dataReader(4, 5, 360, 1, 0, 0, 1)
# testLabels = to_categorical(testLabels, 2)

print(trainSignals[0])

# Model Layers
testModel.add(Conv1D(100, 20, padding='same', activation='relu', input_shape=(360, 1)))
testModel.add(Conv1D(20, 5, padding='same', activation='relu'))
testModel.add(Dense(10, activation='relu'))
testModel.add(Dense(5, activation='relu'))
testModel.add(Flatten())
testModel.add(Dense(1, activation='sigmoid'))
print(testModel.summary())

# Compile Model
testModel.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

# Train Model
trainedModel = testModel.fit(trainSignals, trainLabels, epochs=50)

'''
# Plots
history = trainedModel.history
loss_values = history['loss']
epochs = range(1, len(loss_values)+1)
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.title('Training loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
# plt.show()

plt.clf()
acc_values = history['accuracy']
plt.plot(epochs, acc_values, 'bo', label='Training acc')
plt.title('Training accuracy')
plt.xlabel('Epochs')
plt.ylabel('Acc')
plt.legend()
# plt.show()
'''

# Test Model
test_loss, test_acc = testModel.evaluate(testSignals, testLabels)
print('Accuracy:', test_acc)
print('Loss', test_loss)

