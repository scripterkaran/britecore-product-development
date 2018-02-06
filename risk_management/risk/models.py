from django.db import models
from risk_management.risk_type.models import RiskType


class Risk(models.Model):
    risk_type = models.ForeignKey(RiskType, related_name="risk_types", on_delete=models.CASCADE)
    # ... other fields
