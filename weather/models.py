from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30, help_text='Enter the name of the city to find out the weather in it.')

    def _srt_(self):
        return self.name
