import numpy as np
import pandas as pd

def statistical_calculator(arr_sorted_temperatura, arr_sorted_humedad, arr_sorted_ldr, arr_sorted_tds, arr_sorted_ds18b20, arr_sorted_ph):
    media_temperatura = sum(arr_sorted_temperatura) / len(arr_sorted_temperatura)
    media_humedad = sum(arr_sorted_humedad) / len(arr_sorted_humedad)
    media_ldr = sum(arr_sorted_ldr) / len(arr_sorted_ldr)
    media_tds = sum(arr_sorted_tds) / len(arr_sorted_tds)
    media_ds18b20 = sum(arr_sorted_ds18b20) / len(arr_sorted_ds18b20)
    media_ph = sum(arr_sorted_ph) / len(arr_sorted_ph)

    desviacion_temperatura = 0
    desviacion_humedad = 0
    desviacion_ldr = 0
    desviacion_tds = 0
    desviacion_ds18b20 = 0
    desviacion_ph = 0

    for elemento in arr_sorted_temperatura:
        desviacion_temperatura += abs(elemento - media_temperatura)
    for elemento in arr_sorted_humedad:
        desviacion_humedad += abs(elemento - media_humedad)
    for elemento in arr_sorted_ldr:
        desviacion_ldr += abs(elemento - media_ldr)
    for elemento in arr_sorted_tds:
        desviacion_tds += abs(elemento - media_tds)
    for elemento in arr_sorted_ds18b20:
        desviacion_ds18b20 += abs(elemento - media_ds18b20)
    for elemento in arr_sorted_ph:
        desviacion_ph += abs(elemento - media_ph)

    desviacion_media_temperatura = round(desviacion_temperatura / len(arr_sorted_temperatura), 2)
    desviacion_media_humedad = round(desviacion_humedad / len(arr_sorted_humedad), 2)
    desviacion_media_ldr = round(desviacion_ldr / len(arr_sorted_ldr), 2)
    desviacion_media_tds = round(desviacion_tds / len(arr_sorted_tds), 2)
    desviacion_media_ds18b20 = round(desviacion_ds18b20 / len(arr_sorted_ds18b20), 2)
    desviacion_media_ph = round(desviacion_ph / len(arr_sorted_ph), 2)

    varianza_resultado_temperatura = 0
    varianza_resultado_humedad = 0
    varianza_resultado_ldr = 0
    varianza_resultado_tds = 0
    varianza_resultado_ds18b20 = 0
    varianza_resultado_ph = 0

    for elemento in arr_sorted_temperatura:
        valor = pow(abs(elemento - media_temperatura), 2)
        varianza_resultado_temperatura += valor
    for elemento in arr_sorted_humedad:
            valor = pow(abs(elemento - media_humedad), 2)
            varianza_resultado_humedad += valor
    for elemento in arr_sorted_ldr:
        valor = pow(abs(elemento - media_ldr), 2)
        varianza_resultado_ldr += valor
    for elemento in arr_sorted_tds:
        valor = pow(abs(elemento - media_tds), 2)
        varianza_resultado_tds += valor
    for elemento in arr_sorted_ds18b20:
        valor = pow(abs(elemento - media_ds18b20), 2)
        varianza_resultado_ds18b20 += valor
    for elemento in arr_sorted_ph:
        valor = pow(abs(elemento - media_ph), 2)
        varianza_resultado_ph += valor

    varianza_temperatura = round(varianza_resultado_temperatura / len(arr_sorted_temperatura), 2)
    varianza_humedad = round(varianza_resultado_temperatura / len(arr_sorted_humedad), 2)
    varianza_ldr = round(varianza_resultado_ldr / len(arr_sorted_ldr), 2)
    varianza_tds = round(varianza_resultado_tds / len(arr_sorted_tds), 2)
    varianza_ds18b20 = round(varianza_resultado_ds18b20 / len(arr_sorted_ds18b20), 2)
    varianza_ph = round(varianza_resultado_ph / len(arr_sorted_ph), 2)

    desviacion_estandar_temperatura = varianza_temperatura ** 0.5
    desviacion_estandar_humedad = varianza_humedad ** 0.5
    desviacion_estandar_ldr = varianza_ldr ** 0.5
    desviacion_estandar_tds = varianza_tds ** 0.5
    desviacion_estandar_ds18b20 = varianza_ds18b20 ** 0.5
    desviacion_estandar_ph = varianza_ph ** 0.5

    arr_ordenate_temperatura = np.sort(arr_sorted_temperatura)
    arr_ordenate_humedad = np.sort(arr_sorted_humedad)
    arr_ordenate_ldr = np.sort(arr_sorted_ldr)
    arr_ordenate_tds = np.sort(arr_sorted_tds)
    arr_ordenate_ds18b20 = np.sort(arr_sorted_ds18b20)
    arr_ordenate_ph = np.sort(arr_sorted_ph)

    K_temperatura = 1 + (3.322 * np.log10(len(arr_sorted_temperatura)))
    K_round_temperatura = round(K_temperatura)
    R_temperatura = arr_ordenate_temperatura[-1] - arr_ordenate_temperatura[0]
    A_temperatura = R_temperatura / K_round_temperatura
    A_round_temperatura = round(A_temperatura + 0.1)

    K_humedad = 1 + (3.322 * np.log10(len(arr_sorted_humedad)))
    K_round_humedad = round(K_humedad)
    R_humedad = arr_ordenate_humedad[-1] - arr_ordenate_humedad[0]
    A_humedad = R_humedad / K_round_humedad
    A_round_humedad = round(A_humedad + 0.1)

    K_ldr = 1 + (3.322 * np.log10(len(arr_sorted_ldr)))
    K_round_ldr = round(K_ldr)
    R_ldr = arr_ordenate_ldr[-1] - arr_ordenate_ldr[0]
    A_ldr = R_ldr / K_round_ldr
    A_round_ldr = round(A_ldr + 0.1)

    K_tds = 1 + (3.322 * np.log10(len(arr_sorted_tds)))
    K_round_tds = round(K_tds)
    R_tds = arr_ordenate_tds[-1] - arr_ordenate_tds[0]
    A_tds = R_tds / K_round_tds
    A_round_tds = round(A_tds + 0.1)

    K_ds18b20 = 1 + (3.322 * np.log10(len(arr_sorted_ds18b20)))
    K_round_ds18b20 = round(K_ds18b20)
    R_ds18b20 = arr_ordenate_ds18b20[-1] - arr_ordenate_ds18b20[0]
    A_ds18b20 = R_ds18b20 / K_round_ds18b20
    A_round_ds18b20 = round(A_ds18b20 + 0.1)

    K_ph = 1 + (3.322 * np.log10(len(arr_sorted_ph)))
    K_round_ph = round(K_ph)
    R_ph = arr_ordenate_ph[-1] - arr_ordenate_ph[0]
    A_ph = R_ph / K_round_ph
    A_round_ph = round(A_ph + 0.1)

    variabilidad_temperatura = 0
    variabilidad_humedad = 0
    variabilidad_ldr = 0
    variabilidad_tds = 0
    variabilidad_ds18b20 = 0
    variabilidad_ph = 0

    valor_min_temperatura = arr_ordenate_temperatura[0]
    valor_min_humedad = arr_ordenate_humedad[0]
    valor_min_ldr = arr_ordenate_ldr[0]
    valor_min_tds = arr_ordenate_tds[0]
    valor_min_ds18b20 = arr_ordenate_ds18b20[0]
    valor_min_ph = arr_ordenate_ph[0]

    datos_temperatura = np.zeros((6, 6))
    datos_humedad = np.zeros((6,6))
    datos_ldr = np.zeros((6, 6))
    datos_tds = np.zeros((6, 6))
    datos_ds18b20 = np.zeros((6, 6))
    datos_ph = np.zeros((6, 6))

    table_frecuency_temperatura = pd.DataFrame(
        datos_temperatura, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])
    table_frecuency_humedad = pd.DataFrame(
            datos_humedad, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])
    table_frecuency_ldr = pd.DataFrame(
        datos_ldr, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])
    table_frecuency_tds = pd.DataFrame(
        datos_tds, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])
    table_frecuency_ds18b20 = pd.DataFrame(
        datos_ds18b20, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])
    table_frecuency_ph = pd.DataFrame(
        datos_ph, columns=["LimInf", "LimSup", "Frecuencia", "Marca de clase", "LimInfExacta", "LimSupExacta"])

    table_frecuency_temperatura.iloc[0, 0] = valor_min_temperatura
    table_frecuency_humedad.iloc[0, 0] = valor_min_humedad
    table_frecuency_ldr.iloc[0, 0] = valor_min_ldr
    table_frecuency_tds.iloc[0, 0] = valor_min_tds
    table_frecuency_ds18b20.iloc[0, 0] = valor_min_ds18b20
    table_frecuency_ph.iloc[0, 0] = valor_min_ph

    for i in range(1, table_frecuency_temperatura.shape[0]):
        table_frecuency_temperatura.iloc[i, 0] = table_frecuency_temperatura.iloc[i-1, 1] + 1
        table_frecuency_temperatura.iloc[i, 1] = table_frecuency_temperatura.iloc[i, 0] + A_round_temperatura - variabilidad_temperatura
        table_frecuency_temperatura.iloc[:, 2] = [np.sum((arr_ordenate_temperatura >= table_frecuency_temperatura.iloc[i, 0]) &
                                                         (arr_sorted_temperatura <= table_frecuency_temperatura.iloc[i, 1])) for i in range(table_frecuency_temperatura.shape[0])]
        table_frecuency_temperatura.iloc[:, 3] = (table_frecuency_temperatura["LimInf"] + table_frecuency_temperatura["LimSup"]) / 2
        table_frecuency_temperatura.iloc[:, 4] = (table_frecuency_temperatura["LimInf"] - (variabilidad_temperatura / 2))
        table_frecuency_temperatura.iloc[:, 5] = (table_frecuency_temperatura["LimSup"] + (variabilidad_temperatura / 2))
    for i in range(1, table_frecuency_humedad.shape[0]):
        table_frecuency_humedad.iloc[i, 0] = table_frecuency_humedad.iloc[i-1, 1] + 1
        table_frecuency_humedad.iloc[i, 1] = table_frecuency_humedad.iloc[i, 0] + A_round_humedad - variabilidad_humedad
        table_frecuency_humedad.iloc[:, 2] = [np.sum((arr_ordenate_humedad >= table_frecuency_humedad.iloc[i, 0]) &
                                                         (arr_sorted_humedad <= table_frecuency_humedad.iloc[i, 1])) for i in range(table_frecuency_humedad.shape[0])]
        table_frecuency_humedad.iloc[:, 3] = (table_frecuency_humedad["LimInf"] + table_frecuency_humedad["LimSup"]) / 2
        table_frecuency_humedad.iloc[:, 4] = (table_frecuency_humedad["LimInf"] - (variabilidad_humedad / 2))
        table_frecuency_humedad.iloc[:, 5] = (table_frecuency_humedad["LimSup"] + (variabilidad_humedad / 2))
    for i in range(1, table_frecuency_ldr.shape[0]):
        table_frecuency_ldr.iloc[i, 0] = table_frecuency_ldr.iloc[i-1, 1] + 1
        table_frecuency_ldr.iloc[i, 1] = table_frecuency_ldr.iloc[i, 0] + A_round_ldr - variabilidad_ldr
        table_frecuency_ldr.iloc[:, 2] = [np.sum((arr_ordenate_ldr >= table_frecuency_ldr.iloc[i, 0]) &
                                                 (arr_sorted_ldr <= table_frecuency_ldr.iloc[i, 1])) for i in range(table_frecuency_ldr.shape[0])]
        table_frecuency_ldr.iloc[:, 3] = (table_frecuency_ldr["LimInf"] + table_frecuency_ldr["LimSup"]) / 2
        table_frecuency_ldr.iloc[:, 4] = (table_frecuency_ldr["LimInf"] - (variabilidad_ldr / 2))
        table_frecuency_ldr.iloc[:, 5] = (table_frecuency_ldr["LimSup"] + (variabilidad_ldr / 2))

    for i in range(1, table_frecuency_tds.shape[0]):
        table_frecuency_tds.iloc[i, 0] = table_frecuency_tds.iloc[i-1, 1] + 1
        table_frecuency_tds.iloc[i, 1] = table_frecuency_tds.iloc[i, 0] + A_round_tds - variabilidad_tds
        table_frecuency_tds.iloc[:, 2] = [np.sum((arr_ordenate_tds >= table_frecuency_tds.iloc[i, 0]) &
                                                 (arr_sorted_tds <= table_frecuency_tds.iloc[i, 1])) for i in range(table_frecuency_tds.shape[0])]
        table_frecuency_tds.iloc[:, 3] = (table_frecuency_tds["LimInf"] + table_frecuency_tds["LimSup"]) / 2
        table_frecuency_tds.iloc[:, 4] = (table_frecuency_tds["LimInf"] - (variabilidad_tds / 2))
        table_frecuency_tds.iloc[:, 5] = (table_frecuency_tds["LimSup"] + (variabilidad_tds / 2))

    for i in range(1, table_frecuency_ds18b20.shape[0]):
        table_frecuency_ds18b20.iloc[i, 0] = table_frecuency_ds18b20.iloc[i-1, 1] + 1
        table_frecuency_ds18b20.iloc[i, 1] = table_frecuency_ds18b20.iloc[i, 0] + A_round_ds18b20 - variabilidad_ds18b20
        table_frecuency_ds18b20.iloc[:, 2] = [np.sum((arr_ordenate_ds18b20 >= table_frecuency_ds18b20.iloc[i, 0]) &
                                                     (arr_sorted_ds18b20 <= table_frecuency_ds18b20.iloc[i, 1])) for i in range(table_frecuency_ds18b20.shape[0])]
        table_frecuency_ds18b20.iloc[:, 3] = (table_frecuency_ds18b20["LimInf"] + table_frecuency_ds18b20["LimSup"]) / 2
        table_frecuency_ds18b20.iloc[:, 4] = (table_frecuency_ds18b20["LimInf"] - (variabilidad_ds18b20 / 2))
        table_frecuency_ds18b20.iloc[:, 5] = (table_frecuency_ds18b20["LimSup"] + (variabilidad_ds18b20 / 2))

    for i in range(1, table_frecuency_ph.shape[0]):
        table_frecuency_ph.iloc[i, 0] = table_frecuency_ph.iloc[i-1, 1] + 1
        table_frecuency_ph.iloc[i, 1] = table_frecuency_ph.iloc[i, 0] + A_round_ph - variabilidad_ph
        table_frecuency_ph.iloc[:, 2] = [np.sum((arr_ordenate_ph >= table_frecuency_ph.iloc[i, 0]) &
                                                (arr_sorted_ph <= table_frecuency_ph.iloc[i, 1])) for i in range(table_frecuency_ph.shape[0])]
        table_frecuency_ph.iloc[:, 3] = (table_frecuency_ph["LimInf"] + table_frecuency_ph["LimSup"]) / 2
        table_frecuency_ph.iloc[:, 4] = (table_frecuency_ph["LimInf"] - (variabilidad_ph / 2))
        table_frecuency_ph.iloc[:, 5] = (table_frecuency_ph["LimSup"] + (variabilidad_ph / 2))

    println("Tabla de frecuencias - Temperatura:")
    println(table_frecuency_temperatura)
    println("Tabla de frecuencias - Temperatura:")
    println(table_frecuency_temperatura)
    println("Tabla de frecuencias - LDR:")
    println("table_frecuency_ldr")
    println("Tabla de frecuencias - TDS:")
    println(table_frecuency_tds)
    println("Tabla de frecuencias - DS18B20:")
    println(table_frecuency_ds18b20)
    println("Tabla de frecuencias - pH:")
    println(table_frecuency_ph)

    return (
        desviacion_media_temperatura, media_temperatura, varianza_temperatura, desviacion_estandar_temperatura,
        arr_ordenate_temperatura, table_frecuency_temperatura,
        desviacion_media_humedad, media_humedad, varianza_humedad, desviacion_estandar_humedad,
        arr_ordenate_humedad, table_frecuency_humedad,
        desviacion_media_ldr, media_ldr, varianza_ldr, desviacion_estandar_ldr,
        arr_ordenate_ldr, table_frecuency_ldr,
        desviacion_media_tds, media_tds, varianza_tds, desviacion_estandar_tds,
        arr_ordenate_tds, table_frecuency_tds,
        desviacion_media_ds18b20, media_ds18b20, varianza_ds18b20, desviacion_estandar_ds18b20,
        arr_ordenate_ds18b20, table_frecuency_ds18b20,
        desviacion_media_ph, media_ph, varianza_ph, desviacion_estandar_ph,
        arr_ordenate_ph, table_frecuency_ph
    )
