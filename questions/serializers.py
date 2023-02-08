from rest_framework import serializers
from .models import Question, QuestionAnswer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ['status']


class QuestionAnswerSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'question': {
                'id': instance.question.id,
                'title': instance.question.title,
                'body': instance.question.body,
            },
            'user': {
                'username': instance.user.username,
                'email': instance.user.email,
                'first_name': instance.user.first_name,
                'last_name': instance.user.last_name,
            },
            'file': instance.file,
        }

    class Meta:
        model = QuestionAnswer
        fields = ['user', "question", "file"]

    def create(self, validated_data):
        user = self.validated_data.get("user", None)
        question = self.validated_data.get("question", None)
        file = self.validated_data.get("file", None)
        return QuestionAnswer.objects.create(user=user, question=question, file=file)
