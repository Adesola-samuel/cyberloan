from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from blog.models import Post
now = datetime.datetime.now()

class Cities(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    lat = models.FloatField(max_length=35)
    lng = models.FloatField(max_length=35)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    class Meta:
        ordering = ('city',)
    def __str__(self):
        return self.city +', '+self.country

class ProductCategory(models.Model):
    category = models.CharField(max_length=25)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.category

class Interest(models.Model):
    interest = models.CharField(max_length=35)
    color = models.CharField(max_length=35, default='' ,blank=True, null=True)
    logo = models.CharField(max_length=45 ,blank=True, null=True)
    def __str__(self):
        return self.interest

class Biodata(models.Model):
    profile=models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=8, blank=True, null=True)
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
    lga = models.CharField(max_length=50, default='')
    address = models.TextField(max_length=100, default='')
    phn = models.CharField(max_length=11, default='')
    mrt = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='static/blog/profile_pictures', blank=True, null=True)
    cover_pic = models.ImageField(upload_to='static/blog/cover_pictures', blank=True, null=True)
    about_me = models.CharField(max_length=150, default='')
    business = models.CharField(max_length=25, default='')
    highest_qualification = models.CharField(max_length=25, default='')
    facebook_page = models.URLField(blank=True, null=True)
    instagram_page = models.URLField(blank=True, null=True)
    twitter_page = models.URLField(blank=True, null=True)
    skype_page = models.URLField(blank=True, null=True)
    linked_in = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    works_completed = models.PositiveIntegerField(blank=True, null=True)
    started_work = models.DateField(blank=True, null=True)
    freelance = models.BooleanField(default=True)
    total_clients = models.PositiveIntegerField(blank=True, null=True)
    number_of_workers = models.PositiveIntegerField(blank=True, null=True)
    annual_working_hours = models.PositiveIntegerField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bus_profile = models.ImageField(upload_to='static/Services/profile',blank=True, null=True)
    bus_logo = models.ImageField(upload_to='static/Services/logo',blank=True, null=True)
    bus_title = models.CharField(max_length=35,default='')
    persuade = models.TextField(max_length=150,default='')
    bus_decription = models.TextField(max_length=300, default='')
    interest = models.ManyToManyField(Interest)
    archives = models.ManyToManyField(Post, related_name='archives')

    def delete(self, *args, **kwargs):
        self.profile_pic.delete()
        self.cover_pic.delete()
        self.bus_profile.delete()
        self.bus_logo.delete()
        super().delete(*args, **kwargs)

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, blank=True,null=True,on_delete=models.SET_NULL)
    client = models.CharField(max_length=35)
    title=models.CharField(max_length=35)
    description=models.TextField(max_length=35)
    image1=models.ImageField(upload_to='static/portfolio/images', blank=True, null=True)
    image2=models.ImageField(upload_to='static/portfolio/images', blank=True, null=True)
    image3=models.ImageField(upload_to='static/portfolio/images', blank=True, null=True)
    proj_url=models.URLField(default='')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.title

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=35)
    degree_of_perfection=models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])


class Services(models.Model):
    logo = models.CharField(max_length=45, blank=True, null=True)
    service = models.CharField(max_length=45)
    description = models.TextField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Testimony(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    testimony = models.TextField()
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)

class Certificate(models.Model):
    awarded_qualification =models.CharField(max_length=50)
    year_started=models.PositiveIntegerField(default=1960, validators=[MinValueValidator(1960), MaxValueValidator(now.year)])
    year_completed=models.PositiveIntegerField(default=1960, validators=[MinValueValidator(1960), MaxValueValidator(now.year)])
    school =models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Experience(models.Model):
    post=models.CharField(max_length=100)
    year_started = models.PositiveIntegerField(default=1960,
                                               validators=[MinValueValidator(1960), MaxValueValidator(now.year)])
    year_completed = models.PositiveIntegerField(default=1960,
                                                 validators=[MinValueValidator(1960), MaxValueValidator(now.year)])
    address = models.TextField(max_length=100, default='')
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)
    experience = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


