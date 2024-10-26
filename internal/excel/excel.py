import numpy as np
import pandas as pd
from openpyxl import Workbook

# Пример матрицы
matrix = [
    [1, 2, 3],
    [4, 5, 6, 123, 'wfwef', 'wefwfe'],
    [7, 8, 9, 322, 23],
    ['eqw'],
    [123]
]
df = pd.DataFrame(matrix)

wb = Workbook()
ws = wb.active

# Заполняем ячейки в Excel
for row_index, row in enumerate(df.values):
    for col_index, value in enumerate(row):
        if value == None:
            value = np.nan
        ws.cell(row=row_index + 1, column=col_index + 1).value = value

# Сохраняем файл
wb.save('matrix_to_excel.xlsx')
