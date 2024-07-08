# Define some patterns and responses
patterns_responses = {
    "hi": "Hello!",
    "how are you?": "I'm good, thank you.",
    "I'm fine": "ok!", 
    "what's your name?": "I'm  ShazaAI",
    "Who are you?":"I'm ShazaAI",
    "Tell me about yourself":"I'm a robot",
    "bye": "Goodbye!",

}

# Function to respond to user input
def respond(input_text):
    input_text = input_text.lower()  # Convert input to lowercase
    for pattern, response in patterns_responses.items():
        if pattern in input_text:
            return response
    return "I'm sorry, I don't understand that."

# Main function to run the chatbot
def run_chatbot():
    print("Welcome! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = respond(user_input)
            print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
