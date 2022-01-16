
import json


kitten={
    'name': 'Tyson',
    'age' : 7
}

def read():
    with open('./kittens.txt', 'r') as file:
        text= file.read()
        load_kitten=json.loads(text)
        print(load_kitten['name'])

def write():
    with open('./kittens.txt', 'w') as file:
        kitten_json= json.dumps(kitten)
        file.write(kitten_json)

write()
read()