from django.db import models


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
    stable_min = models.DecimalField(max_digits=18, decimal_places=2)
    stable_percent = models.DecimalField(max_digits=18, decimal_places=2)
    not_stable_min = models.DecimalField(max_digits=18, decimal_places=2)
    not_stable_percent = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField() 

    class Meta:
        ordering = ['id']
        db_table = 'tb_customerscore'