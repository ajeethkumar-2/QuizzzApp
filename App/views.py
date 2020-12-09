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
    try :
        page = int(request.GET.get('page', '1'))
    except :
        page = 1
    try :
        questions = pagination.page(page)
    except(EmptyPage, InvalidPage):
        questions = pagination.page(pagination.num_pages)
    context = {
        'Course': ques,
        'questions': questions
    }
    return render(request, 'quiz.html', context)


def result(request):
    return render(request, 'result.html')
