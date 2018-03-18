from django.test import TestCase
import unittest
import datetime
from django.utils import timezone
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Sending_Info

def create_sending_info(email_from, sending_status):
    created_date = timezone.now()
    return Sending_Info.objects.create(
        email_from=email_from, 
        sending_status=sending_status, 
        created_date=created_date
    )

class not_authorized_user(TestCase):
    def setUp(self):
        self.client = Client()

    def test_not_authorized_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_not_authorized_authorization_page(self):
        response = self.client.get(reverse('authorization'))
        self.assertEqual(response.status_code, 200)

    def test_not_authorized_registeration_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)


class authorized_user(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test_user_1',  
            password='Nsd3434', 
        )
        self.client.login(username='test_user_1', 
                        password='Nsd3434')

    def test_authorized_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_authorized_authorization_page(self):
        response = self.client.get(reverse('authorization'))
        self.assertEqual(response.status_code, 200)

    def test_authorized_registeration_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_create_sending_info(self):
        sending_info = create_sending_info("ds@mail.ru", True)
        check_inf = Sending_Info.objects.get(email_from="ds@mail.ru")
        self.assertEqual(str(check_inf), "ds@mail.ru True")
