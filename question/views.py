from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UserProfile, Tag, Question, Answer, Comment
from rest_framework import viewsets
from .serializers import UserProfileSerializer, TagSerializer, QuestionSerializer
from .serializers import AnswerSerializer, CommentSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

def ask_question(request):
    return render(request, 'ask_question.html')

def question_detail(request, question_id):
    # question = get_object_or_404(Question, id=question_id)
    # context = {'question': question}
    return render(request, 'question_detail.html')

def question_detail_test(request): # TODO: Remove when done testing
    # question = get_object_or_404(Question, id=question_id)
    # context = {'question': question}
    return render(request, 'question_detail.html')
