
continue_running = True


def save_todo_list(todo_list : list):
  """
  Main function to save elements into a file
  @param: todo_list list to save
  """
  file_name = str(input("Ingrese el nombre del archivo con la extension .txt:\n"))

  
  correct_extension = False
  while not correct_extension:
    
    if file_name[-4:] == '.txt':
      correct_extension = True
    else:
      file_name = str(input("El nombre del archivo debe terminar con .txt.\nIntente de nuevo:\n"))

  # Save the todo list into the file
  file = open(file_name, 'a')
  
  for element in todo_list:
    file.write(element+"\n")
  
  file.close()
  print("Archivo guardado con éxito")
  
  

# Initialize an empty list
todo_list = []


while continue_running:
  
  todo = str(input("Ingrese una tarea a realizar (Escriba 'detener' para guardar): \n"))
  
  
  if todo == 'detener':
    continue_running = False
    
    # Here we call the main function to save the elements into a file
    save_todo_list(todo_list)
    
    break
    
  
  todo_list.append(todo)
  
  
  

  
  
  
  
  
  
