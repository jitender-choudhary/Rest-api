from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter


class StudentList(ListAPIView):
    queryset = Student.objects.filter()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
 
 

    
