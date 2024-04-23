class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        if hijos is not None:
            self.hijos = hijos
            for h in hijos:
                h.set_padre(self)
        else:
            self.hijos = []

    def get_hijos(self):
        return self.hijos

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def set_costo(self, costo):
        self.costo = costo

    def set_padre(self, padre):
        self.padre = padre

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def __str__(self):
        return str(self.get_datos())
