from django.db import models

# Create your models here.
class Review (models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    projects = models.ForeignKey(Projects,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=3000,blank=True)
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    


    def __str__(self):
        return self.user.username



