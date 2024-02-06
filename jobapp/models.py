from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name
    
class job(models.Model):
    title=models.CharField(max_length=20)
    company_name=models.CharField(max_length=20)
    experience=models.PositiveBigIntegerField()
    salary=models.PositiveIntegerField()
    qualification=models.CharField(max_length=20)
    skills=models.CharField(max_length=200)
    poster=models.ImageField(upload_to="poster")
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Student(models.Model):
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=30)
    age=models.PositiveBigIntegerField()
    experience=models.PositiveIntegerField()
    qualification=models.CharField(max_length=20)
    skills=models.CharField(max_length=200)
    resume=models.FileField(upload_to="files",null=True)
    options=(
        ("male","male"),("female","female"),("others","others")
    )
    gender=models.CharField(max_length=20,choices=options,default="male")
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING,null=True,related_name="profile")
    #Category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name
    
class Applications(models.Model):
    jobs=models.ForeignKey(job,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("pending","pending"),("rejected","rejected"),("processing","processing")
    )
    status=models.CharField(max_length=20,choices=options,default="pending")