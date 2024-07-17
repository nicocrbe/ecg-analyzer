from filtros import Filtro
from graficador import Graficador

class ProcesadorSenal:
    @staticmethod
    def procesar(muestra, amplitudes, fs, title):
        resultadoFiltro = Filtro.pasabanda(amplitudes, fs)
        resultadoFiltroDerivativo = Filtro.derivativo(resultadoFiltro)
        resultadoAlisado = Filtro.alisado(resultadoFiltroDerivativo)
        resultadoMediaMovil = Filtro.mediaMovil(resultadoAlisado)
        return Graficador.graficarResultados(muestra, amplitudes, resultadoFiltro, resultadoFiltroDerivativo, resultadoAlisado, resultadoMediaMovil, title)
