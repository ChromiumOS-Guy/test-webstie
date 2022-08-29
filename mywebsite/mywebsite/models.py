from email import message
from django.db import models
from django.db import connections

class save_user_data(models.Model):
    username=models.CharField(max_length=50)
    bio=models.CharField(max_length=300)
    
    class Meta:
        db_table="user_data"