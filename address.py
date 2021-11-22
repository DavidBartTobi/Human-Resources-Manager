
class Address:

    def __init__(self, c, street_address, city, country, zipcode):
        self.c = c
        self.street = street_address
        self.city = city
        self.country = country
        self.zipcode = zipcode

        self.add_address()

    def add_address(self):

        insert = "INSERT INTO Addresses (street_address, city, country, zipcode) VALUES (?,?,?,?);"
        data_tuple = (self.street, self.city, self.country, self.zipcode)
        self.c.execute(insert, data_tuple)

    def get_last_row_id(self):

        id = self.c.execute('SELECT max(address_id) FROM Addresses')
        return id.fetchone()[0]
