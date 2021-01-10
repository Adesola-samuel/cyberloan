from django.db import models
from django.contrib.auth.models import User

class Contributor(models.Model):
    name = models.CharField(max_length=35)
    office = models.CharField(max_length=30, default='')
    about = models.TextField(max_length=500, default='')
    phn = models.CharField(max_length=11, default='')
    picture = models.ImageField(upload_to='static/pictures', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Help(models.Model):
    task = models.CharField(max_length=35)
    howto = models.TextField(max_length=500, default='')
    video = models.FileField(upload_to='static/videos', blank=True)
    video_type = models.CharField(max_length=6, blank=True)
    def __str__(self):
        return self.task
    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)

class Prediction(models.Model):
    name = models.CharField(max_length=35)
    gender = models.IntegerField()
    married = models.IntegerField()
    dependents = models.IntegerField()
    education = models.IntegerField()
    self_employed = models.IntegerField()
    applicant_income = models.IntegerField()
    coapplicant_income = models.IntegerField()
    loan_amount_term = models.IntegerField()
    credit_history = models.IntegerField()
    property_area = models.IntegerField()
    loan_amount = models.FloatField()
    loan_status = models.CharField(max_length=12, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
