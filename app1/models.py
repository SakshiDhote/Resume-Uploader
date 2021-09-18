from django.db import models

# Create your models here.

class tbl_state(models.Model):
    stateid=models.AutoField(primary_key=True) #Primary Key
    statename=models.CharField(max_length=50)
    class Meta:
        db_table='tblstate'

    def __str__(self):
        return self.statename


class tbl_city(models.Model):
    cityid=models.AutoField(primary_key=True)    #Primary Key
    stateid = models.ForeignKey(tbl_state,on_delete=models.CASCADE,null=True,blank=True)   #Foreign Key
    cityname=models.CharField(max_length=50)
    class Meta:
        db_table='tblcity'
    def __str__(self):
        return self.cityname


class ResumeModel(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=10)
    locality=models.CharField(max_length=100)
    city=models.ForeignKey(tbl_city,on_delete=models.CASCADE,null=True,blank=True)
    pin=models.PositiveIntegerField()
    state=models.ForeignKey(tbl_state,on_delete=models.CASCADE,null=True,blank=True)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profile_image',blank=True)
    resume=models.FileField(upload_to='doc',blank=True)