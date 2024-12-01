import requests
import pytest

BASE_URL = "https://dog.ceo/api"

def testeCachorroAleatorio():
    """Testa se a API retorna uma imagem de cachorro com sucesso."""
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200, f"Status code inesperado: {response.status_code}"
    assert "message" in response.json()
    assert "status" in response.json()
    assert response.json()["status"] == "success"

def testeCachorroespecifico():
    """Testa se é possível obter imagens de uma raça específica."""
    breed = "hound"
    response = requests.get(f"{BASE_URL}/breed/{breed}/images")
    assert response.status_code == 200, f"Status code inesperado: {response.status_code}"
    assert "message" in response.json()
    assert isinstance(response.json()["message"], list)

def testeEndpoint():
    """Testa um endpoint inválido para verificar erro 404."""
    response = requests.get(f"{BASE_URL}/invalid/endpoint")
    assert response.status_code == 404

def testeRacaInexistente():
    """Testa se a API lida corretamente com uma raça inexistente."""
    breed = "not-a-real-breed"
    response = requests.get(f"{BASE_URL}/breed/{breed}/images")
    assert response.status_code == 404

def testeVelocidade():
    """Testa se a resposta é rápida o suficiente (menos de 1 segundo)."""
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.elapsed.total_seconds() < 1