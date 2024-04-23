from flask import Flask, render_template, request
from Arbol import Nodo

app = Flask(__name__)

def buscar_solucion_DFS_Limitado(nodo_inicial, solucion, limite, visitados=None):
    if visitados is None:
        visitados = []

    frontera = [nodo_inicial]
    alcanzado_limite = False

    while frontera:
        nodo_actual = frontera.pop()

        if nodo_actual.get_datos() == solucion:
            return nodo_actual, alcanzado_limite

        if len(visitados) < limite:
            visitados.append(nodo_actual.get_datos())

            # Expandir los nodos sucesores (hijos)
            dato_nodo = nodo_actual.get_datos()
            hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
            hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
            hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
            nodo_actual.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

            for hijo in nodo_actual.get_hijos():
                if hijo.get_datos() not in visitados:
                    frontera.append(hijo)
        else:
            alcanzado_limite = True

    return None, alcanzado_limite

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario
        estado_inicial = [int(x) for x in request.form['estado_inicial'].split(',')]
        solucion = [int(x) for x in request.form['solucion'].split(',')]
        limite = int(request.form['limite'])

        # Realizar la búsqueda DFS limitada
        nodo_inicial = Nodo(estado_inicial)
        nodo_solucion, alcanzado_limite = buscar_solucion_DFS_Limitado(nodo_inicial, solucion, limite)

        # Reconstruir el camino hacia la solución
        resultado = []
        if nodo_solucion:
            nodo = nodo_solucion
            while nodo is not None:
                resultado.insert(0, nodo.get_datos())
                nodo = nodo.get_padre()
        else:
            resultado.append("No se encontró la solución.")
            if alcanzado_limite:
                resultado.append("Se necesita más límite de profundidad.")

        return render_template('resultado.html', resultado=resultado)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
