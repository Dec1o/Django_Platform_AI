from django.db import models
from companies.models import Company

class GroupFile(models.Model):
    group_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='groups')
    
    def __str__(self):
        return self.group_name
