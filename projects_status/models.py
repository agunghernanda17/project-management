from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from projects.models import Task

#library buat validators 
from django.core.validators import MinValueValidator, MaxValueValidator

        
class Projects_status(models.Model):
    """
    Projects Status
    """
    class Meta:
        ordering = ["task"]
        verbose_name = _("Project Status")
        verbose_name_plural = _("Projects Status")

    task = models.ForeignKey(Task, blank=True, null=True,unique=True, on_delete=models.PROTECT)
    comment = models.TextField(_("comment"), max_length=2000, null=True, blank=True)
    project_owner = models.CharField(_("project owner"), max_length=50, null=True, blank=True)
    user_requirements=models.IntegerField(_("user requirements (%)"),default=0,null=True, blank=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    user_comment = models.TextField(_("remarks"), max_length=3000, null=True, blank=True,)
    development=models.IntegerField(_("development (%)"),default=0,null=True, blank=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    dev_comment = models.TextField(_("remarks"), max_length=3000, null=True, blank=True)
    sit=models.IntegerField(_("SIT (%)"),default=0,null=True, blank=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    sit_comment = models.TextField(_("remarks"), max_length=3000, null=True, blank=True)
    uat=models.IntegerField(_("UAT (%)"),default=0,null=True, blank=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    uat_comment = models.TextField(_("remarks"), max_length=3000, null=True, blank=True)
    implementation=models.IntegerField(_("Implementation (%)"),default=0,null=True, blank=True,validators=[MaxValueValidator(100),MinValueValidator(0)])
    imp_comment = models.TextField(_("remarks"), max_length=3000, null=True, blank=True)	
    is_done = models.BooleanField(_("done?"), default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_assigned', verbose_name=_('PIC IT'),
                                   on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='projects_status_created_by', verbose_name=_('created by'),
                                   on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True, editable=False)

    def __str__(self):
        return self.comment
