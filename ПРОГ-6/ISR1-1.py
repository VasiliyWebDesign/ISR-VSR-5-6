# Задание: разработать скрипт, вычисляющий статистические
# показатели (среднее значение, дисперсия, среднее квадратичное
# отклонение) для данных, считанных из CSV-файла.


"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg


"""

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

        sums = {'Offline': 0, 'Online': 0}
        for _l in data:
            sums['Offline'] += _l['Offline']
            sums['Online'] += _l['Online']

        self._mean = {'Offline': sums['Offline'] / len(data), 'Online': sums['Online'] / len(data)}

        return self._mean

    @property
    def max(self):
        self._max = {'Offline': float('-Inf'), 'Online': float('-Inf')}
        for _l in self.data:
          self._max = {'Offline': max(self._max['Offline'], _l['Offline']), 'Online': max(self._max['Online'], _l['Online'])}
        return self._max

    @property
    def min(self):
        self._min = {'Offline': float('Inf'), 'Online': float('Inf')}
        for _l in self.data:
          self._min = {'Offline': min(self._min['Offline'], _l['Offline']), 'Online': min(self._min['Online'], _l['Online'])}
        return self._min

    @property
    def disp(self):
        fixedmean = self.get_mean(self.data)
        self._disp = {'Offline': 0, 'Online': 0}
        for _l in self.data:
          self._disp['Offline'] += (_l['Offline'] - fixedmean['Offline'])**2
          self._disp['Online'] += (_l['Online'] - fixedmean['Online'])**2
        self._disp = {'Offline': self._disp['Offline'] / len(self.data), 'Online': self._disp['Online'] / len(self.data)}
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        self._sigma_sq = {'Offline': self._disp['Offline']**(1/2), 'Online': self._disp['Online']**(1/2)}
        return self._sigma_sq

FILE2 = 'MarketingSpend.csv'

def main():

    data2 = MathStats(FILE2)
    slice_test1 = data2.data[:2]

    print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)

    print('Максимум: ', data2.max)
    print('Минимум: ', data2.min)
    print('Дисперсия: ', data2.disp)
    print('Средн. кв. отклонение: ', data2.sigma_sq)

main()