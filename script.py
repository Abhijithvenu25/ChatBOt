import random

def get_user_input():
    return input("You: ")

def process_input(user_input):
    # Basic keyword-based logic
    if "hello" or 'hi' or 'hai' or 'hii' or 'hlo' in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "weather" in user_input.lower():
        return "I can check the weather for you, where are you located?"
    else:
        return "I'm not sure how to help with that. Could you clarify?"

def main():
    print("Welcome to your personal assistant!")
    while True:
        user_input = get_user_input()
        response = process_input(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
