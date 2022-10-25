from crypt import methods
from fileinput import filename

from flask import Flask, request, jsonify, render_template
# Sirve para trabajar con los archivos que nos llegan de internet
from werkzeug.utils import secure_filename
# Sirve para la inteligencia artificial
from joblib import load
import numpy as np
import os


# Generar el servidor en Flask (Back-end)

servidorWeb = Flask(__name__)

# Anotación, define la ruta. Después se pone una función


@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('pagina.html')

# Agregar otro servicio. Procesar datos a través del Form


@servidorWeb.route('/modeloIA', methods=["POST"])
def modeloForm():
    # Procesar datos de entrada
    contenido = request.form

    print(contenido)

    return jsonify({"Resultado": "datos recibidos"})

# Procesar datos de un archivo


@servidorWeb.route('/modeloFile', methods=["POST"])
def modeloFile():
    f = request.files['file']
    # PAra poder trabajr con el filename
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), 'files', filename)
    f.save(path)
    file = open(path, 'r')

    for line in file:
        print(line)
    return jsonify({"Resultado": "datos recibidos archivo"})


if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')
