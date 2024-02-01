


class Address:
    def __init__(self,
                 street_and_number: str,
                 postal_code: str,
                 city: str,
                 country: str = 'Hrvatska (Croatia)') -> None:
        self.street_and_number: str = street_and_number
        self.postal_code: str = postal_code
        self.city: str = city
        self.country: str = country

    def __str__(self):
        return (f'{self.street_and_number},\n'
                f'{self.postal_code} {self.city},\n'
                f'{self.country}')
