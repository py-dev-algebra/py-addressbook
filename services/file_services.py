

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
