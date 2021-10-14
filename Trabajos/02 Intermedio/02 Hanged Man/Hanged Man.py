import os
import random as rd

def run():
    # Creación de las variables generales:
    real_name = name_gen() #Se invoca la función para la generación de nombres
    lifes = 6
    guess_list = [' - ' for i in range(len(real_name))]
    guess_clone = guess_list
    rag = {i : open('./files/bodies/{}.txt'.format(str(i)),'r').read() for i in range(7)} # Creación de diccionario con ahorcados

    # Código para jugar al ahorcado 

    while lifes > 0:
        
        os.system('clear') 
        print(open('./files/menu.txt','r',encoding='utf-8').read())
        print(rag[lifes])
        print(''.join(guess_list))
        guessed_char = user_guess()
        
        for i in range(len(real_name)):
            if real_name[i] == guessed_char:
                guess_clone[i] = guessed_char

        if guess_list == guess_clone:
            input("¡Fallaste! Pierdes una vida 😜 \n Presiona Enter para continuar:")
            lifes = lifes - 1

        else:
            input("¡Correcto! Sigue así 😎 \n Presiona Enter para continuar:")
            guess_list = guess_clone
    
    if real_name == guess_list:
        print("¡Ganaste! ✨ \n La palabra era: "+real_name)
    else:
        print("¡Perdiste! 👻 \n La palabra era: "+real_name)
        print(rag[lifes])
    
# Función que genera el nombre a adivinar:
def name_gen():
    f = open('./files/names.txt','r',encoding='utf-8')
    n = [line for line in f]
    n = rd.choice(n)
    return n

# Función que captura la sílaba jugada por el usuario
def user_guess():
    c = ''
    while len(c) == 0:
        c = input("Por favor, adivinar una sílaba de la palabra:"+'\n')
        # Se ejecuta un control para validar los campos ingresados:

        if len(c) > 1:
            input("¡Solo debes ingresar un caracter! 😒"+'\n'+'Presionar "Enter" para continuar')
            c = ''
            continue

        elif c.isnumeric():
            input("¡No están admitidos los números! 😒"+'\n'+'Presionar "Enter" para continuar')
            c = ''
            continue
            
        elif c == '':
            input("¡Debes llenar al menos un caracter! 😒"+'\n'+'Presionar "Enter" para continuar')
            c = ''
            continue
            
        else:
            return c

if __name__ == '__main__':
    run()