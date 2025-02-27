class OrderItem:
    def _init_(self, order_id, item_id, product_id, quantity, list_price, discount):
        self.order_id = order_id
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount = discount

    def _str_(self):
        return f"OrderItem[{self.order_id}-{self.item_id}] Product[{self.product_id}], Quantity: {self.quantity}, List Price: {self.list_price}, Discount: {self.discount}"
