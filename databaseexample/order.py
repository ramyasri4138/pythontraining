class Order:
    def _init_(self, order_id, customer_id, order_status, order_date, required_date, shipped_date, staff_id, store_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_status = order_status
        self.order_date = order_date
        self.required_date = required_date
        self.shipped_date = shipped_date
        self.staff_id = staff_id
        self.store_id = store_id

    def _str_(self):
        return f"Order[{self.order_id}] Customer[{self.customer_id}], Status: {self.order_status}, Order Date: {self.order_date}, Required Date: {self.required_date}, Shipped Date: {self.shipped_date}, Staff: {self.staff_id}, Store: {self.store_id}"
