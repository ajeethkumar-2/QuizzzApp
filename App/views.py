from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Question, Course
from django.shortcuts import render


def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home.html', context)


def quiz(request, id):
    ques = Question.objects.filter(course=id)
    pagination = Paginator(ques, 1)
    page_number = request.GET.get('page')
    questions = Paginator.get_page(pagination, page_number)
    context = {
        'Course': ques,
        'questions': questions
    }
    return render(request, 'quiz.html', context)


def result(request):
    return render(request, 'result.html')
