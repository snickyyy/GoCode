from forum.models import Comments, Conversation


def sample_post(author, **kwargs):
    default = {
        "author": author,
        "title": "test title",
        "content": "The best content on forum",
    }
    default.update(kwargs)
    return Conversation.objects.create(**default)


def sample_comment(author, **kwargs):
    default = {
        "author": author,
        "conversation": sample_post(author),
        "content": "Great comment!",
    }
    default.update(kwargs)
    return Comments.objects.create(**default)
