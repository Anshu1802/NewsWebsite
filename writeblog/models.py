from django.db import models

class CreateBlog(models.Model):
    blogimage=models.ImageField(upload_to='image')
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=300)
    link=models.CharField(max_length=200)


    


