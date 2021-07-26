from django.db import models
class signup_table(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    confirmpassword=models.CharField(max_length=30)


    def __str__(self):
        return self.name

# Create your models here.
