class Customer:
    def _init_(self, customer_id, fname, lname, phone, email, city, state, zipcode, street):
        self.customer_id = customer_id
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street = street

    def _str_(self):
        return f"Customer[{self.customer_id}] {self.fname} {self.lname}, {self.phone}, {self.email}, {self.city}, {self.state}, {self.zipcode}, {self.street}"
