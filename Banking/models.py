from django.db import models
from fontawesome.fields import IconField



# Create your models here.
class Banking(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.TextField(max_length=100)
    tittle=models.TextField(max_length=50, default='SOME STRING')

    def __str__(self):
        return self.tittle
    def summ(self):
        return self.summary[:10]

class header(models.Model):
    Banking=models.ForeignKey(Banking, on_delete='None')
    title=models.TextField(max_length=100, default='SOME STRING')

    def __str__ (self):
       return self.title



#from fontawesome.fields import IconField


class Category(models.Model):

    icon = IconField()
    