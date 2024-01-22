import requests

from api_requests import api_clients_requests

URL = "https://simple-books-api.glitch.me"
token = api_clients_requests.get_token()

headers = {
    'Authorization': token
}


def submit_order(book_id, costumer_name):
    body = {
        "bookId": book_id,
        "customerName": costumer_name
    }
    response = requests.post(f"{URL}/orders", json=body, headers=headers)
    return response

# creates a new method with incorrect entered keys

def submit_order_custom_keys():
    body = {
        "bookId": 1,
        "costumerName": 'Test'
    }
    response = requests.post(f"{URL}/orders", json=body, headers=headers)
    return response


def get_all_orders():
    response = requests.get(f"{URL}/orders", headers=headers)
    return response


def get_order(order_id):
    response = requests.get(f"{URL}/orders/{order_id}", headers=headers)
    return response


def update_order(order_id, new_customer_name):
    body = {
        "customerName": new_customer_name
    }
    response = requests.patch(f"{URL}/orders/{order_id}", json=body, headers=headers)
    return response

def delete_order(order_id):
    response = requests.delete(f"{URL}/orders/{order_id}", headers=headers)
    return response

# print(submit_order(1, "John").json())
# submit_order(1, "John")
# submit_order(3, "Ana")
# submit_order(2, "Philip")
#
# for order in (get_all_orders()):
#     print(order)


# To get an order ID -> create the order and from the answer body retrieve the 'orderId' key value

# order_id = submit_order(3, 'Ana').json()['orderId']
# print(order_id)
#
# Send the ID obtained above as a parameter to get_order() function
# print(get_order(order_id).json())

# UPDATE ORDER
# #Create an order
# order = submit_order(5,"Vlad").json()
# #Create get_order request to the order made above
# print(get_order(order['orderId']).json())
# #Create update request to the order created above, change costumer name from "Vlad" to "John"
# response = update_order(order['orderId'],"John")
# #Display the status code (204)
# print(response.status_code)
# #Returns an error because the request to update_order doesn't return a body
# print(response.json())
# # Create get_order request to check if the order changed
# print(get_order(order['orderId']).json())

#DELETE ORDER
order_id = submit_order(4,"John").json()['orderId']
print(get_order(order_id).json())
print(delete_order(order_id).status_code)
# Returns error because the command with 'order_id' ID doesn't exist anymore
print(get_order(order_id).json())