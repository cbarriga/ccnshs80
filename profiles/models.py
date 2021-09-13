from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.png', upload_to='profile_images')

    married_name = models.CharField(max_length=32, null=True, blank=True)

    address = models.TextField(max_length=500, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    landline_number = models.CharField(max_length=20, null=True, blank=True)

    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return str(self.user.username)

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
    else:
        instance.profile.save()

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)