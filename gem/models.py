from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')

    def __str__(self):
        return os.path.basename(self.file.name)


@receiver(post_delete, sender=Attachment)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False) 