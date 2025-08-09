from django.db import models
from django.conf import settings
# Create your models here.
class Poll(models.Model):
    question=models.CharField(max_length=200)
    end_date=models.DateTimeField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Candidate(models.Model):
    name=models.CharField(max_length=100)
    poll=models.ForeignKey(Poll,on_delete=models.CASCADE,related_name='candidates')

    def __str__(self):
        return self.name

class Vote(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    poll=models.ForeignKey(Poll,on_delete=models.CASCADE)

    class Meta:
        unique_together=('user','poll') 
