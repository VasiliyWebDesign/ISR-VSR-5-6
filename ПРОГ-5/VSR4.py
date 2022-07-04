# Задание: на основе кода, позволяющего визуализировать
# данные о ценах на недвижимость (точечная диаграмма), отобразить
# с помощью библиотеки mathplotlib линейный график и график
# полинома второй степени (квадратичный) соответствующий изменениям
# цен на недвижимость.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = np.genfromtxt('ex1data2.txt', delimiter=',')
x, y = data[:,0], data[:,2]
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

#полином 1

f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full=True)
f1 = np.poly1d(f1p)
fx = np.linspace(min(x), max(x), 500)
plt.scatter(x, y, s=10)
plt.plot(fx, f1(fx), linewidth=1.0, color='r')
plt.title('Насколько стоимость зависит от площади для полинома ст. 1')
plt.xlabel('Значения площади')
plt.ylabel('Значения стомости')
plt.show()
for val in [1650, 2200]:
    print(f'square_house = {val}, cost = {f1(val)}')
y_pred_simple_model = [f1(val) for val in x]

print('R^2: ', r2_score(y, y_pred_simple_model))
print('MAE: ', mean_absolute_error(y, y_pred_simple_model))
print('MSE: ', mean_squared_error(y, y_pred_simple_model))
print('RMSE: ', np.sqrt(mean_squared_error(y, y_pred_simple_model)))

#полином 2

f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 2, full=True)
f1 = np.poly1d(f1p)
fx = np.linspace(min(x), max(x), 500)
plt.scatter(x, y, s=10)
plt.plot(fx, f1(fx), linewidth=1.0, color='r')
plt.title('Насколько стоимость зависит от площади для полинома ст. 2')
plt.xlabel('Значения площади')
plt.ylabel('Значения стомости')
plt.show()
for val in [1650, 2200]:
    print(f'square_house = {val}, cost = {f1(val)}')
y_pred_simple_model = [f1(val) for val in x]

print('R^2: ', r2_score(y, y_pred_simple_model))
print('MAE: ', mean_absolute_error(y, y_pred_simple_model))
print('MSE: ', mean_squared_error(y, y_pred_simple_model))
print('RMSE: ', np.sqrt(mean_squared_error(y, y_pred_simple_model)))

#полином 3

f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 3, full=True)
f1 = np.poly1d(f1p)
fx = np.linspace(min(x), max(x), 500)
plt.scatter(x, y, s=10)
plt.plot(fx, f1(fx), linewidth=1.0, color='r')
plt.title('Насколько стоимость зависит от площади для полинома ст. 3')
plt.xlabel('Значения площади')
plt.ylabel('Значения стомости')
plt.show()
for val in [1650, 2200]:
    print(f'square_house = {val}, cost = {f1(val)}')
y_pred_simple_model = [f1(val) for val in x]

print('R^2: ', r2_score(y, y_pred_simple_model))
print('MAE: ', mean_absolute_error(y, y_pred_simple_model))
print('MSE: ', mean_squared_error(y, y_pred_simple_model))
print('RMSE: ', np.sqrt(mean_squared_error(y, y_pred_simple_model)))
print('\n')

#линейная регрессия
print('Показатели для линейной регрессии')
x, y = data[:,[0,1]], data[:,2]
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]
model = LinearRegression()
model.fit(x, y)
x_test = [[1650, 3], [2200, 4]]
y_pred = model.predict(x_test)

for index in range(0,2):
    print('square_house = {}, rooms = {}, cost = {}'.format(x_test[index][0], x_test[index][1], y_pred[index]))

y_pred_multiple_model = model.predict(x)

print('R^2: ', r2_score(y, y_pred_multiple_model))
print('MAE: ', mean_absolute_error(y, y_pred_multiple_model))
print('MSE: ', mean_squared_error(y, y_pred_multiple_model))
print('RMSE: ', np.sqrt(mean_squared_error(y, y_pred_multiple_model)))
