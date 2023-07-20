from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import os
from reportlab.lib.pagesizes import letter
import  tempfile
from flask import current_app
def generar_graficaHumidity(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    
    
    plt.xlabel('Time')
    plt.ylabel('Humidity')
    plt.title('Humidity')
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
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaWaterTem(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Time')
    plt.ylabel('Water temperature')
    plt.title('Water temperature')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaLight(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Time')
    plt.ylabel('Light')
    plt.title('Luminous intensity')
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
    plt.xlabel('Time')
    plt.ylabel('pH')
    plt.title('PH')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaConduc(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Time')
    plt.ylabel('Conductivity')
    plt.title('Conductivity')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_pdf(table_frecuency_campoTemperature,table_frecuency_campoHumidity,table_frecuency_campoWaterTem, table_frecuency_campoLight,table_frecuency_campoPH,table_frecuency_campoConduc,
        arr_sorted_campoTemperature, desviacion_media_campoTemperature, varianza_campoTemperature, media_campoTemperature, desviacion_estandar_campoTemperature, arr_ordenate_campoTemperature, 
        arr_ordenate_campoHumidity, desviacion_media_campoHumidity, media_campoHumidity, varianza_campoHumidity, desviacion_estandar_campoHumidity, arr_sorted_campoHumidity, pdf_filename,
        desviacion_media_campoWaterTemp, media_campoWaterTemp, varianza_campoWaterTemp, desviacion_estandar_campoWaterTemp, arr_ordenate_campoWaterTemp, arr_sorted_campoWaterTemp,
        desviacion_media_campoLight, media_campoLight, varianza_campoLight, desviacion_estandar_campoLight, arr_ordenate_campoLight, arr_sorted_campoLight,
        desviacion_media_campoPH, media_campoPH, varianza_campoPH, desviacion_estandar_campoPH, arr_ordenate_campoPH, arr_sorted_campoPH, 
        desviacion_media_campoConduc, media_campoConduc, varianza_campoConduc, desviacion_estandar_campoConduc, arr_ordenate_campoConduc, arr_sorted_campoConduc,
        moda_campoTemperature,moda_campoHumidity, moda_campoWaterTemp,moda_campoLight,moda_campoPH, moda_campoConduc):

    table_frecuency_campoTemperature.to_string(index=False)
    table_frecuency_campoHumidity.to_string(index=False)
    table_frecuency_campoWaterTem.to_string(index=False)
    table_frecuency_campoLight.to_string(index=False)
    table_frecuency_campoPH.to_string(index=False)
    table_frecuency_campoConduc.to_string(index=False)

    public_folder = current_app.static_folder
    # Generar la ruta completa del archivo PDF en la carpeta 'Public'
    pdf_filename = 'ReporteDevly_Hydro.pdf'
    pdf_path = os.path.join(public_folder, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(70, 700, "Datos de Humedad:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campoHumidity:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
        # Espacio adicional antes de la desviación media
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 580, "Datos ordenados de Humedad:")
    for dato in arr_ordenate_campoHumidity:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos

    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Humedad:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campoHumidity))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Humedad:")
    c.drawString(70, y_pos - 20, str(varianza_campoHumidity))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Humedad:")
    c.drawString(70, y_pos - 20, str(media_campoHumidity))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar humedad:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campoHumidity,2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Humedad:")
    c.drawString(70, y_pos - 20, str(moda_campoHumidity))
    c.showPage()
    temp_filename = generar_graficaHumidity(arr_sorted_campoHumidity)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Frecuency table")
    y_start -= line_height

    column_headers = table_frecuency_campoHumidity.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campoHumidity.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()
    #Temperatura
    c.drawString(70, 700, "Datos de Temperatura:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campoTemperature:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 580, "Datos ordenados de Temperatura:")
    for dato in arr_ordenate_campoTemperature:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Temperatura:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campoTemperature))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Temperatura:")
    c.drawString(70, y_pos - 20, str(varianza_campoTemperature))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Temperatura:")
    c.drawString(70, y_pos - 20, str(media_campoTemperature))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Temperatura:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campoTemperature, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Temperatura:")
    c.drawString(70, y_pos - 20, str(moda_campoTemperature))
    c.showPage()
    temp_filename = generar_graficaTemperature(arr_sorted_campoTemperature)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    os.remove(temp_filename)
    #Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias Temperatura")
    y_start -= line_height

    column_headers = table_frecuency_campoTemperature.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campoTemperature.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()

    c.drawString(70, 700, "Datos de Temperatura del agua:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campoWaterTemp:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 580, "Datos ordenados de Water Temperature:")
    for dato in arr_ordenate_campoWaterTemp:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Water Temperature:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campoWaterTemp))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Water Temperature:")
    c.drawString(70, y_pos - 20, str(varianza_campoWaterTemp))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Water Temperature:")
    c.drawString(70, y_pos - 20, str(media_campoWaterTemp))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Water Temperature:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campoWaterTemp, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Water Temperature:")
    c.drawString(70, y_pos - 20, str(moda_campoWaterTemp))
    c.showPage()
    temp_filename = generar_graficaWaterTem(arr_sorted_campoWaterTemp)
    c.drawImage(temp_filename, 90, 400, width=400, height=300)
    os.remove(temp_filename)
    # Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias Water Temperature")
    y_start -= line_height

    column_headers = table_frecuency_campoWaterTem.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campoWaterTem.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()

    # CO2
    c.drawString(70, 700, "Datos de Intensidad luminica:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campoLight:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 560, "Datos ordenados de luminous intensity:")
    for dato in arr_ordenate_campoLight:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de luminous intensity:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campoLight))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de luminous intensity:")
    c.drawString(70, y_pos - 20, str(varianza_campoLight))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de luminous intensity:")
    c.drawString(70, y_pos - 20, str(media_campoLight))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar luminous intensity:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campoLight, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda luminous intensity:")
    c.drawString(70, y_pos - 20, str(moda_campoLight))
    c.showPage()
    temp_filename = generar_graficaLight(arr_sorted_campoLight)
    c.drawImage(temp_filename, 90, 400, width=400, height=300)
    os.remove(temp_filename)
    # Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias luminous intensity")
    y_start -= line_height

    column_headers = table_frecuency_campoLight.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campoLight.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()
    #Altitude
    c.drawString(70, 700, "Datos de pH:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campoPH:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    y_pos -= 40  # Espacio adicional antes de la desviación media
    y_pos = 560  # Ajustar la posición vertical para comenzar la tabla de datos ordenados de Altitud
    max_width = 500
    line_height = 30  # Aumentar el espacio vertical entre líneas
    font_size = 12  # Aumentar el tamaño de la fuente

    c.setFont("Helvetica", font_size)  # Configurar el tamaño de la fuente
    arr_sorted_campoPH.sort()
    c.drawString(70, y_pos, "Datos ordenados de pH:")
    for dato in arr_sorted_campoPH:
        dato_redondeado = round(dato, 2)  # Redondear el dato a dos decimales
        text_width = c.stringWidth(str(dato_redondeado), "Helvetica", font_size)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= line_height  # Saltar a la siguiente línea con el nuevo espacio vertical
        c.drawString(x_pos, y_pos, str(dato_redondeado))
        x_pos += text_width + 10  # Reducir el espaciado horizontal entre datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de pH:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campoPH))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de pH:")
    c.drawString(70, y_pos - 20, str(varianza_campoPH))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de pH:")
    c.drawString(70, y_pos - 20, str(media_campoPH))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar pH:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campoPH, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda pH:")
    c.drawString(70, y_pos - 20, str(moda_campoPH))
    c.showPage()
    temp_filename = generar_graficaPH(arr_sorted_campoPH)
    c.drawImage(temp_filename, 90, 400, width=400, height=300)
    os.remove(temp_filename)
    # Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias pH")
    y_start -= line_height

    column_headers = table_frecuency_campoPH.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campoPH.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height
        
    c.showPage()
    
        #Temperatura
    c.drawString(70, 700, "Datos de Conductivity:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campoConduc:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 580, "Datos ordenados de Conductivity:")
    for dato in arr_ordenate_campoConduc:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Conductivity:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campoConduc))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Conductivity:")
    c.drawString(70, y_pos - 20, str(varianza_campoConduc))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Conductivity:")
    c.drawString(70, y_pos - 20, str(media_campoConduc))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Conductivity:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campoConduc, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Conductivity:")
    c.drawString(70, y_pos - 20, str(moda_campoConduc))
    c.showPage()
    temp_filename = generar_graficaConduc(arr_sorted_campoConduc)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    os.remove(temp_filename)
    #Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias Conductivity")
    y_start -= line_height

    column_headers = table_frecuency_campoConduc.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campoConduc.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height



    c.save()

    return pdf_path