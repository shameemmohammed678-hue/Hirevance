from django.shortcuts import render,redirect
from .models import AIConversation
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from django.conf import settings

# Create your views here.

def AI_assistant(request):
    return render(request,'ai_assistant/ai_assistant.html')    


@login_required
def ask_ai(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',

            headers={
                'Authorization': f'Bearer {settings.OPENROUTER_API_KEY}',
                'Content-Type': 'application/json'
            },

            json={
                'model': 'openrouter/free',

                'messages': [
                    {
                        'role': 'user',
                        'content': question
                    }
                ]
            }
        )
        data = response.json()
        ai_response = data['choices'][0]['message']['content']
        AIConversation.objects.create(
            user = request.user,
            question = question,
            response = ai_response
        )

        return JsonResponse({
            'response': ai_response
        })
    return JsonResponse({
        'error': 'Invalid request'
    }, status=400)