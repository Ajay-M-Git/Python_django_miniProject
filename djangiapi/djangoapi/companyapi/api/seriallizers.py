from rest_framework import serializers
from api.models import Company,Employee  # Ensure this path is correct

class CompanySerializer(serializers.HyperlinkedModelSerializer):  # Correct spelling
    Company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company  # Correct syntax for model assignment
        fields = "__all__"  # Ensure the model has fields defined


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    
    class Meta:
        model=Employee
        fields="__all__"









# from rest_framework import serializers
# from api.models import Company

# #create seriallizers here
# class CompanySeriallizer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model:Company
#         fields="__all__"
        