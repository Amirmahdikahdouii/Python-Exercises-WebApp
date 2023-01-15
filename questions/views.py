from rest_framework.generics import ListAPIView
from .models import Question
from .serializers import QuestionSerializer


class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
