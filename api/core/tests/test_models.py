"""
Tests for Models
"""
from django.test import TestCase

from core import models

class ModelTests(TestCase):

    def test_vessel(self):
        """Test Creating a Vessel is Successful"""
        vessel = models.Vessel.objects.create(
            vessel_name = "Titanic"
        )

        self.assertEqual(str(vessel), vessel.vessel_name)