from django.urls import reverse
from companies.models import Companies
import json
import pytest

companies_url = reverse("companies-list")


@pytest.mark.django_db
def test_when_there_is_one_company(client):
    company_obj = Companies.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == company_obj.name
    assert response_content.get("status") == company_obj.status


@pytest.mark.django_db
def test_create_company_that_already_exists(client):
    company_obj = Companies.objects.create(name="Google")
    response = client.post(companies_url, data={"name": "Google"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["companies with this name already exists."]
    }


@pytest.mark.django_db
def test_create_company_with_name_only(client):
    response = client.post(companies_url, data={"name": "SnapChat"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "SnapChat"
    assert response_content.get("status") == "Hiring"


@pytest.mark.django_db
def test_create_company_with_layoffs(client):
    response = client.post(
        companies_url, data={"name": "SnapChat", "status": "Layoffs"}
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"


@pytest.mark.django_db
def test_create_company_with_wrong_status(client):
    response = client.post(
        companies_url, data={"name": "SnapChat", "status": "WrongStatus"}
    )
    assert response.status_code == 400
    assert "WrongStatus" in str(response.content)
    assert "is not a valid choice." in str(response.content)
