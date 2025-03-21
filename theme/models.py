from django.db import models

# Create your models here.
class CustomerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    cust_type = models.CharField(max_length=1)
    cust_code = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, null=True, blank=True)
    card_type = models.CharField(max_length=1)
    card_no = models.CharField(max_length=20)
    birth_date = models.DateField()
    age = models.IntegerField()
    issue_date = models.CharField(max_length=30)
    expire_date = models.CharField(max_length=30)
    nation = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    telephone = models.CharField(max_length=100)
    mobile = models.CharField(max_length=1)
    email = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    refer_name = models.CharField(max_length=50)
    refer_description = models.CharField(max_length=1)
    refer_telephone = models.CharField(max_length=10)
    head_office = models.CharField(max_length=1000)
    branch_no = models.CharField(max_length=1)
    memo = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_grade_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    occupation_id = models.IntegerField()
    pre_name_id = models.IntegerField()
    education_level_id = models.IntegerField()
    user_id = models.IntegerField()
    conversion_id = models.IntegerField()
    refer_name2 = models.CharField(max_length=50)
    refer_description2 = models.CharField(max_length=1)
    refer_telephone2 = models.CharField(max_length=10)
    refer_name3 = models.CharField(max_length=50)
    refer_description3 = models.CharField(max_length=1)
    refer_telephone3 = models.CharField(max_length=10)
    line_id = models.CharField(max_length=100)
    category_occupation = models.IntegerField()
    business_type_id = models.IntegerField()
    shop_type_id = models.IntegerField()
    rentalage_id = models.IntegerField()
    monthlyprofit_id = models.IntegerField()
    businessage_id = models.IntegerField()
    age = models.IntegerField()
    book_no = models.IntegerField()
    book_name = models.CharField(max_length=100)
    guarantor_name = models.CharField(max_length=100)
    country_id = models.IntegerField()
    customer_age_id = models.IntegerField()
    minorchildren_id = models.IntegerField(null=True, blank=True)
    education_level_id = models.IntegerField(null=True, blank=True)
    contract_reason_id = models.IntegerField(null=True, blank=True)
    channel_payment = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'tb_customerinfo'

class Mastercustomerage(models.Model):
    id = models.AutoField(primary_key=True)
    age_code = models.CharField(max_length=20)
    age_name = models.CharField(max_length=20)
    start_age = models.IntegerField()
    end_age = models.IntegerField()
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastercustomerage'
        
class Mastershoptypes(models.Model):
    id = models.AutoField(primary_key=True)
    shop_code = models.CharField(max_length=20)
    shop_name = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastershoptypes'
        
class Masterrentalage(models.Model):
    id = models.AutoField(primary_key=True)
    age_code = models.CharField(max_length=20)
    age_name = models.CharField(max_length=20)
    start_age = models.IntegerField()
    end_age = models.IntegerField()
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterrentalage'
        
class Mastermaritalstatus(models.Model):
    id = models.AutoField(primary_key=True)
    status_code = models.CharField(max_length=20)
    status_name = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastermaritalstatus'
        
class Masterminorchildren(models.Model):
    id = models.AutoField(primary_key=True)
    children_code = models.CharField(max_length=20)
    children_name = models.CharField(max_length=20)
    start_children = models.IntegerField()
    end_children = models.IntegerField()
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterminorchildren'

class Mastereducationlevel(models.Model):
    id = models.AutoField(primary_key=True)
    education_code = models.CharField(max_length=20)
    education_name = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastereducationlevel'


class MasterProvince(models.Model):
    id = models.AutoField(primary_key=True)
    province_code = models.CharField(max_length=20)
    province_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterprovince'


class MasterAmphoe(models.Model):
    id = models.AutoField(primary_key=True)
    province_id = models.IntegerField()
    amphoe_code = models.CharField(max_length=20)
    amphoe_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masteramphoe'


class MasterTambon(models.Model):
    id = models.AutoField(primary_key=True)
    amphoe_id = models.IntegerField()
    tambon_code = models.CharField(max_length=20)
    tambon_name = models.CharField(max_length=100)
    postcode = models.IntegerField()
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastertambon'


class MasterLivingType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterlivingtype'


