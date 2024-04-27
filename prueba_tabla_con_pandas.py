import pandas as pd

# Crear un DataFrame a partir de la tabla de percentiles
tabla_percentiles = pd.DataFrame([
    [2.8,  3.2,  3.6,  4.1,  4.9,  5.6,  6.6],
    [3.5,  4.1,  4.5,  5.2,  5.9,  6.6,  7.7],
    [4.2,  4.8,  5.3,  6.0,  6.7,  7.4,  8.5],
    [4.8,  5.4,  6.0,  6.6,  7.4,  8.2,  9.2],
    [5.3,  6.0,  6.6,  7.2,  8.0,  8.8,  9.8],
[5.7,  6.4,  7.1,  7.7,  8.5,  9.2,  10.3],
[6.1,  6.8,  7.5,  8.2,  8.9,  9.9,  10.8],
[6.4,  7.1,  7.8,  8.6,  9.3,  10.2,  11.2],
[6.7,  7.4,  8.1,  8.9,  9.7,  10.5,  11.6],
[7.0,  7.7,  8.4,  9.2,  10.0,  10.8,  11.9],
[7.3,  8.0,  8.7,  9.5,  10.3,  11.1,  12.2],
[7.6,  8.3,  9.0,  9.8,  10.5,  11.3,  12.5],
[7.9,  8.5,  9.2,  10.0,   10.7,  11.5, 12.8],
[8.1,  8.7,  9.5,  10.2,  10.9,  11.7, 13.0],
[8.3,  8.9,  9.7,  10.4,  11.1,  12.0, 13.2],
[8.5,  9.1,  9.9,  10.6,  11.3,  12.2,  13.4],
[8.7,  9.3,  10.1,  10.8,  11.6,  12.5,  13.6],
[8.8,  9.4,  10.2,  11.0,  11.8,  12.7,  13.8],
[8.9,  9.6,  10.4,  11.1,  12.0,  12.9,  14.0],
[9.0,  9.7,  10.5,  11.3,  12.2,  13.1,  14.2],
[9.1,  9.8,  10.7,  11.4,  12.4,  13.3,  14.4],
[9.2,  9.9,  10.8,  11.6,  12.6,  13.5,  14.6],
[9.3,  10.0,  10.9,  11.8,  12.7,  13.7,  14.8],
[9.4,  10.1,  11.1,  11.9,  12.9,  13.9,  15.0]
    # Resto de la tabla
], columns=[3, 10, 25, 50, 75, 90, 97])

class PercentileFinder:
    def __init__(self, tabla_percentiles):
        self.tabla_percentiles = tabla_percentiles
        self.percentiles = [3, 10, 25, 50, 75, 90, 97]

    def find_percentile(self, edad, peso):
        fila = min(edad, len(self.tabla_percentiles) - 1)  # Encontrar la fila correspondiente a la edad

        for p in self.percentiles:
            if peso <= self.tabla_percentiles.loc[fila, p]:
                return p
        return 97  # Si el peso excede el valor más alto de la tabla, se asume el percentil 97

# Usage
pf = PercentileFinder(tabla_percentiles)
edad = int(input('Diga la edad en meses: '))
peso = float(input('Diga el peso en kg: '))

percentil = pf.find_percentile(edad, peso)
percentil_anterior = pf.percentiles[pf.percentiles.index(percentil) - 1] if percentil!= 3 else None

if percentil_anterior is not None:
    print(f'El bebé se encuentra entre el percentil {percentil_anterior}-{percentil} de peso para su edad.')
else:
    print(f'El bebé se encuentra en el percentil 3 de peso para su edad.')