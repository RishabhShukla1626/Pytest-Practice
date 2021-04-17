from django.db import models
from django.utils import timezone
# Create your models here.
class Companies(models.Model):
    class CompanyStatusChoices(models.TextChoices):
        LAYOFF = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"
    
    name = models.CharField(max_length=120, unique=True)
    status = models.CharField(choices=CompanyStatusChoices.choices, 
                    default=CompanyStatusChoices.HIRING, max_length=30)
    last_updated = models.DateTimeField(default=timezone.now, editable=True)
    application_notes = models.URLField(blank=True, max_length=100)

    def __str__(self):
        return self.name
