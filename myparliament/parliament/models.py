from django.db import models


class ParliamentMembers(models.Model):
    name = models.CharField(max_length=50)
    date_birth = models.CharField(max_length=10, blank=True, null=True)
    place_birth = models.CharField(max_length=250, blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    languages = models.CharField(max_length=250, blank=True, null=True)
    selected_with = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField()
    image = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
