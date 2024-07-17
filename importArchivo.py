import wfdb

class ImportadorArchivo:
    @staticmethod
    def importar(filename):
        record = wfdb.rdrecord(filename)
        numMuestra = [i for i in range(record.sig_len)]
        valor = [float(record.p_signal[i][0]) for i in range(record.sig_len)]
        return numMuestra, valor, record.fs
