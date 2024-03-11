from django.db import models

# Create your models here.
class Vessel(models.Model):
    vessel_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.vessel_name
    
class VesselSchedule(models.Model):
    vessel = models.ForeignKey(Vessel)
    voyage_number = models.CharField(max_length = 50)
    arrival_date = models.DateField()

    def __str__(self):
        return self.vessel.vessel_name - self.voyage_number
    
class BillOfLading(models.Model):
    CUSTOMS_HOLD = "C"
    STEAMSHIP_HOLD = "S"
    RELEASED = "R"
    AVAILABLE_FOR_PICKUP = "A"
    STATUS_CHOICES = {
        CUSTOMS_HOLD: "Customs Hold",
        STEAMSHIP_HOLD: "Steamship Hold",
        RELEASED: "Released",
        AVAILABLE_FOR_PICKUP: "Available for Pickup",
    }
    voyage = models.ForeignKey(Vessel, on_delete=models.PROTECT)
    bol_number = models.CharField(max_length = 200)
    contact_name = models.CharField(max_length = 200)
    contact_number = models.CharField(max_length = 200)
    contact_email = models.EmailField(max_length = 200)
    release_status = models.Choice

    def __str__(self):
        return self.bol_number
    
class Container(models.Model):
    bol = models.ForeignKey(BillOfLading, on_delete=models.PROTECT)
    container_number = models.CharField(max_length = 200)



    


