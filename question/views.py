from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Tag, Question, Answer, Comment
from rest_framework import viewsets
from .serializers import UserProfileSerializer, TagSerializer, QuestionSerializer
from .serializers import AnswerSerializer, CommentSerializer, UserSerializer
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


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


class AllQuestionsView(generic.ListView):
    model = Question
    template_name = 'all_questions.html'
    context_object_name = 'all_questions'

    def get_queryset(self):
        questions = Question.objects.order_by('timestamp')
        return questions


class UserProfileDetail(generic.DetailView):
    model = UserProfile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetail, self).get_context_data(**kwargs)
        return context


class AllUsersView(generic.ListView):
    model = User
    template_name = 'all_users.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        users = User.objects.order_by('last_name')
        return users



def ask_question(request):
    return render(request, 'ask_question.html')


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    print(question.title)
    try:
        question_tags = question.tag_set.all()
    except:
        question_tags = None
        print("No tags for question")
    try:
        question_comments = question.comment_set.all()
    except:
        question_comments = None
        print("No comments for question")
    try:
        answers = question.answer_set.all()
        answer_tags_and_comments = []
        for answer in answers:
            ans = {'answer': answer}
            try:
                ans['tag_set'] = answer.tag_set.all()
            except:
                ans['tag_set'] = None
            try:
                ans['comment_set'] = answer.comment_set.all()
            except:
                ans['comment_set'] = None

            answer_tags_and_comments.append(ans)
    except:
        answers = None
        print("No answers for question")

    context = {'question': question,
               'question_tags': question_tags,
               'question_comments': question_comments,
               'answer': answer_tags_and_comments}
    return render(request, 'question_detail.html', context)


def question_detail_test(request):  # TODO: Remove when done testing
    return render(request, 'question_detail.html')


@login_required
def ajax_test(request):  # TODO: REMOVE AFTER testing
    question = get_object_or_404(Question, id=1)
    user = request.user
    context = {'question': question}
    return render(request, 'ajax_test.html', context)
