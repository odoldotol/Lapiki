from django.db import models

from django.contrib.auth.models import User


class Portfolio(models.Model):
    # 유저계정 종속
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 최근 엑세스 일시
    last_access = models.DateTimeField(auto_now=True)
    # 유저가 설정하는 포트폴리오 이름
    name = models.CharField(
        verbose_name="name",
        max_length=80,
        default="My Portfolio",
    )
    # 메인포트 여부
    is_main = models.BooleanField(default=False)
    # 통화 설정
    main_currency = models.CharField(max_length=10, default="KRW")
    is_sub_currency = models.BooleanField(default=False)
    sub_currency = models.CharField(max_length=10, default="USD")
    # 삭제 여부
    is_deleted = models.BooleanField(default=False)