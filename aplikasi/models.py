from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from vendor.models import Vendor

phones_tr = _("phones")


class Aplikasi(models.Model):
    """
    Aplikasi
    """
    class Meta:
        ordering = ["name"]
        verbose_name = _("Aplikasi")
        verbose_name_plural = _("Aplikasi")

    name = models.CharField(_("name"), max_length=200)
    project_owner =  models.CharField(_("project owner"), max_length=50, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.PROTECT)
    comment = models.TextField(_("comment"), max_length=2000, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='aplikasi_created', verbose_name=_('created by'),
                                   on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True, editable=False)

    def __str__(self):
        return self.name

    @property
    def phones(self):
        return ", ".join(filter(None, (self.phone, self.mobile)))
