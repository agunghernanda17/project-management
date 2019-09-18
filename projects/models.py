import logging
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from vendor.models import Vendor
from coleman.utils.mail import send_mail_async as send_mail
from hashlib import sha1


logger = logging.getLogger(__name__)

number_tr = _("number")


class Task(models.Model):
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    STATUSES = (
        ('A', _('Active/In Progress')),
        ('C', _('Completed')),
        ('W', _('Waiting/Pending')),
        ('E', _('Explore/Requirement Not Clear')),
        ('N', _('Next Year')),
        ('D', _('Drop/Reject/Cancel'))
    )

    PRIORITIES = (
        ('00_low', _('Low')),
        ('10_normal', _('Normal')),
        ('20_high', _('High')),
        ('30_critical', _('Critical')),
        ('40_blocker', _('Blocker'))
    )

    project_title = models.CharField(_("project title"), max_length=200)
    project_owner = models.TextField(_("project owner"), max_length=2000, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.PROTECT)
    blueprint_title = models.CharField(_("blueprint title"), max_length=200)
    blueprint = models.TextField(_("blueprint"), max_length=2000, null=True, blank=True)
    changes = models.TextField(_("changes"), max_length=2000, null=True, blank=True)
    release = models.TextField(_("release"), max_length=2000, null=True, blank=True)
    register_date = models.DateField(_("register date"), null=True, blank=True)
    #year = models.TextField(_("year"), max_length=2000, null=True, blank=True)
    target_implement_date = models.DateField(_("target implement date"), null=True, blank=True)
    actual_implement_date = models.DateField(_("actual implement date"), null=True, blank=True)
    state = models.CharField(_("state"), max_length=20, choices=STATUSES, default='A')
    mandays = models.TextField(_("mandays"), max_length=2000, null=True, blank=True)
    remarks = models.TextField(_("remarks"), max_length=2000, null=True, blank=True)
    references = models.TextField(_("references"), max_length=2000, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project_buat', verbose_name=_('PIC IT'),
                                   on_delete=models.SET_NULL, null=True, blank=True)
    
    priority = models.CharField(_("priority"), max_length=20, choices=PRIORITIES, default='10_normal')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users_created', verbose_name=_('created by'),
                                   on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True, editable=False)

    def __str__(self):
        return "[%s] %s" % (self.number, self.project_title)

    @property
    def number(self):
        return "{:08d}".format(self.pk)

    

    

