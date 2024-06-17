from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
    featured = models.BooleanField(default=False)

# Below is the way to get absolute url
    def get_absolute_url(self):
        # syntax: reverse("name of url we defined in the path function inside url array in url.py", kwargs={key:value}) 
        # here key is the variable in the url and value is the dynamic value from the model
        return reverse("product", kwargs={"my_id": self.id})