class MasterLivingOwner(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterlivingowner'


class MasterResidence(models.Model):
    id = models.AutoField(primary_key=True)
    residence_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterresidence'


class CustomerAddress(models.Model):
    id = models.AutoField(primary_key=True)
    send_doc = models.CharField(max_length=1)
    house_no = models.CharField(max_length=200)
    village = models.CharField(max_length=100)
    soi = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    postcode = models.IntegerField()
    telephone = models.CharField(max_length=100)
    relate = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address_id = models.IntegerField()
    customer_id = models.IntegerField()
    tambon = models.ForeignKey(MasterTambon, on_delete=models.CASCADE)
    amphoe = models.ForeignKey(MasterAmphoe, on_delete=models.CASCADE)
    province = models.ForeignKey(MasterProvince, on_delete=models.CASCADE)
    user_id = models.IntegerField()

    living_owner = models.ForeignKey(MasterLivingOwner, on_delete=models.CASCADE)
    living_type = models.ForeignKey(MasterLivingType, on_delete=models.CASCADE)
    living_rental = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    residence = models.ForeignKey(MasterResidence, on_delete=models.CASCADE)

    living_welfare_month = models.IntegerField()
    living_welfare_year = models.IntegerField()
    convert_id = models.IntegerField()
    conversion_id = models.IntegerField()

    class Meta:
        db_table = 'tb_customeraddress'


class CustomerIncome(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    income_name = models.CharField(max_length=100)
    income_type = models.CharField(max_length=1,default='M')
    position = models.CharField(max_length=100)
    office = models.CharField(max_length=200)
    longevity_year = models.IntegerField()
    longevity_month = models.IntegerField()
    longevity_day = models.IntegerField()
    unit = models.CharField(max_length=1)
    base_income = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    income_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_work = models.DateField()
    social_security = models.CharField(max_length=100)
    user_id = models.IntegerField()

    class Meta:
        db_table = 'tb_customerincome'

    def get_prep_value(self, value):
        if value is not None:
            return round(value, 2)
        return value


class CustomerGuarantor(models.Model):
    id = models.AutoField(primary_key=True)
    CustomerID = models.IntegerField()
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    relation = models.CharField(max_length=20)
    name2 = models.CharField(max_length=100)
    tel2 = models.CharField(max_length=20)
    relation2 = models.CharField(max_length=20)
    name3 = models.CharField(max_length=100)
    tel3 = models.CharField(max_length=20)
    relation3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_customerguarantor'


class MasterOfficer(models.Model):
    id = models.AutoField(primary_key=True)
    officer_code = models.CharField(max_length=20)
    officer_name = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    soi = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    postcode = models.IntegerField()
    tax_id = models.CharField(max_length=15)
    telephone = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department_id = models.IntegerField()
    tambon = models.ForeignKey(MasterTambon, on_delete=models.CASCADE)
    amphoe = models.ForeignKey(MasterAmphoe, on_delete=models.CASCADE)
    province = models.ForeignKey(MasterProvince, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    billcoll_status = models.CharField(max_length=1)
    start_period = models.IntegerField()
    end_period = models.IntegerField()

    class Meta:
        db_table = 'tb_masterofficer'


class Distributor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    checker = models.CharField(max_length=100)
    sales_person = models.CharField(max_length=100)

    class Meta:
        db_table = 'tb_distributor'


class InstallmentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    app_id = models.CharField(max_length=20)
    distributor_id = models.IntegerField()
    customer_id = models.IntegerField()
    brand = models.CharField(max_length=20, null=True, blank=True)
    model = models.CharField(max_length=20, null=True, blank=True)
    code_model = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    down_payment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    installment = models.IntegerField()
    price_installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    start_payment = models.DateField(null=True, blank=True)
    guarantee = models.CharField(max_length=20, null=True, blank=True)
    machine_no = models.CharField(max_length=100, null=True, blank=True)
    chassis_no = models.CharField(max_length=100, null=True, blank=True)
    registration_no = models.CharField(max_length=30, null=True, blank=True)
    product_code = models.CharField(max_length=50, null=True, blank=True)
    contract_no_old = models.CharField(max_length=100, null=True, blank=True)
    mileage = models.IntegerField( default=0)
    next_payment = models.DateField()
    beginning_amount = models.IntegerField(default=0)
    date_read_card = models.DateField()
    status_approve = models.IntegerField()
    approve_date = models.DateField()
    user_approve = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    car_type = models.CharField(max_length=1, null=True, blank=True)
    time_of_work = models.CharField(max_length=50, null=True, blank=True)
    holiday = models.CharField(max_length=50, null=True, blank=True)
    contact_time = models.CharField(max_length=50, null=True, blank=True)
    pay_day = models.DateField(null=True)
    bank_id = models.IntegerField(default=0, null=True, blank=True)
    place_of_work = models.CharField(max_length=100, null=True, blank=True)
    sub_model = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ncb_id = models.IntegerField(null=True, blank=True)
    ncb_description = models.CharField(max_length=200, null=True, blank=True)
    issue_cancel = models.CharField(max_length=100, null=True, blank=True)
    company_tel = models.CharField(max_length=100)
    salary_day = models.CharField(max_length=100)
    place_work_tel = models.CharField(max_length=100, null=True, blank=True)
    condition_approve = models.CharField(max_length=200, null=True, blank=True)
    start_work = models.DateField()
    social_security = models.CharField(max_length=100, null=True, blank=True)
    income_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    base_income = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    income_name = models.CharField(max_length=100, null=True, blank=True)
    income_type = models.CharField(max_length=1, default='M')
    position = models.CharField(max_length=100, null=True, blank=True)
    office = models.CharField(max_length=200)
    longevity_year = models.IntegerField()
    longevity_month = models.IntegerField()
    longevity_day = models.IntegerField()
    unit = models.CharField(max_length=1, default='M')
    create_to_branch_id = models.IntegerField()
    debt_in = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    debt_informal = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    create_to_province_id = models.IntegerField()
    company_id = models.IntegerField()
    lending_description = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = 'tb_installmentdetail'


class MasterCifDigit(models.Model):
    id = models.AutoField(primary_key=True)
    cif_digit = models.CharField(max_length=5)
    cif_char = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastercifdigit'


class MasterCustomerPrename(models.Model):
    id = models.AutoField(primary_key=True)
    pre_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastercustomerprename'


class MasterBrand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_code = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterbrand'


class MasterModel(models.Model):
    id = models.AutoField(primary_key=True)
    brand_id = models.IntegerField()
    model_code = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastermodel'


class MasterColor(models.Model):
    id = models.AutoField(primary_key=True)
    color_code = models.CharField(max_length=100)
    color_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastercolor'


class MasterContractDocument(models.Model):
    id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastercontractdocument'

class InstallmentFile(models.Model):
    id = models.AutoField(primary_key=True)
    installment_id = models.IntegerField()
    name = models.FileField()
    type = models.CharField(max_length=200)
    doc = models.ForeignKey(MasterContractDocument, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)

    class Meta:
        db_table = 'tb_installmentfile'


class MasterBank(models.Model):
    id = models.AutoField(primary_key=True)
    bank_code = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    bank_name_en = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterbank'


class MasterInterestRate(models.Model):
    id = models.AutoField(primary_key=True)
    interest = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterinterestrate'


class MasterNumberOfInstallment(models.Model):
    id = models.AutoField(primary_key=True)
    installment_amount = models.IntegerField()
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masternumberofinstallment'


class apmast(models.Model):
    idno = models.AutoField(primary_key=True)
    apcode = models.CharField(max_length=12)
    apname = models.CharField(max_length=100)
    apnmen = models.CharField(max_length=60)
    apaddr1 = models.CharField(max_length=100)
    apaddr2 = models.CharField(max_length=100)
    aptelp = models.CharField(max_length=100)
    apemail = models.CharField(max_length=20)
    apcontact = models.CharField(max_length=20)
    acc_code = models.CharField(max_length=12)
    credtm = models.DecimalField(max_digits=6, decimal_places=0)
    apgrp = models.CharField(max_length=1)
    credamt = models.DecimalField(max_digits=12, decimal_places=2)
    creddisc = models.DecimalField(max_digits=6, decimal_places=2)
    idreg = models.CharField(max_length=20)
    taxid = models.CharField(max_length=20)
    idcard = models.CharField(max_length=20)
    aptypcod = models.CharField(max_length=12)
    aptax = models.CharField(max_length=1)
    apflag = models.CharField(max_length=1)
    memo1 = models.CharField(max_length=512)
    userid = models.CharField(max_length=15)
    inputdt = models.DateField()
    vatrate = models.DecimalField(max_digits=12, decimal_places=0)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    road = models.CharField(max_length=60)
    tumb = models.CharField(max_length=60)
    aump = models.CharField(max_length=60)
    prov = models.CharField(max_length=60)
    zip = models.CharField(max_length=5)
    apaddren1 = models.CharField(max_length=60)
    apaddren2 = models.CharField(max_length=60)
    calcfl = models.CharField(max_length=1)
    paydesc = models.CharField(max_length=100)
    typlocat = models.CharField(max_length=1)
    taxlocat = models.CharField(max_length=5)
    apaddr3 = models.CharField(max_length=60)
    apaddr4 = models.CharField(max_length=60)
    apaddr5 = models.CharField(max_length=60)
    stat = models.CharField(max_length=1)
    buillding = models.CharField(max_length=60)
    village = models.CharField(max_length=60)
    room_no = models.CharField(max_length=60)
    floor = models.CharField(max_length=60)
    soi = models.CharField(max_length=60)
    telp = models.CharField(max_length=60)
    bankcod = models.CharField(max_length=12)
    bookno = models.CharField(max_length=20)

    class Meta:
        db_table = 'apmast'

    def __str__(self):
        return self.apcode


class MasterBranchAP(models.Model):
    id = models.AutoField(primary_key=True)
    apmast = models.ForeignKey(apmast, on_delete=models.PROTECT)
    branch_code = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    moo = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    soi = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    close_date = models.DateField()
    balance_date = models.DateField()
    balance_amt = models.DateField()
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tambon_id = models.IntegerField()
    amphoe_id = models.IntegerField()
    province_id = models.IntegerField()

    class Meta:
        db_table = 'tb_masterbranch_ap'

    def __str__(self):
        return self.branch_code, self.id


class MasterOccupation(models.Model):
    id = models.AutoField(primary_key=True)
    occup_code = models.CharField(max_length=20)
    occup_name = models.CharField(max_length=100)
    occup_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masteroccupation'

class Masterbusinesstype(models.Model):
    id = models.AutoField(primary_key=True)
    business_type_code = models.CharField(max_length=20)
    business_type_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterbusinesstype'

class Mastermonthlyprofit(models.Model):
    id = models.AutoField(primary_key=True)
    profit_code = models.CharField(max_length=20)
    profit_name = models.CharField(max_length=100)
    start_profit = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    start_profit = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastermonthlyprofit'

class Masterbusinessage(models.Model):
    id = models.AutoField(primary_key=True)
    age_code = models.CharField(max_length=20)
    age_name = models.CharField(max_length=100)
    start_age = models.IntegerField()
    start_age = models.IntegerField()
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterbusinessage'

class Mastercontractreason(models.Model):
    id = models.AutoField(primary_key=True)
    reason_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_mastercontractreason'
                
class MasterSubModel(models.Model):
    id = models.AutoField(primary_key=True)
    sub_model_code = models.CharField(max_length=100)
    sub_model_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    model_id = models.IntegerField()

    class Meta:
        db_table = 'tb_mastersubmodel'


class ContractInfo(models.Model):
    id = models.AutoField(primary_key=True)
    cont_type = models.IntegerField()
    cont_no = models.IntegerField()
    cont_date = models.DateField()
    branch_id = models.IntegerField()
    collateral_id = models.IntegerField()
    cont_group_id = models.IntegerField()
    customer_id = models.IntegerField()
    customer_address_id = models.IntegerField()
    send_bill_status = models.CharField(max_length=100)
    price_estimate = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    market_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    market_price2 = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    market_price3 = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    rate_book = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    application_no = models.CharField(max_length=100)
    market_price_avg = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    land_appraisal = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    building_appraisal = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    land_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    building_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True,
                                                        blank=True)
    land_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    building_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    mortgage_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    status = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
    user_cancel_id = models.IntegerField()
    conversion_id = models.IntegerField(null=True, blank=True, verbose_name='Convert data')

    class Meta:
        db_table = 'tb_contractinfo'


class ContractDetail(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.IntegerField()
    restructure_id = models.IntegerField()
    actual_date = models.DateField()
    ar_type = models.CharField(max_length=1)
    payment_terms = models.CharField(max_length=1)
    sequence_method = models.CharField(max_length=1)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    product_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    collateral_vat_rate = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_product_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_product_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    standard_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_standard_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_standard_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    down_payment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_down_payment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_down_payment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    principal = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_principal = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_principal = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest_flat_rate = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest_eff_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0, null=True, blank=True)
    interest_irr_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0, null=True, blank=True)
    fee_flat_rate = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    fee_eff_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0, null=True, blank=True)
    fee_irr_rate = models.DecimalField(max_digits=18, decimal_places=6, default=0, null=True, blank=True)
    period_installment = models.IntegerField()
    period = models.IntegerField()
    pmt = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    last_installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_last_installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_last_installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    installment_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_installment_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_installment_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    fee_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_total_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_total_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    first_due_date = models.DateField()
    last_due_date = models.DateField()
    interest_forward_status = models.CharField(max_length=1)
    penalty_method = models.CharField(max_length=1)
    penalty_late = models.IntegerField()
    penalty_rate = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    revenue_status = models.CharField(max_length=1)
    stop_revenue_date = models.DateField()
    vat_status = models.CharField(max_length=1)
    stop_vat_date = models.DateField()
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField()
    approve_status = models.CharField(max_length=1)
    approve_date = models.DateField()
    paid_status = models.CharField(max_length=1)
    paid_date = models.DateField()
    expense_status = models.CharField(max_length=1)
    memo = models.CharField(max_length=1000)
    status = models.CharField(max_length=1)
    doc_no = models.CharField(max_length=20)
    doc_date = models.DateField()
    billcollector_id = models.IntegerField()
    checker_id = models.IntegerField()
    sale_id = models.IntegerField()
    target_id = models.IntegerField()
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20)
    campaign_id = models.IntegerField()
    invite_id = models.IntegerField()
    invite_name = models.CharField(max_length=100)
    invite_status = models.CharField(max_length=1)
    reason_id = models.IntegerField()
    action_code_id = models.IntegerField()
    hold_status = models.CharField(max_length=1)
    paid_status_ho = models.CharField(max_length=1)
    paid_status_branch = models.CharField(max_length=1)
    dpd = models.IntegerField()
    car_code = models.CharField(max_length=1)
    car_code_date = models.DateField()
    npl_flag = models.CharField(max_length=1)
    npl_first_date = models.DateField()
    npl_curr_date = models.DateField()
    tdr_dpd = models.IntegerField()
    tdr_car_code = models.CharField(max_length=1)
    tdr_monitor = models.CharField(max_length=1)
    tdr_monitor_period = models.IntegerField()
    tdr_result = models.CharField(max_length=1)
    force_car_code = models.CharField(max_length=1)
    tdr_monitor_end = models.CharField(max_length=1)
    tdr_monitor_end_date = models.DateField()
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    discount_method = models.CharField(max_length=1)
    installment_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_installment_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_installment_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    fee_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    straight_line_principal_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True,
                                                          blank=True)
    straight_line_interest_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True,
                                                         blank=True)
    straight_line_fee_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    last_payment_date = models.DateField()
    down_payment_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    penalty_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    installment_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_installment_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_installment_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    principal_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    fee_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    over_due_period = models.IntegerField()
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    straight_line_principal_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True,
                                                           blank=True)
    straight_line_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True,
                                                          blank=True)
    straight_line_fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    next_due_date = models.DateField()
    next_payment_date = models.DateField()
    next_period = models.IntegerField()
    installment_received = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    net_installment_received = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    vat_installment_received = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest_received = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    fee_received = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    straight_line_interest_received = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True,
                                                          blank=True)
    straight_line_fee_received = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    restructure_status = models.CharField(max_length=1)
    restructure_code = models.CharField(max_length=1)
    restructure_date = models.DateField()
    write_off_status = models.CharField(max_length=1)
    write_off_date = models.DateField()
    collateral_state = models.CharField(max_length=1)

    class Meta:
        db_table = 'tb_contractdetail'


