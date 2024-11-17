import json
import pickle
import numpy as np
import nltk
nltk.download('punkt')

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load data
with open('intents.json') as file:
    intents = json.load(file)

# Load pickle files
with open('words.pkl', 'rb') as file:
    words = pickle.load(file)
with open('classes.pkl', 'rb') as file:
    classes = pickle.load(file)

# Create training data
def tokenize(sentence):
    return [lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(sentence)]

def bag_of_words(sentence):
    sentence_words = tokenize(sentence)
    bag = [0] * len(words)
    for word in sentence_words:
        if word in words:
            bag[words.index(word)] = 1
    return np.array(bag)

X_train = []
y_train = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        bag = bag_of_words(pattern)
        X_train.append(bag)
        y_train.append(classes.index(intent['tag']))

X_train = np.array(X_train)
y_train = np.array(y_train)

# Build and train the model
model = Sequential()
model.add(Dense(128, input_shape=(len(X_train[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(classes), activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer=SGD(learning_rate=0.01), metrics=['accuracy'])
model.fit(X_train, y_train, epochs=200, batch_size=5, verbose=1)

# Save the model
model.save('chatbotmodel.h5')
print("Model trained and saved as 'chatbotmodel.h5'.")
