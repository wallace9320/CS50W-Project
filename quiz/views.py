from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse

from .models import User, Quiz, Question, Option, Score

# Create your views here.

def index(request):

    if request.user.is_authenticated:
        return render(request, "quiz/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "quiz/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "quiz/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "quiz/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "quiz/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "quiz/register.html")


@login_required(login_url="/login")
def create(request):

    if request.method == "POST":
        title = request.POST["title"]
        quiz = Quiz.objects.create(owner=request.user, title=title)
        quiz.save()
        no_of_questions = request.POST["no-of-questions"]
        for i in range(1, int(no_of_questions) + 1):
            question_description = request.POST[f"{i}-question"]
            question = Question.objects.create(quiz=quiz, question_description=question_description)
            question.save()
            for j in range(1, 5):
                option_description = request.POST[f"{i}-option-{j}"]
                correct = False
                if int(request.POST[f"{i}-select"]) == j:
                    correct = True
                option = Option.objects.create(question=question, option_description=option_description, \
                    correct=correct)
                option.save()
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "quiz/create.html", {
            "iterator": range(1,4)
        })


def display(request, type):

    if type == "all":
        quizzes = Quiz.objects.all().order_by('-timestamp')
    elif type == "created":
        quizzes = Quiz.objects.filter(owner=request.user).order_by('-timestamp')
    elif type == "answered":
        quizzes = Quiz.objects.filter(answered__id__exact=request.user.id).order_by('-timestamp')
    else:
        return JsonResponse({"error": "Invalid display type."}, status=400)

    return JsonResponse([quiz.serialize() for quiz in quizzes], safe=False)


def search(request, type, keyword):

    if type == "username":
        quizzes = Quiz.objects.filter(owner__username__iexact=keyword).order_by('-timestamp')
    elif type == "title":
        quizzes = Quiz.objects.filter(title__icontains=keyword).order_by('-timestamp')
    else:
        return JsonResponse({"error": "Invalid search type."}, status=400)

    return JsonResponse([quiz.serialize() for quiz in quizzes], safe=False)


@login_required(login_url="/login")
def attempt(request, quiz_id):

    if Quiz.objects.filter(id=quiz_id, answered__id__exact=request.user.id).exists():
        return render(request, "quiz/attempt.html", {
            "message": "You already did the quiz!"
        })

    quiz = Quiz.objects.get(id=quiz_id)

    if quiz.owner == request.user:
        return render(request, "quiz/attempt.html", {
            "message": "You created the quiz!"
        })

    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        quiz.answered.add(request.user)
        result = 0
        for i in range(1, questions.count() + 1):
            option_id = request.POST[f"{i}"]
            option = Option.objects.get(id=option_id)
            if option.correct:
                result += 1
            option.chosen_user.add(request.user)
        score = Score.objects.create(quiz=quiz, answerer=request.user, result=result)
        score.save()
            
        return HttpResponseRedirect(reverse("result", args=(quiz_id,)))

    qnas = []
    for question in questions:
        qna = [question,]
        options = Option.objects.filter(question=question)
        qna.append(options)
        qnas.append(qna)

    return render(request, "quiz/attempt.html", {
        "quiz": quiz,
        "qnas": qnas
    })


@login_required(login_url="/login")
def result(request, quiz_id):

    if not Quiz.objects.filter(id=quiz_id, answered__id__exact=request.user.id).exists():
        return render(request, "quiz/result.html", {
            "message": "You did not do the quiz!"
        })

    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    score = Score.objects.get(quiz=quiz, answerer=request.user)
    qnas = []

    for question in questions:
        qna = [question,]
        correct_option = Option.objects.get(question=question, correct=True)
        chosen_option = Option.objects.get(question=question, chosen_user__id__exact=request.user.id)
        qna.append(correct_option)
        qna.append(chosen_option)
        qnas.append(qna)

    return render(request, "quiz/result.html", {
        "quiz": quiz,
        "qnas": qnas,
        "score": score.result
    })


@login_required(login_url="/login")
def otherresult(request, quiz_id):

    quiz = Quiz.objects.get(id=quiz_id)
    scores = Score.objects.filter(quiz=quiz).order_by('-result')
    return render(request, "quiz/otherresult.html", {
        "quiz": quiz,
        "no_of_questions": Question.objects.filter(quiz=quiz).count(),
        "scores": scores
    })
