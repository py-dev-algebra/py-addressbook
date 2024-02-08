import time

from UI.components.console_components.main_menu import main_menu
from UI.components.console_components.create_company_form import create_company_form
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
                print(contacts)
            
            case 0:
                return
    
    '''
        1 prikazi main men
        2 omoguci izbor iz menija te ovisno o izboru pokreni funkciju
        3 omoguci izlaz iz aplikacije
        '''