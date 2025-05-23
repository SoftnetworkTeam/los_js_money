from django.db import models

from theme.models import MasterBrand,MasterModel,MasterSubModel,MasterColor,MasterProvince,MasterAmphoe,MasterTambon,MasterResidence
from userauth.models import AuthUser




class HireContract(models.Model):
    id = models.AutoField(primary_key=True)
    cont_no = models.CharField(max_length=20, null=True, blank=True)
    collateral_id = models.IntegerField(null=True, blank=True)
    customer_name = models.CharField(max_length=301, null=True, blank=True)
    card_no = models.CharField(max_length=20, null=True, blank=True)
    cont_status = models.CharField(max_length=1, null=True, blank=True)
    cont_status_name = models.CharField(max_length=20, null=True, blank=True)
    brand_id = models.CharField(max_length=20, null=True, blank=True)
    brand_code = models.CharField(max_length=20, null=True, blank=True)
    model_id = models.CharField(max_length=20, null=True, blank=True)
    model_code = models.CharField(max_length=20, null=True, blank=True)
    sub_model_id = models.CharField(max_length=20, null=True, blank=True)
    sub_model_code = models.CharField(max_length=20, null=True, blank=True)
    color_id = models.CharField(max_length=20, null=True, blank=True)
    color_code = models.CharField(max_length=20, null=True, blank=True)
    chassis_no = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'view_hirecontractoldcar'
        
class IndexHireContract(models.Model):

    contract_detail_id = models.IntegerField(null=True, blank=True)
    branch_id = models.IntegerField(null=True, blank=True)
    branch_code = models.CharField(max_length=20, null=True, blank=True)
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    ar_type = models.CharField(max_length=1, null=True, blank=True)
    ar_type_name = models.CharField(max_length=20, null=True, blank=True)
    cont_type = models.CharField(max_length=1, null=True, blank=True)
    cont_no = models.CharField(max_length=20, null=True, blank=True)
    cont_date = models.DateField(null=True, blank=True)
    application_no = models.CharField(max_length=20, null=True, blank=True)
    actual_date = models.DateField(null=True, blank=True)
    cont_group_id = models.IntegerField(null=True, blank=True)
    cont_group_code = models.CharField(max_length=20, null=True, blank=True)
    cont_group_name = models.CharField(max_length=100, null=True, blank=True)
    customer_id = models.IntegerField(null=True, blank=True)
    cust_code = models.CharField(max_length=20, null=True, blank=True)
    customer_name = models.CharField(max_length=301, null=True, blank=True)
    card_no = models.CharField(max_length=20, null=True, blank=True)
    customer_slug = models.CharField(max_length=200, null=True, blank=True)
    collateral_id = models.IntegerField(null=True, blank=True)
    collateral_type = models.CharField(max_length=1, null=True, blank=True)
    collateral_type_name = models.CharField(max_length=15, null=True, blank=True)
    chassis_no = models.CharField(max_length=50, null=True, blank=True)
    engine_no = models.CharField(max_length=50, null=True, blank=True)
    reg_no = models.CharField(max_length=30, null=True, blank=True)
    province_name = models.CharField(max_length=100, null=True, blank=True)
    collateral_slug = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=1, null=True, blank=True)
    cont_status = models.CharField(max_length=2, null=True, blank=True)
    cont_status_name = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'index_hirecontract'
        ordering = ['id']
        verbose_name = 'Index - สัญญาเช่าซื้อ'
        verbose_name_plural = 'Index - สัญญาเช่าซื้อ'

    def __str__(self):
        return self.cont_no

class CollateralDetail (models.Model) :
    id = models.AutoField(primary_key=True)
    reg_no = models.CharField(max_length=20, null=True, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    reg_expire = models.DateField(null=True, blank=True)
    manu_year = models.IntegerField(null=True, blank=True)
    mile = models.IntegerField(null=True, blank=True) 
    cc = models.IntegerField(null=True, blank=True) 
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateField()
    updated_at = models.DateField()
    brand_id = models.IntegerField(null=True, blank=True) 
    brand_code = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200)
    collateral_id = models.IntegerField(null=True, blank=True) 
    color_id = models.IntegerField(null=True, blank=True) 
    color_code = models.CharField(max_length=200)
    color_name = models.CharField(max_length=200)
    model_id = models.IntegerField(null=True, blank=True) 
    model_code = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    province_id = models.IntegerField(null=True, blank=True) 
    province_code = models.CharField(max_length=200)
    province_name = models.CharField(max_length=200)
    sub_model_id = models.IntegerField(null=True, blank=True) 
    sub_model_code = models.CharField(max_length=200)
    sub_model_name = models.CharField(max_length=200)
    car_age_month = models.IntegerField(null=True, blank=True) 
    car_age_year = models.IntegerField(null=True, blank=True) 

    class Meta:
        managed = False
        db_table = 'view_collateraldetail1'
        
class customerscore(models.Model):
    id = models.AutoField(primary_key=True)
    installmentdetail_id = models.IntegerField() 
    score_name = models.CharField(max_length=100)
    score_1 = models.DecimalField(max_digits=18, decimal_places=2)
    score_2 = models.DecimalField(max_digits=18, decimal_places=2)
    score_3 = models.DecimalField(max_digits=18, decimal_places=2)
    grade = models.CharField(max_length=6)
    status_approve = models.IntegerField()  
    # stable_min = models.DecimalField(max_digits=18, decimal_places=2)
    # stable_percent = models.DecimalField(max_digits=18, decimal_places=2)
    # not_stable_min = models.DecimalField(max_digits=18, decimal_places=2)
    # not_stable_percent = models.DecimalField(max_digits=18, decimal_places=2)
    minimum_score = models.DecimalField(max_digits=18, decimal_places=2)
    minimum_dept_income = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField() 

    class Meta:
        ordering = ['id']
        db_table = 'tb_customerscore'

