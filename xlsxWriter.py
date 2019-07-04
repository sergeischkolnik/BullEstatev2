import uf
import xlsxwriter

def writeXlsx(file, data, columnnames, operacion):

    data = [list(elem) for elem in data]

    #creacion de precios, porcentajes y link
    for i,prop in enumerate(data):
        #porcentaje
        if "Rentabilidad Venta" in columnnames:
            index = columnnames.index("Rentabilidad Venta")
            rent = float(prop[index])
            rent = int(rent*1000)
            rent = float(rent/1000)
            rentS = str(rent).replace('.',',')
            prop[index] = rentS
        if "Rentabilidad Arriendo" in columnnames:
            index = columnnames.index("Rentabilidad Arriendo")
            rent = float(prop[index])

        unf = uf.getUf()

        #arreglar precio
        precio = prop[0]

        #venta
        if operacion=="venta":
            precio=precio/unf
            precio=int(precio)
            precioStr =  format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr = precioStr.replace(",",".")

            if "Precio Venta Tasado" in columnnames:
                index = columnnames.index("Precio Venta Tasado")
                precio2 = prop[index]/unf
                precio2 = int(precio2)
                precioStr2 = format(precio2, ',.2f')
                precioStr2 = precioStr2[:-3]
                precioStr2 = precioStr2.replace(",", ".")
                prop[index] = precioStr2

        #arriendo
        else:
            precioStr = format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr = str(precioStr)
            if "Precio Arriendo Tasado" in columnnames:
                index = columnnames.index("Precio Arriendo Tasado")
                precio2 = int(prop[index])
                precioStr2 = format(precio2, ',.2f')
                precioStr2 = precioStr2[:-3]
                prop[index] = precioStr2

        prop[0] = precioStr

        #quitar decimales a valores
        if "Utiles" in columnnames:
            index = columnnames.index("Utiles")
            prop[index] = int(prop[index])

        if "Total" in columnnames:
            index = columnnames.index("Total")
            prop[index] = int(prop[index])

        if "Estacionamientos" in columnnames:
            index = columnnames.index("Estacionamientos")
            prop[index] = int(prop[index])

        if "Bodegas" in columnnames:
            index = columnnames.index("Bodegas")
            prop[index] = int(prop[index])

        if "Distancia metro" in columnnames:
            index = columnnames.index("Distancia metro")
            prop[index] = int(prop[index])


    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Add a number format for cells with money.
    money = workbook.add_format({'num_format': '$#,##0'})

    # Add a number format for cells with percentage
    perc = workbook.add_format({'num_format': '0.0%'})

    # Write some data headers.
    worksheet.write_row(row=0,col=0,data=columnnames,cell_format=bold)

    #encontrar indices de rentabilidad y arriendo
    index_r_v = columnnames.index("Rentabilidad Venta") if "Rentabilidad Venta" in columnnames else -1
    index_r_a = columnnames.index("Rentabilidad Arriendo") if "Rentabilidad Arriendo" in columnnames else -1
    index_precio = columnnames.index("Precio") if "Precio" in columnnames else -1
    index_precio_a_t = columnnames.index("Precio Arriendo Tasado") if "Precio Arriendo Tasado" in columnnames else -1

    # Iterate over the data and write it out row by row.
    for i,c in enumerate(data):
        for j,f in enumerate(c):
            #caso rentabilidad venta y arriendo
            if j==index_r_v:
                worksheet.write(i + 1, j, f, perc)
            elif j==index_r_a:
                worksheet.write(i + 1, j, f, perc)

            #caso precios
            elif j==index_precio and operacion=="arriendo":
                worksheet.write(i + 1, j, f, money)
            elif j==index_precio_a_t:
                worksheet.write(i + 1, j, f, money)

            else:
                worksheet.write(i+1, j, f)


    workbook.close()


