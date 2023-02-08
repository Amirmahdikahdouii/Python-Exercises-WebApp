from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

routers = SimpleRouter()
routers.register("answers", views.QuestionAnswersViewSet, basename="questions-answers")
routers.register(r"", views.QuestionViewSet, basename="questions")
app_name = 'questions'
urlpatterns = [
    path("", include(routers.urls)),
]
