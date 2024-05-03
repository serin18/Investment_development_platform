from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserdb(AbstractUser):
    full_name=models.CharField(max_length=60,null=True)
    mobile=models.PositiveBigIntegerField(null=True)
    country=models.CharField(max_length=60,null=True)
    designation=models.CharField(max_length=200,null=True)
    proff_bio=models.CharField(max_length=300,null=True)
    twitter=models.URLField()
    linkedin=models.URLField()
    web=models.URLField()
    Location=models.CharField(max_length=300,null=True)
    is_innovator=models.BooleanField(default=False)
    is_investor=models.BooleanField(default=False)
    profile_pic=models.ImageField(upload_to='files',blank=True)

    def __str__(self):
        return self.full_name

class Categorydb(models.Model):
    c_name=models.CharField(max_length=30,null=True)

class Projectdb(models.Model):
    project_name=models.CharField(max_length=40)
    description=models.TextField(max_length=500)
    category=models.ForeignKey(Categorydb,on_delete=models.CASCADE,null=True)
    amount=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    inovator=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True)

class projectupdatedb(models.Model):
    project_name=models.ForeignKey(Projectdb,on_delete=models.CASCADE,null=True)
    update_message=models.CharField(max_length=300,null=True)
    date_time=models.DateTimeField(auto_now=True)

class Messagedb(models.Model):
    sender=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True,related_name='sent_messages')
    receiver=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True,related_name='received_messages')
    message=models.CharField(max_length=100,null=True)

class Notificationdb(models.Model):
    sender=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True,related_name='send')
    receiver=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True,related_name='receive')
    project=models.ForeignKey(Projectdb,on_delete=models.CASCADE,null=True)
    Is_there=models.BooleanField(default=False,null=True)
    date_time=models.DateTimeField(auto_now=True,null=True)

class Investeddb(models.Model):
    project_name=models.ForeignKey(Projectdb,on_delete=models.CASCADE,null=True)
    investor=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True)

class Paymentdb(models.Model):
    sender=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True,related_name='send_amount')
    receiver=models.ForeignKey(CustomUserdb,on_delete=models.CASCADE,null=True,related_name='received_amount')
    amount_recived=models.DecimalField(max_digits=10, decimal_places=2)
    amount_refund=models.DecimalField(max_digits=10, decimal_places=2)
    Bool=models.BooleanField(default=False)
    date_rec=models.DateTimeField(auto_now=True)
    refund_date=models.DateTimeField(auto_now=True)




