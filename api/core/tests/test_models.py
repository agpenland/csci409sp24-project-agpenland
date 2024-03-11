"""
Tests for Models
"""
from django.test import TestCase

from core import models
from datetime import datetime 

def create_vessel():
    return models.Vessel.objects.create(
        vessel_name="Lusitania",
    )

def create_bill_of_lading():
    return models.BillOfLading.objects.create(
        voyage = create_vessel(),
        bol_number = "3",
        contact_name = "Davy Jones",
        contact_number = "777-666-5555",
        contact_email = "djones@gmail.com"
    )


class ModelTests(TestCase):

    def test_vessel(self):
        """Test Creating a Vessel is Successful"""
        vessel = models.Vessel.objects.create(
            vessel_name = "Titanic"
        )

        self.assertEqual(str(vessel), vessel.vessel_name)
    
    def test_vessel_schedule(self):
        vessel_schedule = models.VesselSchedule.objects.create(
            vessel = create_vessel(),
            voyage_number = "14",
            arrival_date = datetime.now()
        )

        self.assertEqual(str(vessel_schedule), str(vessel_schedule.vessel.vessel_name)+vessel_schedule.voyage_number)

    def test_bill_of_lading(self):
        bill_of_lading = models.BillOfLading.objects.create(
            voyage = create_vessel(),
            bol_number = "2",
            contact_name = "George Wilkins",
            contact_number = "843-987-4546",
            contact_email = "gwilkins@gmail.com"
        )

        self.assertEqual(str(bill_of_lading), str(bill_of_lading.bol_number))

    def test_container(self):
        container = models.Container.objects.create(
            bol = create_bill_of_lading(),
            container_number = "21"
        )

        self.assertEqual(str(container), str(container.container_number))

   
