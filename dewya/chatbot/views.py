from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai
from decouple import config

openai.api_key = config('OPENAI_API_KEY')

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        if "face wash" in user_message.lower():
            bot_reply = "For face wash, I recommend using a gentle cleanser like Cetaphil or Neutrogena."
        elif "moisturizer" in user_message.lower():
            bot_reply = "Using a lightweight, non-comedogenic moisturizer daily helps keep your skin hydrated."
        else:
            bot_reply = "I'm a skincare bot. Please ask about skincare tips or products."

        return JsonResponse({'reply': bot_reply})

    return render(request, 'chatbot/chat.html')
