from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name='questions_list_view'),
]
