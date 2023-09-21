import unittest
from django.test import Client, TestCase
from organizzatoreViaggi.forms import CommentForm, InvitationForm, CreateUserForm, TravelForm, StageForm


class TestForms(TestCase):


    """ TEST CREATE USER FORM """
    def test_create_user_form_valid_data(self):
        form = CreateUserForm(data={
            'username': 'user Test',
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'testuser@test.com',
            'password1': 'passwordTest',
            'password2': 'passwordTest'
        })
        self.assertTrue(form.is_valid());

    def test_create_user_form_invalid_data(self):
        form = CreateUserForm(data={
            'username': 'user Test',
            'first_name': 'Test',
            'last_name': 'Test',
            'email': 'testuser@test.com',
            'password1': 'passwordTest',
            'password2': 'wrongPasswordTest'
        })
        self.assertFalse(form.is_valid());


    """ TEST TRAVEL FORM """
    def test_travel_form_valid_data(self):
        form = TravelForm(data= {
            'name': 'Viaggio Test',
            'destination': 'Destinazione Test',
            'start_date': '1/06/2024',
            'end_date': '3/06/2024'
        })
        self.assertTrue(form.is_valid())

    def test_travel_form_invalid_data(self):
        form = TravelForm(data= {
            'name': 'Viaggio Test',
            'destination': 'Destinazione Test',
            'start_date': '3/06/2024',
            'end_date': '1/06/2024'
        })
        self.assertFalse(form.is_valid())