class MasterNCB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_masterncb'


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
        ordering = ['id', ]
        verbose_name = 'Index - สัญญาเช่าซื้อ'
        verbose_name_plural = 'Index - สัญญาเช่าซื้อ'

    def __str__(self):
        return self.cont_no


class CollateralDetail(models.Model):
    id = models.AutoField(primary_key=True)
    reg_no = models.CharField(max_length=20, null=True, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    reg_expire = models.DateField(null=True, blank=True)
    manu_year = models.IntegerField(null=True, blank=True)
    mile = models.IntegerField(null=True, blank=True)
    cc = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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


class CustomerLoanDetail(models.Model):
    id = models.AutoField(primary_key=True)
    app_id = models.CharField(max_length=20,null=True)
    distributor_id = models.IntegerField(null=True, blank=True)
    customer_id = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    code_model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    down_payment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    interest = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    installment = models.IntegerField(null=True, blank=True)
    price_installment = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    start_payment = models.DateField()
    guarantee = models.CharField(max_length=20)
    machine_no = models.CharField(max_length=100)
    chassis_no = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=30)
    product_code = models.CharField(max_length=50)
    contract_no_old = models.CharField(max_length=100)
    mileage = models.IntegerField(null=True, blank=True)
    beginning_amount = models.IntegerField(null=True, blank=True)
    date_read_card = models.DateField()
    status_approve = models.IntegerField(null=True, blank=True)
    approve_date = models.DateTimeField()
    user_approve = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    next_payment = models.DateField()
    car_type = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    time_of_work = models.CharField(max_length=50)
    holiday = models.CharField(max_length=50)
    contact_time = models.CharField(max_length=50)
    pay_day = models.DateField()
    bank_id = models.IntegerField(null=True, blank=True)
    place_of_work = models.CharField(max_length=100)
    sub_model = models.CharField(max_length=20)
    ncb_id = models.IntegerField(null=True, blank=True)
    ncb_description = models.CharField(max_length=200)
    issue_cancel = models.CharField(max_length=100)
    company_tel = models.CharField(max_length=100)
    condition_approve = models.CharField(max_length=200)
    place_work_tel = models.CharField(max_length=100)
    salary_day = models.CharField(max_length=100)
    start_work = models.DateField()
    social_security = models.CharField(max_length=100)
    cust_code = models.CharField(max_length=20)
    pre_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=302)
    nick_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    refer_name = models.CharField(max_length=100)
    refer_description = models.CharField(max_length=100)
    refer_telephone = models.CharField(max_length=50)
    refer_name2 = models.CharField(max_length=100)
    refer_description2 = models.CharField(max_length=100)
    refer_telephone2 = models.CharField(max_length=20)
    refer_name3 = models.CharField(max_length=100)
    refer_description3 = models.CharField(max_length=100)
    refer_telephone3 = models.CharField(max_length=20)
    office = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    base_income = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    income_amount = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    apcode = models.CharField(max_length=12)
    apname = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    checker = models.CharField(max_length=100)
    sales_person = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    model_code = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    sub_model_name = models.CharField(max_length=100)
    color_name = models.CharField(max_length=100)
    longevity_year = models.IntegerField(null=True, blank=True, default=0)
    longevity_month = models.IntegerField(null=True, blank=True, default=0)
    unit = models.CharField(max_length=1)
    card_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    idno = models.IntegerField(null=True, blank=True)
    #create_at_customer = models.DateTimeField()
    unit_income = models.CharField(max_length=8)
    n_status_approve = models.IntegerField(null=True, blank=True)
    status_approve_name = models.CharField(max_length=11)
    contact_time = models.CharField(max_length=50)
    income_name = models.CharField(max_length=100)
    longevity_day = models.IntegerField(null=True, blank=True, default=0)
    office = models.CharField(max_length=200)
    income_type = models.CharField(max_length=1)
    marital_status = models.CharField(max_length=1)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    issue_date = models.DateField()
    expire_date = models.DateField()
    occupation_id = models.BigIntegerField(null=True, blank=True)
    occup_name = models.CharField(max_length=100)
    occup_code = models.CharField(max_length=20)
    cont_no = models.CharField(max_length=20)
    cont_status = models.CharField(max_length=1)
    company_id =  models.IntegerField()
    create_to_branch_id =  models.IntegerField()
    guarantor_name = models.CharField(max_length=200)
    category_occupation = models.IntegerField()
    class Meta:
        db_table = 'view_installmentdetail'

