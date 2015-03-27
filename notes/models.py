from datetime import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Note(TimeStampedModel):
    """
    A simple model to handle adding arbitrary numbers of notes to a generic object.
    """
    date = models.DateField(_('Date'), default=datetime.now())
    content = models.TextField(_('Content'))
    public = models.BooleanField(_('Public'), default=True)
    author = models.ForeignKey(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    objects = models.Manager()

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

    @models.permalink
    def get_absolute_url(self):
        return ('notes-view', (), {'pk': self.pk})
