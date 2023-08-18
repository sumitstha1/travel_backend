from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.dispatch import receiver
from django.db.models.signals import post_save
from base.email import send_account_activation_email
import uuid

# Create your models here.
class Profile(BaseModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile")
    contact_number = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "Profile"

class Contact(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self) -> str:
        return self.first_name
    
class Newsletter(BaseModel):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email
    
@receiver(post_save, sender = User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance, email_token = email_token)
            email = instance.email
            send_account_activation_email(email, email_token)
        
    except Exception as e:
            print(e)