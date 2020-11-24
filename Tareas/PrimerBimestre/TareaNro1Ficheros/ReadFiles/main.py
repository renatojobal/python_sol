# Parte 1
# with open('message.txt','r') as file:
#  print(file.read())
#    
  
# Parte 2
# with open('alice.txt','r') as file:
#   (file.read())


# Parte 2
#with open('alice.txt','r') as file:
#  line_counter = 0
#  for line in file:
#    print(line, end="")
#    
#    if (line_counter != 0) and (line_counter % 20 == 0) :
#      continuar = input("\n------\n\tPresione 'Enter' para continuar ->")
#    
#    line_counter += 1
#

# Parte 3

words_to_change = {
  "Alice":"Bob", 
  "She":"He", 
  "Her":"His", 
  "Herself":"Himself", 
  "she":"he",
  "her":"his", 
  "herself":"himself",
  "Lewis":"Renato",
  "Carroll":"Balcazar"
}

with open('alice.txt','r') as file:
  line_counter = 0
  for line in file:
    for word in words_to_change:
      line = line.replace(word, words_to_change[word]) # Esta linea reemplaza las palabras del direccionario por sus valores en el mismo
    print(line, end="")
    
    if (line_counter != 0) and (line_counter % 20 == 0) :
      continuar = input("\n------\n\tPresione 'Enter' para continuar ->")
    
    line_counter += 1
