from django.db import models
from django.urls import reverse 
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    date = models.DateField()

    def get_absolute_url(self):
        # return f"/render_lookup_view/{self.id}/"
        return reverse("blog:article-details", kwargs={"id": self.id})