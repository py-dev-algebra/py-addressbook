import time

from UI.components.console_components.main_menu import main_menu
from UI.components.console_components.create_company_form import create_company_form
from UI.components.console_components.select_contact_id_form import select_contact_id
from services.contact_services.contact_managers import ContactManager

def start_app():
    while True:
        main_menu()

        choice = int(input('Upisite broj iz izbornika: '))

        match choice:
            case 1:
                create_company_form()
            case 2:
                print('Izabrali smo izbor DVA')
                time.sleep(2)
            case 3:
                contact_manager = ContactManager()
                contacts = contact_manager.get_all()
                if contacts != []:
                    print(contacts)
                else:
                    print('Nema trazenih informacija u bazi ili se dogodila greska')

                input('\nZa nastavak pritisnite tipku ENTER\n')
            case 4:
                contact_id = select_contact_id()
                contact_manager = ContactManager()
                contacts = contact_manager.get_contact(contact_id)
                if contacts != []:
                    print(contacts)
                else:
                    print('Nema trazenih informacija u bazi ili se dogodila greska')

                input('\nZa nastavak pritisnite tipku ENTER\n')
            
            case 0:
                return
    
    '''
        1 prikazi main men
        2 omoguci izbor iz menija te ovisno o izboru pokreni funkciju
        3 omoguci izlaz iz aplikacije
        '''