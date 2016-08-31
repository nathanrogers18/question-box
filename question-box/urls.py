from django.conf.urls import url, include
from rest_framework import routers
from question import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'user', views.UserProfileViewSet)
router.register(r'username', views.UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('question.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
]
