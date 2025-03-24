from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import SavedAnswer
import os
def home(request):
    """
    The main view: 
    - Displays a form to ask a question.
    - Shows a list of all saved Q&As.
    """
    saved_answers = SavedAnswer.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'saved_answers': saved_answers})

def ask_question(request):
    """
    Receives an AJAX POST request with a question.
    For simplicity, we'll return a placeholder answer.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question', '')
            if not question:
                return JsonResponse({'error': 'Question cannot be empty!'}, status=400)
            # api_key = os.environ.get('GEMINI_API_KEY')
            # if not api_key:
            #     return JsonResponse({'error': 'GEMINI_API_KEY not found in environment variables. Please check your .env file.'}, status=500)

            # Placeholder answer logic
            generated_answer = f"This is a placeholder response to your question: '{question}'"
            return JsonResponse({'answer': generated_answer})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def save_answer(request):
    """
    Saves the question and answer to the database (POST).
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question', '')
            answer = data.get('answer', '')

            if not question or not answer:
                return JsonResponse({'error': 'Both question and answer are required!'}, status=400)

            saved_answer = SavedAnswer.objects.create(question=question, answer=answer)
            
            return JsonResponse({'success': True, 'id': saved_answer.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
