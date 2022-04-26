from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from .models import Student, TakenQuiz

class TakenQuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = TakenQuiz
        fields = ('id', 'student', 'quiz', 'score')

class StudentSerializer(serializers.ModelSerializer):
    # instuctor = UserSerializer(read_only=True)
    quizzes = TakenQuizSerializer(many=True, read_only=True)


    class Meta:
        model = Student
        fields = ('id', 'instuctor', 'name', 'avatar', 'grade', 'reward', 'quizzes')

class UserSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'students')
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user


