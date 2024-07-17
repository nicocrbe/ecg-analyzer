import scipy.signal as signal

class Filtro:
    @staticmethod
    def pasabanda(amplitudes, fs):
        n = signal.firwin(19, [5 * 2 / fs, 15 * 2 / fs], pass_zero=False)
        return signal.lfilter(n, 1, amplitudes)

    @staticmethod
    def derivativo(input):
        h_d = [-1 / 8, -2 / 8, 0, 2 / 8, 1 / 8]
        return signal.convolve(input, h_d)

    @staticmethod
    def alisado(input):
        return [x ** 2 for x in input]

    @staticmethod
    def mediaMovil(input, n=25):
        salida = [0] * len(input)
        for i in range(n - 1, len(input)):
            salida[i] = sum(input[i - j] for j in range(n)) / n
        return salida
