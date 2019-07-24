def main():
    estadosMain=['inicial']
    estadosCanjeador=['inicial','operacion','tipo','region','comuna','preciomin','preciomax','utilmin','utilmax','terraza','dormitorios','banos','estacionamientos','bodegas','confirmar']
    estadosFicha=['inicial','portal','id','confirmar']

    comunasMetropolitana=[
"buin",
"calera de tango",
"cerrillos",
"cerro navia",
"colina",
"conchalí",
"el bosque",
"el monte",
"estación central",
"huechuraba",
"independencia",
"la cisterna",
"la florida",
"la granja",
"la pintana",
"la reina",
"lampa",
"las condes",
"lo barnechea",
"lo espejo",
"lo prado",
"macul",
"maipú",
"melipilla",
"padre hurtado",
"paine",
"pedro aguirre cerda",
"peñaflor",
"peñalolén",
"pirque",
"providencia",
"pudahuel",
"puente alto",
"quilicura",
"quinta normal",
"recoleta",
"renca",
"san bernardo",
"san joaquín",
"san miguel",
"san pedro",
"san ramón",
"santiago",
"talagante",
"tiltil",
"vitacura",
"ñuñoa"]

    print(len(comunasMetropolitana))

if __name__ == '__main__':
    main()
