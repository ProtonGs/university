from django.db import models

class Data_users(models.Model):
    nickname = models.CharField('nick', max_length=30)
    login = models.CharField('login', max_length=30)
    password = models.CharField('password', max_length=30)
    password_confirmation = models.CharField('password_confirmation', max_length=30)

    def __str__(self):
        return self.nickname
    
    class Meta:
        verbose_name = 'Data_user'
        verbose_name_plural = "Data_users"