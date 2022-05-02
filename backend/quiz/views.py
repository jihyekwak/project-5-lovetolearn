from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
from .models import Quiz, Question, Answer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return HttpResponse("Backend Home")

class QuizView(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.order_by('-created_at')
    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     return Quiz.objects.all()

    # def get_object(self, queryset=None, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     return get_object_or_404(Quiz, pk=pk)

    # def get_queryset(self):
    #     qs = super().get_queryset()

    #     search = self.request.query_params.get('search', '')
    #     if search:
    #         qs = qs.filter(title_icontains = search)
    #     return qs

class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

# class AnswerView(viewsets.ModelViewSet):
#     serializer_class = AnswerSerializer
#     queryset = Answer.objects.all()