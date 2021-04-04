from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    desc= models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='awwad/')
    link = models.URLField(max_length=70)
    technologies = models.CharField(max_length=100)


    def __str__(self):
        return self.title

    def save_awwa(self):
        self.save()

    def delete_awwa(self):
        self.delete()



