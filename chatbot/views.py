from django.http import JsonResponse

def chatbot(request):
    user_query = request.GET.get('query', '').strip().lower()

    if not user_query:
        return JsonResponse({'response': 'Please provide a message.'})

    
    if 'hello' in user_query or 'hi' in user_query:
        bot_response = 'Hello! How can I assist you today?'
    elif 'task' in user_query:
        bot_response = 'You can manage your tasks by going to the "Tasks" section.'
    elif 'help' in user_query:
        bot_response = 'I am here to help! You can ask me about tasks, registration, or account settings.'
    else:
        bot_response = "I'm sorry, I don't understand. Could you please rephrase?"
    
    return JsonResponse({'response': bot_response})




