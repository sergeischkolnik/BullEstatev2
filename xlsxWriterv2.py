import uf
import xlsxwriter

def writeXlsx(file, data, columnnames, operacion):
    unf = uf.getUf()
    data = [list(elem) for elem in data]

    #creacion de precios, porcentajes y link
    for i,prop in enumerate(data):



        #arreglar precio
        precio = prop[1]

        #venta
        if operacion=="venta":
            precio=precio/unf
            precio=int(precio)
            prop[1] = precio

            if "Pr. Venta Tasado" in columnnames:
                index = columnnames.index("Pr. Venta Tasado")
                precio2 = prop[index]/unf
                precio2 = int(precio2)
                prop[index] = precio2

        #arriendo
        else:

            if "Pr. Arriendo Tasado" in columnnames:
                index = columnnames.index("Pr. Arriendo Tasado")
                precio2 = int(prop[index])
                prop[index] = precio2

        #quitar decimales a valores
        if "Utiles" in columnnames:
            index = columnnames.index("Utiles")
            prop[index] = int(prop[index])

        if "Total" in columnnames:
            index = columnnames.index("Total")
            prop[index] = int(prop[index])

        if "Estac." in columnnames:
            index = columnnames.index("Estac.")
            prop[index] = int(prop[index])

        if "Bod." in columnnames:
            index = columnnames.index("Bod.")
            prop[index] = int(prop[index])

        if "Dist metro" in columnnames:
            index = columnnames.index("Dist metro")
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

    # Add a date format
    date = workbook.add_format({'num_format': 'dd/mm/yy'})

    # Write some data headers.
    worksheet.write_row(row=0,col=0,data=columnnames,cell_format=bold)

    #encontrar indices
    index_r_v = columnnames.index("Rent. Venta") if "Rent. Venta" in columnnames else -1
    index_r_a = columnnames.index("Rent. Arriendo") if "Rent. Arriendo" in columnnames else -1


    index_precio = columnnames.index("Precio") if "Precio" in columnnames else -1
    index_precio_a_t = columnnames.index("Pr. Arriendo Tasado") if "Pr. Arriendo Tasado" in columnnames else -1
    index_fecha_e = columnnames.index("fecha encontrado") if "fecha encontrado" in columnnames else -1
    index_metro = columnnames.index("Metro") if "Metro" in columnnames else -1
    index_link = columnnames.index("Link") if "Link" in columnnames else -1
    index_mail = columnnames.index("Mail") if "Mail" in columnnames else -1
    index_tel = columnnames.index("Telefono") if "Telefono" in columnnames else -1
    index_obs = columnnames.index("Observaciones") if "Observaciones" in columnnames else -1

    #ancho de columnas
    length_list = [len(x) for x in columnnames]
    for i, width in enumerate(length_list):
        worksheet.set_column(i, i, width+2)
    if index_metro!=-1:
        worksheet.set_column(index_metro, index_metro, 15)
    if index_link!=-1:
        worksheet.set_column(index_link, index_link, 10)
    if index_mail!=-1:
        worksheet.set_column(index_mail, index_mail, 30)
    if index_tel != -1:
        worksheet.set_column(index_tel, index_tel, 15)
    if index_obs != -1:
        worksheet.set_column(index_obs, index_obs, 50)



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

            #caso fechas
            elif j==index_fecha_e:
                worksheet.write(i + 1, j, f, date)

            else:
                worksheet.write(i+1, j, f)

    print('xlsx creado')
    workbook.close()


