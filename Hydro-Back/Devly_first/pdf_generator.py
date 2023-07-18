from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import os
from reportlab.lib.pagesizes import letter
import tempfile
import numpy as np

def generar_graficaHumedad(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('Humedad')
    plt.title('Gráfica de Humedad')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaTemperature(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.title('Gráfica de Temperatura')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaLDR(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('LDR')
    plt.title('Gráfica de LDR')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaTDS(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('TDS')
    plt.title('Gráfica de TDS')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaPH(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('pH')
    plt.title('Gráfica de pH')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaDS18B20(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('DS18B20')
    plt.title('Gráfica de DS18B20')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def calcular_regresion_lineal(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(np.multiply(x, y))
    sum_xx = np.sum(np.multiply(x, x))

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

def generar_pdf(table_frecuency_campo2, table_frecuency_campo1, arr_sorted_campo2, desviacion_media_campo2, varianza_campo2,
                media_campo2, desviacion_estandar_campo2, arr_sorted_campo1, arr_ordenate_campo2, arr_ordenate_campo1,
                desviacion_media_campo1, media_campo1, varianza_campo1, desviacion_estandar_campo1, pdf_filename):
    table_str = table_frecuency_campo2.to_string(index=False)
    table_str1 = table_frecuency_campo1.to_string(index=False)
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    # Combinar la ruta de descargas con el nombre del archivo PDF
    pdf_path = os.path.join(download_folder, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(70, 700, "Datos de Humedad:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
        # Espacio adicional antes de la desviación media
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 600, "Datos ordenados de Humedad:")
    for dato in arr_ordenate_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos

    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Humedad:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Humedad:")
    c.drawString(70, y_pos - 20, str(varianza_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Humedad:")
    c.drawString(70, y_pos - 20, str(media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar humedad:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo2, 2)))
    c.showPage()
    temp_filename = generar_graficaHumedad(arr_sorted_campo2)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    c.showPage()

    # Agregar regresión lineal de humedad
    slope_humidity, intercept_humidity = calcular_regresion_lineal(range(len(arr_sorted_campo2)), arr_sorted_campo2)
    c.drawString(70, 700, "Regresión Lineal de Humedad:")
    c.drawString(70, 680, f"Pendiente (Slope): {slope_humidity:.2f}")
    c.drawString(70, 660, f"Intercepto: {intercept_humidity:.2f}")
    c.drawString(70, 640, f"y = {slope_humidity:.2f}x + {intercept_humidity:.2f}")

    c.showPage()

    c.drawString(70, 700, "Datos de Temperatura:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo1:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 535, "Datos ordenados de Temperatura:")
    for dato in arr_ordenate_campo1:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Temperatura:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo1))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Temperatura:")
    c.drawString(70, y_pos - 20, str(varianza_campo1))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Temperatura:")
    c.drawString(70, y_pos - 20, str(media_campo1))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Temperatura:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo1, 2)))
    c.showPage()
    temp_filename = generar_graficaTemperature(arr_sorted_campo1)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    c.showPage()

    # Agregar regresión lineal de temperatura
    slope_temperature, intercept_temperature = calcular_regresion_lineal(range(len(arr_sorted_campo1)), arr_sorted_campo1)
    c.drawString(70, 700, "Regresión Lineal de Temperatura:")
    c.drawString(70, 680, f"Pendiente (Slope): {slope_temperature:.2f}")
    c.drawString(70, 660, f"Intercepto: {intercept_temperature:.2f}")
    c.drawString(70, 640, f"y = {slope_temperature:.2f}x + {intercept_temperature:.2f}")

    c.showPage()

    c.drawString(70, 700, "Datos de LDR:")
    # Ajustar la posición de los datos de LDR en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 600, "Datos ordenados de LDR:")
    for dato in arr_ordenate_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos

    # Ajustar la posición vertical después de mostrar los datos de LDR
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de LDR:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de LDR:")
    c.drawString(70, y_pos - 20, str(varianza_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de LDR:")
    c.drawString(70, y_pos - 20, str(media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar LDR:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo2, 2)))
    c.showPage()
    temp_filename = generar_graficaLDR(arr_sorted_campo2)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    c.showPage()

    # Agregar regresión lineal de LDR
    slope_ldr, intercept_ldr = calcular_regresion_lineal(range(len(arr_sorted_campo2)), arr_sorted_campo2)
    c.drawString(70, 700, "Regresión Lineal de LDR:")
    c.drawString(70, 680, f"Pendiente (Slope): {slope_ldr:.2f}")
    c.drawString(70, 660, f"Intercepto: {intercept_ldr:.2f}")
    c.drawString(70, 640, f"y = {slope_ldr:.2f}x + {intercept_ldr:.2f}")

    c.showPage()

    c.drawString(70, 700, "Datos de TDS:")
    # Ajustar la posición de los datos de TDS en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 600, "Datos ordenados de TDS:")
    for dato in arr_ordenate_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos

    # Ajustar la posición vertical después de mostrar los datos de TDS
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de TDS:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de TDS:")
    c.drawString(70, y_pos - 20, str(varianza_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de TDS:")
    c.drawString(70, y_pos - 20, str(media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar TDS:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo2, 2)))
    c.showPage()
    temp_filename = generar_graficaTDS(arr_sorted_campo2)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    c.showPage()

    # Agregar regresión lineal de TDS
    slope_tds, intercept_tds = calcular_regresion_lineal(range(len(arr_sorted_campo2)), arr_sorted_campo2)
    c.drawString(70, 700, "Regresión Lineal de TDS:")
    c.drawString(70, 680, f"Pendiente (Slope): {slope_tds:.2f}")
    c.drawString(70, 660, f"Intercepto: {intercept_tds:.2f}")
    c.drawString(70, 640, f"y = {slope_tds:.2f}x + {intercept_tds:.2f}")

    c.showPage()

    c.drawString(70, 700, "Datos de pH:")
    # Ajustar la posición de los datos de pH en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 600, "Datos ordenados de pH:")
    for dato in arr_ordenate_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos

    # Ajustar la posición vertical después de mostrar los datos de pH
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de pH:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de pH:")
    c.drawString(70, y_pos - 20, str(varianza_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de pH:")
    c.drawString(70, y_pos - 20, str(media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar pH:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo2, 2)))
    c.showPage()
    temp_filename = generar_graficaPH(arr_sorted_campo2)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    c.showPage()

    # Agregar regresión lineal de pH
    slope_ph, intercept_ph = calcular_regresion_lineal(range(len(arr_sorted_campo2)), arr_sorted_campo2)
    c.drawString(70, 700, "Regresión Lineal de pH:")
    c.drawString(70, 680, f"Pendiente (Slope): {slope_ph:.2f}")
    c.drawString(70, 660, f"Intercepto: {intercept_ph:.2f}")
    c.drawString(70, 640, f"y = {slope_ph:.2f}x + {intercept_ph:.2f}")

    c.showPage()

    c.drawString(70, 700, "Datos de DS18B20:")
    # Ajustar la posición de los datos de DS18B20 en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 600, "Datos ordenados de DS18B20:")
    for dato in arr_ordenate_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos

    # Ajustar la posición vertical después de mostrar los datos de DS18B20
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de DS18B20:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de DS18B20:")
    c.drawString(70, y_pos - 20, str(varianza_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de DS18B20:")
    c.drawString(70, y_pos - 20, str(media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar DS18B20:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo2, 2)))
    c.showPage()
    temp_filename = generar_graficaDS18B20(arr_sorted_campo2)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    c.showPage()

    # Agregar regresión lineal de DS18B20
    slope_ds18b20, intercept_ds18b20 = calcular_regresion_lineal(range(len(arr_sorted_campo2)), arr_sorted_campo2)
    c.drawString(70, 700, "Regresión Lineal de DS18B20:")
    c.drawString(70, 680, f"Pendiente (Slope): {slope_ds18b20:.2f}")
    c.drawString(70, 660, f"Intercepto: {intercept_ds18b20:.2f}")
    c.drawString(70, 640, f"y = {slope_ds18b20:.2f}x + {intercept_ds18b20:.2f}")

    c.showPage()

    c.save()

    return pdf_path
