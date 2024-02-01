import json


# try:
#     with open('files/user_01.json', 'r') as file_reader:
#         text_json = file_reader.read()
# except Exception as ex:
#     print(f'Dogodila se greska {ex}')

# # print(text_json)

# text_dict = json.loads(text_json)
# # print(text_dict)

# for key, value in text_dict.items():
#     print(f'{key}\t{value}')


try:
    with open('files/user_01.json', 'r') as file_reader:
        text_dict = json.load(file_reader)
except Exception as ex:
    print(f'Dogodila se greska {ex}')


for key, value in text_dict.items():
    print(f'{key}\t{value}')
