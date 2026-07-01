"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd

    from homework.lectura_archivo import leer_datos
    
    input = "files/input/"
    lectura_archivo = leer_datos(input)

    datos = {
        "cluster" : [],
        "cantidad_de_palabras_clave" : [],
        "porcentaje_de_palabras_clave" : [],
        "principales_palabras_clave" : []
    }

    principales_palabras_clave = []

    indice = 0

    for linea in lectura_archivo[4:]:
        elementos = linea.split()
        
        if not elementos:
            continue
        
        primer_elemento = elementos[0]
        
        if primer_elemento.isdigit():
            indice = int(primer_elemento) - 1
            datos["cluster"].append(int(primer_elemento))
            datos["cantidad_de_palabras_clave"].append(int(elementos[1]))
            datos["porcentaje_de_palabras_clave"].append(float(elementos[2].replace(",", ".")))
            principales_palabras_clave.append(elementos[4:])
        else:
            principales_palabras_clave[indice] += elementos
    
    for lista in principales_palabras_clave:
        datos["principales_palabras_clave"].append(" ".join(lista).rstrip("."))

    df = pd.DataFrame(datos)
    return df
