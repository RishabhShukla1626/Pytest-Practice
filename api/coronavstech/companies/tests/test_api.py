from unittest import TestCase
from django.test import Client
from django.urls import reverse
from django.conf import settings
from companies.models import Companies
import json
import pytest


@pytest.mark.django_db
class TestGetCompanies(TestCase):

    def test_zero_companies(self):
        client = Client()
        companies_url = reverse("companies-list")
        response = client.get(companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_when_there_is_one_company(self):
        client = Client()
        company_obj = Companies.objects.create(name='Amazon')
        companies_url = reverse("companies-list")
        response = client.get(companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get('name'), company_obj.name)
        self.assertEqual(response_content.get('status'), company_obj.status)

