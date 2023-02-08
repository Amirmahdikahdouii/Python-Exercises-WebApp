# Models and Serializers
from .models import Question, QuestionAnswer
from .serializers import QuestionSerializer, QuestionAnswerSerializer

# Permissions
from .permissions import IsStaffOrReadOnly
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.filter(status=True)
    serializer_class = QuestionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = "question_id"
    permission_classes = (IsStaffOrReadOnly,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title', 'body']
    ordering_fields = ['id']
    ordering = ['-id']


class QuestionAnswersViewSet(ModelViewSet):
    def get_permissions(self):
        permission_classes = [AllowAny]
        if self.action not in ['list', 'retrieve']:
            permission_classes = [IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

    def create(self, request, *args, **kwargs):
        question_id = request.data.get("questionID")
        file = request.data.get("file")
        serializer = QuestionAnswerSerializer(data={'user': request.user.id, 'question': question_id, "file": file})
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
