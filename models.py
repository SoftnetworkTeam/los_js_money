# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class BatchJoblogdetail(models.Model):
#     job = models.ForeignKey('BatchJobloginfo', models.DO_NOTHING)
#     job_code = models.CharField(max_length=20)
#     job_name = models.CharField(max_length=100, blank=True, null=True)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField(blank=True, null=True)
#     effective_date = models.DateField()
#     job_status = models.BooleanField()
#     message = models.CharField(max_length=1000, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'batch_joblogdetail'


class BatchJobloginfo(models.Model):
    job_type = models.CharField(max_length=1)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    effective_date = models.DateField()
    job_total = models.IntegerField(blank=True, null=True)
    job_success = models.IntegerField(blank=True, null=True)
    job_error = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('BatchUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_jobloginfo'


class BatchMainmenu(models.Model):
    menu_code = models.CharField(unique=True, max_length=20)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    menu_group_code = models.CharField(max_length=20, blank=True, null=True)
    menu_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_mainmenu'


class BatchMenuuser(models.Model):
    flg_access = models.BooleanField()
    flg_create = models.BooleanField()
    flg_update = models.BooleanField()
    flg_delete = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    menu = models.ForeignKey(BatchMainmenu, models.DO_NOTHING)
    user = models.ForeignKey('BatchUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch_menuuser'


class BatchUser(models.Model):
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'batch_user'


class BatchUserlog(models.Model):
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    username = models.CharField(max_length=150)
    menu = models.ForeignKey(BatchMainmenu, models.DO_NOTHING)
    user = models.ForeignKey(BatchUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'batch_userlog'


class TbArcollection(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    collection_no = models.CharField(unique=True, max_length=20)
    collection_date = models.DateField()
    cont_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    collection = models.ForeignKey('TbMastercollection', models.DO_NOTHING)
    collection_status = models.CharField(max_length=1)
    appointment_status = models.CharField(max_length=1)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    alert = models.CharField(max_length=1)
    dtstart_message = models.DateField(blank=True, null=True)
    dtstop_message = models.DateField(blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arcollection'


class TbArhold(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    hold_no = models.CharField(unique=True, max_length=20)
    hold_date = models.DateField()
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    cont_type = models.CharField(max_length=1)
    cont_status_date = models.DateField()
    branch_stk = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    hold_amount = models.DecimalField(max_digits=18, decimal_places=2)
    confirm_status = models.CharField(max_length=1)
    confirm_date = models.DateField(blank=True, null=True)
    confirm_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    confirm_id = models.BigIntegerField()
    redeem_status = models.CharField(max_length=1)
    com_amount = models.DecimalField(max_digits=18, decimal_places=2)
    cont_group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING)
    follow = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    hold = models.ForeignKey('TbMasterhold', models.DO_NOTHING)
    old_cont_group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_close_acc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    officer = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    active_post_gl = models.CharField(max_length=1, blank=True, null=True)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1, blank=True, null=True)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arhold'


class TbArholdforsale(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    forsale_no = models.CharField(unique=True, max_length=20)
    forsale_date = models.DateField()
    arhold = models.ForeignKey(TbArhold, models.DO_NOTHING)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    cont_type = models.CharField(max_length=1)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    cost_value = models.DecimalField(max_digits=18, decimal_places=2)
    selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    net_selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    vat_selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField(blank=True, null=True)
    confirm_status = models.CharField(max_length=1)
    confirm_date = models.DateField(blank=True, null=True)
    confirm_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_close_acc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    officer = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arholdforsale'


class TbArholdtosold(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField()
    arholdforsale = models.ForeignKey(TbArholdforsale, models.DO_NOTHING)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    cont_type = models.CharField(max_length=1)
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    confirm_status = models.CharField(max_length=1)
    confirm_date = models.DateField(blank=True, null=True)
    confirm_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    officer = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    auction_type = models.CharField(max_length=1, blank=True, null=True)
    auction_id = models.BigIntegerField(blank=True, null=True)
    cost_value = models.DecimalField(max_digits=18, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    net_selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    vat_selling_price = models.DecimalField(max_digits=18, decimal_places=2)
    selling_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    profit_and_loss = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_close_acc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    user_cancel_date = models.DateField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arholdtosold'


class TbArholdupimg(models.Model):
    id = models.BigAutoField(primary_key=True)
    hold_no = models.CharField(max_length=20, blank=True, null=True)
    arhold_id = models.BigIntegerField(blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)
    contract_detail_id = models.BigIntegerField(blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    file_path = models.CharField(max_length=100, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    file_type = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arholdupimg'


class TbArletterdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    arletter = models.ForeignKey('TbArletterinfo', models.DO_NOTHING)
    cont_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    billcoll = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    due_date = models.DateField()
    period = models.IntegerField()
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    over_due_amount = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_amount = models.DecimalField(max_digits=18, decimal_places=2)
    collection_amount = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arletterdetail'


class TbArletterinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField()
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    cont_group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING, blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    due_date = models.DateField()
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_arletterinfo'


class TbArotherdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    other = models.ForeignKey('TbArotherinfo', models.DO_NOTHING)
    cont_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    payfor = models.ForeignKey('TbMasterpayfor', models.DO_NOTHING)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    payment = models.DecimalField(max_digits=18, decimal_places=2)
    total_payment = models.DecimalField(max_digits=18, decimal_places=2)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arotherdetail'


class TbArotherinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    other_no = models.CharField(unique=True, max_length=20)
    other_date = models.DateField()
    other_type = models.CharField(max_length=1)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    cont_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_arotherinfo'


class TbArredeem(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    redeem_no = models.CharField(unique=True, max_length=20)
    redeem_date = models.DateField()
    arhold = models.ForeignKey(TbArhold, models.DO_NOTHING)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    cont_type = models.CharField(max_length=1)
    penalty = models.DecimalField(max_digits=18, decimal_places=2)
    discount_penalty = models.DecimalField(max_digits=18, decimal_places=2)
    discount_hold_amount = models.DecimalField(max_digits=18, decimal_places=2)
    confirm_status = models.CharField(max_length=1)
    confirm_date = models.DateField(blank=True, null=True)
    confirm_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    cont_group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_close_acc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    request_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    officer = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arredeem'


class TbArwriteoff(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField()
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_type = models.CharField(max_length=1)
    cont_no = models.CharField(max_length=20)
    cause_writeoff = models.ForeignKey('TbMasterwriteoff', models.DO_NOTHING, blank=True, null=True)
    writeoff_type = models.CharField(max_length=1)
    write_off_amount = models.DecimalField(max_digits=18, decimal_places=2)
    write_off_used = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_close_acc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_arwriteoff'


class TbBillingconfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    grace_period = models.IntegerField()
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_billingconfig'


class TbCancelmemo(models.Model):
    id = models.BigAutoField(primary_key=True)
    sys_type = models.CharField(max_length=1)
    ref_id = models.IntegerField()
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    canceled_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cancelmemo'


class TbChangecollateralinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    change = models.ForeignKey('TbChangecontractinfo', models.DO_NOTHING)
    data_status = models.CharField(max_length=1)
    collateral_type = models.CharField(max_length=1)
    collateral = models.ForeignKey('TbCollateralinfo', models.DO_NOTHING)
    collateral_detail_id = models.BigIntegerField(blank=True, null=True)
    chassis_no = models.CharField(max_length=50)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_changecollateralinfo'


class TbChangecontractdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    change = models.ForeignKey('TbChangecontractinfo', models.DO_NOTHING)
    data_status = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_type = models.CharField(max_length=1)
    cont_no = models.CharField(max_length=20)
    doc_no = models.CharField(max_length=20, blank=True, null=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    send_bill_status = models.CharField(max_length=1, blank=True, null=True)
    discount_method = models.CharField(max_length=1, blank=True, null=True)
    penalty_method = models.CharField(max_length=1)
    penalty_late = models.IntegerField()
    penalty_rate = models.DecimalField(max_digits=18, decimal_places=2)
    billcollector_id = models.BigIntegerField()
    checker_id = models.BigIntegerField()
    sale_id = models.BigIntegerField()
    target_id = models.BigIntegerField()
    expense_status = models.CharField(max_length=1)
    campaign = models.ForeignKey('TbMastercampaign', models.DO_NOTHING, blank=True, null=True)
    invite_id = models.BigIntegerField(blank=True, null=True)
    invite_name = models.CharField(max_length=100, blank=True, null=True)
    invite_status = models.CharField(max_length=1)
    reason_id = models.BigIntegerField(blank=True, null=True)
    appraiser = models.ForeignKey('TbMastercollateralappraiser', models.DO_NOTHING, blank=True, null=True)
    appraiser_type = models.CharField(max_length=1)
    ownership = models.CharField(max_length=200, blank=True, null=True)
    date_estimate = models.DateField(blank=True, null=True)
    price_estimate = models.DecimalField(max_digits=18, decimal_places=2)
    rate_book = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_amount = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_date = models.DateField(blank=True, null=True)
    mortgage_type = models.ForeignKey('TbMastermortgagetype', models.DO_NOTHING, blank=True, null=True)
    market_price = models.DecimalField(max_digits=18, decimal_places=2)
    market_price2 = models.DecimalField(max_digits=18, decimal_places=2)
    market_price3 = models.DecimalField(max_digits=18, decimal_places=2)
    market_price_avg = models.DecimalField(max_digits=18, decimal_places=2)
    market_source = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    market_source2 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    market_source3 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    collateral_state = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tb_changecontractdetail'


class TbChangecontractexpense(models.Model):
    id = models.BigAutoField(primary_key=True)
    change = models.ForeignKey('TbChangecontractinfo', models.DO_NOTHING)
    data_status = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_type = models.CharField(max_length=1)
    cont_no = models.CharField(max_length=20)
    payfor = models.ForeignKey('TbMasterpayfor', models.DO_NOTHING)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    paid = models.DecimalField(max_digits=18, decimal_places=2)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_changecontractexpense'


class TbChangecontractguarantor(models.Model):
    id = models.BigAutoField(primary_key=True)
    change = models.ForeignKey('TbChangecontractinfo', models.DO_NOTHING)
    data_status = models.CharField(max_length=1)
    guarantor_type = models.CharField(max_length=1)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    relation = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_changecontractguarantor'


class TbChangecontractinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    change_no = models.CharField(unique=True, max_length=20)
    change_date = models.DateField()
    contract_type = models.CharField(max_length=1)
    contract_id = models.IntegerField()
    contract_detail_id = models.IntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    change_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_changecontractinfo'


class TbChangecustomeraddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    change = models.ForeignKey(TbChangecontractinfo, models.DO_NOTHING)
    data_status = models.CharField(max_length=1)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    customer_address_id = models.BigIntegerField()
    send_bill_status = models.CharField(max_length=1)
    address = models.ForeignKey('TbMastercustomeraddress', models.DO_NOTHING)
    send_doc = models.CharField(max_length=1)
    house_no = models.CharField(max_length=100)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    amphoe = models.ForeignKey('TbMasteramphoe', models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    postcode = models.IntegerField(blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    relate = models.CharField(max_length=100, blank=True, null=True)
    living_owner_id = models.BigIntegerField(blank=True, null=True)
    living_type_id = models.BigIntegerField(blank=True, null=True)
    living_rental = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    living_welfare_month = models.IntegerField(blank=True, null=True)
    living_welfare_year = models.IntegerField(blank=True, null=True)
    residence_id = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_changecustomeraddress'


class TbChangecustomerinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    change = models.ForeignKey(TbChangecontractinfo, models.DO_NOTHING)
    data_status = models.CharField(max_length=1)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    customer_address_id = models.BigIntegerField()
    cust_type = models.CharField(max_length=1)
    cust_code = models.CharField(max_length=20)
    card_no = models.CharField(max_length=20)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_changecustomerinfo'


class TbCollateraldetail1(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey('TbCollateralinfo', models.DO_NOTHING)
    brand = models.ForeignKey('TbMasterbrand', models.DO_NOTHING)
    model = models.ForeignKey('TbMastermodel', models.DO_NOTHING)
    sub_model = models.ForeignKey('TbMastersubmodel', models.DO_NOTHING)
    color = models.ForeignKey('TbMastercolor', models.DO_NOTHING)
    reg_no = models.CharField(max_length=30, blank=True, null=True)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING, blank=True, null=True)
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
        managed = False
        db_table = 'tb_collateraldetail1'


class TbCollateraldetail2(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey('TbCollateralinfo', models.DO_NOTHING)
    land_no = models.CharField(max_length=20)
    survey_no = models.CharField(max_length=20, blank=True, null=True)
    book_no = models.CharField(max_length=20, blank=True, null=True)
    page_no = models.CharField(max_length=20, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    rai = models.IntegerField(blank=True, null=True)
    ngan = models.IntegerField(blank=True, null=True)
    square_wa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    amphoe = models.ForeignKey('TbMasteramphoe', models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    land_status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_collateraldetail2'


class TbCollateraldetail3(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey('TbCollateralinfo', models.DO_NOTHING)
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
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    amphoe = models.ForeignKey('TbMasteramphoe', models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    residence = models.ForeignKey('TbMasterresidence', models.DO_NOTHING, blank=True, null=True)
    relate = models.CharField(max_length=100, blank=True, null=True)
    usable_area = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    building_age_month = models.IntegerField(blank=True, null=True)
    building_age_year = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_collateraldetail3'


class TbCollateralinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral_type = models.CharField(max_length=1)
    product_type = models.ForeignKey('TbMasterproducttype', models.DO_NOTHING)
    chassis_no = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50)
    appraiser = models.ForeignKey('TbMastercollateralappraiser', models.DO_NOTHING, blank=True, null=True)
    appraiser_type = models.CharField(max_length=1)
    ownership = models.CharField(max_length=200, blank=True, null=True)
    date_estimate = models.DateField(blank=True, null=True)
    price_estimate = models.DecimalField(max_digits=18, decimal_places=2)
    rate_book = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_amount = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_date = models.DateField(blank=True, null=True)
    mortgage_type = models.ForeignKey('TbMastermortgagetype', models.DO_NOTHING, blank=True, null=True)
    market_price = models.DecimalField(max_digits=18, decimal_places=2)
    market_price2 = models.DecimalField(max_digits=18, decimal_places=2)
    market_price3 = models.DecimalField(max_digits=18, decimal_places=2)
    market_price_avg = models.DecimalField(max_digits=18, decimal_places=2)
    market_source = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    market_source2 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    market_source3 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_collateralinfo'


class TbCollateralinsure(models.Model):
    id = models.BigAutoField(primary_key=True)
    collateral = models.ForeignKey(TbCollateralinfo, models.DO_NOTHING)
    insure_no = models.CharField(max_length=50, blank=True, null=True)
    insure_date = models.DateField(blank=True, null=True)
    insure_expire = models.DateField(blank=True, null=True)
    insure = models.ForeignKey('TbMasterinsure', models.DO_NOTHING, blank=True, null=True)
    insure_type = models.ForeignKey('TbMasterinsuretype', models.DO_NOTHING)
    insure_type_other = models.CharField(max_length=200, blank=True, null=True)
    insured_capital = models.DecimalField(max_digits=18, decimal_places=2)
    insured_premium = models.DecimalField(max_digits=18, decimal_places=2)
    premium_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    duty_stamp = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    premium_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    assured1 = models.CharField(max_length=200, blank=True, null=True)
    assured2 = models.CharField(max_length=200, blank=True, null=True)
    expense_status = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    pn_no = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)
    contract_detail_id = models.IntegerField(blank=True, null=True)
    contract_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_collateralinsure'


class TbConfirmtohold(models.Model):
    id = models.BigAutoField(primary_key=True)
    waitconfirm = models.ForeignKey('TbWaitconfirmtoholdinfo', models.DO_NOTHING)
    waitconfirm_detail = models.ForeignKey('TbWaitconfirmtoholddetail', models.DO_NOTHING)
    cont_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    approved_date = models.DateField()
    confirm_status = models.CharField(max_length=1)
    confirm_date = models.DateField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    tdr_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_close_acc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    payment_info_id = models.BigIntegerField(blank=True, null=True)
    officer = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    officer_approved = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_confirmtohold'


class TbContgroupmapcodegl(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING)
    map_id = models.BigIntegerField()
    map_name = models.CharField(max_length=100, blank=True, null=True)
    map_type = models.CharField(max_length=1)
    account_code = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_contgroupmapcodegl'


class TbContgroupsequence(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=1)
    group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING)
    sequence_no = models.IntegerField()
    sequence_code = models.CharField(max_length=1)
    sequence_name = models.CharField(max_length=100, blank=True, null=True)
    sequence_fee = models.IntegerField()
    sequence_interest = models.IntegerField()
    sequence_principal = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_contgroupsequence'


class TbContractdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey('TbContractinfo', models.DO_NOTHING)
    restructure_id = models.BigIntegerField(blank=True, null=True)
    actual_date = models.DateField()
    ar_type = models.CharField(max_length=1)
    payment_terms = models.CharField(max_length=1)
    sequence_method = models.CharField(max_length=1)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    product_price = models.DecimalField(max_digits=18, decimal_places=2)
    collateral_vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    net_product_price = models.DecimalField(max_digits=18, decimal_places=2)
    vat_product_price = models.DecimalField(max_digits=18, decimal_places=2)
    standard_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_standard_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_standard_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    down_payment = models.DecimalField(max_digits=18, decimal_places=2)
    net_down_payment = models.DecimalField(max_digits=18, decimal_places=2)
    vat_down_payment = models.DecimalField(max_digits=18, decimal_places=2)
    principal = models.DecimalField(max_digits=18, decimal_places=2)
    net_principal = models.DecimalField(max_digits=18, decimal_places=2)
    vat_principal = models.DecimalField(max_digits=18, decimal_places=2)
    interest_flat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    interest_eff_rate = models.DecimalField(max_digits=18, decimal_places=6)
    interest_irr_rate = models.DecimalField(max_digits=18, decimal_places=6)
    fee_flat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    fee_eff_rate = models.DecimalField(max_digits=18, decimal_places=6)
    fee_irr_rate = models.DecimalField(max_digits=18, decimal_places=6)
    period_installment = models.IntegerField()
    period = models.IntegerField()
    pmt = models.DecimalField(max_digits=18, decimal_places=2)
    installment = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment = models.DecimalField(max_digits=18, decimal_places=2)
    last_installment = models.DecimalField(max_digits=18, decimal_places=2)
    net_last_installment = models.DecimalField(max_digits=18, decimal_places=2)
    vat_last_installment = models.DecimalField(max_digits=18, decimal_places=2)
    installment_amount = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_amount = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_amount = models.DecimalField(max_digits=18, decimal_places=2)
    interest_amount = models.DecimalField(max_digits=18, decimal_places=2)
    fee_amount = models.DecimalField(max_digits=18, decimal_places=2)
    total_amount = models.DecimalField(max_digits=18, decimal_places=2)
    net_total_amount = models.DecimalField(max_digits=18, decimal_places=2)
    vat_total_amount = models.DecimalField(max_digits=18, decimal_places=2)
    first_due_date = models.DateField()
    last_due_date = models.DateField()
    interest_forward_status = models.CharField(max_length=1)
    penalty_method = models.CharField(max_length=1)
    penalty_late = models.IntegerField()
    penalty_rate = models.DecimalField(max_digits=18, decimal_places=2)
    revenue_status = models.CharField(max_length=1)
    stop_revenue_date = models.DateField(blank=True, null=True)
    vat_status = models.CharField(max_length=1)
    stop_vat_date = models.DateField(blank=True, null=True)
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField(blank=True, null=True)
    approve_status = models.CharField(max_length=1)
    approve_date = models.DateField(blank=True, null=True)
    paid_status = models.CharField(max_length=1)
    paid_date = models.DateField(blank=True, null=True)
    expense_status = models.CharField(max_length=1)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    doc_no = models.CharField(max_length=20, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    billcollector = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    checker = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    sale = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    target = models.ForeignKey('TbMastertarget', models.DO_NOTHING)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    campaign = models.ForeignKey('TbMastercampaign', models.DO_NOTHING, blank=True, null=True)
    invite = models.ForeignKey('TbMasterinvitation', models.DO_NOTHING, blank=True, null=True)
    invite_name = models.CharField(max_length=100, blank=True, null=True)
    invite_status = models.CharField(max_length=1)
    reason = models.ForeignKey('TbMastercontractreason', models.DO_NOTHING, blank=True, null=True)
    action_code_id = models.BigIntegerField(blank=True, null=True)
    hold_status = models.ForeignKey('TbMasterholdstatus', models.DO_NOTHING, db_column='hold_status', blank=True, null=True)
    paid_status_ho = models.CharField(max_length=1, blank=True, null=True)
    paid_status_branch = models.CharField(max_length=1, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    car_code = models.CharField(max_length=1, blank=True, null=True)
    car_code_date = models.DateField(blank=True, null=True)
    npl_flag = models.CharField(max_length=1, blank=True, null=True)
    npl_first_date = models.DateField(blank=True, null=True)
    npl_curr_date = models.DateField(blank=True, null=True)
    tdr_dpd = models.IntegerField(blank=True, null=True)
    tdr_car_code = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_period = models.IntegerField(blank=True, null=True)
    tdr_result = models.CharField(max_length=1, blank=True, null=True)
    force_car_code = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_end = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_end_date = models.DateField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    discount_method = models.CharField(max_length=1)
    installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    last_payment_date = models.DateField(blank=True, null=True)
    down_payment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    installment_due = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_due = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_due = models.DecimalField(max_digits=18, decimal_places=2)
    fee_due = models.DecimalField(max_digits=18, decimal_places=2)
    over_due_period = models.IntegerField()
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    next_due_date = models.DateField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    next_period = models.IntegerField()
    installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    restructure_status = models.CharField(max_length=1)
    restructure_code = models.CharField(max_length=1, blank=True, null=True)
    restructure_date = models.DateField(blank=True, null=True)
    write_off_status = models.CharField(max_length=1)
    write_off_date = models.DateField(blank=True, null=True)
    collateral_state = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tb_contractdetail'


class TbContractdocumentfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    document = models.ForeignKey('TbMastercontractdocument', models.DO_NOTHING)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    file_path = models.CharField(max_length=100)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_contractdocumentfile'


class TbContractexpense(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey('TbContractinfo', models.DO_NOTHING)
    payfor = models.ForeignKey('TbMasterpayfor', models.DO_NOTHING)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    paid = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_contractexpense'


class TbContractguarantor(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey('TbContractinfo', models.DO_NOTHING)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    guarantor_type = models.CharField(max_length=1)
    relation = models.CharField(max_length=50, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_contractguarantor'


class TbContractinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cont_type = models.CharField(max_length=1)
    cont_no = models.CharField(unique=True, max_length=20)
    cont_date = models.DateField()
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    collateral = models.ForeignKey(TbCollateralinfo, models.DO_NOTHING)
    cont_group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    customer_address = models.ForeignKey('TbCustomeraddress', models.DO_NOTHING)
    send_bill_status = models.CharField(max_length=1)
    price_estimate = models.DecimalField(max_digits=18, decimal_places=2)
    market_price = models.DecimalField(max_digits=18, decimal_places=2)
    market_price2 = models.DecimalField(max_digits=18, decimal_places=2)
    market_price3 = models.DecimalField(max_digits=18, decimal_places=2)
    rate_book = models.DecimalField(max_digits=18, decimal_places=2)
    application_no = models.CharField(max_length=20, blank=True, null=True)
    market_price_avg = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_amount = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_contractinfo'


class TbContractinsure(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    insure_no = models.CharField(max_length=50, blank=True, null=True)
    insure_date = models.DateField(blank=True, null=True)
    insure_expire = models.DateField(blank=True, null=True)
    insure = models.ForeignKey('TbMasterinsure', models.DO_NOTHING, blank=True, null=True)
    insure_type = models.ForeignKey('TbMasterinsuretype', models.DO_NOTHING)
    insure_type_other = models.CharField(max_length=200, blank=True, null=True)
    insured_capital = models.DecimalField(max_digits=18, decimal_places=2)
    insured_premium = models.DecimalField(max_digits=18, decimal_places=2)
    premium_vat = models.DecimalField(max_digits=18, decimal_places=2)
    duty_stamp = models.DecimalField(max_digits=18, decimal_places=2)
    premium_total = models.DecimalField(max_digits=18, decimal_places=2)
    assured1 = models.CharField(max_length=200, blank=True, null=True)
    assured2 = models.CharField(max_length=200, blank=True, null=True)
    expense_status = models.CharField(max_length=1, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_contractinsure'


class TbContractothercharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbContractdetail, models.DO_NOTHING)
    payfor = models.ForeignKey('TbMasterpayfor', models.DO_NOTHING)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    paid = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_contractothercharge'


class TbContractperiod(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbContractdetail, models.DO_NOTHING)
    period = models.IntegerField()
    due_date = models.DateField()
    due_days = models.IntegerField()
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    installment = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    principal = models.DecimalField(max_digits=18, decimal_places=2)
    interest = models.DecimalField(max_digits=18, decimal_places=2)
    fee = models.DecimalField(max_digits=18, decimal_places=2)
    net_principal = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee = models.DecimalField(max_digits=18, decimal_places=2)
    cover_date = models.DateField(blank=True, null=True)
    cover_amount = models.DecimalField(max_digits=18, decimal_places=2)
    payment_date = models.DateField(blank=True, null=True)
    payment = models.DecimalField(max_digits=18, decimal_places=2)
    net_payment = models.DecimalField(max_digits=18, decimal_places=2)
    vat_payment = models.DecimalField(max_digits=18, decimal_places=2)
    principal_paid = models.DecimalField(max_digits=18, decimal_places=2)
    interest_paid = models.DecimalField(max_digits=18, decimal_places=2)
    fee_paid = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_paid = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_paid = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_paid = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    arletter_id = models.BigIntegerField(blank=True, null=True)
    collection_amount = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    penalty_day = models.IntegerField()
    penalty_amount = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_paid_date = models.DateField(blank=True, null=True)
    penalty_paid = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_contractperiod'


class TbContractrevenue(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey(TbContractinfo, models.DO_NOTHING)
    contract_detail = models.ForeignKey(TbContractdetail, models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    days_period = models.IntegerField(blank=True, null=True)
    interest_flat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    fee_flat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    interest = models.DecimalField(max_digits=18, decimal_places=2)
    fee = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee = models.DecimalField(max_digits=18, decimal_places=2)
    revenue_status = models.CharField(max_length=1)
    payment_id = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_contractrevenue'


class TbContractrevenueperiod(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey(TbContractinfo, models.DO_NOTHING)
    contract_detail = models.ForeignKey(TbContractdetail, models.DO_NOTHING)
    period = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    days_period = models.IntegerField(blank=True, null=True)
    interest_flat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    fee_flat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    interest = models.DecimalField(max_digits=18, decimal_places=2)
    fee = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee = models.DecimalField(max_digits=18, decimal_places=2)
    revenue_status = models.CharField(max_length=1)
    payment_id = models.BigIntegerField(blank=True, null=True)
    post_gl = models.CharField(max_length=1)
    voucher_no = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    unearned = models.CharField(max_length=1)
    unearned_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_contractrevenueperiod'


class TbCreditlimit(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    credit_no = models.CharField(max_length=20)
    credit_date = models.DateField()
    credit_sequence = models.IntegerField()
    credit_limit = models.DecimalField(max_digits=18, decimal_places=2)
    credit_using = models.DecimalField(max_digits=18, decimal_places=2)
    credit_hold = models.DecimalField(max_digits=18, decimal_places=2)
    credit_balance = models.DecimalField(max_digits=18, decimal_places=2)
    credit_apply_date = models.DateField(blank=True, null=True)
    credit_status = models.CharField(max_length=1)
    approve_status = models.CharField(max_length=1)
    approve_date = models.DateField(blank=True, null=True)
    approve = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_creditlimit'


class TbCustomeraddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    send_doc = models.CharField(max_length=1)
    house_no = models.CharField(max_length=200)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    relate = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    address = models.ForeignKey('TbMastercustomeraddress', models.DO_NOTHING)
    amphoe = models.ForeignKey('TbMasteramphoe', models.DO_NOTHING)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    living_owner = models.ForeignKey('TbMasterlivingowner', models.DO_NOTHING, blank=True, null=True)
    living_type = models.ForeignKey('TbMasterlivingtype', models.DO_NOTHING, blank=True, null=True)
    living_rental = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    living_welfare_month = models.IntegerField(blank=True, null=True)
    living_welfare_year = models.IntegerField(blank=True, null=True)
    convert_id = models.IntegerField(blank=True, null=True)
    residence = models.ForeignKey('TbMasterresidence', models.DO_NOTHING, blank=True, null=True)
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_customeraddress'


class TbCustomerexpense(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    expense_name = models.CharField(max_length=100, blank=True, null=True)
    expense_type = models.CharField(max_length=1)
    note = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=1)
    expense_amount = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_customerexpense'


class TbCustomerincome(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('TbCustomerinfo', models.DO_NOTHING)
    income_name = models.CharField(max_length=100, blank=True, null=True)
    income_type = models.CharField(max_length=1)
    position = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=200, blank=True, null=True)
    longevity_year = models.IntegerField(blank=True, null=True)
    longevity_month = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=1)
    income_amount = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_customerincome'


class TbCustomerinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cust_type = models.CharField(max_length=1)
    cust_code = models.CharField(unique=True, max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    card_type = models.CharField(max_length=1)
    card_no = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    nation = models.CharField(max_length=30, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=1, blank=True, null=True)
    refer_name = models.CharField(max_length=100, blank=True, null=True)
    refer_description = models.CharField(max_length=100, blank=True, null=True)
    refer_telephone = models.CharField(max_length=50, blank=True, null=True)
    head_office = models.CharField(max_length=1)
    branch_no = models.CharField(max_length=10, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer_grade = models.ForeignKey('TbMastercustomergrade', models.DO_NOTHING, blank=True, null=True)
    customer_group = models.ForeignKey('TbMastercustomergroup', models.DO_NOTHING, blank=True, null=True)
    occupation = models.ForeignKey('TbMasteroccupation', models.DO_NOTHING, blank=True, null=True)
    pre_name = models.ForeignKey('TbMastercustomerprename', models.DO_NOTHING)
    education_level = models.ForeignKey('TbMastereducationlevel', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_customerinfo'


class TbDocumentrunning(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    document = models.ForeignKey('TbMasterdocument', models.DO_NOTHING)
    running = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_documentrunning'


class TbEditactioncode(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField()
    contract_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    n_action_code = models.ForeignKey('TbMasteractioncode', models.DO_NOTHING, blank=True, null=True)
    o_action_code = models.ForeignKey('TbMasteractioncode', models.DO_NOTHING, blank=True, null=True)
    n_billcollector = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    o_billcollector = models.ForeignKey('TbMasterofficer', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_editactioncode'


class TbEffarcollection(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField()
    contract_detail = models.ForeignKey('TbEffcontractdetail', models.DO_NOTHING)
    next_payment_date = models.DateField(blank=True, null=True)
    dpd = models.IntegerField()
    over_due_period = models.IntegerField()
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    collection_amount = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effarcollection'


class TbEffarletter(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField()
    contract_detail = models.ForeignKey('TbEffcontractdetail', models.DO_NOTHING)
    principle_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    dpd = models.IntegerField()
    over_due_period = models.IntegerField()
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principle_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effarletter'


class TbEffcontractbeginning(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey('TbEffcontractinfo', models.DO_NOTHING)
    contract_detail = models.ForeignKey('TbEffcontractdetail', models.DO_NOTHING)
    begining_date = models.DateField()
    current_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_accrued = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_amont = models.DecimalField(max_digits=18, decimal_places=2)
    next_due_date = models.DateField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    dpd = models.IntegerField()
    over_due_period = models.IntegerField()
    installment_partial = models.DecimalField(max_digits=18, decimal_places=2)
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    period_begin = models.IntegerField()
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_effcontractbeginning'


class TbEffcontractbilling(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey('TbEffcontractdetail', models.DO_NOTHING)
    billing_date = models.DateField()
    billing_day = models.IntegerField()
    due_date = models.DateField()
    due_period = models.IntegerField()
    principle_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    next_payment_date = models.DateField(blank=True, null=True)
    dpd = models.IntegerField()
    over_due_period = models.IntegerField()
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principle_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    amount_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    installment_due = models.DecimalField(max_digits=18, decimal_places=2)
    principle_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_due = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_due = models.DecimalField(max_digits=18, decimal_places=2)
    collection_due = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_due = models.DecimalField(max_digits=18, decimal_places=2)
    amount_due = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractbilling'


class TbEffcontractcollateral(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey('TbEffcontractdetail', models.DO_NOTHING)
    collateral = models.ForeignKey(TbCollateralinfo, models.DO_NOTHING)
    appraiser = models.ForeignKey('TbMastercollateralappraiser', models.DO_NOTHING, blank=True, null=True)
    appraiser_type = models.CharField(max_length=1)
    ownership = models.CharField(max_length=200, blank=True, null=True)
    date_estimate = models.DateField(blank=True, null=True)
    price_estimate = models.DecimalField(max_digits=18, decimal_places=2)
    rate_book = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_government = models.DecimalField(max_digits=18, decimal_places=2)
    land_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    building_appraisal_company = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_amount = models.DecimalField(max_digits=18, decimal_places=2)
    mortgage_date = models.DateField(blank=True, null=True)
    mortgage_type = models.ForeignKey('TbMastermortgagetype', models.DO_NOTHING, blank=True, null=True)
    market_price = models.DecimalField(max_digits=18, decimal_places=2)
    market_price2 = models.DecimalField(max_digits=18, decimal_places=2)
    market_price3 = models.DecimalField(max_digits=18, decimal_places=2)
    market_price_avg = models.DecimalField(max_digits=18, decimal_places=2)
    market_source = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    market_source2 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    market_source3 = models.ForeignKey('TbMastermarketpricesource', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractcollateral'


class TbEffcontractdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract = models.ForeignKey('TbEffcontractinfo', models.DO_NOTHING)
    ar_type = models.CharField(max_length=1)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    cont_group = models.ForeignKey('TbMastercontgroup', models.DO_NOTHING)
    payment_terms = models.CharField(max_length=1)
    pn_status = models.CharField(max_length=1)
    doc_no = models.CharField(max_length=20, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    actual_date = models.DateField()
    principal = models.DecimalField(max_digits=18, decimal_places=2)
    period = models.IntegerField()
    payment_day = models.IntegerField()
    sequence_method = models.CharField(max_length=1)
    pmt = models.DecimalField(max_digits=18, decimal_places=2)
    first_due_date = models.DateField()
    last_due_date = models.DateField()
    penalty_method = models.CharField(max_length=1)
    penalty_late = models.IntegerField()
    revenue_status = models.CharField(max_length=1)
    stop_revenue_date = models.DateField(blank=True, null=True)
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField(blank=True, null=True)
    approve_status = models.CharField(max_length=1)
    approve_date = models.DateField(blank=True, null=True)
    paid_status = models.CharField(max_length=1)
    paid_date = models.DateField(blank=True, null=True)
    expense_status = models.CharField(max_length=1)
    target = models.ForeignKey('TbMastertarget', models.DO_NOTHING)
    campaign = models.ForeignKey('TbMastercampaign', models.DO_NOTHING, blank=True, null=True)
    billcollector = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    checker = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    sale = models.ForeignKey('TbMasterofficer', models.DO_NOTHING)
    invite_status = models.CharField(max_length=1)
    invite = models.ForeignKey('TbMasterinvitation', models.DO_NOTHING, blank=True, null=True)
    invite_name = models.CharField(max_length=100, blank=True, null=True)
    reason = models.ForeignKey('TbMastercontractreason', models.DO_NOTHING, blank=True, null=True)
    acct_no = models.CharField(max_length=20, blank=True, null=True)
    action_code = models.ForeignKey('TbMasteractioncode', models.DO_NOTHING, blank=True, null=True)
    hold_status = models.ForeignKey('TbMasterholdstatus', models.DO_NOTHING, db_column='hold_status')
    paid_status_ho = models.CharField(max_length=1)
    paid_status_branch = models.CharField(max_length=1)
    restructure_status = models.CharField(max_length=1)
    restructure_code = models.CharField(max_length=1, blank=True, null=True)
    restructure_date = models.DateField(blank=True, null=True)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_stop_revenue = models.DecimalField(max_digits=18, decimal_places=2)
    interest_advance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_rebate = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    installment_advance = models.DecimalField(max_digits=18, decimal_places=2)
    next_due_date = models.DateField()
    next_principal_date = models.DateField()
    next_interest_date = models.DateField()
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    dpd = models.IntegerField()
    over_due_period = models.IntegerField()
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    total_interest_accrued = models.DecimalField(max_digits=18, decimal_places=2)
    last_post_interest_accrued = models.DateField(blank=True, null=True)
    total_post_interest_accrued = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    write_off_id = models.BigIntegerField(blank=True, null=True)
    write_off_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user_id = models.IntegerField()
    user_cancel_id = models.IntegerField(blank=True, null=True)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    period_installment = models.IntegerField()
    car_code = models.CharField(max_length=1, blank=True, null=True)
    car_code_date = models.DateField(blank=True, null=True)
    npl_flag = models.CharField(max_length=1, blank=True, null=True)
    npl_first_date = models.DateField(blank=True, null=True)
    npl_curr_date = models.DateField(blank=True, null=True)
    tdr_dpd = models.IntegerField(blank=True, null=True)
    tdr_car_code = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_period = models.IntegerField(blank=True, null=True)
    tdr_result = models.CharField(max_length=1, blank=True, null=True)
    force_car_code = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_end = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_end_date = models.DateField(blank=True, null=True)
    int_suspend_status = models.CharField(max_length=1)
    int_suspend_paid = models.DecimalField(max_digits=18, decimal_places=2)
    installment = models.DecimalField(max_digits=18, decimal_places=2)
    last_installment = models.DecimalField(max_digits=18, decimal_places=2)
    installment_paid = models.DecimalField(max_digits=18, decimal_places=2)
    principal_paid = models.DecimalField(max_digits=18, decimal_places=2)
    interest_paid = models.DecimalField(max_digits=18, decimal_places=2)
    begining_date = models.DateField(blank=True, null=True)
    next_period = models.IntegerField()
    write_off_status = models.CharField(max_length=1)
    write_off_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_effcontractdetail'


class TbEffcontractexpense(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    payfor = models.ForeignKey('TbMasterpayfor', models.DO_NOTHING)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    paid = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_effcontractexpense'


class TbEffcontractguarantor(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    customer = models.ForeignKey(TbCustomerinfo, models.DO_NOTHING)
    guarantor_type = models.CharField(max_length=1)
    relation = models.CharField(max_length=50, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractguarantor'


class TbEffcontractinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cont_no = models.CharField(unique=True, max_length=20)
    cont_date = models.DateField()
    customer = models.ForeignKey(TbCustomerinfo, models.DO_NOTHING)
    customer_address = models.ForeignKey(TbCustomeraddress, models.DO_NOTHING)
    send_bill_status = models.CharField(max_length=1)
    ref_contract_id = models.BigIntegerField(blank=True, null=True)
    application_no = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey('TbMasterbranch', models.DO_NOTHING)
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_effcontractinfo'


class TbEffcontractinstallment(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    period = models.IntegerField()
    effect_date = models.DateField()
    payment_code = models.CharField(max_length=1)
    installment_cover = models.DecimalField(max_digits=18, decimal_places=2)
    principal_cover = models.DecimalField(max_digits=18, decimal_places=2)
    interest_cover = models.DecimalField(max_digits=18, decimal_places=2)
    installment_month = models.IntegerField()
    principal_month = models.IntegerField()
    interest_month = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractinstallment'


class TbEffcontractinterest(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    period = models.IntegerField()
    effect_date = models.DateField()
    interest_code = models.CharField(max_length=1)
    bank = models.ForeignKey('TbMasterbank', models.DO_NOTHING, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=8, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    fee_rate = models.DecimalField(max_digits=8, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'tb_effcontractinterest'


class TbEffcontractothercharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    payfor = models.ForeignKey('TbMasterpayfor', models.DO_NOTHING)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    paid = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractothercharge'


class TbEffcontractpenalty(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    period = models.IntegerField()
    effect_date = models.DateField()
    penalty_rate = models.DecimalField(max_digits=8, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractpenalty'


class TbEffcontractperiod(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail_id = models.BigIntegerField()
    period = models.IntegerField()
    due_date = models.DateField()
    due_days = models.IntegerField()
    payment_code = models.CharField(max_length=1)
    principal_begin = models.DecimalField(max_digits=18, decimal_places=2)
    interest_begin = models.DecimalField(max_digits=18, decimal_places=2)
    installment = models.DecimalField(max_digits=18, decimal_places=2)
    principal_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_due = models.DecimalField(max_digits=18, decimal_places=2)
    int_current = models.DecimalField(max_digits=18, decimal_places=2)
    int_maturity = models.DecimalField(max_digits=18, decimal_places=2)
    payment_date = models.DateField(blank=True, null=True)
    payment = models.DecimalField(max_digits=18, decimal_places=2)
    principal_paid = models.DecimalField(max_digits=18, decimal_places=2)
    interest_paid = models.DecimalField(max_digits=18, decimal_places=2)
    int_current_paid = models.DecimalField(max_digits=18, decimal_places=2)
    int_maturity_paid = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_deferred = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_day = models.IntegerField(blank=True, null=True)
    penalty_amount = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_round = models.DecimalField(max_digits=8, decimal_places=7)
    penalty_paid_date = models.DateField(blank=True, null=True)
    penalty_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractperiod'


class TbEffcontractperiodstart(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    period = models.IntegerField()
    due_date = models.DateField()
    due_days = models.IntegerField()
    payment_code = models.CharField(max_length=1)
    principal_begin = models.DecimalField(max_digits=18, decimal_places=2)
    interest_begin = models.DecimalField(max_digits=18, decimal_places=2)
    installment = models.DecimalField(max_digits=18, decimal_places=2)
    principal_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_deferred = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractperiodstart'


class TbEffcontractsuspend(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    restructure_id = models.BigIntegerField()
    restructure_date = models.DateField(blank=True, null=True)
    tdr_interest = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_penalty = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_collection = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_other_charge = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effcontractsuspend'


class TbEffinterestaccrued(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    effective_date = models.DateField()
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=8, decimal_places=4)
    days = models.IntegerField()
    interest_before = models.DecimalField(max_digits=18, decimal_places=7)
    interest_actual = models.DecimalField(max_digits=18, decimal_places=7)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effinterestaccrued'


class TbEffinterestadjust(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    transaction_date = models.DateField()
    effective_date = models.DateField()
    transaction_by = models.CharField(max_length=1)
    transaction_id = models.BigIntegerField()
    interest_adjust = models.DecimalField(max_digits=18, decimal_places=2)
    interest_round = models.DecimalField(max_digits=8, decimal_places=7)
    post_gl = models.CharField(max_length=1)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effinterestadjust'


class TbEffinterestbalance(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    start_date = models.DateField()
    effective_date = models.DateField()
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_code = models.CharField(max_length=1)
    bank = models.ForeignKey('TbMasterbank', models.DO_NOTHING, blank=True, null=True)
    fix_rate = models.DecimalField(max_digits=8, decimal_places=4)
    float_rate = models.DecimalField(max_digits=8, decimal_places=4)
    interest_rate = models.DecimalField(max_digits=8, decimal_places=4)
    days = models.IntegerField()
    interest_accrued = models.DecimalField(max_digits=18, decimal_places=2)
    interest_round = models.DecimalField(max_digits=8, decimal_places=7)
    manual_interest_adjust = models.DecimalField(max_digits=18, decimal_places=2)
    net_interest_accrued = models.DecimalField(max_digits=18, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effinterestbalance'


class TbEffpenaltyaccrued(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    next_payment_date = models.DateField()
    due_date = models.DateField()
    effective_date = models.DateField()
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=8, decimal_places=4)
    penalty_rate = models.DecimalField(max_digits=8, decimal_places=4)
    delay_day = models.IntegerField()
    penalty_before = models.DecimalField(max_digits=18, decimal_places=7)
    penalty_actual = models.DecimalField(max_digits=18, decimal_places=7)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effpenaltyaccrued'


class TbEffpenaltyadjust(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    transaction_date = models.DateField()
    effective_date = models.DateField()
    transaction_by = models.CharField(max_length=1)
    transaction_id = models.BigIntegerField()
    penalty_adjust = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_round = models.DecimalField(max_digits=8, decimal_places=7)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effpenaltyadjust'


class TbEffprincipaladjust(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    balance_id = models.BigIntegerField()
    transaction_date = models.DateField()
    effective_date = models.DateField()
    transaction_by = models.CharField(max_length=1)
    transaction_id = models.BigIntegerField()
    principal_adjust = models.DecimalField(max_digits=18, decimal_places=2)
    post_gl = models.CharField(max_length=1)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effprincipaladjust'


class TbEffstatement(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_detail = models.ForeignKey(TbEffcontractdetail, models.DO_NOTHING)
    transaction_date = models.DateField()
    effective_date = models.DateField()
    days = models.IntegerField(blank=True, null=True)
    transaction_by = models.CharField(max_length=1)
    transaction_id = models.IntegerField()
    transaction_code = models.CharField(max_length=20, blank=True, null=True)
    effective_code = models.CharField(max_length=2)
    dr_amount = models.DecimalField(max_digits=18, decimal_places=2)
    cr_amount = models.DecimalField(max_digits=18, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    sequence = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_effstatement'


class TbGrouppermissionauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.ForeignKey('TbGrouppermissioninfo', models.DO_NOTHING)
    auth = models.ForeignKey('TbMasterauth', models.DO_NOTHING)
    o_status = models.BooleanField()
    n_status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_grouppermissionauth'


class TbGrouppermissiondetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.ForeignKey('TbGrouppermissioninfo', models.DO_NOTHING)
    menu = models.ForeignKey('TbMastermainmenu', models.DO_NOTHING)
    o_flg_access = models.BooleanField()
    o_flg_create = models.BooleanField()
    o_flg_update = models.BooleanField()
    o_flg_delete = models.BooleanField()
    n_flg_access = models.BooleanField()
    n_flg_create = models.BooleanField()
    n_flg_update = models.BooleanField()
    n_flg_delete = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_grouppermissiondetail'


class TbGrouppermissioninfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_user = models.ForeignKey('TbGroupuser', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_grouppermissioninfo'


class TbGrouppermissionreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.ForeignKey(TbGrouppermissioninfo, models.DO_NOTHING)
    report = models.ForeignKey('TbMasterreport', models.DO_NOTHING)
    o_status = models.BooleanField()
    n_status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_grouppermissionreport'


class TbGroupuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_user_code = models.CharField(unique=True, max_length=20)
    group_user_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_groupuser'


class TbGroupuserauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_user = models.ForeignKey(TbGroupuser, models.DO_NOTHING, blank=True, null=True)
    auth = models.ForeignKey('TbMasterauth', models.DO_NOTHING)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_groupuserauth'


class TbGroupuserreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_user = models.ForeignKey(TbGroupuser, models.DO_NOTHING, blank=True, null=True)
    report = models.ForeignKey('TbMasterreport', models.DO_NOTHING)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_groupuserreport'


class TbHireinterestdue(models.Model):
    id = models.BigAutoField(primary_key=True)
    effect_date = models.DateField()
    contract_detail = models.ForeignKey(TbContractdetail, models.DO_NOTHING)
    revenue_status = models.CharField(max_length=1)
    stop_revenue_date = models.DateField(blank=True, null=True)
    vat_status = models.CharField(max_length=1)
    stop_vat_date = models.DateField(blank=True, null=True)
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField(blank=True, null=True)
    approve_status = models.CharField(max_length=1)
    approve_date = models.DateField(blank=True, null=True)
    paid_status = models.CharField(max_length=1)
    paid_date = models.DateField(blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    car_code = models.CharField(max_length=1, blank=True, null=True)
    car_code_date = models.DateField(blank=True, null=True)
    npl_flag = models.CharField(max_length=1, blank=True, null=True)
    npl_first_date = models.DateField(blank=True, null=True)
    npl_curr_date = models.DateField(blank=True, null=True)
    tdr_dpd = models.IntegerField(blank=True, null=True)
    tdr_car_code = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_period = models.IntegerField(blank=True, null=True)
    tdr_result = models.CharField(max_length=1, blank=True, null=True)
    force_car_code = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_end = models.CharField(max_length=1, blank=True, null=True)
    tdr_monitor_end_date = models.DateField(blank=True, null=True)
    installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    last_payment_date = models.DateField(blank=True, null=True)
    down_payment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    installment_due = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_due = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_due = models.DecimalField(max_digits=18, decimal_places=2)
    fee_due = models.DecimalField(max_digits=18, decimal_places=2)
    over_due_period = models.IntegerField()
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    next_due_date = models.DateField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    next_period = models.IntegerField()
    installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    restructure_status = models.CharField(max_length=1)
    restructure_code = models.CharField(max_length=1, blank=True, null=True)
    restructure_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_hireinterestdue'
        unique_together = (('effect_date', 'contract_detail'),)


class TbMasteractioncode(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_code = models.CharField(unique=True, max_length=20)
    action_name = models.CharField(max_length=100, blank=True, null=True)
    paid_status = models.CharField(max_length=1)
    paid_status_ho = models.CharField(max_length=1)
    ncb_code = models.CharField(max_length=20, blank=True, null=True)
    ncb_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masteractioncode'


class TbMasteramphoe(models.Model):
    id = models.BigAutoField(primary_key=True)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    amphoe_code = models.CharField(unique=True, max_length=20)
    amphoe_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masteramphoe'


class TbMasterauction(models.Model):
    id = models.BigAutoField(primary_key=True)
    auction_code = models.CharField(unique=True, max_length=20)
    auction_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterauction'


class TbMasterauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    auth_code = models.CharField(unique=True, max_length=20)
    auth_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterauth'


class TbMasterbank(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank_code = models.CharField(unique=True, max_length=20)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_name_en = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterbank'


class TbMasterbankbranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank = models.ForeignKey(TbMasterbank, models.DO_NOTHING)
    branch_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    branch_name_en = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterbankbranch'
        unique_together = (('bank', 'branch_code'),)


class TbMasterbankinterest(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank = models.ForeignKey(TbMasterbank, models.DO_NOTHING)
    effect_date = models.DateField()
    mlr_rate = models.DecimalField(max_digits=8, decimal_places=4)
    mor_rate = models.DecimalField(max_digits=8, decimal_places=4)
    mrr_rate = models.DecimalField(max_digits=8, decimal_places=4)
    max_rate = models.DecimalField(max_digits=8, decimal_places=4)
    penalty_rate = models.DecimalField(max_digits=8, decimal_places=4)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterbankinterest'
        unique_together = (('bank', 'effect_date'),)


class TbMasterbookbank(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank = models.ForeignKey(TbMasterbank, models.DO_NOTHING)
    bank_branch = models.ForeignKey(TbMasterbankbranch, models.DO_NOTHING)
    book_no = models.CharField(unique=True, max_length=20)
    book_name = models.CharField(max_length=100, blank=True, null=True)
    book_name_en = models.CharField(max_length=100, blank=True, null=True)
    book_type = models.CharField(max_length=3)
    account_code = models.CharField(max_length=12, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterbookbank'


class TbMasterbranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey('TbMastercompany', models.DO_NOTHING)
    branch_code = models.CharField(unique=True, max_length=20)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    branch_doc = models.CharField(unique=True, max_length=5)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    tax_id = models.CharField(max_length=15, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    head_office = models.CharField(max_length=1)
    branch_no = models.CharField(max_length=10, blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    balance_date = models.DateField(blank=True, null=True)
    balance_amt = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    amphoe = models.ForeignKey(TbMasteramphoe, models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tb_masterbranch'


class TbMasterbrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand_code = models.CharField(unique=True, max_length=100)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterbrand'


class TbMastercampaign(models.Model):
    id = models.BigAutoField(primary_key=True)
    campaign_code = models.CharField(unique=True, max_length=20)
    campaign_name = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercampaign'


class TbMastercarcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    car_code = models.CharField(unique=True, max_length=1)
    car_code_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercarcode'


class TbMastercarcodeconfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    dpd_monitor = models.IntegerField()
    monitor_period = models.IntegerField()
    grace_period = models.IntegerField()
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercarcodeconfig'


class TbMastercifdigit(models.Model):
    id = models.BigAutoField(primary_key=True)
    cif_digit = models.CharField(unique=True, max_length=5)
    cif_char = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercifdigit'


class TbMastercollateralappraiser(models.Model):
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
        managed = False
        db_table = 'tb_mastercollateralappraiser'


class TbMastercollection(models.Model):
    id = models.BigAutoField(primary_key=True)
    collection_code = models.CharField(unique=True, max_length=20)
    collection_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercollection'


class TbMastercollectionsetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    max_collection_amount = models.DecimalField(max_digits=18, decimal_places=2)
    grace_period = models.IntegerField()
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    min_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_mastercollectionsetting'


class TbMastercolor(models.Model):
    id = models.BigAutoField(primary_key=True)
    color_code = models.CharField(unique=True, max_length=100)
    color_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercolor'


class TbMastercompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_code = models.CharField(unique=True, max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    tax_id = models.CharField(max_length=15, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    amphoe = models.ForeignKey(TbMasteramphoe, models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    max_collection_amount = models.DecimalField(max_digits=18, decimal_places=2)
    billing_day = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_mastercompany'


class TbMastercontgroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    cont_type = models.CharField(max_length=1)
    group_code = models.CharField(unique=True, max_length=20)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    payment_terms = models.CharField(max_length=1)
    sequence_method = models.CharField(max_length=1)
    penalty_late = models.IntegerField()
    pn_status = models.CharField(max_length=1)
    writeoff_status = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    step_rate = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tb_mastercontgroup'


class TbMastercontgroupinterest(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(TbMastercontgroup, models.DO_NOTHING)
    period = models.IntegerField()
    interest_code = models.CharField(max_length=1)
    bank = models.ForeignKey(TbMasterbank, models.DO_NOTHING, blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=8, decimal_places=4)
    fee_rate = models.DecimalField(max_digits=8, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercontgroupinterest'
        unique_together = (('group', 'period'),)


class TbMastercontgrouppenalty(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(TbMastercontgroup, models.DO_NOTHING)
    period = models.IntegerField()
    penalty_rate = models.DecimalField(max_digits=8, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercontgrouppenalty'
        unique_together = (('group', 'period'),)


class TbMastercontractdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercontractdocument'


class TbMastercontractreason(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercontractreason'


class TbMastercustomeraddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    address_name = models.CharField(max_length=100, blank=True, null=True)
    idcard_status = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercustomeraddress'


class TbMastercustomergrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    grade_code = models.CharField(unique=True, max_length=20)
    grade_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    black_list = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tb_mastercustomergrade'


class TbMastercustomergroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_code = models.CharField(unique=True, max_length=20)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercustomergroup'


class TbMastercustomerprename(models.Model):
    id = models.BigAutoField(primary_key=True)
    pre_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastercustomerprename'


class TbMasterdepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    department_code = models.CharField(unique=True, max_length=20)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterdepartment'


class TbMasterdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc_id = models.IntegerField(unique=True)
    doc_name = models.CharField(max_length=100, blank=True, null=True)
    doc_code = models.CharField(max_length=5)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    app_name = models.CharField(max_length=100, blank=True, null=True)
    model_name = models.CharField(max_length=100, blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_masterdocument'


class TbMastereditperiod(models.Model):
    id = models.BigAutoField(primary_key=True)
    edit_code = models.CharField(unique=True, max_length=20)
    edit_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastereditperiod'


class TbMastereducationlevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    education_code = models.CharField(unique=True, max_length=20)
    education_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastereducationlevel'


class TbMasterhold(models.Model):
    id = models.BigAutoField(primary_key=True)
    hold_code = models.CharField(unique=True, max_length=20)
    hold_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterhold'


class TbMasterholdstatus(models.Model):
    hold_status = models.CharField(unique=True, max_length=1)
    hold_status_name = models.CharField(max_length=100, blank=True, null=True)
    paid_status_ho = models.CharField(max_length=1)
    paid_status_branch = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterholdstatus'


class TbMasterholiday(models.Model):
    id = models.BigAutoField(primary_key=True)
    holiday_date = models.DateField(unique=True)
    holiday_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    slug = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'tb_masterholiday'


class TbMasterinsure(models.Model):
    id = models.BigAutoField(primary_key=True)
    insure_code = models.CharField(unique=True, max_length=20)
    insure_name = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    amphoe = models.ForeignKey(TbMasteramphoe, models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    postcode = models.BigIntegerField(blank=True, null=True)
    tax_id = models.CharField(max_length=15, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterinsure'


class TbMasterinsuretype(models.Model):
    id = models.BigAutoField(primary_key=True)
    insure_type_code = models.CharField(unique=True, max_length=20)
    insure_type_name = models.CharField(max_length=100, blank=True, null=True)
    insure_type_group = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterinsuretype'


class TbMasterinvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    invite_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterinvitation'


class TbMasterletterperiodrate(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_period = models.IntegerField()
    end_period = models.IntegerField()
    collection_amount = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterletterperiodrate'


class TbMasterletterperiodrate2(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_period = models.IntegerField()
    end_period = models.IntegerField()
    collection_amount = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=1)
    survey_amount = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tb_masterletterperiodrate2'


class TbMasterlivingowner(models.Model):
    id = models.BigAutoField(primary_key=True)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterlivingowner'


class TbMasterlivingtype(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterlivingtype'


class TbMastermainmenu(models.Model):
    menu_code = models.CharField(unique=True, max_length=20)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    menu_group_code = models.CharField(max_length=20, blank=True, null=True)
    menu_level = models.IntegerField(blank=True, null=True)
    sorting = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermainmenu'


class TbMastermapcodegl(models.Model):
    id = models.BigAutoField(primary_key=True)
    map_code = models.CharField(unique=True, max_length=20)
    map_name = models.CharField(max_length=100, blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermapcodegl'


class TbMastermarketpricesource(models.Model):
    id = models.BigAutoField(primary_key=True)
    source_code = models.CharField(unique=True, max_length=20)
    source_name = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermarketpricesource'


class TbMastermodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.ForeignKey(TbMasterbrand, models.DO_NOTHING)
    model_code = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermodel'
        unique_together = (('model_code', 'brand'),)


class TbMastermortgagetype(models.Model):
    id = models.BigAutoField(primary_key=True)
    mortgage_code = models.CharField(unique=True, max_length=20)
    mortgage_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermortgagetype'


class TbMastermrrratedetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    mrr = models.ForeignKey('TbMastermrrrateinfo', models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    mrr_rate = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermrrratedetail'


class TbMastermrrrateinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    mrr_base = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastermrrrateinfo'


class TbMasteroccupation(models.Model):
    id = models.BigAutoField(primary_key=True)
    occup_code = models.CharField(unique=True, max_length=20)
    occup_name = models.CharField(max_length=100, blank=True, null=True)
    occup_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masteroccupation'


class TbMasterofficer(models.Model):
    id = models.BigAutoField(primary_key=True)
    officer_code = models.CharField(unique=True, max_length=20)
    officer_name = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    tax_id = models.CharField(max_length=15, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    department = models.ForeignKey(TbMasterdepartment, models.DO_NOTHING)
    tambon = models.ForeignKey('TbMastertambon', models.DO_NOTHING)
    amphoe = models.ForeignKey(TbMasteramphoe, models.DO_NOTHING)
    province = models.ForeignKey('TbMasterprovince', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_masterofficer'


class TbMasterpayfor(models.Model):
    id = models.BigAutoField(primary_key=True)
    payfor_code = models.CharField(unique=True, max_length=20)
    payfor_name = models.CharField(max_length=100, blank=True, null=True)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    account_code = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1)
    redeem_status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    bill_payment_code = models.CharField(max_length=20, blank=True, null=True)
    branch_paid = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tb_masterpayfor'


class TbMasterpaytype(models.Model):
    id = models.BigAutoField(primary_key=True)
    paytype_code = models.CharField(unique=True, max_length=20)
    paytype_name = models.CharField(max_length=100, blank=True, null=True)
    paytype_group = models.CharField(max_length=1)
    account_code = models.CharField(max_length=20, blank=True, null=True)
    bill_payment_bank = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1)
    gl_status = models.CharField(max_length=1, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch_paid = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tb_masterpaytype'


class TbMasterproducttype(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_type_code = models.CharField(unique=True, max_length=20)
    product_type_name = models.CharField(max_length=100, blank=True, null=True)
    collateral_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterproducttype'


class TbMasterprovince(models.Model):
    id = models.BigAutoField(primary_key=True)
    province_code = models.CharField(unique=True, max_length=20)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterprovince'


class TbMasterreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    menu = models.ForeignKey(TbMastermainmenu, models.DO_NOTHING)
    report_name = models.CharField(max_length=100)
    report_file = models.CharField(unique=True, max_length=100)
    template_name = models.CharField(max_length=100, blank=True, null=True)
    cont_type = models.CharField(max_length=1)
    sort = models.IntegerField()
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterreport'


class TbMasterresidence(models.Model):
    id = models.BigAutoField(primary_key=True)
    residence_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterresidence'


class TbMasterrestructure(models.Model):
    id = models.BigAutoField(primary_key=True)
    restructure_code = models.CharField(unique=True, max_length=20)
    restructure_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterrestructure'


class TbMastersequence(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=1)
    sequence_no = models.IntegerField()
    sequence_code = models.CharField(max_length=1)
    sequence_name = models.CharField(max_length=100, blank=True, null=True)
    sequence_fee = models.IntegerField()
    sequence_interest = models.IntegerField()
    sequence_principal = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastersequence'


class TbMasterstopvatconfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    stop_vat_period = models.IntegerField()
    stop_revenue_period = models.IntegerField()
    grace_period = models.IntegerField()
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterstopvatconfig'


class TbMastersubmodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    sub_model_code = models.CharField(unique=True, max_length=100)
    sub_model_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastersubmodel'


class TbMastertable1(models.Model):
    period = models.IntegerField()
    period_72 = models.DecimalField(max_digits=18, decimal_places=2)
    period_66 = models.DecimalField(max_digits=18, decimal_places=2)
    period_60 = models.DecimalField(max_digits=18, decimal_places=2)
    period_54 = models.DecimalField(max_digits=18, decimal_places=2)
    period_48 = models.DecimalField(max_digits=18, decimal_places=2)
    period_42 = models.DecimalField(max_digits=18, decimal_places=2)
    period_36 = models.DecimalField(max_digits=18, decimal_places=2)
    period_30 = models.DecimalField(max_digits=18, decimal_places=2)
    period_24 = models.DecimalField(max_digits=18, decimal_places=2)
    period_18 = models.DecimalField(max_digits=18, decimal_places=2)
    period_12 = models.DecimalField(max_digits=18, decimal_places=2)
    period_10 = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastertable1'


class TbMastertable2(models.Model):
    period = models.IntegerField()
    period_72 = models.DecimalField(max_digits=18, decimal_places=2)
    period_66 = models.DecimalField(max_digits=18, decimal_places=2)
    period_60 = models.DecimalField(max_digits=18, decimal_places=2)
    period_54 = models.DecimalField(max_digits=18, decimal_places=2)
    period_48 = models.DecimalField(max_digits=18, decimal_places=2)
    period_42 = models.DecimalField(max_digits=18, decimal_places=2)
    period_36 = models.DecimalField(max_digits=18, decimal_places=2)
    period_30 = models.DecimalField(max_digits=18, decimal_places=2)
    period_24 = models.DecimalField(max_digits=18, decimal_places=2)
    period_18 = models.DecimalField(max_digits=18, decimal_places=2)
    period_12 = models.DecimalField(max_digits=18, decimal_places=2)
    period_10 = models.DecimalField(max_digits=18, decimal_places=2)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastertable2'


class TbMastertambon(models.Model):
    id = models.BigAutoField(primary_key=True)
    amphoe = models.ForeignKey(TbMasteramphoe, models.DO_NOTHING)
    tambon_code = models.CharField(unique=True, max_length=20)
    tambon_name = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastertambon'


class TbMastertarget(models.Model):
    id = models.BigAutoField(primary_key=True)
    target_code = models.CharField(unique=True, max_length=20)
    target_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastertarget'


class TbMastervatrate(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_mastervatrate'


class TbMasterwriteoff(models.Model):
    id = models.BigAutoField(primary_key=True)
    writeoff_code = models.CharField(unique=True, max_length=5)
    writeoff_desc = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_masterwriteoff'


class TbMenugroupuser(models.Model):
    group_user = models.ForeignKey(TbGroupuser, models.DO_NOTHING, blank=True, null=True)
    menu = models.ForeignKey(TbMastermainmenu, models.DO_NOTHING)
    flg_access = models.BooleanField()
    flg_create = models.BooleanField()
    flg_update = models.BooleanField()
    flg_delete = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_menugroupuser'


class TbMenuuser(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    menu = models.ForeignKey(TbMastermainmenu, models.DO_NOTHING)
    flg_access = models.BooleanField()
    flg_create = models.BooleanField()
    flg_update = models.BooleanField()
    flg_delete = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_menuuser'


class TbMessageremind(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey(TbMasterbranch, models.DO_NOTHING)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField()
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_type = models.CharField(max_length=1)
    cont_no = models.CharField(max_length=20)
    title = models.CharField(max_length=200, blank=True, null=True)
    dtstart_message = models.DateField(blank=True, null=True)
    dtstop_message = models.DateField(blank=True, null=True)
    message = models.CharField(max_length=1024, blank=True, null=True)
    alert = models.CharField(db_column='Alert', max_length=1)  # Field name made lowercase.
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_messageremind'


class TbMovedetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    move = models.ForeignKey('TbMoveinfo', models.DO_NOTHING)
    arhold = models.ForeignKey(TbArhold, models.DO_NOTHING)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    cont_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_movedetail'


class TbMoveinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey(TbMasterbranch, models.DO_NOTHING)
    branch_to = models.ForeignKey(TbMasterbranch, models.DO_NOTHING)
    move_no = models.CharField(unique=True, max_length=20)
    move_date = models.DateField()
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_moveinfo'


class TbPasswordresetlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    assign_user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_passwordresetlog'


class TbPaymentdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_info = models.ForeignKey('TbPaymentinfo', models.DO_NOTHING)
    payfor = models.ForeignKey(TbMasterpayfor, models.DO_NOTHING)
    payfor_type = models.CharField(max_length=1)
    vat_status = models.CharField(max_length=1)
    vat_rate = models.DecimalField(max_digits=6, decimal_places=2)
    payment = models.DecimalField(max_digits=18, decimal_places=2)
    net_payment = models.DecimalField(max_digits=18, decimal_places=2)
    vat_payment = models.DecimalField(max_digits=18, decimal_places=2)
    discount = models.DecimalField(max_digits=18, decimal_places=2)
    withholding_tax = models.DecimalField(max_digits=18, decimal_places=2)
    total_payment = models.DecimalField(max_digits=18, decimal_places=2)
    principal_paid = models.DecimalField(max_digits=18, decimal_places=2)
    interest_paid = models.DecimalField(max_digits=18, decimal_places=2)
    int_current_paid = models.DecimalField(max_digits=18, decimal_places=2)
    int_suspend_paid = models.DecimalField(max_digits=18, decimal_places=2)
    interest_adjust = models.DecimalField(max_digits=18, decimal_places=2)
    fee_paid = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_paid = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_paid = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_paid = models.DecimalField(max_digits=18, decimal_places=2)
    first_partial = models.CharField(max_length=1, blank=True, null=True)
    first_period = models.IntegerField(blank=True, null=True)
    last_partial = models.CharField(max_length=1, blank=True, null=True)
    last_period = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    conversion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_paymentdetail'


class TbPaymentinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_no = models.CharField(unique=True, max_length=20)
    payment_date = models.DateField()
    effective_date = models.DateField()
    bill_no = models.CharField(max_length=20)
    branch = models.ForeignKey(TbMasterbranch, models.DO_NOTHING)
    customer = models.ForeignKey(TbCustomerinfo, models.DO_NOTHING)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    contract_type = models.CharField(max_length=1)
    billing_type = models.CharField(max_length=1)
    source_by = models.CharField(max_length=1)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_penalty_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_collection_balance = models.DecimalField(max_digits=18, decimal_places=2)
    tdr_other_charge_balance = models.DecimalField(max_digits=18, decimal_places=2)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_paymentinfo'


class TbPaymenttype(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_info = models.ForeignKey(TbPaymentinfo, models.DO_NOTHING)
    paytype = models.ForeignKey(TbMasterpaytype, models.DO_NOTHING)
    paytype_group = models.CharField(max_length=1)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    ref_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_paymenttype'


class TbStoprevenue(models.Model):
    id = models.BigAutoField(primary_key=True)
    stop_date = models.DateField()
    cont_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    due_date = models.DateField(blank=True, null=True)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_stoprevenue'


class TbStopvat(models.Model):
    id = models.BigAutoField(primary_key=True)
    stop_date = models.DateField()
    cont_type = models.CharField(max_length=1)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    due_date = models.DateField(blank=True, null=True)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_over_due = models.DecimalField(max_digits=18, decimal_places=2)
    installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_balance = models.DecimalField(max_digits=18, decimal_places=2)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_principal_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_balance = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_balance = models.DecimalField(max_digits=18, decimal_places=2)
    installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    net_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    vat_installment_received = models.DecimalField(max_digits=18, decimal_places=2)
    interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_interest_received = models.DecimalField(max_digits=18, decimal_places=2)
    straight_line_fee_received = models.DecimalField(max_digits=18, decimal_places=2)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_stopvat'


class TbTaxinvoicedetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    tax_invoice_info = models.ForeignKey('TbTaxinvoiceinfo', models.DO_NOTHING)
    tax_description = models.CharField(max_length=100, blank=True, null=True)
    payment = models.DecimalField(max_digits=18, decimal_places=2)
    net_payment = models.DecimalField(max_digits=18, decimal_places=2)
    vat_payment = models.DecimalField(max_digits=18, decimal_places=2)
    first_partial = models.CharField(max_length=1, blank=True, null=True)
    first_period = models.IntegerField(blank=True, null=True)
    last_partial = models.CharField(max_length=1, blank=True, null=True)
    last_period = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_taxinvoicedetail'


class TbTaxinvoiceinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    tax_no = models.CharField(unique=True, max_length=20)
    tax_date = models.DateField()
    transaction_date = models.DateField(blank=True, null=True)
    branch = models.ForeignKey(TbMasterbranch, models.DO_NOTHING)
    customer = models.ForeignKey(TbCustomerinfo, models.DO_NOTHING)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    contract_type = models.CharField(max_length=1)
    tax_type = models.CharField(max_length=1)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2)
    tax_flag = models.CharField(max_length=1, blank=True, null=True)
    payment_info_id = models.BigIntegerField(blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    active_post_gl = models.CharField(max_length=1)
    active_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    cancel_post_gl = models.CharField(max_length=1)
    cancel_voucher_no = models.CharField(max_length=20, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_taxinvoiceinfo'


class TbUserauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    auth = models.ForeignKey(TbMasterauth, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_userauth'


class TbUserpermissionauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.ForeignKey('TbUserpermissioninfo', models.DO_NOTHING)
    auth = models.ForeignKey(TbMasterauth, models.DO_NOTHING)
    o_status = models.BooleanField()
    n_status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_userpermissionauth'


class TbUserpermissiondetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.ForeignKey('TbUserpermissioninfo', models.DO_NOTHING)
    menu = models.ForeignKey(TbMastermainmenu, models.DO_NOTHING)
    o_flg_access = models.BooleanField()
    o_flg_create = models.BooleanField()
    o_flg_update = models.BooleanField()
    o_flg_delete = models.BooleanField()
    n_flg_access = models.BooleanField()
    n_flg_create = models.BooleanField()
    n_flg_update = models.BooleanField()
    n_flg_delete = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_userpermissiondetail'


class TbUserpermissioninfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    assign_user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_userpermissioninfo'


class TbUserpermissionreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    permission = models.ForeignKey(TbUserpermissioninfo, models.DO_NOTHING)
    report = models.ForeignKey(TbMasterreport, models.DO_NOTHING)
    o_status = models.BooleanField()
    n_status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_userpermissionreport'


class TbUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey(TbMasterbranch, models.DO_NOTHING, blank=True, null=True)
    officer = models.ForeignKey(TbMasterofficer, models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)
    group_user = models.ForeignKey(TbGroupuser, models.DO_NOTHING)
    slug = models.CharField(unique=True, max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_userprofile'


class TbUserreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    report = models.ForeignKey(TbMasterreport, models.DO_NOTHING)
    status = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_userreport'


class TbWaitconfirmtoholddetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    waitconfirm = models.ForeignKey('TbWaitconfirmtoholdinfo', models.DO_NOTHING)
    contract_id = models.BigIntegerField()
    contract_detail_id = models.BigIntegerField()
    cont_no = models.CharField(max_length=20)
    cont_type = models.CharField(max_length=1)
    cont_group = models.CharField(max_length=20)
    over_due_period = models.IntegerField(blank=True, null=True)
    over_due_from = models.IntegerField(blank=True, null=True)
    over_due_to = models.IntegerField(blank=True, null=True)
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField(blank=True, null=True)
    confirm_status = models.CharField(max_length=1)
    confirm_date = models.DateField(blank=True, null=True)
    confirm_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    payment_info_id = models.BigIntegerField(blank=True, null=True)
    officer = models.ForeignKey(TbMasterofficer, models.DO_NOTHING, blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_interest_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_penalty_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_other_charge_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tdr_collection_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unearned_vat = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_close_acc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    next_payment_date = models.DateField(blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_waitconfirmtoholddetail'


class TbWaitconfirmtoholdinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    branch = models.ForeignKey(TbMasterbranch, models.DO_NOTHING)
    doc_no = models.CharField(unique=True, max_length=20)
    doc_date = models.DateField(blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20)
    cont_group = models.CharField(max_length=20, blank=True, null=True)
    over_due_from = models.IntegerField()
    over_due_to = models.IntegerField()
    cont_status = models.CharField(max_length=1)
    cont_status_date = models.DateField(blank=True, null=True)
    confirm_status = models.CharField(max_length=1)
    confirm_date = models.DateField(blank=True, null=True)
    confirm_user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1)
    slug = models.CharField(unique=True, max_length=200)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    user_cancel = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_waitconfirmtoholdinfo'


class TmpAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    cust_code = models.CharField(max_length=20, blank=True, null=True)
    address_name = models.CharField(max_length=1, blank=True, null=True)
    send_doc = models.CharField(max_length=1, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    soi = models.CharField(max_length=100, blank=True, null=True)
    road = models.CharField(max_length=100, blank=True, null=True)
    tambon_id = models.IntegerField(blank=True, null=True)
    tambon_code = models.CharField(max_length=20, blank=True, null=True)
    tambon_name = models.CharField(max_length=100, blank=True, null=True)
    amphoe_id = models.IntegerField(blank=True, null=True)
    amphoe_code = models.CharField(max_length=20, blank=True, null=True)
    amphoe_name = models.CharField(max_length=100, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    province_code = models.CharField(max_length=20, blank=True, null=True)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    relate = models.CharField(max_length=100, blank=True, null=True)
    living_owner = models.CharField(max_length=100, blank=True, null=True)
    living_type = models.CharField(max_length=100, blank=True, null=True)
    living_rental = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    living_welfare_month = models.IntegerField(blank=True, null=True)
    living_welfare_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_address'


class TmpCollateral(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    chassis_no = models.CharField(max_length=50, blank=True, null=True)
    engine_no = models.CharField(max_length=50, blank=True, null=True)
    product_type_id = models.IntegerField(blank=True, null=True)
    product_type_code = models.CharField(max_length=100, blank=True, null=True)
    reg_no = models.CharField(max_length=30, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    province_code = models.CharField(max_length=100, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    reg_expire = models.DateField(blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    brand_code = models.CharField(max_length=100, blank=True, null=True)
    model_id = models.IntegerField(blank=True, null=True)
    model_code = models.CharField(max_length=100, blank=True, null=True)
    sub_model_id = models.IntegerField(blank=True, null=True)
    sub_model_code = models.CharField(max_length=100, blank=True, null=True)
    sub_model_name = models.CharField(max_length=100, blank=True, null=True)
    color_id = models.IntegerField(blank=True, null=True)
    color_code = models.CharField(max_length=100, blank=True, null=True)
    manu_year = models.IntegerField(blank=True, null=True)
    mile = models.IntegerField(blank=True, null=True)
    cc = models.IntegerField(blank=True, null=True)
    car_age_month = models.IntegerField(blank=True, null=True)
    car_age_year = models.IntegerField(blank=True, null=True)
    price_estimate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    market_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    market_price2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    market_price3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    market_price_avg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    rate_book = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    date_estimate = models.DateField(blank=True, null=True)
    appraiser_type = models.CharField(max_length=1, blank=True, null=True)
    appraiser_id = models.IntegerField(blank=True, null=True)
    appraiser_code = models.CharField(max_length=20, blank=True, null=True)
    ownership = models.CharField(max_length=200, blank=True, null=True)
    market_source_code = models.CharField(max_length=20, blank=True, null=True)
    market_source2_code = models.CharField(max_length=20, blank=True, null=True)
    market_source3_code = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_collateral'


class TmpCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    cust_type = models.CharField(max_length=1, blank=True, null=True)
    cust_code = models.CharField(max_length=20, blank=True, null=True)
    pre_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    group_code = models.CharField(max_length=20, blank=True, null=True)
    grade_code = models.CharField(max_length=20, blank=True, null=True)
    card_type = models.CharField(max_length=50, blank=True, null=True)
    card_no = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    nation = models.CharField(max_length=30, blank=True, null=True)
    race = models.CharField(max_length=30, blank=True, null=True)
    education_level = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    office = models.CharField(max_length=200, blank=True, null=True)
    longevity_year = models.IntegerField(blank=True, null=True)
    longevity_month = models.IntegerField(blank=True, null=True)
    main_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_income = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    income_description = models.CharField(max_length=100, blank=True, null=True)
    main_expense = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    refer_name = models.CharField(max_length=200, blank=True, null=True)
    refer_description = models.CharField(max_length=100, blank=True, null=True)
    refer_telephone = models.CharField(max_length=50, blank=True, null=True)
    head_office = models.CharField(max_length=50, blank=True, null=True)
    branch_no = models.CharField(max_length=50, blank=True, null=True)
    branch_seq = models.CharField(max_length=50, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_customer'


class TmpEffcontract(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    cont_date = models.DateField(blank=True, null=True)
    application_no = models.CharField(max_length=20, blank=True, null=True)
    cust_code = models.CharField(max_length=20, blank=True, null=True)
    card_no = models.CharField(max_length=20, blank=True, null=True)
    collateral_type = models.CharField(max_length=1, blank=True, null=True)
    chassis_no = models.CharField(max_length=50, blank=True, null=True)
    cont_group = models.CharField(max_length=100, blank=True, null=True)
    send_bill_status = models.CharField(max_length=1, blank=True, null=True)
    branch_code = models.CharField(max_length=20, blank=True, null=True)
    new_branch_code = models.CharField(max_length=20, blank=True, null=True)
    actual_date = models.DateField(blank=True, null=True)
    pn_no = models.CharField(max_length=20, blank=True, null=True)
    principal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_flat_rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    period_installment = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    payment_terms = models.CharField(max_length=1, blank=True, null=True)
    installment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    payment_day = models.IntegerField(blank=True, null=True)
    first_due_date = models.DateField(blank=True, null=True)
    last_due_date = models.DateField(blank=True, null=True)
    penalty_method = models.CharField(max_length=1, blank=True, null=True)
    penalty_late = models.IntegerField(blank=True, null=True)
    penalty_rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sale_code = models.CharField(max_length=20, blank=True, null=True)
    billcollector_code = models.CharField(max_length=20, blank=True, null=True)
    checker_code = models.CharField(max_length=20, blank=True, null=True)
    reason_name = models.CharField(max_length=100, blank=True, null=True)
    begining_date = models.DateField(blank=True, null=True)
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_accrued = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_amont = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    next_due_date = models.CharField(max_length=100, blank=True, null=True)
    new_next_due_date = models.DateField(blank=True, null=True)
    next_payment_date = models.CharField(max_length=100, blank=True, null=True)
    new_next_payment_date = models.DateField(blank=True, null=True)
    installment_over_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    dpd = models.IntegerField(blank=True, null=True)
    over_due_period = models.IntegerField(blank=True, null=True)
    period_begin = models.IntegerField(blank=True, null=True)
    installment_partial = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_effcontract'


class TmpEffpayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    payment_no = models.CharField(max_length=20, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)
    contract_detail_id = models.BigIntegerField(blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    cust_code = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    wl_payfor = models.CharField(max_length=1, blank=True, null=True)
    wl_paytype = models.CharField(max_length=1, blank=True, null=True)
    payfor_id = models.BigIntegerField(blank=True, null=True)
    payfor_code = models.CharField(max_length=20, blank=True, null=True)
    payfor_type = models.CharField(max_length=1, blank=True, null=True)
    payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    principal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    officer = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_effpayment'


class TmpGuarantor(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    cust_code = models.CharField(max_length=20, blank=True, null=True)
    cust_type = models.CharField(max_length=1, blank=True, null=True)
    cust_relation = models.CharField(max_length=50, blank=True, null=True)
    card_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_guarantor'


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
    engine_no =models.CharField(max_length=50)
    reg_no = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'view_hirecontractoldcar'



class TmpHirecontract(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    cont_date = models.DateField(blank=True, null=True)
    application_no = models.CharField(max_length=20, blank=True, null=True)
    cust_code = models.CharField(max_length=10, blank=True, null=True)
    card_no = models.CharField(max_length=20, blank=True, null=True)
    collateral_type = models.CharField(max_length=1, blank=True, null=True)
    chassis_no = models.CharField(max_length=50, blank=True, null=True)
    cont_group = models.CharField(max_length=100, blank=True, null=True)
    send_bill_status = models.CharField(max_length=1, blank=True, null=True)
    branch_code = models.CharField(max_length=20, blank=True, null=True)
    branch_desc = models.CharField(max_length=20, blank=True, null=True)
    collateral_vat_rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    product_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_product_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_product_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    standard_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_standard_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_standard_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    down_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_down_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_down_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    principal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_principal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_principal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_flat_rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    period_installment = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    installment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_installment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_installment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    first_due_date = models.DateField(blank=True, null=True)
    last_due_date = models.DateField(blank=True, null=True)
    installment_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_installment_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_installment_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    penalty_method = models.CharField(max_length=1, blank=True, null=True)
    penalty_late = models.IntegerField(blank=True, null=True)
    penalty_rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    material_group = models.CharField(max_length=20, blank=True, null=True)
    deferred_interest = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sale_code = models.CharField(max_length=20, blank=True, null=True)
    billcollector_code = models.CharField(max_length=20, blank=True, null=True)
    checker_code = models.CharField(max_length=20, blank=True, null=True)
    reason_name = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    contyp = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_hirecontract'


class TmpHirepayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    branch_id = models.BigIntegerField(blank=True, null=True)
    branch_code = models.CharField(max_length=20, blank=True, null=True)
    payment_no = models.CharField(max_length=20, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    bill_no = models.CharField(max_length=20, blank=True, null=True)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    ref_date = models.DateField(blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)
    contract_detail_id = models.BigIntegerField(blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    cust_code = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    wl_paytype_code = models.CharField(max_length=20, blank=True, null=True)
    wl_paytype_name = models.CharField(max_length=100, blank=True, null=True)
    wl_payfor_code = models.CharField(max_length=20, blank=True, null=True)
    wl_payfor_name = models.CharField(max_length=20, blank=True, null=True)
    payfor_id = models.BigIntegerField(blank=True, null=True)
    payfor_code = models.CharField(max_length=20, blank=True, null=True)
    payfor_type = models.CharField(max_length=1, blank=True, null=True)
    paytype_id = models.BigIntegerField(blank=True, null=True)
    paytype_code = models.CharField(max_length=20, blank=True, null=True)
    paytype_group = models.CharField(max_length=1, blank=True, null=True)
    payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    withholding_tax = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    principal_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    principal_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    int_current_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    int_suspend_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    straight_line_principal_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    straight_line_interest_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    straight_line_fee_paid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    first_partial = models.CharField(max_length=1, blank=True, null=True)
    first_period = models.IntegerField(blank=True, null=True)
    last_partial = models.CharField(max_length=1, blank=True, null=True)
    last_period = models.IntegerField(blank=True, null=True)
    officer = models.CharField(max_length=100, blank=True, null=True)
    payment_info_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_hirepayment'


class TmpHiretax(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    branch_id = models.BigIntegerField(blank=True, null=True)
    branch_code = models.CharField(max_length=20, blank=True, null=True)
    wl_tax_no = models.CharField(max_length=20, blank=True, null=True)
    tax_no = models.CharField(max_length=20, blank=True, null=True)
    tax_date = models.DateField(blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)
    contract_detail_id = models.BigIntegerField(blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    cust_code = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vat_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    memo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_hiretax'


class TmpMasteroffocer(models.Model):
    id = models.BigAutoField()
    cocd = models.CharField(db_column='CoCd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coname = models.CharField(db_column='CoName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    persno = models.CharField(db_column='PersNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    persname = models.CharField(db_column='PersName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paname = models.CharField(db_column='PAName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eegrp = models.CharField(db_column='EEGrp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eegrpname = models.CharField(db_column='EEGrpName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esgrp = models.CharField(db_column='ESgrp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esgrpname = models.CharField(db_column='ESgrpName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keycd = models.CharField(db_column='KeyCd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keyname = models.CharField(db_column='KeyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zonecd = models.CharField(db_column='ZoneCd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zonename = models.CharField(db_column='ZoneName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parea = models.CharField(db_column='PArea', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pareaname = models.CharField(db_column='PAreaName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    departcd = models.CharField(db_column='DepartCd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    departname = models.CharField(db_column='DepartName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    positioncd = models.CharField(db_column='PositionCd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    positionname = models.CharField(db_column='PositionName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workcd = models.CharField(db_column='WorkCd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    workname = models.CharField(db_column='WorkName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grp = models.CharField(db_column='Grp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coar = models.CharField(db_column='COAr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    costcentercd = models.CharField(db_column='CostCenterCd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    costcentername = models.CharField(db_column='CostCenterName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    s = models.CharField(db_column='S', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_masteroffocer'


class TmpOthercharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    begining_date = models.DateField(blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    payfor_code = models.CharField(max_length=20, blank=True, null=True)
    payfor_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_othercharge'


class TmpOthercharge2(models.Model):
    id = models.BigAutoField(primary_key=True)
    begining_date = models.DateField(blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)
    contract_detail_id = models.BigIntegerField(blank=True, null=True)
    cont_type = models.CharField(max_length=1, blank=True, null=True)
    cont_no = models.CharField(max_length=20, blank=True, null=True)
    payfor_code = models.CharField(max_length=20, blank=True, null=True)
    payfor_name = models.CharField(max_length=100, blank=True, null=True)
    payfor_id = models.BigIntegerField(blank=True, null=True)
    payfor_type = models.CharField(max_length=1, blank=True, null=True)
    vat_status = models.CharField(max_length=1, blank=True, null=True)
    vat_rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    branch_id = models.BigIntegerField(blank=True, null=True)
    branch_code = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    other_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_othercharge2'


class TmpPatchcollateral(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    chassis_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_patchcollateral'


class Accgroup(models.Model):
    idno = models.AutoField(primary_key=True)
    accgrpcod = models.CharField(unique=True, max_length=12)
    accgrpnam = models.CharField(max_length=60, blank=True, null=True)
    accgrpeng = models.CharField(max_length=40, blank=True, null=True)
    memo1 = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accgroup'


class Accmst(models.Model):
    idno = models.AutoField(primary_key=True)
    accmstcod = models.CharField(unique=True, max_length=12)
    accmstnam = models.CharField(max_length=100, blank=True, null=True)
    accmsteng = models.CharField(max_length=100, blank=True, null=True)
    acctypcod = models.ForeignKey('Acctype', models.DO_NOTHING, db_column='acctypcod')
    accgrpcod = models.CharField(max_length=12)
    acclevel = models.CharField(max_length=1)
    acctypjob = models.CharField(max_length=1)
    accbalndrcr = models.CharField(max_length=1)
    accontrol = models.CharField(max_length=12, blank=True, null=True)
    accflag = models.CharField(max_length=1)
    memo1 = models.CharField(max_length=512, blank=True, null=True)
    accflaguse = models.CharField(max_length=1, blank=True, null=True)
    divifl = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accmst'


class Acctype(models.Model):
    idno = models.AutoField(primary_key=True)
    acctypcod = models.CharField(unique=True, max_length=12)
    acctypnam = models.CharField(max_length=60, blank=True, null=True)
    acctypeng = models.CharField(max_length=40, blank=True, null=True)
    memo1 = models.CharField(max_length=512, blank=True, null=True)
    inpdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acctype'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Setjour(models.Model):
    idno = models.AutoField(primary_key=True)
    jourcod = models.CharField(unique=True, max_length=12)
    journam = models.CharField(max_length=60, blank=True, null=True)
    joureng = models.CharField(max_length=40, blank=True, null=True)
    shortj = models.CharField(max_length=2, blank=True, null=True)
    memo1 = models.CharField(max_length=512, blank=True, null=True)
    dbrun = models.CharField(max_length=1, blank=True, null=True)
    bbflag = models.CharField(max_length=1, blank=True, null=True)
    inpdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setjour'


class TbCustomerguarantor(models.Model):
    customerid = models.IntegerField(db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    relation = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_customerguarantor'


class TbDistributor(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    checker = models.CharField(max_length=100, blank=True, null=True)
    sales_person = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_distributor'


class TbInstallmentdetail(models.Model):
    id = models.AutoField()
    distributor_id = models.IntegerField(blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    code_model = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    down_payment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    interest = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    installment = models.IntegerField(blank=True, null=True)
    price_installment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    start_payment = models.DateField(blank=True, null=True)
    guarantee = models.CharField(max_length=20, blank=True, null=True)
    machine_no = models.CharField(max_length=100, blank=True, null=True)
    chassis_no = models.CharField(max_length=100, blank=True, null=True)
    registration_no = models.CharField(max_length=30, blank=True, null=True)
    product_code = models.CharField(max_length=50, blank=True, null=True)
    contract_no_old = models.CharField(max_length=100, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    zone_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_installmentdetail'
