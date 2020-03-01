from django.db import models


# Create your models here.
class Banking(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.TextField(max_length=100,null=True)
    tittle=models.TextField(max_length=50,null=True)

    def __str__(self):
        return self.tittle
    def summ(self):
        return self.summary[:10]

class ki(models.Model):
    tittle=models.TextField(max_length=50,null=True)
    