# Neuralite
*A Streamlined Python Framework for Rapidly Building and Deploying Machine Learning-Based Conversational Agents*

Build, deploy, and scale your AI projects with Neuralite! Whether you're a seasoned AI developer or just starting out, Neuralite offers a simple and efficient way to implement AI features into your software.

## Table of Contents
- [Getting Started 🚀](#getting-started-🚀)
- [Basic Chatbot 🤖](#basic-chatbot-🤖)
- [Customizable Training Epochs 🔄](#customizable-training-epochs-🔄)
- [Compiling Your Model 📦](#compiling-your-model-📦)
- [Loading a Compiled Model 🔓](#loading-a-compiled-model-🔓)
- [Example Conversational Dataset 💬](#example-conversational-dataset-💬)

## Getting Started 🚀
To get started, install Neuralite with pip:
```bash
pip install Neuralite
```

## Basic Chatbot 🤖
Creating a basic chatbot is simple:
```python
from neuralite.interpreter import ai # Imports framework

assistant = ai('dataset.json') # Loads dataset

cycle_end = False # Starts the AI cycle

while not cycle_end: # Main cycle
    message = input("Enter a message: ") # Prompts user with message
    if message.lower() == "stop": # Exit with 'stop'
        cycle_end = True # Ends cycle
    else:
        print(assistant.process_input(message)) # Prints the response
```

# Customizable Training Epochs 🔄
Train your AI model with a customizable number of epochs. The higher the epochs, the more refined your model will be.
```python
from neuralite.interpreter import ai # Imports framework

# Initialize the AI model with 200 epochs
assistant = ai('dataset.json', epochs=200)

# Continue with your chatbot as usual
```

# Compiling Your Model 📦
To make your dataset unreadable, load faster, and to package it into a neat file.

```python
from neuralite.interpreter import ai # Imports framework

assistant = ai('dataset.json') # Loads dataset

assistant.compile('model.nlite') # Packages dataset to 'model.nlite'
```

# Loading a Compiled Model 🔓
To load a precompiled model.

```python
from neuralite.interpreter import ai # Imports framework

assistant = ai.compiled('model.nlite') # Loads the compiled model

cycle_end = False # Starts the AI cycle

while not cycle_end: # Main cycle
    message = input("Enter a message: ") # Prompts user with message
    if message.lower() == "stop": # Exit with 'stop'
        cycle_end = True # Ends cycle
    else:
        print(assistant.process_input(message)) # Prints the response
```
# Example Conversational Dataset 💬
```json
{
  "greeting": ["Hi", "Hello", "Hey there"],
  "greeting_responses": ["Hello!", "Hi, how can I help?", "Hey! What's up?"],
  "farewell": ["Goodbye", "See you", "Ciao"],
  "farewell_responses": ["Goodbye!", "See you soon!", "Take care!"],
  "how_are_you": ["How are you?", "How's it going?", "What's up?"],
  "how_are_you_responses": ["I'm good, thank you!", "I'm doing well. How about you?", "Not much, what about you?"],
  "compliment": ["You're great!", "You're amazing!", "You're awesome!"],
  "compliment_responses": ["Thank you! You're pretty awesome too.", "Thanks! You're great as well!", "Thanks! That means a lot."],
  "name": ["What's your name?", "Who are you?", "Tell me your name."],
  "name_responses": ["I'm Neuralite, your AI assistant.", "Call me Neuralite.", "I'm Neuralite! Nice to meet you."],
  "jokes": ["Tell me a joke.", "Do you know any jokes?", "Make me laugh."],
  "jokes_responses": ["Why did the scarecrow win an award? Because he was outstanding in his field!", "I told my computer I needed a break. Now it won't stop sending me Kit-Kats.", "Why did the math book look sad? Because it had too many problems."]
}
```