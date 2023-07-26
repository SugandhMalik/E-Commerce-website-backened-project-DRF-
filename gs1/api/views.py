from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse #HttpResponse , JsonResponse

# Create your views here.
#Get 1 id Data
# def Student_detail(request):                        #can add (request,pk)
#     stu = Student.objects.get(id=1)                 #if using pk then id=pk
#     serializer = StudentSerializer(stu)
#     json_data = JSONRenderer().render(serializer.data)                          #1
#     return HttpResponse(json_data, content_type = 'application/json')           #2

#     # can use #3 instead of #1 and #2
#     return JsonResponse(serializer.data , safe= False)                          #3
#     # here safe = False set because we are not using pk

# Get all Data
def Student_detail(request):                            #can add (request,pk)
    stu = Student.objects.all()                         #if using pk then id=pk, or using id = 1,2,... then .all becomes .get
    serializer = StudentSerializer(stu, many = True)    #here many = True so can get all data
    # json_data = JSONRenderer().render(serializer.data)                          #1
    # return HttpResponse(json_data, content_type = 'application/json')           #2

    # can use #3 instead of #1 and #2
    return JsonResponse(serializer.data , safe = False)                          #3
    # here safe = False set because we are not using pk