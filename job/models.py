from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.contrib.auth.models import User




JOB_TYPE = (
    ('full-time', 'full-time'),
    ('part-time', 'part-time'),
)

def image_upload(instance, filename):
    imagename,  extension = filename.split(".")
    return "jobs/%s.%s"%(extension.id ,extension)

class Job(models.Model):

    CHOICES = [
        ('WEB DEVELOPMENT'          , 'WEB DEVELOPMENT'),
        ('SOFTWARE DEVELOPMENT'     , 'SOFTWARE DEVELOPMENT'),
        ('MARKETING DEVELOPMENT'    , 'MARKETING DEVELOPMENT'),
        ('MOBILE DEVELOPMENT'       , 'MOBILE DEVELOPMENT'),

    ]

    title           = models.CharField(max_length=100)
    job_type        = models.CharField(max_length=100, choices= JOB_TYPE)
    description     = models.TextField(max_length=1000)
    published_at    = models.DateTimeField(auto_now=True)
    categories      = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True)
    vacancy         = models.IntegerField(default=1)
    salary          = models.IntegerField(default=0)
    experience      = models.IntegerField(default=1)
    image           = models.ImageField(image_upload, blank=True, null=True)
    country         = CountryField(multiple=False, blank=True, null=True)
    city            = models.CharField(max_length=50, blank=True, null=True)
    slug            = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['-published_at']


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
        

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, related_name='Apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    cv = models.FileField(upload_to="Apply/")
    cover_letter = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now=True)
    image   = models.ImageField(upload_to='Candidate_profile/', blank=True, null=True)
    job_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    




class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, related_name='Resume', on_delete=models.CASCADE, blank=True, null=True )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
    cv = models.FileField(upload_to="Apply/")
    cover_letter = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class PopularCategorie(models.Model):
    POPCat      = models.CharField(max_length=100, blank=True, null=True)
    image       = models.ImageField(image_upload, blank=True, null=True)
    POPNumber       = models.IntegerField()


    def __str__(self):
        return str(self.POPCat)







    
  


