
def chatbot_response(user_input):
    
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "create task": "Sure! Please provide the task details.",
        "update task": "Which task would you like to update?",
        "delete task": "Let me know the task you want to delete.",
        "help": "I can assist you with creating, updating, or deleting tasks. Just type your query!",
    }

    
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Please try again.")
