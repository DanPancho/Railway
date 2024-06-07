import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sum_numbers():
    if request.method == 'POST':
        # Obtener los números ingresados por el usuario desde el formulario
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        # Calcular la suma de los números
        result = num1 + num2
        
        # Retornar un HTML con el resultado de la suma
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Suma de Dos Números</title>
        </head>
        <body>
            <h1>Suma de Dos Números</h1>
            <p>El resultado de la suma de {num1} y {num2} es: {result}</p>
            <a href="/">Volver al inicio</a>
        </body>
        </html>
        """.format(num1=num1, num2=num2, result=result)
    else:
        # Si la solicitud es GET, mostrar el formulario para ingresar los números
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Suma de Dos Números</title>
        </head>
        <body>
            <h1>Suma de Dos Números</h1>
            <form method="post">
                <label for="num1">Número 1:</label>
                <input type="number" id="num1" name="num1" required>
                <br>
                <label for="num2">Número 2:</label>
                <input type="number" id="num2" name="num2" required>
                <br>
                <button type="submit">Calcular Suma</button>
            </form>
            <p>Variable servidor: {name}</p>
        </body>
        </html>
        """.format(name=os.environ.get('NAME', 'DANIEL'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
