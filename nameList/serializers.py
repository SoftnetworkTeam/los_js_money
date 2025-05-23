from abc import ABC

from rest_framework import serializers

from nameList.models import HireContract,Mastercollateralappraiser,Masterproducttype,MasterMortgageType

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
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = MasterBrand
        fields = ['id', 'brand_code', 'brand_name', 'status','full_name']

    def get_full_name(self, obj):
        return f"{obj.brand_code} - {obj.brand_name}"



class MasterModelSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = MasterModel
        fields = ['id', 'model_code', 'model_name', 'brand_id', 'status','full_name']

    def get_full_name(self, obj):
        return f"{obj.model_code} - {obj.model_name}"


class MasterSubModelSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = MasterSubModel
        fields = ['id', 'sub_model_code', 'sub_model_name', 'model_id', 'status','full_name']

    def get_full_name(self, obj):
        return f"{obj.sub_model_code} - {obj.sub_model_name}"


class MasterColorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = MasterColor
        fields = ['id', 'color_code', 'color_name', 'status','full_name']
        
    def get_full_name(self, obj):
        return f"{obj.color_code} - {obj.color_name}"


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
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = MasterProvince
        fields = ['id', 'province_code', 'province_name', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.province_code} - {obj.province_name}"


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

class MastercollateralappraiserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Mastercollateralappraiser
        fields = '__all__'

    def get_full_name(self, obj):
        return f"{obj.appr_code} - {obj.appr_name}"
    
class MasterproducttypeSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Masterproducttype
        fields = '__all__'
        
    def get_full_name(self, obj):
        return f"{obj.product_type_code} - {obj.product_type_name}"

class MasterMortgageTypeSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = MasterMortgageType
        fields = '__all__'
        
    def get_full_name(self, obj):
        return f"{obj.mortgage_code} - {obj.mortgage_name}"