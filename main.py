from importArchivo import ImportadorArchivo
from procesadorSenal import ProcesadorSenal
from frecuenciaCardiaca import FrecuenciaCardiaca

if __name__ == "__main__":
    archivosECG = [
        {"title": "ECG adulto saludable", "filename": "111", "fetal": 0},
        {"title": "ECG con arritmia taquicardia", "filename": "233", "fetal": 0},
        {"title": "ECG con arritmia bradicardia", "filename": "231", "fetal": 0},
        {"title": "ECG fetal", "filename": "a02", "fetal": 1}
    ]
    
    for archivo in archivosECG:
        muestra, amplitudes, fs = ImportadorArchivo.importar(archivo["filename"])
        salida = ProcesadorSenal.procesar(muestra, amplitudes, fs, archivo["title"])
        FrecuenciaCardiaca.calcular(salida, fs, archivo["fetal"], archivo["title"])
