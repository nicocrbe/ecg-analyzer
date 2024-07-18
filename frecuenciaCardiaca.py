import matplotlib.pyplot as plt
import numpy as np
from graficador import Graficador

class FrecuenciaCardiaca:
    @staticmethod
    def calcular(input, fs, fetal, title):
        if fetal:
            limiteSuperior = 160
            limiteInferior = 120
            print("ECG FETAL")
        else:
            limiteSuperior = 100
            limiteInferior = 60

        print("La frecuencia cardíaca se considera normal entre: " + str(limiteInferior) + " y " + str(limiteSuperior))
        frecuenciaCardiaca = []
        for i in range(len(input) - 1):
            if input[i + 1] != input[i]:
                frecuenciaCardiaca.append(fs * 60 / (input[i + 1] - input[i]))
        
        x = [i for i in range(len(frecuenciaCardiaca))]
        Graficador.graficar(6, x, frecuenciaCardiaca, "Frecuencia cardíaca vs. latidos", 30, 200, len(frecuenciaCardiaca), "N° latidos", "Frecuencia [lat/min]", title)

        plt.plot([0, len(frecuenciaCardiaca)], [limiteInferior, limiteInferior], 'r')
        plt.plot([0, len(frecuenciaCardiaca)], [limiteSuperior, limiteSuperior], 'r')
        freqMedia = np.mean(frecuenciaCardiaca)

        plt.figtext(0.05, 0.04, "Frecuencia media: " + str(int(freqMedia)), fontsize=12, va="bottom", ha="left")
        plt.figtext(0.05, 0.02, "La frecuencia cardíaca se considera normal entre: " + str(limiteInferior) + " y " + str(limiteSuperior), fontsize=12, va="bottom", ha="left")
        if freqMedia < limiteInferior:
            print("Bradicardia")
            plt.figtext(0.05, 0, "Bradicardia", fontsize=12, va="bottom", ha="left")
        elif freqMedia > limiteSuperior:
            print("Taquicardia")
            plt.figtext(0.05, 0, "Taquicardia", fontsize=12, va="bottom", ha="left")
        else:
            print("Frecuencia regular")
            plt.figtext(0.05, 0, "Frecuencia regular", fontsize=12, va="bottom", ha="left")
        plt.show()
        print("Frecuencia media: " + str(int(freqMedia)))
