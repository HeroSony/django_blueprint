from django.db import models
from django.utils.translation import ugettext as translate
from django.utils.timezone import now


class AutoCreatedUpdatedMixin(models.Model):

    created_at = models.DateTimeField(
        verbose_name=translate('created at'),
        unique=False,
        null=True,
        blank=True,
        db_index=True,
    )

    updated_at = models.DateTimeField(
        verbose_name=translate('updated at'),
        unique=False,
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.created_at:
        # if not self.id or not self.created_at:
            self.created_at = now()
            self.updated_at = self.created_at
        else:
            auto_updated_at_is_disabled = kwargs.pop('disable_auto_updated_at', False)
            if not auto_updated_at_is_disabled:
                self.updated_at = now()
        super(AutoCreatedUpdatedMixin, self).save(*args, **kwargs)


class SoftDeleteMixin(models.Model):

    deleted_at = models.DateTimeField(
        verbose_name=translate('deleted at'),
        unique=False,
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = now()
        kwargs = {
            'using': using,
        }
        if hasattr(self, 'updated_at'):
            kwargs['disable_auto_updated_at'] = True
        self.save(**kwargs)


# Usage:
#
# from django.contrib.auth.models import AbstractUser
# from base.mixins import (
#     AutoCreatedUpdatedMixin,
#     SoftDeleteMixin,
# )
# 
# 
# class User(AbstractUser, AutoCreatedUpdatedMixin, SoftDeleteMixin):
#
#     # Unset AbstractUser.date_joined attribute.
#     date_joined = None
# 
#     def save(self, *args, **kwargs):
#         return super(User, self).save(*args, **kwargs)
#