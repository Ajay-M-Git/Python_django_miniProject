from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from rest_framework.decorators import action
from rest_framework.response import Response

# from api.seriallizers import CompanySeriallizer
from api.seriallizers import CompanySerializer,EmployeeSerializer
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):  
        try:
            company = Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emp_serialezer=EmployeeSerializer(emps,many=True,context={'request':request})
            # print("get employees of ",pk ,"company")
            return Response(emp_serialezer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exits...!! Error'
            })
            
class EmployeeViewSet(viewsets.ModelViewSet):
    
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer