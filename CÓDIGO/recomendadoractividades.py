#En la empresa que trabajas como programador, tu jefe de equipo te pide que desarrolles
#un programa en Python que recomiende actividades basandose en tres factores: clima,
#hora del dia y estado de animo del usuario, utilizando operadores logicos como and, or y
#not
"""Define tres variables:
• Clima: Puede ser “soleado”, “lluvioso” o “nublado”.
• Hora: Puede ser “mañana”, “tarde” o “noche”.
• Estado_animo: Puede ser “activo” o “relajado”."""

clima =['soleado','lluvioso','nublado']
hora= ['mañana', 'tarde', 'noche']
estado_animo = ['activo', 'relajado']
eleccion_clima= int(input("escribe:"))
eleccion_hora= int(input())
eleccion_animo= int(input())
a= clima[eleccion_clima]
b= hora[eleccion_hora]
c= estado_animo[eleccion_animo]

estado_animo= eleccion_animo


if (eleccion_clima== 0 or eleccion_clima == 2) and eleccion_animo == 0:
    print(' haz ejercicio')