class CustomerAddressDetail(models.Model):
    id = models.BigIntegerField(primary_key=True)
    customer_id = models.BigIntegerField(null=False, blank=False)
    address_id = models.BigIntegerField(null=False, blank=False)
    send_doc = models.CharField(max_length=1)
    house_no = models.CharField(max_length=200)
    village = models.CharField(max_length=100)
    soi = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    tambon_id = models.BigIntegerField(null=False, blank=False)
    tambon_code = models.CharField(max_length=20)
    tambon_name = models.CharField(max_length=100)
    amphoe_id = models.BigIntegerField(null=False, blank=False)
    amphoe_code = models.CharField(max_length=20)
    amphoe_name = models.CharField(max_length=100)
    province_id = models.BigIntegerField(null=False, blank=False)
    province_code = models.CharField(max_length=20)
    province_name = models.CharField(max_length=100)
    postcode = models.IntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=100)
    relate = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner_name = models.CharField(max_length=100)
    type_name = models.CharField(max_length=100)
    residence_name = models.CharField(max_length=100)
    living_type = models.CharField(max_length=100)
    living_rental = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    residence_id = models.BigIntegerField()
    living_owner_id = models.BigIntegerField()
    living_type_id = models.BigIntegerField()

    class Meta:
        db_table = 'view_customeraddressdwn'

