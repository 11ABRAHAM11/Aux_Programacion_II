# ============================      
# CLASE ANIME
# ============================

class Anime:
    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre
        self.genero = genero
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []

    # Método para agregar episodio
    def agregar_episodio(self, episodio):
        self.__episodios.append(episodio)

    # Getter
    def get_nroEpisodios(self):
        return self.__nroEpisodios

    def __str__(self):
        return f"Anime: {self.nombre} | Género: {self.genero} | Episodios: {self.__nroEpisodios}"


if __name__ == "__main__":
    # Crear 2 objetos Anime
    anime1 = Anime("Naruto", "Shonen", 220)
    anime2 = Anime("Attack on Titan", "Acción", 75)

    print(anime1)
    print(anime2)