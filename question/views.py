from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Tag, Question, Answer, Comment
from rest_framework import viewsets
from .serializers import UserProfileSerializer, TagSerializer, QuestionSerializer
from .serializers import AnswerSerializer, CommentSerializer, UserSerializer


# Create your views here.
class IndexView(generic.ListView):
    model = Question
    template_name = 'index.html'
    context_object_name = 'all_questions'

    def get_queryset(self):
        questions = Question.objects.order_by('vote')
        return questions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


class SearchView(generic.ListView):
    model = Tag
    select_related = ['topic']
    template_name = 'search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            searched_topics = self.model.objects.filter(topic__icontains=query)
            return searched_topics


# TODO: All_questions view
# class AllQuestionsView(generic.ListView):
#     model = Question
#     template_name = 'all_questions.html'
#     context_object_name = 'all_questions'


def ask_question(request):
    if request.POST:
        tags = request.POST
        print(tags)
    return render(request, 'ask_question.html')


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set
    context = {'question': question}
    return render(request, 'question_detail.html')


def question_detail_test(request): # TODO: Remove when done testing
    # question = get_object_or_404(Question, id=question_id)
    # context = {'question': question}
    return render(request, 'question_detail.html')

@login_required
def ajax_test(request):  # TODO: REMOVE AFTER testing
    question = get_object_or_404(Question, id=1)
    user = request.user
    context = {'question': question}
    return render(request, 'ajax_test.html', context)
