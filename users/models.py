from django.db import models
from django.contrib.auth.models import User
from  PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=18)
    voters_card_num = models.CharField(max_length=200)
    constituancy = models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{ self.user} profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            output_zise =(200, 200)
            img.thumbnail(output_zise)
            img.save(self.image.path)
