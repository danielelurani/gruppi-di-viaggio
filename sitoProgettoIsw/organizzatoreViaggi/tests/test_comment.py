import unittest
from django.test import Client, TestCase
from organizzatoreViaggi.forms import CreateUserForm, TravelForm, InvitationForm, CommentForm
from organizzatoreViaggi.models import CustomUser, Travel, Invitation, Stage, Comment
from django.urls import reverse

class TestComment(TestCase):


    def setUp(self):
        self.client = Client()
        self.myTravels_url = reverse('myTravels')

        self.username = 'testuser'
        self.password = 'testpassword'

        self.user = CustomUser.objects.create_user(
            username= self.username,
            password=  self.password
        )

        self.travel = Travel.objects.create(
            name='Viaggio Test',
            destination='Destinazione Test ',
            start_date='2024-06-01',
            end_date='2024-06-03'
        )

    def test_create_comment(self):
        self.client.login(username = self.username, password = self.password)
        valid_data = {
            'content': 'Commento Test',
            'user': self.user,
            'travel': self.travel
        }
        form = CommentForm(data=valid_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('addComment', args=[self.travel.id]), valid_data)
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.content, 'Commento Test')
        self.assertEqual(comment.travel, self.travel)
        self.assertEqual(comment.user, self.user)









