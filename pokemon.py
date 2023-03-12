from PIL import Image
import random

class Pokemon:
    def __init__(self, nom, pv=100, niveau=1, attaque=10, defense=0):
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense

    def attaquer(self, autre_pokemon):
        if random.random() <= 0.9:
            print(f"{self.nom} a raté son attaque !")

            multiplicateur_attaque = 1.0
            multiplicateur_defense = 1.0
            if self.type.faiblesse and autre_pokemon.type.nom in self.type.faiblesse:
                multiplicateur_attaque *= 1.5
            elif self.type.resistance and autre_pokemon.type.nom in self.type.resistance:
                multiplicateur_attaque *= 0.5

            if autre_pokemon.type.faiblesse and self.type.nom in autre_pokemon.type.faiblesse:
                multiplicateur_defense *= 1.5
            elif autre_pokemon.type.resistance and self.type.nom in autre_pokemon.type.resistance:
                multiplicateur_defense *= 0.5

            degats = int(self.attaque * multiplicateur_attaque) - int(autre_pokemon.defense * multiplicateur_defense)
            autre_pokemon.pv -= degats
            print(f'{self.nom} attaque {autre_pokemon.nom} et lui inflige {degats} dégats.')
            if autre_pokemon.pv <= 0:
                print(f'{autre_pokemon.nom} est K.O.!')
                return True
            return False

    def augmenter_niveau(self):
        self.niveau += 1
        self.attaque += 10
        self.defense += 5
        self.pv += 10


class Type:
    def __init__(self, nom, faiblesse=None, resistance=None):
        self.nom = nom
        self.faiblesse = faiblesse
        self.resistance = resistance


class Feu(Type):
    def __init__(self):
        super().__init__("Feu", faiblesse=["Eau"], resistance=["Plante"])


class Eau(Type):
    def __init__(self):
        super().__init__("Eau", faiblesse=["Plante"], resistance=["Feu"])


class Plante(Type):
    def __init__(self):
        super().__init__("Plante", faiblesse=["Feu"], resistance=["Eau"])



class Normal(Type):
    def __init__(self):
        super().__init__("Normal", faiblesse=["Combat"], resistance=["Spectre"])


class Electric(Type):
    def __init__(self):
        super().__init__("Electric", faiblesse=["Sol"], resistance=["Vol"])


class Glace(Type):
    def __init__(self):
        super().__init__("Glace", faiblesse=["Feu"], resistance=["Eau"])


class Combat(Type):
    def __init__(self):
        super().__init__("Combat", faiblesse=["Vol"], resistance=["Insecte"])


class Poison(Type):
    def __init__(self):
        super().__init__("Poison", faiblesse=["Psy"], resistance=["Combat"])


class Sol(Type):
    def __init__(self):
        super().__init__("Sol", faiblesse=["Eau"], resistance=["Poison"])

class Vol(Type):
    def __init__(self):
        super().__init__("Vol", faiblesse=["Electric"], resistance=["Combat"])


class Psy(Type):
    def __init__(self):
        super().__init__("Eau", faiblesse=["Insecte"], resistance=["Combat"])


class Insecte(Type):
    def __init__(self):
        super().__init__("Insecte", faiblesse=["Feu"], resistance=["Plante"])

class Roche(Type):
    def __init__(self):
        super().__init__("Roche", faiblesse=["Eau", "Combat"], resistance=["Feu"])


class Spectre(Type):
    def __init__(self):
        super().__init__("Spectre", faiblesse=["Tenebre"], resistance=["Poison"])


class Dragon(Type):
    def __init__(self):
        super().__init__("Plante", faiblesse=["Glace"], resistance=["Feu"])

class Tenebre(Type):
    def __init__(self):
        super().__init__("Tenebre", faiblesse=["Combat"], resistance=["Spectre"])


class Acier(Type):
    def __init__(self):
        super().__init__("Acier", faiblesse=["Feu"], resistance=["Glace"])


class Fee(Type):
    def __init__(self):
        super().__init__("Fée", faiblesse=["Acier"], resistance=["Combat"])


class PokemonFeu(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, attaque=20)
        self.type = Feu()


class PokemonEau(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, pv=120)
        self.type = Eau()


class PokemonPlante(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, defense=10)
        self.type = Plante()

