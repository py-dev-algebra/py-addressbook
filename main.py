from services.file_services import get_last_id


if get_last_id() != -1:
    id = get_last_id() + 1
else:
    id = 1

print(id)

