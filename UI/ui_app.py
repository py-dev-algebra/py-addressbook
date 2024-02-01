import time
from UI.components.console_components.main_menu import main_menu

def start_app():
    while True:
        main_menu()

        choice = int(input('Upisite broj iz izbornika: '))

        match choice:
            case 1:
                print('Izabrali smo izbor JEDAN')
                time.sleep(2)
            case 2:
                print('Izabrali smo izbor DVA')
                time.sleep(2)
            
            case 0:
                return
    
    '''
        1 prikazi main men
        2 omoguci izbor iz menija te ovisno o izboru pokreni funkciju
        3 omoguci izlaz iz aplikacije
        '''