class PokemonNormal(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, attaque=20)
        self.type = Normal()


class PokemonElectric(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, pv=120)
        self.type = Electric()


class PokemonGlace(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, defense=10)
        self.type = Glace()

class PokemonCombat(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, attaque=20)
        self.type = Combat()


class PokemonPoison(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, pv=120)
        self.type = Poison()


class PokemonSol(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, defense=10)
        self.type = Sol()

class PokemonVol(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, attaque=20)
        self.type = Vol()


class PokemonPsy(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, pv=120)
        self.type = Psy()


class PokemonInsecte(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, defense=10)
        self.type = Insecte()

class PokemonRoche(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, attaque=20)
        self.type = Roche()


class PokemonSpectre(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, pv=120)
        self.type = Spectre()


class PokemonDragon(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, defense=10)
        self.type = Dragon()

class PokemonTenebre(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, attaque=20)
        self.type = Tenebre()


class PokemonAcier(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, pv=120)
        self.type = Acier()


class PokemonFee(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, defense=10)
        self.type = Fee()


class Dresseur:
    def __init__(self, nom):
        self.nom = nom
        self.pokemons = []

    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self.nom} a ajouté {pokemon.nom} à son équipe.')

    def combattre(self, dresseur):
        print(f'{self.nom} commence un combat contre {dresseur.nom}.')
        pokemon_actif = self.pokemons[0]
        pokemon_adverse = dresseur.pokemons[0]
        while True:
            if pokemon_actif.attaquer(pokemon_adverse):
                print(f"{pokemon_actif.nom} a vaincu {pokemon_adverse.nom} !")
                if len(dresseur.pokemons) == 1:
                    print(f"{dresseur.nom} n'a plus de Pokémon en état de combattre.")
                    print(f'{self.nom} a gagné le combat!')
                    pokemon_actif.augmenter_niveau()
                    break
                else:
                    if pokemon_adverse in dresseur.pokemons:
                        dresseur.pokemons.remove(pokemon_adverse)
                    pokemon_adverse = dresseur.pokemons[0]
            pokemon_actif, pokemon_adverse = pokemon_adverse, pokemon_actif
            print(f'{self.nom} envoie {pokemon_actif.nom} au combat.')
            print(f'{dresseur.nom} envoie {pokemon_adverse.nom} au combat.')

    def afficher_equipe(self):
        print(f'Équipe de {self.nom}:')
        for pokemon in self.pokemons:
            print(pokemon.nom)

img = Image.open("image/pokemon_platine.png")

width, height = img.size
aspect_ratio = height/width
new_width = 150
new_height = int(aspect_ratio * new_width * 0.5)
img = img.resize((new_width, new_height))

chars = ["/"," ", "#"]
char_len = len(chars)

ascii_img = ""
pixels = img.load()
for i in range(new_height):
    for j in range(new_width):
        pixel = pixels[j, i]
        if isinstance(pixel, int):
            r = g = b = pixel
        else:
            r, g, b = pixel
        gray = int(0.2126*r + 0.7152*g + 0.0722*b)
        index = int(gray/255 * (char_len-1))
        if chars[index] == "/":
            ascii_img += "\033[31m/\033[0m" # changer la couleur du caractère en rouge
        else:
            ascii_img += chars[index]
    ascii_img += "\n"

print(ascii_img)

Dresseur1 = Dresseur("Louka")
Dresseur2 = Dresseur("Aurore")

pokemon1 = PokemonFeu("salamèche")
pokemon2 = PokemonEau("carapuce")
pokemon3 = PokemonPlante("bulbizarre")
pokemon4 = PokemonFeu("ouisticram")
pokemon5 = PokemonEau("tiplouf")
pokemon6 = PokemonPlante("tortipouss")

Dresseur1.ajouter_pokemon(pokemon1)
Dresseur1.ajouter_pokemon(pokemon2)
Dresseur1.ajouter_pokemon(pokemon3)
Dresseur2.ajouter_pokemon(pokemon4)
Dresseur2.ajouter_pokemon(pokemon5)
Dresseur2.ajouter_pokemon(pokemon6)

Dresseur1.afficher_equipe()
Dresseur2.afficher_equipe()

Dresseur1.combattre(Dresseur2)
