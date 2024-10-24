def chatbot_response(user_input):
    user_input = user_input.lower()  # Normalize the input to lowercase

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking! How can I assist you?"
    elif "what is your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "help" in user_input:
        return "Sure! I can help you with general inquiries. What do you need?"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase your question?"


def main():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
