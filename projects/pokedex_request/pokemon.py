import requests

def pegar_habilidades(poke):
    print(f"habilidades do {pokemon}")
    for i in poke['abilities']:
        print(i['ability']['name'])

def main():
    global pokemon
    pokemon = str(input('Pokemon : '))
    api = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    res=requests.get(api)

    poke=res.json()
    pegar_habilidades(poke)

if __name__ == '__main__':
    main()