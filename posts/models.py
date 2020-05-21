from django.db import models
# Create your models here.
    
class Blog(models.Model):
   blogtopic = models.CharField(max_length= 200)
   blogcontent = models. TextField()
   blogsummary= models.CharField(max_length= 500)
   draft =models. BooleanField()
   image= models.ImageField(upload_to = 'pics')
   date_published=  models.DateTimeField(auto_now=True)

def __str__(self):
	return self.blogtopic

