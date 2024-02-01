from services.file_services.file_services import (get_last_id,
                                    get_contact)


if get_last_id() != -1:
    id = get_last_id() + 1
else:
    id = 1

print(id)

id_contact = 15
contact = get_contact(id_contact)
if contact != None:
    print(contact)
    print(contact.id)
else:
    print(f'Ne postoji trazeni kontakt s ID: {id_contact} u bazi!')
