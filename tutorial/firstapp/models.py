from django.db import models

# Create your models here.
class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    # print() <= 클래스 출력 시 더블 언더스코어 str 함수가 호출!
    def __str__(self):
        return self.name
    class Meta:
        # 테이블명을 curriculum 으로 지정
        db_table = 'firstapp_curriculum'
        # 현재 위치(App)가 아닌 외부에 정의된 경우
        app_label = 'firstapp'
        # 데이터 조회 기본 정렬 상태
        ordering = ['-id', 'name']