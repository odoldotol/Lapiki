from django.db import models

from django.db.models.fields import CharField

from django.contrib.auth.models import User


class Portfolio(models.Model):

    name = models.CharField(
        verbose_name="name",
        max_length=80,
        default="My Portfolio",
    )

    created_at = models.DateTimeField(
        verbose_name="created_at"
    )

    user = models.ForeignKey(to=User, on_delete=models.RESTRICT)

    is_main = models.BooleanField(default=False)
