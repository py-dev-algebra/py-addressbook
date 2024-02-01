from services.file_services.file_manager import FileManager


def create_company_form():
    # print('Pozdrav iz forme za kreiranje Company')
    # input()

    title = input('Upisite naziv tvrtke: ')
    vat_id = input('Upisite OIB tvrtke: ')

    file_mgr = FileManager()
    file_mgr.insert_company(title, vat_id)


    '''
    header

    forma za unos podataka - input()-i

    poziv funkcije iz servisa za pohranu podataka
    '''