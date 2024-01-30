from api_requests.orders_requests import *
from api_requests.api_clients_requests import *


class TestOrders:

    def test_valid_order_request_status_code(self):
        response = submit_order(1, "Iulian")
        # print(response.json())
        assert response.status_code == 201
        # clean-up
        delete_order(response.json()['orderId'])

    def test_valid_order_request_body(self):
        # Testing the True value of the key 'created'
        response = submit_order(1, "Mihai")
        body = response.json()
        assert body['created'] is True
        # clean-up
        delete_order(body['orderId'])

    def test_delete_order(self):
        order_id = submit_order(3, "Matei").json()['orderId']
        response = delete_order(order_id)
        assert response.status_code == 204

    def test_get_all_orders_with_zero_orders(self):
        response = get_all_orders()
        assert len(response.json()) == 0

    def test_get_multiple_orders(self):
        order_id_1 = submit_order(1, "Mihai").json()['orderId']
        order_id_2 = submit_order(1, "John").json()['orderId']
        order_id_3 = submit_order(1, "Matei").json()['orderId']
        response = get_all_orders()
        assert len(response.json()) == 3
        # clean-up
        delete_order(order_id_1)
        delete_order(order_id_2)
        delete_order(order_id_3)

    def test_get_order(self):
        order_id = submit_order(1, "Victor").json()['orderId']
        response = get_order(order_id)
        body = response.json()
        assert body['id'] == order_id
        assert body['bookId'] == 1
        assert body['customerName'] == "Victor"
        # clean-up
        delete_order(order_id)

    def test_update_order(self):
        order_id = submit_order(1, "Mihai").json()['orderId']
        response = update_order(order_id, "John")
        assert response.status_code == 204
        # Call the get_order function to verify the new 'customerName' key
        response_get_order = get_order(order_id)
        assert response_get_order.json()['customerName'] == "John"
        # clean-up
        delete_order(order_id)

    def test_submit_order_bad_request(self):
        response = submit_order_custom_keys()
        # clean-up
        delete_order(response.json()['orderId'])
        assert response.status_code == 400
        # Test fails because the code should not work introducing the wrong keys

    def test_submit_order_bad_request_customer_name_field_presence(self):
        response = submit_order_custom_keys()
        # clean-up
        delete_order(response.json()['orderId'])
        assert 'customerName' in response.json().keys()
        # The test fails because introducing the wrong key, customerName field disappears

    def test_submit_book_order_out_of_stock(self):
        response = submit_order(2, "Mihai")
        assert response.status_code == 404
        error = response.json()['error']
        assert error == "This book is not in stock. Try again later."

    # test submit_a_book_order_with_invalid_id

    def test_submit_a_book_order_with_invalid_id(self):
        response = submit_order(9, "Mihai")
        assert response.status_code == 400
        error = response.json()['error']
        assert error == "Invalid or missing bookId."

    def test_invalid_email_format(self):
        body = {
            "clientName": "Postman_test",
            "clientEmail": "@example.com"
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 400
        assert response.json()['error'] == "Invalid or missing client email."

    def test_auth_without_client_name(self):
        body = {
            "clientName": "",
            "clientEmail": f"@example.com"
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 400
        assert response.json()['error'] == "Invalid or missing client name."

    def test_auth_without_client_email(self):
        body = {
            "clientName": "Postman",
            "clientEmail": ""
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 400
        assert response.json()['error'] == "Invalid or missing client email."

    def test_auth_with_client_name_only_special_characters(self):
        body = {
            'clientName': "#@",
            'clientEmail': "test@postman.com"
        }
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.status_code == 400
        # Test fails because the authentication should not be able to be made in reality having only
        # special characters in clientName field

    def test_auth_with_existing_email(self):
        random_number_1 = random.randint(1, 999999)  # Generates a random number between 1 and 999999
        body = {
            "clientName": "Postman_test",
            "clientEmail": f"test123_2131{random_number_1}@example.com"
        }
        create_user(body['clientName'], body['clientEmail'])
        response = create_user(body['clientName'], body['clientEmail'])
        assert response.json()['error'] == "API client already registered. Try a different email."
