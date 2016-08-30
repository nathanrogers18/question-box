from rest_framework import serializers

from django.contrib.auth.models import User
from .models import UserProfile, Tag, Question, Comment, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'score')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('topic',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'question', 'text', 'answer', 'timestamp')


class AnswerSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ('user', 'question', 'text', 'accepted', 'vote', 'timestamp', 'comment_set')


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    tag_set = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('user', 'title', 'text', 'tag', 'vote', 'timestamp',
                  'answer_set', 'comment_set', 'tag_set')
