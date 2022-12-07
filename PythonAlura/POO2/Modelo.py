class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def dar_like(self):
        self._likes += 1
        
    

class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} Min - Likes: {self._likes}'
        
class Serie (Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'
    
class Playlist (list):
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
        

        

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
starwars = Filme('Star Wars IV', 1978, 148)
demolidor = Serie('Demolidor', 2016, 3)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
starwars.dar_like()
starwars.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filme_e_series = [vingadores, atlanta, demolidor, starwars]
playlist_fim_de_semana = Playlist ('Final de semana', filme_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)
    
