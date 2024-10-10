
# from csv import reader, writer, DictReader,  DictWriter

# #funcion reader

# with open("a.csv", "r") as file:
#   lector = reader(file) # se convienre en un iterable
#   for row in lector:
#     print(row)

# #funcion writer
# # myData = [
# #   ["firstName","secondName","Grade"],
# #   ["Alex","Dodoy","2"],
# #   ["Carlos","De la  torre","2"],
# # ]

# # myFile = open("personas.csv", "w", newline= '')

# # while myFile:
# #   escritor = writer(myFile)
# #   escritor.writerows(myData)

# # Funcion DisctReader()
# with open('ventas_semana_pasada.csv') as f:
#   DictReader_obj = DictReader(f)
#   for item in DictReader_obj:
#     print(item['DIA'])

# #Funcion DisctWriater()

# def writer_reservations(f,reservations,headers):
#   with open(f,"w",newline='') as f2:
#     writer =DictWriter(f2, fieldnames= headers)
#     if headers:
#       writer.writeheader()
#     for reservation in reservations:
#       writer.writerow({
#         'availability_zone':reservation['availability_zone'],
#         'tenancy': reservation['tenancy'],
#         'product': reservation['product'],
#         'cost_hourly': reservation['cost_hourly'],
#         'cost_upfront': reservation['cost_upfront'],
#         'count': reservation['count'],
#         'count_used': reservation['count_used'],
#       })
# headers = [
# 'availability_zone',
# 'tenancy',
# 'product',
# 'cost_hourly',
# 'cost_upfront',
# 'count',
# 'count_used',
# ]
# reservations = [
# {'availability_zone': 2,
# 'tenancy': 3,
# 'product': 1,
# 'cost_hourly': 3500,
# 'cost_upfront': 4800,
# 'count': 45,
# 'count_used': 1,
# },{'availability_zone': 3,
# 'tenancy': 3,
# 'product': 4,
# 'cost_hourly': 3700,
# 'cost_upfront': 5800,
# 'count': 25,
# 'count_used': 13,
# }
# ]
# writer_reservations("reservations.csv", reservations, headers)


# ir la diapositiva

import json

#abrir y leer un JSON file

# file = open("object.json")
# users = json.load(file)

# for user in users:
#  print("nombre del usuario:", user["name"], ",edad:", user["age"])
#  file.close()

#========================================================================================= 

 #guardar un archivo json

dicctionary = [
    { 
        "table": 12,
        "chair": 14,
        "id": 567
        },{
        "table": 44,
        "chair": 10,
        "id": 56
    }
]


# Pasamos el diccionario a objeto tipo json
things = json.dumps(dicctionary)                      # convercion de un diccionadio a un objeto JSON


# usamos open para abrir el archivo o para generarlo si no existe y abrirlo
file =  open("things.json", "w") 


# Escribimos sobre todo el archivo
file.write(things)


# Cerramos el archivo
file.close()

