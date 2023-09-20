import unittest
from django.test import Client, TestCase
from django.urls import reverse
from organizzatoreViaggi.forms import CreateUserForm
from organizzatoreViaggi.models import CustomUser

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.signup_url = reverse('signup')
        self.myTravels_url = reverse('myTravels')
        self.changeItinerary_url = reverse('changeItinerary', kwargs={'travel_id':1})
        self.detailsTravel_url = reverse('detailsTravel', kwargs={'travel_id': 1})
        self.userHomePage_url = reverse('userHomePage')
        self.invite_url = reverse('invite')
        #self.processIvitation_url = reverse('processInvitation', kwargs={'inv_id': 1})
        #self.addComment_url = reverse('addComment', kwargs={'inv_id': 1})

        #Utente di test
        self.username = 'testuser'
        self.password = 'Testpassword#1'
        self.user = CustomUser.objects.create_user(
            username=self.username,
            password=self.password
        )

        self.valid_data = {
            'username': 'signuser',
            'password1': 'password#1',
            'password2': 'password#1',
            'email': 'testuser@test.com',
            'first_name': 'Test',
            'last_name': 'Test',
        }


    def test_login_view_GET(self):
        #simulazione richiesta di tipo get all'url specificato
        response = self.client.get(self.login_url)
        #verifica che lo status code sia 200, ovvero quello di successo
        self.assertEqual(response.status_code, 200)
        #verifica che il template risultato dalla richiesta sia effettivamente quello di login
        self.assertTemplateUsed(response, 'organizzatoreViaggi/login.html')
        # self.assertIsInstance(response.context['form_login'], forms.C)
        #verificare che sia un instanza del form login (?)

    def test_login_view_POST_success(self):
        # simulazione richiesta di tipo post all'url specificato
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        #verifica che la richiesta di tipo post riconduca alla home
        self.assertRedirects(response, self.userHomePage_url)
        # verifica che lo status code sia 200, ovvero quello di reindirizamento
        self.assertEqual(response.status_code, 302)

    def test_login_view_POST_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,  'organizzatoreViaggi/login.html')
        self.assertEqual(response.context['login_error'], 'Username o password errati!')

    def test_logout_view(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.login_url)
        self.assertFalse('_auth_user_id' in self.client.session)
        self.assertEqual(response.status_code, 302)

    def test_signup_view_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizzatoreViaggi/signup.html')
        self.assertIsInstance(response.context['form'], CreateUserForm)


    def test_signup_view_POST_valid_form(self):
        response = self.client.post(self.signup_url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomUser.objects.filter(username=self.valid_data['username']).exists())

    def test_signup_view_POST_invalid_form(self):
        invalid_data = {
            'username': 'wronguser',
            'password1': 'Testpassword#1',
            'password2': 'DifferentPassword#1',
            'email': 'testuser@test.com',
            'first_name': 'Test',
            'last_name': 'Test',
        }
        response = self.client.post(self.signup_url, invalid_data)

        # Verifica che la risposta non sia un reindirizzamento, ma un render della stessa pagina di registrazione
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizzatoreViaggi/signup.html')
        self.assertFalse(response.context['form'].is_valid())
        self.assertFalse(CustomUser.objects.filter(username=invalid_data['username']).exists())
