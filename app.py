from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/ejercicio1/', methods=['GET', 'POST'])
def ejercicio1():
    result = None

    if request.method == 'POST':
        number = request.form.get('number')
        number = int(number) if number else 0
        signo = "positivo" if number > 0 else "negativo" if number < 0 else "cero"
        tipo = "par" if number % 2 == 0 else "impar"
        result = {"signo": signo, "tipo": tipo}

    return render_template('index.html', result=result)

@app.route('/ejercicio2/', methods=['GET', 'POST'])
def ejercicio2():
    base = ""
    exponente = ""
    result = None
    if request.method == 'POST':
        base = request.form.get('base')
        exponente = request.form.get('exponente')
        base = int(base) if base else 0
        exponente = int(exponente) if exponente else 2
        result = base ** exponente

    return render_template('potencia.html', exponente=exponente, base=base, result=result)

@app.route('/ejercicio3/', methods=['GET', 'POST'])
def estadisticas():
    lista = ""
    result = None
    sumatorio = 0
    mayor = None
    menor = None
    promedio  = 0

    if request.method == 'POST':
        lista = request.form.get('lista')  #"25,25,62,54,85,85,25,21"
        if lista:
            numeros = [int(x) for x in lista.split(',')] 
            #1.- ["25","25","62","54","85","85","25","21"] 
            #2.- [25, 25, 62, 54, 85, 85, 25, 21]
            sumatorio = sum(numeros)
            promedio = sumatorio / len(numeros) 
            mayor = max(numeros) 
            menor = min(numeros) 
            result = {"sumatorio": sumatorio, "promedio": promedio, "mayor": mayor, "menor": menor}

    return render_template('estadisticas.html', lista=lista, result=result)


if __name__ == '__main__':
    app.run(debug=True)