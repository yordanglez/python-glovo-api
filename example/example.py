from ..services import Order, Customer, CustomerList, OrderList
from libs.glovo.api import Api,configure

def createCustomer():

    api = Api(client_id="144723572812336",client_secret="a86b5c06fcfa42a1a04dbddf1afebe3e")
    data = {
        "type": "PartnerCustomer",
        "paymentWay": "MONTHLY",
        "preferredCityCode": "BCN",
        "password": "123456",
        "description": "This is my first Customer",
        "email": "yorda891216@gmail.com",
        "phoneNumber": {
            "number": "+34 611 000 000",
            "countryCode": "ES"
        },
        "name": "First Customer"
    }

    customer = Customer(data,api=api)
    customer.create()


def createOrder():
    # api = Api(client_id="144723572812336",client_secret="a86b5c06fcfa42a1a04dbddf1afebe3e")
    configure(client_id="144723572812336",client_secret="a86b5c06fcfa42a1a04dbddf1afebe3e")
    data = {
        "description": "My first Order",
        "phoneNumber": "+34 611 000 000",
        "cityCode": "BCN",
        "points": [
            {
                "index": 0,
                "address": {
                    "label": "Carrer Llacuna, 162 -164, 08018 Barcelona",
                    "details": "escalera A, planta 2, puerta 202"
                },
                "type": "PICKUP"
            }
        ],
        "scheduledTime": "2553081904000",
        "subtype": "SHIPMENT",
        "type": "Order"
    }

    order = Order(data)
    order.create(data,customer_urn="glv:customers:cf02a682-90b6-47a4-9bcb-56d8d2239e07")

def getListCustomers():
    configure(client_id="144723572812336", client_secret="a86b5c06fcfa42a1a04dbddf1afebe3e")
    customer_list= CustomerList()
    return customer_list.getList()


def getListOrders():
    configure(client_id="144723572812336", client_secret="a86b5c06fcfa42a1a04dbddf1afebe3e")
    order_list= OrderList()
    return order_list.getList(customer_urn="glv:customers:cf02a682-90b6-47a4-9bcb-56d8d2239e07")
