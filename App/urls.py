from .views import home, quiz, result
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('quiz/<id>', quiz, name='quiz'),
    path('result', result, name='result'),
]
