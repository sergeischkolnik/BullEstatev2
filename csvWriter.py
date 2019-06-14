import csv
import uf

def writeCsv(file, data, columnnames, operacion):

    data = [list(elem) for elem in data]

    #creacion de precios, porcentajes y link
    for i,prop in enumerate(data):
        #porcentaje
        rent = float(prop[9])
        rent = int(rent*1000)
        rent = float(rent/10)
        prop[9] = rent
        if (operacion=="venta"):
            rent = float(prop[11])
            rent = int(rent*1000)
            rent = float(rent/10)
            prop[11] = rent

        #arreglar precio
        precio = prop[0]
        if operacion=="venta":
            unf=uf.getUf()
            precio=precio/unf
            precio=int(precio)
            precioStr =  format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr = precioStr.replace(",",".")
        else:
            precioStr = format(precio, ',.2f')
            precioStr = precioStr[:-3]
            precioStr = str(precioStr)

        prop[0] = precioStr
        ufn=uf.getUf()
        #quitar decimales a valores
        prop[1] = int(prop[1])
        prop[2] = int(prop[2])
        prop[3] = int(prop[3])
        prop[4] = int(prop[4])
        prop[5] = int(prop[5])
        prop[7] = int(prop[7])

        if (operacion=="venta"):
            prop[8] = int(prop[8]/ufn)
            prop[8] = format(prop[8], ',.2f')
            prop[8] =prop[8][:-3]
            prop[8] = str(prop[8])
            prop[10] = int(prop[10])
            prop[10] = format(prop[10], ',.2f')
            prop[10] =prop[10][:-3]
            prop[10] =str(prop[10])


        else:

            prop[8] = int(prop[8])
            prop[8] = format(prop[8], ',.2f')
            prop[8] =prop[8][:-3]
            prop[8] =str(prop[8])


    with open(file, 'w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columnnames)
        for row in data:
            writer.writerow(row)
