from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MasterAuth(models.Model):
    auth_code = models.CharField(max_length=20, null=False, unique=True, verbose_name='รหัสสิทธิ์การใช้งาน')
    auth_name = models.CharField(max_length=100, null=False, verbose_name='ชื่อสิทธิ์การใช้งาน')
    status = models.CharField(max_length=1, null=False, verbose_name='สถานะ')
    slug = models.SlugField(max_length=200, null=False, unique=True)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)

    class Meta:
        db_table = 'tb_sermmasterauth'

class MasterOfficer(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

class UserAuth(models.Model):
    status = models.BooleanField(default=False, null=False, verbose_name='สถานะ')
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)
    auth = models.ForeignKey(MasterAuth, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tb_sermuserauth'


class AuthList(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=150)
    auth_code = models.CharField(max_length=20)
    auth_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False, null=False, verbose_name='สถานะ')
    username = models.CharField(max_length=150, verbose_name='FormatUser01')

    class Meta:
        db_table = 'view_sermuserauth'

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