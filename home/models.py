from django.db import models
from django.contrib.auth.models import User


# Create your models here.

shift = [
    ('Day','Day'),
    ('Night','Night')
]

class Handover(models.Model):
    Shift=models.CharField(choices=shift, max_length=50)
    Handover_From=models.ForeignKey(User, on_delete=models.CASCADE,related_name='handovers_from')
    Handover_To=models.ForeignKey(User, on_delete=models.CASCADE,related_name='handovers_to')
    title=models.CharField(max_length=500,)
    Tasks_In_Progress = models.TextField(blank=True, null=True)
    Important_Notes = models.TextField(blank=True, null=True)
    Date= models.DateTimeField(auto_now_add=True)
    Completed_task=models.BooleanField(default=False)
    completed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    


#Notices Model
class Notices(models.Model):
    Title=models.CharField(max_length=500)
    Notice=models.TextField()
    Notice_by=models.ForeignKey(User, on_delete=models.CASCADE)
    Date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
    
class Comment(models.Model):
    notice=models.ForeignKey(Notices, on_delete=models.CASCADE)
    comment_by=models.ForeignKey(User, on_delete=models.CASCADE,)
    remarks=models.TextField()
    date=models.DateTimeField(auto_now_add=True)