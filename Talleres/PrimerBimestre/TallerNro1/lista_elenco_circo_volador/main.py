def crear_lista_reparto(file_name : str):
  lista_reparto = []
  #use with para abrir el nombre de archivo
  #utiliza la sintaxis del bucle for para procesar cada linea
  #y agrega el nombre del actor a lista_reparto

  with open(file_name) as file:
    actors_list = file.readlines()
    for actor_information in actors_list:
      lista_reparto.append(actor_information.split(',')[0])
  return lista_reparto

cast_list = crear_lista_reparto('reparto_circo_volador.txt')

print("Lista de actores: ")
for actor in cast_list:
  print(actor)