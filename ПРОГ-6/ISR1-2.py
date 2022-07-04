# Задание: осуществить рефакторинг (модификацию) скрипта,
# вычисляющего статистические показатели для данных, считанных из
# CSV, с использованием библиотеки научных вычислений numpy.


"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg


"""

import numpy as np
import scipy.stats as sps

class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        self._disp = None
        self._sigma_sq = None
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self):
        return self._data

    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """
        
        self._mean = {'Offline': np.mean([_el['Offline'] for _el in data]), 'Online': np.mean([_el['Online'] for _el in data])}
        
        return self._mean

    @property
    def max(self):
        self._max = {'Offline': np.max([_el['Offline'] for _el in self.data]), 'Online': np.max([_el['Online'] for _el in self.data])}
        return self._max

    @property
    def min(self):
        self._min = {'Offline': np.min([_el['Offline'] for _el in self.data]), 'Online': np.min([_el['Online'] for _el in self.data])}
        return self._min

    @property
    def disp(self):
        self._disp = {'Offline': np.var([_el['Offline'] for _el in self.data]), 'Online': np.var([_el['Online'] for _el in self.data])}
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        self._sigma_sq = {'Offline': np.std([_el['Offline'] for _el in self.data]), 'Online': np.std([_el['Online'] for _el in self.data])}
        return self._sigma_sq
