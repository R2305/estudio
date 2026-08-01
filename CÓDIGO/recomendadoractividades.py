#En la empresa que trabajas como programador, tu jefe de equipo te pide que desarrolles
#un programa en Python que recomiende actividades basandose en tres factores: clima,
#hora del dia y estado de animo del usuario, utilizando operadores logicos como and, or y
#not
"""Define tres variables:
• Clima: Puede ser “soleado”, “lluvioso” o “nublado”.
• Hora: Puede ser “mañana”, “tarde” o “noche”.
• Estado_animo: Puede ser “activo” o “relajado”."""

c =['soleado','lluvioso','nublado'] #c = clima 
h= ['mañana', 'tarde', 'noche'] # h = hora
ea = ['activo', 'relajado'] # ea = estado_animo

clima= int(input("""elige una opcion: 
                 0.soleado
                 1.lluvioso
                 2.nublado\n"""))
hora= int(input("""elige una opcion:
                 0.mañana
                 1.tarde
                 2.noche\n"""))
animo= int(input("""elige una opcion:
                 0.activo
                 1.relajado\n"""))



opcion_impresa= False


if (clima== 0 or clima == 2) and animo == 0 and hora !=2:
    print(' haz ejercicio')
    opcion_impresa = True

if (clima == 1 or clima == 2) and animo !=0:
    print('lee un libro')
    opcion_impresa = True

if (hora == 2 and animo ==0) and clima == 2:
    print('escucha musica animada')
    opcion_impresa = True
if hora ==2 and animo ==1:
    print('meditar')
    opcion_impresa = True

if not opcion_impresa:
    print('ve una pelicula o una serie')