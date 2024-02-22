import requests
# Ovaj impost je zbog eliminiacije problema s circularnim importom
from __future__ import annotations 

from commons.app_constants import (BASE_URL,
                                   LOG_INFO,
                                   LOG_ERROR,
                                   REPO_DB)
from commons.message_generator import generate_log_message
from services.file_services.logging_manager import LoggingManager
from models.contacts.contacts import Contact


class ContactManager:
    def __init__(self,
                 base_url: str = BASE_URL,
                 contacts_url: str = '/users',
                 repository: str = REPO_DB) -> None:
        self.base_url: str = base_url
        self.contacts_url: str = contacts_url
        self.repository: str = repository
        self.logger: LoggingManager = LoggingManager()

    @staticmethod
    def get_all(self):
        try:
            response = requests.get(f'{self.base_url}{self.contacts_url}')
            if response.status_code == 200:
                return response.json()
            else:
                return []
        except Exception as ex:
            message = generate_log_message(ex, LOG_ERROR)
            self.logger.save_message(message)
            return []

    @staticmethod
    def get_contact(self, contact_id: int):
        try:
            response = requests.get(f'{self.base_url}{self.contacts_url}/{contact_id}')
            if response.status_code == 200:
                return response.json()
            else:
                return []
        except Exception as ex:
            message = generate_log_message(ex, LOG_ERROR)
            self.logger.save_message(message)
            return []

    @staticmethod
    def create_contact(self, contact: Contact):
        
        # Kreiraj konekciju prema bazi i pohrani 
        
        message = generate_log_message(message, LOG_INFO)
        self.logger.save_message(message)
        pass
