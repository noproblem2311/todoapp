from django.db import models

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Type(models.Model):
    name = models.CharField(max_length=200)
    Plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-created", "-updated"]

class Task(models.Model):
    Type = models.ForeignKey(Type, on_delete=models.CASCADE,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:30]
    class Meta:
        ordering = ["-created", "-updated"]
