from api_requests.api_clients_requests import create_user
import random

class TestAuth:
    def test_auth_with_correct_values_status_code(self):
        random_number_1 = random.randint(1, 999999)  # Generates a random number between 1 and 999999
        body = {
            "clientName": "Postman_test",
            "clientEmail": f"test123_2131{random_number_1}@example.com"
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 201

    def test_auth_with_correct_values_response_token(self):
        random_number_1 = random.randint(1, 999999)   # Generates a random number between 1 and 999999
        body = {
            "clientName": "Postman_test",
            "clientEmail": f"test123_2131{random_number_1}@example.com"
        }
        response = create_user(body['clientName'], body['clientEmail'])
        responseBody = response.json()
        assert 'accessToken' in responseBody.keys()