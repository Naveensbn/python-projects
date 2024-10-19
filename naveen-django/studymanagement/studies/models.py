from django.db import models

class Study(models.Model):
    PHASE_CHOICES = [('phase I', 'phase I'),
                     ('phase II', 'phase II'),
                     ('phase III', 'phase III'),
                     ('phase IV', 'phase IV')
                     ]
    study_name= models.CharField(max_length=50)
    study_phase=models.CharField(max_length=50,choices=PHASE_CHOICES)
    sponsor_name = models.CharField(max_length=60)
    study_description = models.TextField()

    # def __str__(self):
    #     return self.study_name
# Create your models here.

