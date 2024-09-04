import random,os

class ChatAssistant:
    def __init__(self, filename='reminders.txt'):
        self.filename = filename
        self.reminders = self.load_data()

    def load_data(self):
        reminders = {}
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    key, message = line.strip().split(':', 1)
                    reminders[key.strip()] = message.strip()
        return reminders

    def save_data(self):
        with open(self.filename, 'w') as f:
            for key, message in self.reminders.items():
                f.write(f"{key}: {message}\n")

    def add_reminder(self, key, message):
        self.reminders[key] = message
        self.save_data()
        return f"Reminder set: {key} - {message}"

    def get_reminder(self, key):
        return self.reminders.get(key, "No reminder found for that.")

    def handle_reminders(self, user_input):
        if "remind me" in user_input:
            parts = user_input.split("to", 1)
            if len(parts) > 1:
                key = parts[0].strip().replace("remind me", "").strip()
                message = parts[1].strip()
                return self.add_reminder(key, message)
            else:
                return "I didn't catch that. Can you repeat your reminder?"
        else:
            return self.get_reminder(user_input)

    def handle_general_conversation(self, user_input):
        responses = {
            "how are you": "I'm just a bunch of code, but I'm doing well!",
            "what's your name": "I'm your personal assistant!",
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! What can I do for you?",
            'who are you' : "I'm your personal assistant!"
        }
        user_input = user_input.lower()
        for key in responses:
            if key in user_input:
                return responses[key]
        return "I didn't understand that, but I'm learning every day!"

    def process_input(self, user_input):
        if "remind me" in user_input or ":" in user_input:
            return self.handle_reminders(user_input)
        else:
            return self.handle_general_conversation(user_input)

def main():
    assistant = ChatAssistant()
    print("Welcome to your personal assistant!")
    while True:
        user_input = input("You: ")
        response = assistant.process_input(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()
