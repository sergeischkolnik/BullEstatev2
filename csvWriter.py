import csv
import uf

def writeCsv(file, data, columnnames, operacion):

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
            rent = int(rent*1000)
            rent = float(rent/1000)
            rentS = str(rent).replace('.',',')
            prop[index] = rentS

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

        if "Distancia metro" in columnnames:
            index = columnnames.index("Distancia metro")
            prop[index] = int(prop[index])


    with open(file, 'w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columnnames)
        for row in data:
            writer.writerow(row)

def writeCsvCanje(file, data, columnnames, operacion):

    data = [list(elem) for elem in data]

    #creacion de precios, porcentajes y link
    for i,prop in enumerate(data):

        #arreglar precio
        precio = prop[0]
        if operacion=="venta":
            unf=uf.getUf()
            precio=precio/unf
            precio=int(precio)
            precioStr = str(precio)
        else:

            precioStr = str(precio)

        prop[0] = precioStr
        ufn=uf.getUf()
        #quitar decimales a valores
        prop[1] = int(prop[1])
        prop[2] = int(prop[2])
        prop[3] = int(prop[3])
        prop[4] = int(prop[4])
        prop[5] = int(prop[5])

    with open(file, 'w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columnnames)
        for row in data:
            writer.writerow(row)