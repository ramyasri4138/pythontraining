# products = [
#     {"name": "Laptop", "price": 92000},
#     {"name": "Smartphone", "price": 48000},
#     {"name": "Tablet", "price": 20000},
#     {"name": "Monitor", "price": 8000}
#     ]
#     Display the Product in ascending order based on the price of the product

numbers=[3,2,6,1,9,10]
numbers_asc=sorted(numbers)
print(numbers_asc)
numbers = [1, 2, 3, 4, 5]
numbers_lambda=(numbers,lambda x: x*2)
print(numbers_lambda)
products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
]
# Sort products in ascending order based on price
# Great question! The reason we didn't use map here is that the map function is designed to transform
# each element in a collection based on a provided function and return a new collection with the
# transformed elements. In your case, we aren't transforming the elements of the products list; 
# we are sorting them based on their price.
sorted_products = sorted(products, key=lambda x: x['price'])
# Display the sorted products
for product in sorted_products:
    print(f"Product: {product['name']}, Price: {product['price']}")
    

products = [
    {"name": "Laptop", "price": 92000},
    {"name": "Smartphone", "price": 48000},
    {"name": "Tablet", "price": 20000},
    {"name": "Monitor", "price": 8000}
    ]
products_asc=sorted(products,key=lambda x:x['price'])
print(products_asc)
