College Enquiry Chatbot System 🤖
Overview
The College Enquiry Chatbot System is an AI-powered chatbot designed to answer common college-related queries like admissions, events, courses, and more. Using Natural Language Processing (NLP) and deep learning, this chatbot provides quick and reliable responses, enhancing user experience.

Features ✨
Interactive: Provides instant answers to user questions.
NLP-based Understanding: Uses tokenization and lemmatization for accurate input interpretation.
Customizable: Easily update responses and intents.
Scalable: Can be trained with more data for improved accuracy.
Tech Stack 🛠️
Python: Main programming language
TensorFlow/Keras: For building the neural network model
NLTK: For text preprocessing (tokenization and lemmatization)
NumPy: For numerical operations
JSON: For intents and responses
Pickle: For saving processed data
Project Structure 📁
├── intents.json         # Predefined intents and responses
├── words.pkl            # Pickle file for unique words
├── classes.pkl          # Pickle file for unique classes (intents)
├── chatbotmodel.h5      # Trained neural network model
├── chatbot_train.py     # Script for data preprocessing and model training
├── chatbot_app.py       # Main script to run the chatbot
├── README.md            # Project documentation
Contributing 🤝
Open to contributions! Feel free to create a pull request or raise issues.
License 📜
This project is licensed under the MIT License.
