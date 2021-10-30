from django.db import models

from django.contrib.auth.models import User

class Portfolio(models.Model):
    # 유저계정 종속
    user = models.ForeignKey(to=User, on_delete=models.RESTRICT)
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 유저가 설정하는 포트폴리오 이름
    name = models.CharField(
        verbose_name="name",
        max_length=80,
        default="My Portfolio",
    )
    # 메인포트 여부
    is_main = models.BooleanField(default=False)
    # 기본통화 설정
    Currency = models.CharField(max_length=10, default="KRW")


class AccountFormat(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 포멧이름
    title = models.CharField(max_length=50)


class AssetFormat(models.Model):
    # 생성 및 마지막 수정 일시
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    # 포멧이름
    title = models.CharField(max_length=50)



    # 수량 소숫점 이하 자릿수
    amount_decimal_places = models.IntegerField()