from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()

    def __str__(self):
        return f"{self.name} / {self.cnt}"

class AmyShop(models.Model):
    # id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    class Meta:
        # 테이블명을 curriculum 으로 지정
        db_table = 'army_shop'
        # 현재 위치(App)가 아닌 외부에 정의된 경우
        app_label = 'secondapp'
        # 데이터 조회 기본 정렬 상태
        ordering = ['year', 'month']