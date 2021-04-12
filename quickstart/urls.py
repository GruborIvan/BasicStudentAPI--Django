from django.urls import path
from quickstart.views import index,StudentView,StudentByIndex

urlpatterns = [
    path('index/<int:pk>',index),
    path('students',StudentView.as_view()),
    path('students/<int:pk>',StudentByIndex.as_view())
]