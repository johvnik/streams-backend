from django.db import models
from streams.apps.core.models import TimestampedModel
from streams.settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _


# In the case the account or comment is deleted and it has children, we wan't to
# mark it deleted in the UI, not hide it completely.
class CommentManager(models.Manager):
    def get_queryset(self):
        return super(CommentManager, self).get_queryset().select_related('account')\
            .filter(account__is_active=True, is_deleted=False)


class Comment(TimestampedModel):
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, default=None)
    account = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption = models.CharField(max_length=2200)
    is_deleted = models.BooleanField(default=False)

    objects = models.Manager()
    active = CommentManager()

    def __str__(self):
        return f'account: {self.account}, comment: {self.caption[:20]}'

    def set_deleted(self):
        self.is_deleted = True
        self.save()
