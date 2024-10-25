from django.contrib import admin

from forum.models import Comments, Conversation

# Register your models here.


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin): ...


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin): ...
