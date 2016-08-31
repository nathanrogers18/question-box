from django.conf.urls import url
from . import views
# from .views import BoardViewSet
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout

user_detail = views.UserProfileViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'

    ), name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^ask/$', views.ask_question, name='ask'),
    url(r'^question/(?P<question_id>[0-9]+)/$',
        views.question_detail, name='question_detail'),
    url(r'^question_test/$', views.question_detail_test, name='question_detail'),  # TODO: Remove this when finished testing
    url(r'^ajax_test/$', views.ajax_test, name='ajax_test'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UserProfileDetail.as_view(), name='profile_detail'),
    url(r'^allquestions/$', views.AllQuestionsView.as_view(), name='all_questions'),
    url(r'^allusers/$', views.AllUsersView.as_view(), name='all_users'),
    ]
