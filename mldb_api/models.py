from django.db import models

class models_repo(models.Model):
    model_name = models.CharField(max_length=50) #모델 이름
    model_type = models.TextField() # 길이 제한이 없는 문자열
    model_base64 = models.TextField() # base64 로 인코딩된 모델 파일 저장
    model_file = models.TextField() # 모델 파일이 있는 경로
    created_at = models.DateTimeField(auto_now_add=True)    # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)  # 해당 레코드 갱신시 현재 시간 자동저장

