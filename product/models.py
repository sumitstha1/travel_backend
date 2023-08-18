from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.
class Country(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class City(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Destination(BaseModel):
    title = models.CharField(max_length=255)
    location = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city")
    grade = models.CharField(max_length=255)
    fees = models.IntegerField()
    meta_desc = models.TextField()
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Destination, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class DestinationImage(BaseModel):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="imgSrc")
    imgSrc = models.ImageField(upload_to="destination")

    def __str__(self):
        return self.destination.title