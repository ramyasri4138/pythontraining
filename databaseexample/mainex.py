from customers import Customer
from order import Order
from orderItem import OrderItem

def get_customer_input():
    customer_id = input("Enter customer ID: ")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zipcode = input("Enter zipcode: ")
    street = input("Enter street: ")
    return Customer(customer_id, fname, lname, phone, email, city, state, zipcode, street)

def get_order_input():
    order_id = input("Enter order ID: ")
    customer_id = input("Enter customer ID: ")
    order_status = input("Enter order status: ")
    order_date = input("Enter order date: ")
    required_date = input("Enter required date: ")
    shipped_date = input("Enter shipped date: ")
    staff_id = input("Enter staff ID: ")
    store_id = input("Enter store ID: ")
    return Order(order_id, customer_id, order_status, order_date, required_date, shipped_date, staff_id, store_id)

def get_order_item_input():
    order_id = input("Enter order ID: ")
    item_id = input("Enter item ID: ")
    product_id = input("Enter product ID: ")
    quantity = input("Enter quantity: ")
    list_price = input("Enter list price: ")
    discount = input("Enter discount: ")
    return OrderItem(order_id, item_id, product_id, quantity, list_price, discount)

def main():
    customer = get_customer_input()
    print(customer)

    order = get_order_input()
    print(order)

    order_item = get_order_item_input()
    print(order_item)

if __name__ == "_main_":
    main()
