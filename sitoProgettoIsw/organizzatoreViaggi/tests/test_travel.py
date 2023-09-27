import unittest
from django.test import Client, TestCase
from organizzatoreViaggi.forms import CreateUserForm, TravelForm, InvitationForm
from organizzatoreViaggi.models import CustomUser, Travel, Invitation, Stage
from django.urls import reverse



class TestTravel(TestCase):

    @classmethod
    def setUp(self):

        self.client = Client()
        self.userHomePage_url = reverse('userHomePage')
        self.myTravels_url = reverse('myTravels')

        self.username= 'testuser'
        self.password= 'testpassword'

        self.user = CustomUser.objects.create_user(
            username= self.username,
            password=self.password
        )

        self.travel = Travel.objects.create(
            name= 'Viaggio Test',
            destination= 'Destinazione Test ',
            start_date= '2024-06-01',
            end_date= '2024-06-03'
        )

        self.stage = Stage.objects.create(
            name='Tappa Test',
            date= '2024-06-03',
            travel=self.travel
        )
        self.changeItinerary_url = reverse('changeItinerary', args=[self.travel.id])

        self.valid_data = {
            'name': 'Viaggio Test 1',
            'destination': 'Destinazione Test 1',
            'start_date': '2024-06-01',
            'end_date': '2024-06-03'
        }

        self.invalid_data = {
            'name': 'Viaggio Test 2',
            'destination': 'Destinazione Test 2',
            'start_date': '2024-06-03',
            'end_date': '2024-06-01'
        }

    def test_travel_form_valid_data(self):
        form = TravelForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_travel_form_invalid_data(self):
        form = TravelForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())


    def test_create_travel(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.userHomePage_url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.myTravels_url)
        test_travel = Travel.objects.get(id=2)
        self.assertEqual(test_travel.name, 'Viaggio Test 1')
        self.assertEqual(test_travel.destination, 'Destinazione Test 1')
        self.assertEqual(str(test_travel.start_date), '2024-06-01')
        self.assertEqual(str(test_travel.end_date), '2024-06-03')
        self.assertIn(self.user, test_travel.participants.all())


    def test_create_wrong_travel(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.userHomePage_url, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizzatoreViaggi/userHomePage.html')
        self.assertFalse(response.context['form'].is_valid())
        self.assertFalse(Travel.objects.filter(name='ViaggioTest 2').exists())


    def test_modify_travel(self):
        self.client.login(username=self.username, password=self.password)
        new_data_travel = {
            'edit_travel': 'Edit Travel',
            'name': 'Viaggio Test 3',
            'destination': 'Destinazione Test 3',
            'start_date': '2024-09-01',
            'end_date': '2024-09-03'
        }
        response = self.client.post(reverse('changeItinerary', args=[self.travel.id]), new_data_travel)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.myTravels_url)


    def test_remove_stage(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('changeItinerary', args=[self.travel.id]), {
            'remove_stage': 'Remove Stage',
            'stage_id': self.stage.id,
        })
        self.assertRedirects(response, reverse('detailsTravel', args=[self.travel.id]))
        self.assertFalse(Stage.objects.filter(id=self.stage.id).exists())
