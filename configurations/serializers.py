from abc import ABC

from rest_framework import serializers
from .models import AuthUser,Masterscoringdetail,Mastermonthlysalary,Mastereducationlevel,Masterworkingage,Mastercustomerage,Mastershoptypes,Masterrentalage,Mastermaritalstatus,Mastercustomerage,Mastershoptypes,Masterrentalage,Masterbusinesstype,Mastermonthlyprofit,Masterbusinessage,Masterminorchildren,Mastercontractreason,Mastercountry

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'
        
class MasterscoringdetailSerializer(serializers.ModelSerializer):
    score_name = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Masterscoringdetail
        fields = '__all__'
        
class MastermonthlysalarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastermonthlysalary
        fields = '__all__'
        
class MastereducationlevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastereducationlevel
        fields = '__all__'
        
class MasterworkingageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Masterworkingage
        fields = '__all__'

class MastershoptypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastershoptypes
        fields = '__all__'
        
class MasterrentalageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Masterrentalage
        fields = '__all__'
                        
class MastermaritalstatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastermaritalstatus
        fields = '__all__'       
        
class MastercustomerageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastercustomerage
        fields = '__all__' 
        
class MastershoptypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastershoptypes
        fields = '__all__' 

class MasterrentalageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Masterrentalage
        fields = '__all__' 
        
class MasterbusinesstypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Masterbusinesstype
        fields = '__all__' 
                 
class MastermonthlyprofitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastermonthlyprofit
        fields = '__all__' 
        
class MasterbusinessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Masterbusinessage
        fields = '__all__'         
                
class MasterminorchildrenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Masterminorchildren
        fields = '__all__'         
        
class MastercontractreasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastercontractreason
        fields = '__all__'         
        
class MastercountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Mastercountry
        fields = '__all__'         