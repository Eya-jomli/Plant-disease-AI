from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from plant_disease.chat import get_response, bot_name

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('message', '')
        bot_response = get_response(user_message)

        # Log the bot response for debugging
        print(f"User message: {user_message}, Bot response: {bot_response}")

        return JsonResponse({'response': bot_response})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def chat_interface(request):
    return render(request, 'chat.html', {'bot_name': bot_name})  # Make sure 'chat.html' is the correct template name