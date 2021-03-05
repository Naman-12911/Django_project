from django.db import models

# Create your models here.

class Sinup(models.Model):
    name = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=122)
    def __str__(self):
        return self.name
"""""    
class login(models.Model):
    login_username = models.CharField(max_length=122)
    login_password = models.CharField(max_length=122)
    def __str__(self):
        return self.login_username
      """""
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.IntegerField()
    text = models.TextField()
    def __str__(self):
        return self.name


#class CaptchaTestModelForm(forms.ModelForm):
    #captcha = CaptchaField()

    #class Meta:
        #model = MyModel