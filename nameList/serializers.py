from abc import ABC

from rest_framework import serializers

from nameList.models import HireContract
from theme.models import MasterTambon, MasterAmphoe, MasterProvince, apmast, MasterBranchAP, MasterOfficer, \
    MasterContractDocument, MasterBank, \
    MasterLivingType, MasterLivingOwner, MasterResidence, MasterNCB, MasterOccupation, MasterNumberOfInstallment, \
    MasterBrand, MasterModel, MasterSubModel, MasterColor, MasterInterestRate, CustomerLoanDetail, IndexHireContract, MasterCustomerPrename,Masterbranch


class CustomDateTimeField(serializers.ReadOnlyField, ABC):
    def to_representation(self, value):
        return value.date() if value else None


class HireContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = HireContract
        fields = '__all__'


class CustomerLoanDetailSerializer(serializers.ModelSerializer):
    create_at_customer = CustomDateTimeField()

    class Meta:
        model = CustomerLoanDetail
        fields = '__all__'


class MasterBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterBrand
        fields = ['id', 'brand_code', 'brand_name', 'status']


class MasterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterModel
        fields = ['id', 'model_code', 'model_name', 'brand_id', 'status']


class MasterSubModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterSubModel
        fields = ['id', 'sub_model_code', 'sub_model_name', 'model_id', 'status']


class MasterColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterColor
        fields = ['id', 'color_code', 'color_name', 'status']


class interestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterInterestRate
        fields = ['id', 'interest']


class MasterNumberOfInstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterNumberOfInstallment
        fields = ['id', 'installment_amount','status']


class MasterOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterOccupation
        fields = ['id', 'occup_name', 'occup_code','status']


class MasterNCBSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterNCB
        fields = ['id', 'name']


class MasterResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterResidence
        fields = ['id', 'residence_name','status']


class MasterLivingOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterLivingOwner
        fields = ['id', 'owner_name','status']


class MasterLivingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterLivingType
        fields = ['id', 'type_name','status']


class MasterBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterBank
        fields = ['id', 'bank_name','status']


class MasterContractDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterContractDocument
        fields = ['id', 'doc_name','status']


class MasterOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterOfficer
        fields = ['id', 'officer_name', 'officer_code']


class MasterBranchAPSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterBranchAP
        fields = ['id', 'branch_name', 'branch_code', 'apmast_id']


class apmastSerializer(serializers.ModelSerializer):
    class Meta:
        model = apmast
        fields = ['idno', 'apname']


class MasterProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProvince
        fields = ['id', 'province_name']


class MasterAmphoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterAmphoe
        fields = ['id', 'amphoe_name', 'province_id']


class MasterTambonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterTambon
        fields = ['id', 'tambon_name', 'amphoe_id', 'postcode']
        
class MasterCustomerPrenameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCustomerPrename
        fields = '__all__'

class MasterbranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masterbranch
        fields = '__all__'