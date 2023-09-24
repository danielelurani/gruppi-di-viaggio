import unittest
from django.test import Client, TestCase
from organizzatoreViaggi.forms import CreateUserForm, TravelForm, InvitationForm
from organizzatoreViaggi.models import CustomUser, Travel, Invitation



class TestTravel(TestCase):

    @classmethod
    def setUp(self):

        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.valid_data = {
            'name': 'Viaggio Test',
            'destination': 'Destinazione Test',
            'start_date': '01/06/2024',
            'end_date': '03/06/2024'
        }

        self.invalid_data = {
            'name': 'Viaggio Test',
            'destination': 'Destinazione Test',
            'start_date': '03/06/2024',
            'end_date': '01/06/2024'
        }

    def test_travel_form_valid_data(self):
        form = TravelForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_travel_form_invalid_data(self):
        form = TravelForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

