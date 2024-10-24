from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import SET_DEFAULT
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

# Create your models here.


class Conversation(BaseModel):
    title = models.CharField(max_length=100, help_text=_("The maximum number of characters is 100."))
    author = models.ForeignKey(get_user_model(), default="Unknown", on_delete=SET_DEFAULT)
    content = models.TextField(blank=True, max_length=11000, help_text=_("The maximum number of characters is 11000."))
    image = models.ImageField(upload_to="forum/conversation/images", null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.author.username if self.author else 'Unknown'} created: {self.created_at} last updated: {self.last_updated}"


class Comments(BaseModel):
    author = models.ForeignKey(get_user_model(), default="Unknown", on_delete=SET_DEFAULT)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField(blank=True, max_length=8000, help_text=_("The maximum number of characters is 8000."))
    image = models.ImageField(upload_to="forum/comments/images", null=True, blank=True)

    def __str__(self):
        return f"{self.author.username if self.author else 'Unknown'} commented: {self.created_at} last updated: {self.last_updated}"
