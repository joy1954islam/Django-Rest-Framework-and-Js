from django.db import models


class PersonalInformation(models.Model):
    name = models.CharField(
        max_length=254,
        verbose_name='Name'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    country = models.CharField(
        max_length=50,
        verbose_name='Country'
    )

    def __str__(self):
        return self.name
