import matplotlib.pyplot as plt
import numpy as np

class Graficador:
    @staticmethod
    def graficar(i, x, y, titulo, inf, sup, n, xlabel, ylabel, title):
        fig1 = plt.figure(title)
        fig1.subplots_adjust(hspace=0.75, wspace=0.75)
        ax = fig1.add_subplot(3, 2, i)
        ax.plot(x, y)
        plt.axis([-1, n, inf, sup])
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(titulo)
        plt.grid()

    @staticmethod
    def graficarResultados(muestra, amplitudes, resultadoFiltro, resultadoFiltroDerivativo, resultadoAlisado, resultadoMediaMovil, title):
        n = len(muestra)
        muestra2 = list(muestra) + list(range(n, len(resultadoFiltroDerivativo)))

        inicio, fin, avanzar, umbral = 0, 0, 1, np.mean(resultadoMediaMovil)
        m = []

        while avanzar:
            for i in range(fin, len(resultadoMediaMovil)):
                if i == len(resultadoMediaMovil) - 200:
                    avanzar = 0
                if resultadoMediaMovil[i] >= umbral:
                    inicio = i
                    break
            for i in range(inicio, len(resultadoMediaMovil)):
                if resultadoMediaMovil[i] <= umbral:
                    fin = i
                    break
            if inicio < fin and len(resultadoMediaMovil[inicio:fin]) > 0:
                m.append(inicio + np.argmax(resultadoMediaMovil[inicio:fin]))

        muestra_2 = [i - 24 for i in m]
        cantidadMuestras = 1500

        Graficador.graficarECG(amplitudes, cantidadMuestras, muestra, title)
        Graficador.graficarFiltroPasabanda(cantidadMuestras, muestra, resultadoFiltro, title)
        Graficador.graficarFiltroDerivativo(cantidadMuestras, muestra2, resultadoFiltroDerivativo, title)
        Graficador.graficarAlisado(cantidadMuestras, muestra2, resultadoAlisado, title)
        Graficador.graficarMediaMovil(cantidadMuestras, muestra2, resultadoMediaMovil, title)

        plt.plot([0, cantidadMuestras], [umbral, umbral], 'g')
        plt.plot([inicio, inicio], [min(resultadoMediaMovil) - 0.001, (max(resultadoMediaMovil) + 0.001)], 'g')
        plt.plot([fin, fin], [min(resultadoMediaMovil) - 0.001, (max(resultadoMediaMovil) + 0.001)], 'g')

        return muestra_2

    @staticmethod
    def graficarECG(amplitudes, cantidadMuestras, muestra, title):
        Graficador.graficar(1, muestra, amplitudes, "ECG", min(amplitudes) - 0.01, (max(amplitudes) + 0.01), cantidadMuestras, "Número muestras [n]", "amplitud [mV]", title)

    @staticmethod
    def graficarFiltroPasabanda(cantidadMuestras, muestra, resultadoFiltro, title):
        Graficador.graficar(2, muestra, resultadoFiltro, "Filtro pasabanda", min(resultadoFiltro) - 0.01, (max(resultadoFiltro) + 0.01), cantidadMuestras, "Número muestras [n]", "Amplitud [mV]", title)

    @staticmethod
    def graficarFiltroDerivativo(cantidadMuestras, muestra2, resultadoFiltroDerivativo, title):
        Graficador.graficar(3, muestra2, resultadoFiltroDerivativo, "Filtro derivativo", min(resultadoFiltroDerivativo) - 0.01, (max(resultadoFiltroDerivativo) + 0.01), cantidadMuestras, "Número muestras [n]", "Amplitud [mV]", title)

    @staticmethod
    def graficarAlisado(cantidadMuestras, muestra2, resultadoAlisado, title):
        Graficador.graficar(4, muestra2, resultadoAlisado, "Alisado", min(resultadoAlisado) - 0.01, (max(resultadoAlisado) + 0.01), cantidadMuestras, "Número muestras [n]", "Amplitud [mV]", title)

    @staticmethod
    def graficarMediaMovil(cantidadMuestras, muestra2, resultadoMediaMovil, title):
        Graficador.graficar(5, muestra2, resultadoMediaMovil, "Media móvil", min(resultadoMediaMovil) - 0.001, (max(resultadoMediaMovil) + 0.001), cantidadMuestras, "Número muestras [n]", "Amplitud [mV]", title)
