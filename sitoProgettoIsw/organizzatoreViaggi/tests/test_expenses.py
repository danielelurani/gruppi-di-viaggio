import unittest
from django.test import Client, TestCase
from organizzatoreViaggi.forms import CreateUserForm, TravelForm, InvitationForm, CommentForm, ExpenseForm
from organizzatoreViaggi.models import CustomUser, Travel, Invitation, Stage, Comment, Expense
from django.urls import reverse


class TestExpenses(TestCase):

    def setUp(self):
        self.client = Client()
        self.myTravels_url = reverse('myTravels')

        self.username = 'testuser'
        self.password = 'testpassword'

        self.user = CustomUser.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.travel = Travel.objects.create(
            name='Viaggio Test',
            destination='Destinazione Test ',
            start_date='2024-06-01',
            end_date='2024-06-03'
        )

        self.expense = Expense.objects.create(
            travel=self.travel,
            name = 'Spesa Test',
            price= 20
        )

    def test_create_expense(self):
        self.client.login(username=self.username, password=self.password)
        valid_data = {
            'travel': self.travel,
            'name': 'Spesa Test 1',
            'price': 10
        }
        form = ExpenseForm(data=valid_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('addExpense', args=[self.travel.id]), valid_data)
        self.assertEqual(response.status_code, 302)
        expense = Expense.objects.get(id=2)
        self.assertEqual(expense.name, 'Spesa Test 1')
        self.assertEqual(expense.travel, self.travel)
        self.assertEqual(expense.price, 10)


    def test_remove_expense(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('removeExpense', args=[self.travel.id, self.expense.id]), {
            'stage_id': self.expense.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Expense.objects.filter(id=self.expense.id).exists())




