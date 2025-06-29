def chatbot_reply(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello there! 👋 How can I help you today?"
    
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm feeling pretty good! 😊 What about you?"
    
    elif user_input in ["i'm fine", "i am fine", "i'm good", "i am good"]:
        return "Glad to hear that! 😄"

    elif user_input in ["what can you do", "help", "what are your features"]:
        return "I’m a simple chatbot! I can reply to greetings, small talk, and respond to some common questions."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! 🙌"

    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Take care! 👋"

    elif user_input in ["who made you", "who created you"]:
        return "I was created by Prince Kumar as part of a CodeAlpha Internship project. 💻"

    elif user_input in ["what is your name", "your name"]:
        return "You can just call me ChatBuddy 🤖"

    else:
        return "Hmm... I’m not sure how to respond to that. Try saying 'help' to see what I can do."

print("\n🤖 ChatBuddy is ready to talk! (Type 'bye' to exit)\n")

while True:
    user_message = input("You: ")
    response = chatbot_reply(user_message)
    print("Bot:", response)

    if user_message.lower().strip() in ["bye", "goodbye", "see you"]:
        break