class Masterincomestable(models.Model):
    id = models.AutoField(primary_key=True)
    grade_code = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = 'tb_masterincomestable'
        
        
class Masterincomenotstable(models.Model):
    id = models.AutoField(primary_key=True)
    grade_code = models.CharField(max_length=20)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        db_table = 'tb_masterincomenotstable'
        
class Masterscoringinfo(models.Model):
    id = models.AutoField(primary_key=True)
    score_name = models.CharField(max_length=100)
    stable_min = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    stable_percent = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    not_stable_min = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    not_stable_percent = models.DecimalField(max_digits=18, decimal_places=2, default=0, null=True, blank=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    user_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['id']
        db_table = 'tb_masterscoringinfo'
        
class Masterbranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_id = models.IntegerField(null=True, blank=True)
    branch_code = models.CharField(max_length=50, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    branch_doc = models.CharField(max_length=255, null=True, blank=True)
    house_no = models.CharField(max_length=50, null=True, blank=True)
    village = models.CharField(max_length=255, null=True, blank=True)
    soi = models.CharField(max_length=255, null=True, blank=True)
    road = models.CharField(max_length=255, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    tax_id = models.CharField(max_length=20, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    head_office = models.CharField(max_length=10, null=True, blank=True)
    branch_no = models.CharField(max_length=10, null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    balance_date = models.DateField(null=True, blank=True)
    balance_amt = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tambon_id = models.IntegerField(null=True, blank=True)
    amphoe_id = models.IntegerField(null=True, blank=True)
    province_id = models.IntegerField(null=True, blank=True)
    bank_id = models.IntegerField(null=True, blank=True)
    bank_branch_id = models.IntegerField(null=True, blank=True)
    book_no = models.CharField(max_length=50, null=True, blank=True)
    cash_card = models.CharField(max_length=50, null=True, blank=True)
    cash_beginning = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    bank_beginning = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        managed = False  
        db_table = 'tb_masterbranch' 
        
class MasterCompany(models.Model):
    id = models.AutoField(primary_key=True)
    company_code = models.CharField(max_length=50, unique=True)
    company_name = models.CharField(max_length=255)
    house_no = models.CharField(max_length=50, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    tax_id = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1) 
    slug = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tambon_id = models.IntegerField(blank=True, null=True)
    amphoe_id = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    max_collection_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    billing_day = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'tb_mastercompany'

class UserBranch(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField() 
    branch_id = models.IntegerField()
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_userbranch'

class LogUserLogin(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-increment primary key
    user_id = models.IntegerField()          # User ID
    company_id = models.IntegerField()       # Company ID
    branch_id = models.IntegerField()        # Branch ID
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the record is created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp when the record is updated

    class Meta:
        db_table = 'log_userlogin'