diccionario = {
                "GG": "Abreviacion de 'Good Game' tuviste una buena partida con alguien",
                "EZ": "Abreviacion del termino 'Easy' se usa para 'insultar' a alguien",
                "XD": "Algo muy gracioso, aprovado por la RAE como 'jajaja'",
                "LOL": "Lo mismo que XD, algo gracioso, pero en este caso se usa más por la comunidad inglesa"
    
                }
                
palabra = input("¿Sobre qué palabra tienes duda? ")

if palabra in diccionario.keys():
    print(diccionario[palabra])
else:
    print("Esta palabra no se encuentra en el diccionario.")
