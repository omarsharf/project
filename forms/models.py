from django.db import models
import uuid

class VehicleType(models.TextChoices):
    MOTORCYCLE = 'motorcycle', 'دراجة نارية'
    CAR = 'car', 'سيارة'
    VAN = 'van', 'فان'
    TRUCK = 'truck', 'شاحنة'

class ShipmentRequest(models.Model):
    id = models.AutoField(primary_key=True)
    pickup_address = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=20, choices=VehicleType.choices)
    scheduled_at = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    tracking_number = models.CharField(max_length=12, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = uuid.uuid4().hex[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + '---' + self.tracking_number