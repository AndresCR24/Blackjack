class Carta:

    def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = True

class Mano:

    def __init__(self, cartas: list[Carta]):
        self.cartas: list[Carta] = cartas
        self.cartas.append(cartas)

    def es_blackjack(self) -> bool:
        pass

    def validar_cartas_jugador(self):
        pass

    def validar_cartas_casa(self):
        pass

class Baraja:

    def __init__(self) -> None:
        pass

    def revolver(self):
        pass

    def repartir_carta(self, tapada: bool) -> Carta:
        self

class Blackjack:
    
    def __init__(self) -> None:
        pass
    
    def iniciar_juego(self):
        pass
    
    def registrar_jugador(self):
        pass

    def resultado_partida(self):
        pass

    def cobrar_apuesta(self):
        pass

    def finalizar_juego(self):
        pass
    
    def verificar_fichas(self):
        pass
    
class Jugador:
    
    def __init__(self) -> None:
        pass

    def crear_jugador(self):
        pass

    def inicializar_mano(self, cartas):
        pass

    def hacer_jugada_jugador(self):
        pass
    
class casa:
    
    def __init__(self) -> None:
        pass

    def inicializar_mano(self, cartas):
        pass

    def hacer_jugada_casa(self):