import uuid

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db import models
from jsonfield import JSONField

TEXT = 'text'
NUMBER = 'number'
DATE = 'date'
CHOICES = 'enum'

TYPE_CHOICES = (
    (TEXT, _(u"Text")),
    (NUMBER, _(u"Integer")),
    (DATE, _(u"Date")),
    (CHOICES, _(u"Multiple Choice")),
)


def get_default_meta(type):
    """
    nice helper function to create meta for field when the user is creating a form
    :param type:
    :return:
    """
    obj = {'is_required': False}
    if type == TEXT:
        obj['default'] = ''
    if type == DATE:
        obj['default'] = ''
    if type == CHOICES:
        obj['options'] = []
    if type == NUMBER:
        obj['default'] = 0
    return obj


class FormTemplate(models.Model):
    """
    Idea revolves around the fact that a user creating a insurance risk can create it from template predefined by
    britecore or any other moderator admins
    """
    name = models.CharField(max_length=255)


class FormTemplateField(models.Model):
    """
    fields for template
    """
    template = models.ForeignKey(FormTemplate, related_name="fields", on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    meta = JSONField(null=True, blank=True)


class RiskType(models.Model):
    """
    defined risk types, a user can have the flexibility of creating new form (riskType form) or use existing template.
    this structure allows for user to use the template fields and also create new fields or edit template fields.
    When ever user selects "use from template" The RiskType instance will be created and it will copy the fields
    (FromTemplateFields) to RiskTypeField.
    """
    name = models.CharField(max_length=255)
    template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % self.name


class RiskTypeField(models.Model):
    """
    Fields that form creator uses
    meta: allows users to create some validations of the fields,
    meta = {
        "is_required" : true,
        "default" : <some-value>
        "color" : '#ffffff'
    }
    """
    label = models.CharField(max_length=60)
    risk_type = models.ForeignKey(RiskType, related_name="fields", on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    meta = JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('label', 'risk_type')

    def __str__(self):
        return "%s : %s" % (self.label, self.risk_type)

    def save(self, *args, **kwargs):
        if self.type == CHOICES:
            if not self.meta:
                raise ValueError('need meta field')
            if 'options' not in self.meta:
                raise ValueError('Emum fields needs an options keyword')
            if not self.meta.get('options'):
                raise ValueError('Atleast One Option is required')
        return super(RiskTypeField, self).save(*args, **kwargs)

# class UserResponse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="form_responses")
#     risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE, related_name="user_responses")
#
# class UserFieldResponse(models.Model):
#     response = models.ForeignKey(UserResponse, on_delete=models.CASCADE, related_name="user_field_responses")
#     field = models.ForeignKey(RiskTypeField, on_delete=models.CASCADE, related_name="user_responses")
#     value = models.TextField(null=True, blank=True)
