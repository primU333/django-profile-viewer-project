from django.db import models
'''from django.contrib.auth.models import User

class Info(models.Model):
    #photo = models.ImageField(upload_to='images')
    Email = models.CharField(max_length=100)
    Gender = models.CharField(max_length=6)
    About = models.TextField()
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Email'''