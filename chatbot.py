import random
import wikipedia

responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How are you?"],
    "how are you": ["I'm good, thanks!", "Doing great!", "All good here, what about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "who made you": ["I am an AI made by LootyPlayz aka Gaurav"],
}

def safe_eval(expr):
    """Safely evaluate simple math expressions"""
    allowed_chars = "0123456789+-*/(). "
    if all(char in allowed_chars for char in expr):
        try:
            return str(eval(expr))
        except Exception:
            return None
    return None

def get_response(user_input):
    user_input = user_input.lower().strip()

    # 🔹 Step 1: Check custom responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # 🔹 Step 2: Check for math expressions
    math_result = safe_eval(user_input)
    if math_result is not None:
        return f"The answer is {math_result}"

    # 🔹 Step 3: Fallback → Search Wikipedia
    try:
        summary = wikipedia.summary(user_input, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query matched multiple topics: {', '.join(e.options[:5])}..."
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn’t find anything about that."
    except Exception:
        return "Something went wrong while searching Wikipedia."

    # 🔹 Step 4: Final fallback
    return "Sorry, I don't understand that."

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot:", random.choice(responses["bye"]))
            break
        print("Chatbot:", get_response(user_input))
