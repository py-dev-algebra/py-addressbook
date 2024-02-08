import requests
from commons.app_constants import BASE_URL


class ContactManager:
    def __init__(self,
                 base_url: str = BASE_URL,
                 contacts_url: str = '/users') -> None:
        self.base_url: str = base_url
        self.contacts_url: str = contacts_url

    def get_all(self):
        try:
            response = requests.get(f'{self.base_url}{self.contacts_url}')
            if response.status_code == 200:
                return response.json()
            else:
                return []
        except Exception as ex:
            error_message = f'Dogodila se greska {ex}'
            return []
