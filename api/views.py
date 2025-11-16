from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def studentsView(request):
    # manual serialization
    # students = Student.objects.all()
    # student_list = list(students.values())
    # return JsonResponse(student_list,safe=False)
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)