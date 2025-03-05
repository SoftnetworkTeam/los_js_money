from abc import ABC

from nameList.models import HireContract
from rest_framework import serializers
from .models import CustomerLoanDetail, InstallmentFile, MasterCustomerPrename,MasterTambon,MasterBranchAP,Masterincomestable,Masterincomenotstable,Masterscoringinfo,CustomerInfo,Masterbranch


class CustomDateTimeField(serializers.ReadOnlyField, ABC):
    def to_representation(self, value):
        return value.date() if value else None


class CustomerLoanDetailSerializer(serializers.ModelSerializer):
    create_at_customer = CustomDateTimeField()

    class Meta:
        model = CustomerLoanDetail
        fields = '__all__'


class MasterCustomerPrenameSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterCustomerPrename
        fields = '__all__'


class InstallmentFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = InstallmentFile
        fields = ['id', 'installment_id', 'name', 'type', 'doc', 'path']
        
class MasterTambonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterTambon
        fields = ['id', 'tambon_name', 'amphoe_id', 'postcode']
        
class MasterBranchAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterBranchAP
        fields = ['id', 'branch_name', 'branch_code', 'apmast_id']
        
class HireContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireContract
        fields = '__all__'

class MasterincomestableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masterincomestable
        fields = '__all__'

class MasterincomenotstableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masterincomenotstable
        fields = '__all__'

class MasterscoringinfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True) 
    first_name = serializers.CharField(read_only=True)  
    class Meta:
        model = Masterscoringinfo
        fields = '__all__'

class CustomerInfoSerializer(serializers.ModelSerializer):
    business_type_name = serializers.CharField(read_only=True) 
    class Meta:
        model = CustomerInfo
        fields = '__all__'

class MasterbranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masterbranch
        fields = '__all__'
