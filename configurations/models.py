from django.db import models

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        
class Masterscoringdetail(models.Model):
    id = models.AutoField(primary_key=True)
    score_type = models.CharField(max_length=20)
    score_id = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    type_id  = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tb_masterscoringdetail'
        
class Mastermonthlysalary(models.Model):
    id = models.AutoField(primary_key=True)
    salary_code = models.CharField(max_length=20)
    salary_name = models.CharField(max_length=100)
    start_salary = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    end_salary = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    status = models.CharField(max_length=20)
    slug  = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_mastermonthlysalary'

class Mastereducationlevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    education_code = models.CharField(unique=True, max_length=20)
    education_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'tb_mastereducationlevel'
        
class Masterminorchildren(models.Model):
    id = models.BigAutoField(primary_key=True)
    children_code = models.CharField(unique=True, max_length=20)
    children_name = models.CharField(max_length=100, blank=True, null=True)
    start_children = models.IntegerField(blank=True, null=True)
    end_children = models.IntegerField(blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'tb_masterminorchildren'        
        
class Masterworkingage(models.Model):
    id = models.BigAutoField(primary_key=True)
    age_code = models.CharField(unique=True, max_length=20)
    age_name = models.CharField(max_length=100, blank=True, null=True)
    start_age = models.IntegerField(blank=True, null=True)
    end_age = models.IntegerField(blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterworkingage'             

class Masterrentalage(models.Model):
    id = models.BigAutoField(primary_key=True)
    age_code = models.CharField(unique=True, max_length=20)
    age_name = models.CharField(max_length=100, blank=True, null=True)
    start_age = models.IntegerField(blank=True, null=True)
    end_age = models.IntegerField(blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'tb_masterrentalage'            
        
class Mastermaritalstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_code = models.CharField(unique=True, max_length=20)
    status_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermaritalstatus'      
        
class Mastercustomerage(models.Model):
    id = models.BigAutoField(primary_key=True)
    age_code = models.CharField(unique=True, max_length=20)
    age_name = models.CharField(max_length=100, blank=True, null=True)
    start_age = models.IntegerField(blank=True, null=True)
    end_age = models.IntegerField(blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        ordering = ['age_name']
        db_table = 'tb_mastercustomerage'          

class Mastershoptypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_code = models.CharField(unique=True, max_length=20)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'tb_mastershoptypes'      

class Masterbusinesstype(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.CharField(unique=True, max_length=20)
    updated_at = models.CharField(max_length=100, blank=True, null=True)
    business_type_code = models.CharField(unique=True, max_length=20)
    business_type_name = models.CharField(unique=True, max_length=100)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)

    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'tb_masterbusinesstype'              

class Mastermonthlyprofit(models.Model):
    id = models.BigAutoField(primary_key=True)
    profit_code = models.CharField(unique=True, max_length=20)
    profit_name = models.CharField(max_length=100, blank=True, null=True)
    start_profit = models.IntegerField(blank=True, null=True)
    end_profit = models.IntegerField(blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'tb_mastermonthlyprofit'          
        
class Masterbusinessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    age_code = models.CharField(unique=True, max_length=20)
    age_name = models.CharField(max_length=100, blank=True, null=True)
    start_age = models.IntegerField(blank=True, null=True)
    end_age = models.IntegerField(blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    class Meta:
        ordering = ['id']
        managed = False
        db_table = 'tb_masterbusinessage'   
                                       
class Masterresidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    residence_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(unique=True, max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    class Meta:
        managed = False
        db_table = 'tb_masterresidence' 
        
class Mastercontractreason(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'tb_mastercontractreason'
        
class Mastercountry(models.Model):
    id = models.BigAutoField(primary_key=True)
    nation_name_th = models.CharField(max_length=100, blank=True, null=True)
    nation_name_en = models.CharField(max_length=100, blank=True, null=True)
    country_name_th = models.CharField(max_length=100, blank=True, null=True)
    country_name_en = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_country'    