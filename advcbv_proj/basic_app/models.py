from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class School(models.Model):
    ques = models.TextField()
    ans = models.TextField(blank = True)

    def __str__(self):
        return self.ques

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk':self.pk})

class SchoolSt(models.Model):
    ques = models.TextField()
    ans = models.TextField(blank = True)

    def __str__(self):
        return self.ques

    def get_absolute_url(self):
        return reverse('basic_app:detailst', kwargs={'pk':self.pk})
