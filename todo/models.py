from django.db import models

# Create your models here.
class todoItem(models.Model):
  content = models.TextField()

  def _str_(self):
    return self.content