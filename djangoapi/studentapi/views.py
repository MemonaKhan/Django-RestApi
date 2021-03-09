from django.shortcuts import render

from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):             # ModelViewSet is a special view that Django Rest Framework provides
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer