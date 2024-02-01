


class Contact:
    def __init__(self,
                 id: int,
                 first_name: str,
                 last_name: str,
                 phone: str) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone


    # TODO Prilagoditi ispis kontakta!!!
    def __str__(self) -> str:
        contact_card = f'\nIme: {self.first_name}\n'
        contact_card += f'Prezime: {self.last_name}\n'
        contact_card += f'Telefon: {self.phone}\n'
        return contact_card
