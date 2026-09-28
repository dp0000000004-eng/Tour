from django.db import models

# Create your models here.


class Branch(models.Model):
    branch = models.CharField(max_length=355)

    def __str__(self):
        return self.branch
    
class TourForm(models.Model):
    name = models.CharField(max_length=355)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="tour_branch")
    contact_no = models.BigIntegerField()
    email = models.EmailField()