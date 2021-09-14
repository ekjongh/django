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
    course = CharField(max_length=100, null=True)
    course_name = CharField(max_length=100, null=True)
    distance = FloatField()
    time_info = CharField(max_length=100, null=True)
    start_end_info = CharField(max_length=100, null=True)
    cre_date = DateField()
    class Meta:
        db_table = 'jeju_olle'
        app_label = 'thirdapp'

# 강사님 코드
# class JejuOlle(models.Model):
#     course = CharField(max_length=10)
#     course_name = CharField(max_length=20)
#     distance = FloatField()
#     time_info = CharField(max_length=10)
#     start_end_info = CharField(max_length=30)
#     cre_date = DateField()

#     class Meta:
#         db_table = 'jeju_olle'



