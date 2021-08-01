from django.db import models

# Create your models here. 
# 
# DATABASE USE
# INTEGRATION TESTING USE
class FormsModel(models.Model):
    reply1 = models.CharField(
        max_length=240,
    ),
    reply2 = models.CharField(
        max_length=240,
    ),
    reply3 = models.CharField(
        max_length=240,
    )

    def __str__(self):
        return str(self.id) + " " + self.reply1 + " " + self.reply2 + " " + self.reply3
