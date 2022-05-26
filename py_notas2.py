import xml.etree.ElementTree as ET
tree = ET.parse('notas.xml')
root = tree.getroot()

continuar = True

while continuar == True:
    print('Presiona: \n1 si quieres crear una nueva nota; \n2 si quieres ver todas las notas por pantalla; \n3 para modificar una nota; \n4 para mostrar una nota concreta; \nCualquier otra tecla para salir:')
    accion = input()
    if accion == "1":
        posicion = len(root)
        id = posicion+1
        print('Introduce: \n1 si es un recordatorio \n2 si es una nota manuscrita \n3 si es una lista-')
        tipo = input()
        if tipo == "1":
            attrib = {'id': str(id)}
            element = root.makeelement('nota', attrib)
            root.append(element)

            attrib = {}
            ET.SubElement(root[posicion], 'id', attrib)
            root[posicion][0].text = str(id)

            attrib = {}
            ET.SubElement(root[posicion], 'tipo', attrib)
            root[posicion][1].text = 'Recordatorio'

            print('Introduce la fecha a recordar: ')
            fecha = input()
            attrib = {}
            ET.SubElement(root[posicion], 'fecha', attrib)
            root[posicion][2].text = fecha

            print('Introduce el tema: ')
            tema = input()
            attrib = {}
            ET.SubElement(root[posicion], 'tema', attrib)
            root[posicion][3].text = tema

            tree.write('notas.xml')
            print("El id de tu nota es: ", end=f"{id}")
            print(". Guárdalo para futuras consultas y modificaciones.")

        elif tipo == "2":
            attrib = {'id': str(id)}
            element = root.makeelement('nota', attrib)
            root.append(element)

            attrib = {}
            ET.SubElement(root[posicion], 'id', attrib)
            root[posicion][0].text = str(id)

            attrib = {}
            ET.SubElement(root[posicion], 'tipo', attrib)
            root[posicion][1].text = 'Manuscrita'

            print('Introduce una url o ruta a una imagen: ')
            imagen = input()
            attrib = {}
            ET.SubElement(root[posicion], 'imagen', attrib)
            root[posicion][2].text = imagen

            print('Introduce el comentario: ')
            comentario = input()
            attrib = {}
            ET.SubElement(root[posicion], 'tipo', attrib)
            root[posicion][3].text = comentario
            

            tree.write('notas.xml')
            print("El id de tu nota es: ", end=f"{id}")
            print(". Guárdalo para futuras consultas y modificaciones.")

        elif tipo == "3":
            attrib = {'id': str(id)}
            element = root.makeelement('nota', attrib)
            root.append(element)

            attrib = {}
            ET.SubElement(root[posicion], 'id', attrib)
            root[posicion][0].text = str(id)

            attrib = {}
            ET.SubElement(root[posicion], 'tipo', attrib)
            root[posicion][1].text = 'Lista'

            print('¿Cuántos elementos deseas introducir?')
            numero = int(input())
            for i in range(2,numero+2):
                print('Introduce el dato:')
                dato = input()
                attrib = {'id':str(i-1)}
                ET.SubElement(root[posicion], 'elemento', attrib)
                root[posicion][i].text = dato

            tree.write('notas.xml')
            print("El id de tu nota es: ", end=f"{id}")
            print(". Guárdalo para futuras consultas y modificaciones.")

    elif accion == "2":
        print('Todas las notas tras sus ids:')
        for elem in root:
            for subelem in elem:
                print(subelem.text)
    elif accion == "3":
        encontrado = False
        print('Introduce el id de la nota a modificar: ')
        idNota = input()
        for elem in root:
            if elem.get('id') == idNota:
                encontrado = True
                if elem.find('tipo').text == 'Recordatorio':
                    print('Introduce campo a modificar (fecha o tema): ')
                    campo = input()
                    if campo == 'fecha':
                        print('Introduce nueva fecha: ')
                        nFecha = input()
                        elem.find('fecha').text = nFecha
                    elif campo == 'tema':
                        print('Introduce el nuevo tema: ')
                        nTema = input()
                        elem.find('tema').text = nTema
                    else:
                        print('Campo incorrecto.')
                elif elem.find('tipo').text == 'Manuscrita':
                    print('Introduce campo a modificar (imagen o comentario): ')
                    campo = input()
                    if campo == 'imagen':
                        print('Introduce nueva imagen: ')
                        nImagen = input()
                        elem.find('imagen').text = nImagen
                    elif campo == 'comentario':
                        print('Introduce el nuevo comentario: ')
                        nComentario = input()
                        elem.find('comentario').text = nComentario
                    else:
                        print('Campo incorrecto.')
                elif elem.find('tipo').text == 'Lista':
                    print("Introduce el número del elemento a modificar: ")
                    numElem = input()
                    for sub in elem:
                        if sub.get('id') == numElem:
                            print('Introduce el nuevo elemento: ')
                            newElem = input()
                            sub.text = newElem
                        else:
                            print('Elemento no encontrado.')
                tree.write('notas.xml')

        if encontrado == False:
            print('Id no encontrado.')

    elif accion == "4":
        encontrado = False
        print('Introduce el id de la nota que deseas ver: ')
        nota = input()
        for elem in root:
            if elem.get('id') == nota:
                encontrado = True
                for subelem in elem: 
                    print(subelem.text)
        if encontrado == False:
            print('Id no encontrado.')
    else:
        continuar = False
else: print('Hasta la próxima!')


