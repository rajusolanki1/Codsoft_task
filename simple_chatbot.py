def chatbot():
    print("Chatbot: Hello! I am a simple chatbot.")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print(" Chatbot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print(" Chatbot: I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("Chatbot: My name is SimpleBot.")
        elif "help" in user_input:
            print("Chatbot: I can answer simple questions like greetings, time, and date.")
        elif "time" in user_input:
            from datetime import datetime
            print(" Chatbot: Current time is", datetime.now().strftime("%H:%M:%S"))
        elif "date" in user_input:
            from datetime import datetime
            print("l Chatbot: Today's date is", datetime.now().strftime("%d-%m-%Y"))
        elif user_input == "bye":
            print(" Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print(" Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
