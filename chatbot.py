# chatbot.py
import random

responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How are you?"],
    "how are you": ["I'm good, thanks!", "Doing great!", "All good here, what about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I don't understand that."

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot:", random.choice(responses["bye"]))
            break
        print("Chatbot:", get_response(user_input))
