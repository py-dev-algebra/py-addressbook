import json
from models.companies.companies import Company


class FileManager:
    def __init__(self, file_type: str = 'json',
                 file_path: str = 'files/companies.json') -> None:
        self.file_type = file_type
        self.file_path = file_path

    def insert_company(self, title, vat_id):
        # print(f'Tvrtka {title} je uspjesno kreirana')
        # input('\nPritisnike tipku ENTER za nastavak')

        company = Company(title, vat_id)

        try:
            with open(self.file_path, 'a') as file_writer:
                json.dump(company, file_writer)
                print(f'Uspjesno je kreirana firma {company}')
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
        
