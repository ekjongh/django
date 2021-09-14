from django.db import models

# Create your models here.
from django.db.models.fields import CharField, DateTimeField, FloatField, IntegerField, DateField
class Shop(models.Model):
    shop_id = IntegerField(primary_key=True)
    shop_name = CharField(max_length=100, null=True)
    shop_desc = CharField(max_length=100, null=True)
    rest_date = CharField(max_length=100, null=True)
    parking_info = CharField(max_length=100, null=True)
    img_path = CharField(max_length=255, null=True)
    class Meta:
        db_table = 'shop'
        app_label = 'thirdapp'

class JejuOlle(models.Model):
    course = CharField(max_length=10)
    course_name = CharField(max_length=20)
    distance = FloatField()
    time_info = CharField(max_length=10)
    start_end_info = CharField(max_length=30)
    cre_date = DateField()

    class Meta:
        db_table = 'jeju_olle'

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)  # 기본키 지정
    dname = models.CharField(max_length=14)
    loc = models.CharField(max_length=13)

    class Meta:
        db_table = 'dept'

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    dept = models.ForeignKey(Dept, db_column='deptno', on_delete=models.CASCADE)

    class Meta:
        db_table = 'emp'
