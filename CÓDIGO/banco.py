#sistema bancario,
# el usuario debe: estar registrado y recordar su contraseña, tambien debe tener una opcion de recuperación de contraseña 
# condiciones: El usuario debe estar registrado y recordar su contraseña, opcion de recuperación de contraseña
registro = True
password = False
recuperar_contraseña = False 

print("""Bienvenido, seleccione una de las siguientes opciones: 
      1.Ingresar al sistema
      2.Recuperar contraseña 
      """)
a= int(input())

if a ==1:
    
    if registro == True and not  password ==True:
        print ("Bienvenido al sistema")
    else:
        print('su usuario o contraseña tiene un error')
elif a == 2:
    new_password = not recuperar_contraseña
    if new_password == True:
        print ('Se recupero la contraseña')
    else:
        print('Error seleccione una opción válida')
else:
    print('No válido')
