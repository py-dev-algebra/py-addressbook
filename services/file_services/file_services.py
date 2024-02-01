from models.contacts.contacts import Contact



def get_last_id() -> int:
    '''
    Returns id of last Addressbook entry
    If Addressbook is empty returs -1
    '''
    try:
        with open('files/addressbook.txt', 'r') as file_reader:
            # file_data = file_reader.readlines()
            # return file_data[-1].split(';')[0]
            return int(file_reader.readlines()[-1].split(';')[0])

    except Exception as ex:
        print(f'Dogodila se greska {ex}')
        return -1


def get_last_name(id: int = 0) -> str:
    pass


def get_contact(id: int = 0) -> Contact:
    try:
        with open('files/addressbook.txt', 'r') as file_reader:
            lines = file_reader.readlines()
            if id > 0 and id < len(lines):
                contact_data = lines[id - 1].split(';')
                return Contact(int(contact_data[0]), 
                            contact_data[1], 
                            contact_data[2],
                            contact_data[3])
            else:
                return None
            
    except Exception as ex:
        print(f'Dogodila se greska {ex}')
        return None
