from django.shortcuts import render
from quickstart.models import Student
from rest_framework.views import APIView
from django.http import HttpResponse
from quickstart.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status,generics
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.

def index(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        student = None

    if student == None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return render(request, "user.html",{"student":student})


class StudentView(generics.ListCreateAPIView):

    #permission_classes = (IsAuthenticated,IsAdminUser)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Student.objects.all()

        # FILTERING BY 'br_indeksa' & 'ime'
        br_indeksa = self.request.query_params.get('br_indeksa')
        ime = self.request.query_params.get('ime')

        if br_indeksa is not None:
            queryset = queryset.filter(br_indeksa=br_indeksa)

        if ime is not None:
            queryset = queryset.filter(ime=ime)

        return queryset

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def get(self,request,format = None):
    #     allStudents = Student.objects.all()
    #     smer = self.request.query_params.get('br_indeksa')
    #     if smer is not None:
    #         allStudents = allStudents.filter(br_indeksa=smer)
    #     serializedStudents = StudentSerializer(allStudents,many=True)
    #     return Response(serializedStudents.data)

    # def post(self,request):
    #     serializedObject = StudentSerializer(data = request.data)
    #     if serializedObject.is_valid():
    #         serializedObject.save()
    #         return Response(serializedObject.data,status=status.HTTP_201_CREATED)
    #     return Response(serializedObject.errors,status = status.HTTP_400_BAD_REQUEST)


class StudentByIndex(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,IsAdminUser)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def get_object(self,pk):
    #     try:
    #         return Student.objects.get(pk=pk)
    #     except Student.DoesNotExist:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


    # def get(self,request,pk):
    #     studObj = self.get_object(pk)
    #     serializedStd = StudentSerializer(studObj)
    #     return Response(serializedStd.data)

    # def put(self,request,pk):
    #     stdObj = self.get_object(pk)
    #     serializedObj = StudentSerializer(stdObj,data=request.data)
    #     if serializedObj.is_valid():
    #         serializedObj.save()
    #         return Response(serializedObj.data,status=status.HTTP_200_OK)
    
    # def delete(self,request,pk):
    #     stdObj = self.get_object(pk)
    #     stdObj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)