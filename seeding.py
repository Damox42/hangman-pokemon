import connection

db = connection.client['hangman_pokemon']
collection_names = db['names']

names = open('pokemon.txt', 'r').read().splitlines()

try: 
    for name in names:
        collection_names.insert_one({'name': name})
except Exception as e:
    print(f"Seeding fallito: {e}")