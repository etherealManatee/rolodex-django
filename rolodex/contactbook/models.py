from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=11)
    description = models.TextField()
    