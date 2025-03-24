from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Main page
    path('ask/', views.ask_question, name='ask'),   # Endpoint to handle question
    path('save/', views.save_answer, name='save'),  # Endpoint to save Q&A
]
