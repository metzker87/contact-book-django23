from django.db import models
from django.utils import timezone
# first_name (string), last_name (string) , phone (string)
# email (email), created_date (date) description (text)
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

class Contact(models.Model):
    first_name = models.CharField('Name', max_length=100, blank=False )
    last_name  = models.CharField("Surname",max_length=254,blank=True,)
    phone = models.CharField('Phone', max_length=11)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
