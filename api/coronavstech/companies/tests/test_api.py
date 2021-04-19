from unittest import TestCase
from django.test import Client
from django.urls import reverse
from django.conf import settings
from companies.models import Companies
import json
import pytest


@pytest.mark.django_db
class BasicCompanyAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def tearDown(self):
        pass


class TestGetCompanies(BasicCompanyAPITestCase):
    def test_zero_companies(self):
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_when_there_is_one_company(self):
        company_obj = Companies.objects.create(name="Amazon")
        response = self.client.get(self.companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), company_obj.name)
        self.assertEqual(response_content.get("status"), company_obj.status)


class TestPostCompanies(BasicCompanyAPITestCase):
    def test_company_without_data(self):
        response = self.client.post(self.companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_create_company_that_already_exists(self):
        company_obj = Companies.objects.create(name="Google")
        response = self.client.post(self.companies_url, data={"name": "Google"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content),
            {"name": ["companies with this name already exists."]},
        )

    def test_create_company_with_name_only(self):
        response = self.client.post(self.companies_url, data={"name": "SnapChat"})
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("name"), "SnapChat")
        self.assertEqual(response_content.get("status"), "Hiring")

    def test_create_company_with_layoffs(self):
        response = self.client.post(
            self.companies_url, data={"name": "SnapChat", "status": "Layoffs"}
        )
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("status"), "Layoffs")

    def test_create_company_with_wrong_status(self):
        response = self.client.post(
            self.companies_url, data={"name": "SnapChat", "status": "WrongStatus"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("WrongStatus", str(response.content))
        self.assertIn("is not a valid choice.", str(response.content))
