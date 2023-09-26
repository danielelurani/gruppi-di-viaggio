import unittest
from django.test import TestCase, Client
from django.urls import reverse
from organizzatoreViaggi.forms import CreateUserForm, TravelForm, InvitationForm
from organizzatoreViaggi.models import CustomUser, Travel, Invitation


class test_invitation(TestCase):

    @classmethod
    def setUpClass(self):

        super().setUpClass()
        self.client = Client()

        self.user1 = CustomUser.objects.create_user(username='test1', email='test1@test.com')
        self.user2 = CustomUser.objects.create_user(username='test2', email='test2@test.com')


        self.travel = Travel.objects.create(
            name='Viaggio Test',
            destination= 'Destinazione Test',
            start_date='2024-06-01',
            end_date='2024-06-03'
        )
        self.travel.participants.add(self.user1)

    def test_existence(self):
        self.assertTrue(CustomUser.objects.filter(username=self.user1.username).exists())
        self.assertTrue(CustomUser.objects.filter(username=self.user2.username).exists())
        self.assertTrue(Travel.objects.filter(name=self.travel.name).exists())
        self.assertIn(self.user1, self.travel.participants.all())

    def test_valid_data(self):
        self.client.login(username=self.user1.username, password=self.user1.password)
        form = InvitationForm(sender=self.user1,
                              data={'receiver': self.user2.email, 'travel': self.travel})
        self.assertTrue(form.is_valid())


    def test_invitation_form_invalid_data(self):
        non_existing_email = 'non_existing_email@email.com'
        form = InvitationForm(sender=self.user1,
                              data={'receiver': non_existing_email, 'travel': self.travel})
        self.assertFalse(form.is_valid())

    def test_invitation_already_exists(self):

        form = InvitationForm(sender=self.user1,
                              data={'receiver': self.user2.email, 'travel': self.travel})
        self.assertTrue(form.is_valid())

        inv = Invitation.objects.create(
            sender=self.user1,
            receiver=self.user2.email,
            travel=self.travel
        )
        inv.save()

        form = InvitationForm(sender=self.user1,
                              data={'receiver': self.user2.email, 'travel': self.travel})
        self.assertFalse(form.is_valid())
        self.assertNotIn(self.user2, self.travel.participants.all())
        self.assertEqual(inv, Invitation.objects.get(receiver=self.user2.email, travel=self.travel))

