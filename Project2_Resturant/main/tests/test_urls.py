import pytest
from django.urls import reverse
from django.test import Client


@pytest.fixture
def client():
    return Client()


def test_home_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    
    
def test_about_view(client):
    response = client.get(reverse('about/'))
    assert response.status_code == 200
    

def test_invalid_view(client):
    response = client.get('/invalid-url/')
    assert response.status_code == 404
    
    
    # TO TEST
    
    
    #contact/'
    #blog/'
    #chefs/'
    #'order/'