class Mastercollateralappraiser(models.Model):
    id = models.BigAutoField(primary_key=True)
    appr_code = models.CharField(unique=True, max_length=20)
    appr_name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    collateral_type1 = models.BooleanField()
    collateral_type2 = models.BooleanField()
    collateral_type3 = models.BooleanField()
    collateral_type4 = models.BooleanField()
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        ordering = ['appr_code', ]
        db_table = 'tb_mastercollateralappraiser'

    def __str__(self):
        return '%s - %s' % (self.appr_code, self.appr_name)
    
class Masterproducttype(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_type_code = models.CharField(unique=True, max_length=20)
    product_type_name = models.CharField(max_length=100, blank=True, null=True)
    collateral_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        ordering = ['product_type_code', ]
        db_table = 'tb_masterproducttype'

class MasterMortgageType(models.Model):
    id = models.BigAutoField(primary_key=True)
    mortgage_code = models.CharField(max_length=20, unique=True, verbose_name='รหัสประเภทการจำนอง')
    mortgage_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='คำอธิบาย')
    status = models.CharField(max_length=1, default='A', verbose_name='สถานะ')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        db_table = 'tb_mastermortgagetype'
        ordering = ['mortgage_code', ]
        verbose_name = 'กำหนดข้อมูลประเภทการจำนอง'
        verbose_name_plural = 'กำหนดข้อมูลประเภทการจำนอง'

    def __str__(self):
        return '%s - %s' % (self.mortgage_code, self.mortgage_name)
    
class Collateralinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral_type = models.CharField(max_length=1)
    product_type = models.ForeignKey(Masterproducttype, models.DO_NOTHING)
    chassis_no = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50)
    appraiser = models.ForeignKey(Mastercollateralappraiser, models.DO_NOTHING, blank=True, null=True)
    appraiser_type = models.CharField(max_length=1)
    ownership = models.CharField(max_length=200, blank=True, null=True)
    date_estimate = models.DateField(blank=True, null=True)
    price_estimate = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    rate_book = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_amount = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_date = models.DateField(blank=True, null=True)
    mortgage_type = models.ForeignKey(MasterMortgageType, models.DO_NOTHING, blank=True, null=True)
    # market_price = models.DecimalField(max_digits=18, decimal_places=2)
    # market_price2 = models.DecimalField(max_digits=18, decimal_places=2)
    # market_price3 = models.DecimalField(max_digits=18, decimal_places=2)
    # market_price_avg = models.DecimalField(max_digits=18, decimal_places=2)
    application_no = models.CharField(max_length=20, default='', null=True, blank=True, verbose_name='เลขที่อนุมัติสินเชื่อ')
    # market_source = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    # market_source2 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    # market_source3 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['id', ]
        db_table = 'tb_Collateralinfo'

class Collateraldetail1(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey(Collateralinfo, models.DO_NOTHING)
    brand = models.ForeignKey(MasterBrand, models.DO_NOTHING)
    model = models.ForeignKey(MasterModel, models.DO_NOTHING)
    sub_model = models.ForeignKey(MasterSubModel, models.DO_NOTHING)
    color = models.ForeignKey(MasterColor, models.DO_NOTHING)
    reg_no = models.CharField(max_length=30, blank=True, null=True)
    province = models.ForeignKey(MasterProvince, models.DO_NOTHING, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    reg_expire = models.DateField(blank=True, null=True)
    manu_year = models.IntegerField(blank=True, null=True)
    mile = models.IntegerField(blank=True, null=True)
    cc = models.IntegerField(blank=True, null=True)
    car_age_month = models.IntegerField(blank=True, null=True)
    car_age_year = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        ordering = ['id']
        db_table = 'tb_collateraldetail1'

class Collateraldetail2(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey(Collateralinfo, models.DO_NOTHING)
    land_no = models.CharField(max_length=20)
    survey_no = models.CharField(max_length=20, blank=True, null=True)
    book_no = models.CharField(max_length=20, blank=True, null=True)
    page_no = models.CharField(max_length=20, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    rai = models.IntegerField(blank=True, null=True)
    ngan = models.IntegerField(blank=True, null=True)
    square_wa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tambon = models.ForeignKey(MasterTambon, models.DO_NOTHING)
    amphoe = models.ForeignKey(MasterAmphoe, models.DO_NOTHING)
    province = models.ForeignKey(MasterProvince, models.DO_NOTHING)
    land_status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        ordering = ['id']
        db_table = 'tb_collateraldetail2'

class Collateraldetail3(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey(Collateralinfo, models.DO_NOTHING)
    land_no = models.CharField(max_length=20, blank=True, null=True)
    survey_no = models.CharField(max_length=20, blank=True, null=True)
    book_no = models.CharField(max_length=20, blank=True, null=True)
    page_no = models.CharField(max_length=20, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    rai = models.IntegerField(blank=True, null=True)
    ngan = models.IntegerField(blank=True, null=True)
    square_wa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    house_no = models.CharField(max_length=100)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    tambon = models.ForeignKey(MasterTambon, models.DO_NOTHING)
    amphoe = models.ForeignKey(MasterAmphoe, models.DO_NOTHING)
    province = models.ForeignKey(MasterProvince, models.DO_NOTHING)
    residence = models.ForeignKey(MasterResidence, models.DO_NOTHING, blank=True, null=True)
    relate = models.CharField(max_length=100, blank=True, null=True)
    usable_area = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    building_age_month = models.IntegerField(blank=True, null=True)
    building_age_year = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        ordering = ['id']
        db_table = 'tb_collateraldetail3'
