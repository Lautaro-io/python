import random
import time 
import io
import asyncio
import pyttsx3
import pygame
import shutil
import os
import threading 

##ACLARACIONES
#Para correr el juego es necesario instalar en consola las librerias pygame y pyttsx3 con un pip install nombre_libreria . 

global limpiar_consola
limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
nombre = ""

global miedo
miedo = 0
global objetos_random
objetos_random = ["paquete de cigarrillos", "Frasco", "Diario", "Jeringa", "Cuchillo ensangrentado", "Muñeca", "Reloj", "Máscara", "Radio", "ouija", "Collar", "Ojo", "Manchas", "Dientes", "muñeco budu", "carta", "un pajaro podrido", "cucarachas", "veneno"]

inventario = []

def encontrar_objeto(objeto):
    global inventario 
    return inventario.append(objeto)
    



#Inicializador de motor de voz. 

engine = pyttsx3.init()
voices=  engine.getProperty('voices')
engine.setProperty('voice', voices[3].id) # los [ numero] se deben cambiar acuerdo a las necesidades de su sistema, si su lenguaje predeterminado es distinto al espaniol debera ajustar el numero 
engine.setProperty('language', 'es')
engine.setProperty('rate', 190)     # Velocidad de habla (palabras por minuto)
engine.setProperty('volume', 0.9)
engine.runAndWait()


#Iniciamos la musica especificando la ruta. 
pygame.init()
# Ruta del archivo de música
ruta_musica = "fondo.mp3"

# #Iniciar la reproducción de la música de fondo
pygame.mixer.music.load(ruta_musica)
pygame.mixer.music.play(-1)
pygame.mixer_music.set_volume(0.1)
engine = pyttsx3.init()

#cambiar el color de las letras de la consola
os.system("color 0" + "5") 
# os.system('mode con: cols=60 lines=30')

consola_ancho = shutil.get_terminal_size().columns

def animacion(texto, velocidad=0.1):
    
    for letra in texto:
        print(letra,end="", flush=True)
        time.sleep(velocidad)


def centrar_texto(texto):

    consola_ancho = shutil.get_terminal_size().columns

    espacios = (consola_ancho - len(texto)) // 2
    texto_centralizado = ' ' * espacios + texto
        
    return texto_centralizado



def primera_decision():
    global nombre 
    global miedo    # Volumen (0.0 a 1.0)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(centrar_texto("   /             (__)             \\")   )
    print(centrar_texto("                  ,%;,"))
    print(centrar_texto("                  ,%%,"))
    print(centrar_texto("    ______________)(______________"))
    print(centrar_texto("   /     [----  '{}']             \\"))
    print(centrar_texto("  /________________________________\\"))
    print(centrar_texto("  [________________________________]"))
    print(centrar_texto("     \\ \\  / /            \\ \\  / /"))
    print(centrar_texto("      \\ \\/ /              \\ \\/ /"))
    print(centrar_texto("      _\\/ /________________\\ \\/_"))
    print(centrar_texto("     [_/o/__________________\\o\\_]"))
    print(centrar_texto("      / /\\ \\              / /\\ \\"))
    print(centrar_texto("     lc/  \\_\\            /_/  \\_\\"))
    print("")
    print("")
    print("")
    print("")
    print(f"{nombre} encuentra una linterna..")
    print("Linterna se ha agregado a tu inventario. ")
    engine.say(f"{nombre} encuentra una linterna..")
    engine.say("1 -- Presiona 1 para prender linterna. Presiona 2 para Seguir en la oscuridad")
    engine.runAndWait()
    encontrar_objeto("linterna")
    opcion = int(input("1 -- Prender linterna. 2 -- Seguir en la oscuridad. "))
    if opcion == 1 :
        print("Al encender la linterna, ilumina un pasillo oscuro y descubre una puerta secreta que conduce a una habitación oculta llena de antigüedades. Cuando entra a la habitacion, siente que algo lo toca ")
        engine.say("Al encender la linterna, ilumina un pasillo oscuro y descubre una puerta secreta que conduce a una habitación oculta llena de antigüedades. Cuando entra a la habitacion, siente que algo lo toca")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo += 50
    elif opcion == 2 :
        print(f"Decidió seguir en la oscuridad, pero tropezó con un objeto que hizo ruido, alertando a algo en la casa. Sintió que algo lo persiguió.")
        engine.say(f"Decidió seguir en la oscuridad, pero tropezó con un objeto que hizo ruido, alertando a algo en la casa. Sintió que algo lo persiguió.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo += 100
    else:
        print("Ingrese una opción correcta.")
        engine.say("Ingrese una opción correcta.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        primera_decision( )


def segunda_decision():
    global miedo
    print("")
    print("")
    print("")
    print("")
    print("")
    print(centrar_texto("              ________"))            
    print(centrar_texto("             / ______ \\"))
    print(centrar_texto("             || _  _ ||"))
    print(centrar_texto("             ||| || |||"))
    print(centrar_texto("             |||_||_|||"))
    print(centrar_texto("                 || _  _o|| (o)"))
    print(centrar_texto("             ||| || |||"))
    print(centrar_texto("                         |||_||_|||      ^~^  ,"))
    print(centrar_texto("                         ||______||     ('Y') )"))
    print(centrar_texto("                        /__________\\    /   \\/"))
    print(centrar_texto("    ________|__________|__ (\\|||/) _________"))
    print(centrar_texto("   hjw     /____________\\"))
    print(centrar_texto("   `97     |____________|"))
    print("")
    print("")
    print("")
    print("")

    print(f"--Corriendo por su vida, {nombre} se mete en un pasillo y ve una puerta cerrada:")
    encontrar_objeto(random.choice(objetos_random))
    print("Has encontrado un objeto, mìra tu inventario . ")
    engine.say(f"--Corriendo por su vida, {nombre} se mete en un pasillo y ve una puerta cerrada:")
    engine.runAndWait()
    engine.say("Presione 1 para abrir la puerta o 2 para buscar otra salida")
    engine.runAndWait()
    opcion = int(input("1 -- Abrir la puerta. 2 -- Buscar otra salida. "))
    if opcion == 1:
        print(f"Al abrir la puerta, descubre una habitación sellada con símbolos extraños en las paredes. Dentro, encuentra un mapa que revela la ubicación de una posible salida pero donde estaria la salida la hoja se encuentra rota.")
        engine.say(f"Al abrir la puerta, descubre una habitación sellada con símbolos extraños en las paredes. Dentro, encuentra un mapa que revela la ubicación de una posible salida pero donde estaria la salida la hoja se encuentra rota.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=150
    elif opcion == 2:
        print(f" Al buscar otra salida, encuentra una ventana rota que le permite escapar, pero se da cuenta demasiado tarde de que lo ha llevado más adentro del bosque y más lejos de la civilización.")
        engine.say(f" Al buscar otra salida, encuentra una ventana rota que le permite escapar, pero se da cuenta demasiado tarde de que lo ha llevado más adentro del bosque y más lejos de la civilización.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=100
    else:
        print("Elige una opcion valida. ")
        engine.say("Elige una opcion valida. ")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        segunda_decision( )


def tercera_decision():
    global miedo
    print("")
    print("")
    print(centrar_texto(" __________________________________________________________"))
    print(centrar_texto(" |     ,--.                                                |")          )
    print(centrar_texto(" |    //^\\\\\   ,;;;,                        .            |"))
    print(centrar_texto(" |   ((-_-))) (-_- ;                       /_\\            |"))
    print(centrar_texto(" |    )))(((   >..'.    .:.     .--.      |SSt|            |"))
    print(centrar_texto(" |   ((_._ )  /.   .|  :-_-;   /-_-))                      |"))
    print(centrar_texto(" |   _))A ((_//| S ||  ,`-'.   ))-((                       |"))
    print(centrar_texto(" |   `(    )`' |___|),;, C \\\\_/,`I ))                    |"))
    print(centrar_texto(" |     \  /    | | |`' |___(/-'|___()  ,-.                 | "))
    print(centrar_texto(" |      )(     | | |   | | |   | | |  (-_-)    _____       |"))
    print(centrar_texto(" |     /__\\    |_|_|   |_|_|   |_|_|  (\\I/\\.__|A|R|T|   |"))
    print(centrar_texto(" |     `''     `-'-'   `-'-'   `-'-'  `'-`'   `o' `o'      |"))
    print(centrar_texto(" |___________________Familia Robinson______________________|"))
    print(centrar_texto(" |_________________________1976____________________________|"))
    print(centrar_texto(" |_________________________________________________________|"))
    print("")
    print("")
    print("")

    print(f"Recorriendo la casa {nombre}se encuentra una fotografía") 
    engine.say(f"Recorriendo la casa {nombre}se encuentra una fotografía") 
    engine.runAndWait()
    engine.say("presione 1 para examinar fotografia o 2 para dejar a un lado")
    engine.runAndWait()
    opcion = int(input("1-- Examinar la fotografía. 2-- Dejarla a un lado. "))
    if opcion == 1:
        print("Fotografia fue agregada a inventario")
        encontrar_objeto("Fotografìa ")
        print("Al examinar la fotografía, descubre pistas sobre el pasado de la casa y la identidad de aquellos que la habitaban. Esto le ayuda a entender mejor el misterio que rodea al lugar.")
        engine.say("Al examinar la fotografía, descubre pistas sobre el pasado de la casa y la identidad de aquellos que la habitaban. Esto le ayuda a entender mejor el misterio que rodea al lugar.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=50    
    elif opcion == 2 :
        print(f"Al dejar la fotografía de lado,{nombre} continúa su camino y se encuentra con una presencia fantasmal que parece estar relacionada con la imagen que ignoró.")
        engine.say(f"Al dejar la fotografía de lado,{nombre} continúa su camino y se encuentra con una presencia fantasmal que parece estar relacionada con la imagen que ignoró.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=100
    else:
        print("Elige una opcion valida. ")
        tercera_decision( )




def cuarta_decision():
    global miedo
    print("")
    print("")
    print("")
    print("")
    print(centrar_texto("       _.--._  _.--._"))
    print(centrar_texto(",-=.-\":;:;:;\\':;:;:;\"-._"))
    print(centrar_texto("\\\\\\:;:;:;:;:;\\:;:;:;:;:;\\"))
    print(centrar_texto(" \\\\\\:;:;:;:;:;\\:;:;:;:;:;\\"))
    print(centrar_texto("  \\\\\\:;:;:;:;:;\\:;:;:;:;:;\\"))
    print(centrar_texto("   \\\\\\:;:;:;:;:;\\:;::;:;:;:\\"))
    print(centrar_texto("    \\\\\\;:;::;:;:;\\:;:;:;::;:\\"))
    print(centrar_texto("     \\\\\\;;:;:_:--:\\:_:--:_;:;\\    "))
    print(centrar_texto("      \\\\\\_.-\"      :      \"-._\\"))
    print(centrar_texto("       \\`_..--\"\"--.;.--\"\"--.._= >"))
    print(centrar_texto("        \"")  )
    print("")
    print("")
    print("")
    print("")
    print("")

    print("Encuentra un diario con páginas arrancadas") 
    print("Diario ha sido agregado a su inventario. ")
    encontrar_objeto("Diario")
    engine.say("Encuentra un diario con páginas arrancadas")
    engine.runAndWait()
    engine.say("presione 1 para buscar pistas . 2 para dejar a un lado ")
    engine.runAndWait()
    opcion = int(input("1 -- Buscar pistas. 2 -- Dejar a un lado. "))
    if opcion == 1:
        print(f"{nombre} busca pistas en las páginas restantes y descubre la verdad sobre una tragedia que ocurrió en la casa, lo que le permite resolver el misterio y liberar a las almas atormentadas que la habitaban.  ")
        engine.say(f"{nombre} busca pistas en las páginas restantes y descubre la verdad sobre una tragedia que ocurrió en la casa, lo que le permite resolver el misterio y liberar a las almas atormentadas que la habitaban.  ")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=100
    elif opcion == 2:
        print("Decidió dejar el diario de lado, pero más tarde se arrepiente cuando se da cuenta de que las páginas arrancadas contenían información crucial para entender el peligro que enfrentaba.")
        engine.say("Decidió dejar el diario de lado, pero más tarde se arrepiente cuando se da cuenta de que las páginas arrancadas contenían información crucial para entender el peligro que enfrentaba.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=50
    else:
        print("Ingrese una opción válida. ")
        engine.say("Ingrese una opción válida. ")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        cuarta_decision(   )
    

def quinta_decision():
    global miedo
    print(centrar_texto("                    []"))
    print(centrar_texto("                    []"))
    print(centrar_texto("                    []"))
    print(centrar_texto("                    []"))
    print(centrar_texto("                    []"))
    print(centrar_texto("                    []"))
    print(centrar_texto("   _______________  []         _________________"))
    print(centrar_texto("   _______________) []        (_______________"))
    print(centrar_texto("    !     !     !   []        '  !     !     !"))
    print(centrar_texto("    !     !     !   []       ,!  !     !     !"))
    print(centrar_texto("    !     !     !   []      ! !  !     !     !"))
    print(centrar_texto("    !_____!_____!___[]_____'!_!__!_____!_____!_____"))
    print(centrar_texto("                    []__,_!_!_!"))
    print(centrar_texto("                    []_!__!_!|"))
    print(centrar_texto("                   ,[]_!__!_!"))
    print(centrar_texto("                 ,! []_!__!|"))
    print(centrar_texto("               ,! ! []_!__!"))
    print(centrar_texto("              ! ! ! []_!|"))
    print(centrar_texto("             !! ! !|[]_|"))
    print(centrar_texto("             !!!._|_[]"))
    print(centrar_texto("             !!!|!_.[]"))
    print(centrar_texto("             !|!_!__[]!."))
    print(centrar_texto("             !_!_!__[]! !."))
    print(centrar_texto("             !_!_!__[]! ! `."))
    print(centrar_texto("              |!_!__|]! ! ! `."))
    print(centrar_texto("               |_!__|]! ! ! ! `."))
    print(centrar_texto("                 |____|_! ! ! !  `"))
    print(centrar_texto("                   |____|_! ! !"))
    print(centrar_texto("                    []____|_! !"))
    print(centrar_texto("                    []______|_!"))
    print(centrar_texto("                    []________|_!"))
    print(centrar_texto("  __________________[]__________|____________________"))
    encontrar_objeto(random.choice(objetos_random))
    print("Has encontrado un objeto, mìra tu inventario . ")
    print(f"{nombre} Escucha pasos en el piso de arriba:") 
    engine.say(f"{nombre} Escucha pasos en el piso de arriba:")
    engine.runAndWait()
    engine.say("presione 1 para investigar o presione 2 para esconderse")
    engine.runAndWait()
    opcion = int(input("1 -- Investigar. 2 -- Esconderse. "))
    if opcion == 1:
        print(f"Decide investigar y descubre que los pasos eran de un animal herido que necesitaba ayuda. Al ayudarlo, el animal lo guía de regreso a la seguridad.")
        engine.say(f"Decide investigar y descubre que los pasos eran de un animal herido que necesitaba ayuda. Al ayudarlo, el animal lo guía de regreso a la seguridad.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=50
    elif opcion == 2:
        print("Prefiere esconderse, pero luego se encuentra atrapado en una habitación sin salida, donde descubre que los pasos eran una distracción mientras algo más acechaba en la oscuridad.")
        engine.say("Prefiere esconderse, pero luego se encuentra atrapado en una habitación sin salida, donde descubre que los pasos eran una distracción mientras algo más acechaba en la oscuridad.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=100
    else:
        print("Ingrese una opcion valida. ")
        engine.say("Ingrese una opcion valida. ")
        engine.runAndWait()
        quinta_decision( )


def sexta_decision():
    global miedo
    print( centrar_texto("        _________________________"))
    print( centrar_texto("       (, ______________________ )"))
    print( centrar_texto("       | |                      ||"))
    print(centrar_texto( "       | |          @@@@        ||            @@@@"))
    print( centrar_texto("       | |        @@@@@@@       ||          @@@@@@@"))
    print( centrar_texto("       | |         @@ - -       ||          - @@@@"))
    print( centrar_texto("       | |          @  c/       ||         '_ @@@"))
    print( centrar_texto("       | |        _@| |_        ||         __\@ \@"))
    print(centrar_texto( "       | |       ( \ )/_\ /_    ||  _\\  (/ ) @\_/)"))
    print( centrar_texto("       | |        \ \|) / \)    ||   |(__/ /     /|"))
    print( centrar_texto("       | |        |\_/ ( -/     ||    \___/ ----/_|"))
    print( centrar_texto("       | |        /     \       ||       ,:   '("))
    print( centrar_texto("       | |       :    _/|       ||       |:     \\"))
    print( centrar_texto("       | |       :      |       ||       |:      )"))
    print( centrar_texto("       | |       :      |       ||       |:      |"))
    print(centrar_texto( "       | |_______'____,_|_______||       |_____,_|"))
    print( centrar_texto("   .---('________________________)--.     |   / ("))
    print( centrar_texto("   |____          __________       _|     |  /\  )"))
    print( centrar_texto("    |___|   -o-  |       |__|  -o- |      (  \| /"))
    print(centrar_texto( "    |___|   -o-  |       |__|  -o- |      |  /'=. "))
    print( centrar_texto("   |________|       |__|______|      '=>/  \\"))
    print(centrar_texto("                                         /  \\ /|/"))
    print( centrar_texto("                                       ,___/|") )
    encontrar_objeto(random.choice(objetos_random))
    print("Has encontrado otro objeto, mìra tu inventario . ")

    print("Encuentra un espejo empañado:") 
    engine.say("Encuentra un espejo empañado:")
    engine.runAndWait()
    engine.say("Presione 1 para limpiar el espejo o 2 para ignorar el espejo")
    engine.runAndWait()
    opcion = int(input("1-- Limpiar el espejo. 2-- Ignorar espejo. "))
    if opcion == 1:
        print("Al limpiar el espejo, se enfrenta a su propio reflejo distorsionado y descubre que el espejo es una entrada a otro mundo donde debe enfrentar sus miedos internos para escapar.")
        engine.say("Al limpiar el espejo, se enfrenta a su propio reflejo distorsionado y descubre que el espejo es una entrada a otro mundo donde debe enfrentar sus miedos internos para escapar.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif opcion == 2:
        print
        engine.say(" Decidió ignorar el espejo, pero más tarde se encuentra atrapado en una ilusión creada por el espejo que lo hace dudar de su propia cordura.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=100
    else:
        print("Ingrese una opcion valida ")
        engine.say("Ingrese una opcion valida ")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        sexta_decision()
 

def septima_decision():
    global miedo
    print( centrar_texto("     8 8 8 8                     ,ooo."))
    print( centrar_texto("     8a8 8a8                    oP   ?b"))
    print( centrar_texto("    d888a888zzzzzzzzzzzzzzzzzzzz8     8b"))
    print( centrar_texto("     `\"\"^\"\"'                    ?o___oP'"))
    print(centrar_texto( " __"))
    print(centrar_texto("              /o \_____"))
    print(centrar_texto( "              \__/-=\"=\"`"))
    print( centrar_texto("            __"))
    print(centrar_texto( "           / o\\"))
    print( centrar_texto("           \_ /"))
    print( centrar_texto("            <|"))
    print(centrar_texto( "            <|"))
    print(centrar_texto( "     jgs    <|"))
    print( centrar_texto("            `") )


    print("Encuentra una llave oxidada. ") 
    engine.say("Encuentra una llave oxidada. ")
    engine.runAndWait()
    engine.say("Presione 1 para guardar la llave o presione 2 para tirar la llave")
    engine.runAndWait()
    opcion = int(input("1-- Guardar llave. 2-- Tirar la llave. "))
    if opcion == 1:
        print("Llave ha sido agregada a su inventario. ")
        encontrar_objeto("Llave")
        print("Guarda la llave y más tarde descubre que abre una caja fuerte que contiene información vital para resolver el misterio de la casa.")
        engine.say("Guarda la llave y más tarde descubre que abre una caja fuerte que contiene información vital para resolver el misterio de la casa.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif opcion == 2:
        print("Decide tirar la llave, pero luego se da cuenta de que era la única manera de escapar de una habitación cerrada y encontrar ayuda.")
        engine.say("Decide tirar la llave, pero luego se da cuenta de que era la única manera de escapar de una habitación cerrada y encontrar ayuda.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=100
    else:
        print("Ingrese una opción válida. ")
        engine.say("Ingrese una opción válida! ")
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        septima_decision()


def octava_decision():
    print(  centrar_texto(" __________________________________________________________________"))
    print(  centrar_texto("/ \\-----     ---------  -----------     -------------- ------    ----\\"))
    print(centrar_texto( "\\_/__________________________________________________________________/"))
    print( centrar_texto( "|~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|"))
    print(centrar_texto( "|  _   ~~ ~~ __,---'_       \"         `. ~~~ _,--.  ~~~~ __,---.  ~~|"))
    print(  centrar_texto("| | \\___ ~~ /      ( )   \"          \"   `-.,' (') \\~~ ~ (  / _\\ \\~~ |"))
    print(  centrar_texto("|  \\    \\__/_   __(( _)_      (    \"   \"     (_\\_) \\___~ `-.___,'  ~|"))
    print( centrar_texto("|~~ \\     (  )_(__)_|( ))  \"   ))          \"   |    \"  \\ ~~ ~~~ _ ~~|"))
    print(  centrar_texto("|  ~ \\__ (( _( (  ))  ) _)    ((     \\\\//    \" |   \"    \\_____,' | ~|"))
    print( centrar_texto( "|~~ ~   \\  ( ))(_)(_)_)|  \"    ))    //\\\\ \" __,---._  \"  \"   \"  /~~~|"))
    print( centrar_texto("|    ~~~ |(_ _)| | |   |   \"  (   \"      ,-'^~~~ ~~~ `-.   ___  /~ ~ |"))
    print( centrar_texto( "| ~~     |  |  |   |   _,--- ,--. _  \"  (~   ~~~~  ~~~ ) /___\\ \\~~ ~|"))
    print(centrar_texto( "|  ~ ~~ /   |      _,----._,'`--'\\.`-._  `._~~_~__~_,-'  |H__|  \\ ~~|"))
    print(  centrar_texto("|~~    / \"     _,-' / `\\ ,' / _'  \\`.---.._          __        \" \\~ |"))
    print(centrar_texto(  "| ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   \" \" \\~|"))
    print( centrar_texto( "|  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \\ \\_   \" |~|"))
    print( centrar_texto( "| ~ | | -- _    /~/  `-_- _  _,' '  \\ \\_`-._,-'  / --   \\  - \\_   / |"))
    print( centrar_texto( "|~~ | \\ -      /~~| \"     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|"))
    print( centrar_texto( "| ~~\\  \\_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|"))
    print( centrar_texto( "|~   \\      ,'~~|  \" (o o)   \"         \" \" |~~~ \\_,-' ~ `.     ,'~~ |"))
    print( centrar_texto( "| ~~ ~|__,-'~~~~~\\    \\\"/      \"  \"   \"    /~ ~~   O ~ ~~`-.__/~ ~~~|"))
    print( centrar_texto( "|~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|"))
    print( centrar_texto( "|____~_____~__~_______~~_~____~~_____~~___~_~~___~\\_|_/ ~_____~___~__|"))
    print( centrar_texto( "/ \\----- ----- ------------  ------- ----- -------  --------  -------\\"))
    print( centrar_texto( "\\_/__________________________________________________________________/") )

    global miedo
    print("Encuentra un mapa dibujado a mano") 
    engine.say("Encuentra un mapa dibujado a mano")
    engine.runAndWait()
    engine.say("presione 1 para seguir el mapa o presione 2 para descartarlo")
    engine.runAndWait()
    opcion = int(input("1-- Seguir el mapa. 2--Descartar el mapa. "))
    if opcion == 1:
        encontrar_objeto("Mapa")
        print("Mapa se ha agregado a tu inventario . ")
        print("Sigue el mapa y encuentra una salida segura del bosque, sin embargo se encuentra obstruída por escombros, pero también descubre un lugar secreto donde puede encontrar ayuda")
        engine.say("Sigue el mapa y encuentra una salida segura del bosque, sin embargo se encuentra obstruída por escombros, pero también descubre un lugar secreto donde puede encontrar ayuda")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif opcion == 2:
        print("Descarta el mapa, pero más tarde se da cuenta de que habría llevado a una salida segura y rápida del peligro.")
        engine.say("Descarta el mapa, pero más tarde se da cuenta de que habría llevado a una salida segura y rápida del peligro.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=100
    else:
        print("Ingrese una opcion valida! ")
        engine.say("Ingrese una opcion valida")
        engine.runAndWait()
        octava_decision( )

 

def novena_decision():
    print( centrar_texto( "                                    _______________________      |"))
    print( centrar_texto( "                                  |  ________   ________  |     |"))
    print( centrar_texto("                                  | |        | |    ___ | |     |"))
    print(centrar_texto( "                                  | |        | |  ,',.('| |     |"))
    print( centrar_texto("                                  | |        | | :  .'  | |     |"))
    print( centrar_texto("                                  | |        | | :) _  (| |     |"))
    print( centrar_texto("                                  | |        | |  `:_)_,| |     |"))
    print(centrar_texto( "                                  | |________| |________| |     |"))
    print(centrar_texto( "                                  |  ________   ________  |     |"))
    print(centrar_texto( "                                  | |        | |        | |     |"))
    print( centrar_texto("                                  | |        | |        | |     |"))
    print(centrar_texto( "                                  | |        | |        | |     |"))
    print( centrar_texto("                                  | |        | |        | |     |"))
    print( centrar_texto( "                                  | |        | |        | |     |"))
    print( centrar_texto("                                  | |________| |________| |     |"))
    print( centrar_texto("                                  |_______________________|     |"))
    print( centrar_texto("                                                                |"))
    print( centrar_texto("                                                                |"))
    print( centrar_texto("                   _____________________________________________|"))
    print( centrar_texto("                                                                `."))
    print(centrar_texto( "                                                                  `."))
    print(centrar_texto( "                                                                    `."))
    print(centrar_texto( "                                                                      `."))
    print( centrar_texto("                     ..::::::::::::' .:::::::::::::::                   `."))
    print( centrar_texto("                 ..:::::::::::::::' .:::::::::::::::'                     `"))
    print(centrar_texto( "             ..:::::::::::::::::' .:::::::::::::::::"))
    print(centrar_texto( "         ..::::::::::::::::::::' .:::::::::::::::::'"))
    print( centrar_texto("     ..::::::::::::::::::::::' .:::::::::::::::::::"))
    print(centrar_texto( " ..:::::::::::::::::::::::::' .:::::::::::::::::::'"))
    print(centrar_texto( "..........................  ......................"))
    print(centrar_texto( ":::::::::::::::::::::::::' .:::::::::::::::::::::'"))
    print( centrar_texto(":::::::::::::::::::::::' .:::::::::::::::::::::::"))
    print(centrar_texto( "::::::::::::::::::::::' .:::::::::::::::::::::::'"))
    print( centrar_texto("::::::::::::::::::::' .:::::::::::::::::::::::::"))
    print( centrar_texto(":::::::::::::::::::' .:::::::::::::::::::::::::'"))

    global miedo
    print("Encuentra un sótano oscuro") 
    engine.say("Encuentra un sótano oscuro")
    engine.runAndWait()
    engine.say("Presione 1 para bajar e investigar el sotano o 2 para evitar el sotano.")
    engine.runAndWait()
    opcion = int(input("1-- Bajar e investigar el sòtano 2-- Evitar el sòtano. "))
    if opcion == 1:
        print("Decide bajar y descubre un laboratorio abandonado donde se llevaban a cabo experimentos peligrosos. Allí encuentra una solución para deshacer una maldición que afectaba a la casa.")
        engine.say("Decide bajar y descubre un laboratorio abandonado donde se llevaban a cabo experimentos peligrosos. Allí encuentra una solución para deshacer una maldición que afectaba a la casa.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=100
    elif opcion == 2:
        print("Prefiere evitar el sótano, pero más tarde se da cuenta de que era la única ruta segura para escapar de la casa antes de que fuera demasiado tarde.")
        engine.say("Prefiere evitar el sótano, pero más tarde se da cuenta de que era la única ruta segura para escapar de la casa antes de que fuera demasiado tarde.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    else:
        engine.say("Ingrese una opcion valida")    
        engine.runAndWait()
        novena_decision( ) 

def decima_decision():
    global miedo
    print( centrar_texto("      _________      "))
    print( centrar_texto("     /\ ()()()/\           (^)"))
    print( centrar_texto("    /  \_\\_\\_\\__\         {(o)}"))
    print(centrar_texto( "    \  /\        \         \O/"))
    print( centrar_texto("     \/::\   dos  \          v"))
    print(centrar_texto( "      \:::\ patitos\       ,---@"))
    print(centrar_texto( "       \:::\        \      | . |_"))
    print(centrar_texto( "        \:::\        \     |____7"))
    print(centrar_texto( "         \:::\________\    |    |"))
    print(centrar_texto( "          \::/        /    |    |"))
    print(centrar_texto( "           \/________/     |    |"))
    print( centrar_texto("                           |    |"))
    print( centrar_texto("                           |    |"))
    print( centrar_texto("                           |____|"))
    print("Fosforos y vela se han agregado a tu inventario")
    encontrar_objeto("Fosforo")
    encontrar_objeto("Vela")
    print("Encuentra una vela y fósforos") 
    engine.say("Encuentra una vela y fósforos")
    engine.runAndWait()
    engine.say("Presione 1 para encender la vela con los fosforos o 2 para guardar ")
    engine.runAndWait()
    opcion = int(input("1 --Enciende la vela con los fosforos . 2 --Guarda ambos "))
    if opcion == 1:
        print("Enciende la vela y los fósforos, lo que le permite explorar más a fondo la casa y encontrar una salida segura.")
        engine.say("Enciende la vela y los fósforos, lo que le permite explorar más a fondo la casa y encontrar una salida segura.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif opcion == 2:
        print("Guarda la vela y los fósforos, pero luego se encuentra en completa oscuridad y sin poder ver dónde está, lo que lo hace vulnerable a los peligros que acechan en la casa.")
        engine.say("Guarda la vela y los fósforos, pero luego se encuentra en completa oscuridad y sin poder ver dónde está, lo que lo hace vulnerable a los peligros que acechan en la casa.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=100
    else:
        print("Ingrese una opcion valida! ")
        engine.say("Ingrese una opcion valida! .")
        engine.runAndWait()
        decima_decision()


def onceava_decision():
    global miedo
    print( centrar_texto("         ___         _______________________________"))
    print(centrar_texto( "      |                               |"))
    print(centrar_texto( "      |                               |"))
    print( centrar_texto("      |                               |"))
    print( centrar_texto("      |   .|,        ,'drx.           |"))
    print( centrar_texto("      |  -(_)-      |::|888L          |"))
    print(centrar_texto( "      |   '|`       ;:::8888L         |"))
    print(centrar_texto( "      |            ;::::Y8888L        |"))
    print(centrar_texto( "      |------------|::::|88888L-------|"))
    print(centrar_texto( "      |            ;:::::888888L      |"))
    print(centrar_texto( "      |           ;::::::Y888888L     |"))
    print( centrar_texto("      |           |::::::|888888'L.   |"))
    print(centrar_texto( "      |           `-::::::888F'MMMML. |"))
    print(centrar_texto( "      |               `-::F'MMMMMMMMML|"))
    print(centrar_texto( "      |                   `\"**MMMMMMMM|"))
    print( centrar_texto("      |                          `\"**M|"))
    print( centrar_texto("      |                               |"))
    print( centrar_texto("      |                               |"))
    print( centrar_texto("      |    .;                         |"))
    print( centrar_texto("      |                               |"))
    print( centrar_texto("      |                               |"))
    print( centrar_texto("      |_______________________________|"))
    print( centrar_texto("       _/ ..\\"))
    print( centrar_texto("      ( \\  0/__"))
    print( centrar_texto("       \\    \\__)"))
    print(centrar_texto( "       /     \\"))
    print(centrar_texto( " jgs  /      _\\"))
    print( centrar_texto("     `\"\"\"\"\"``")  )

    print("Ve una sombra moviendose rapidamente hacia una de las habitaciones.") 
    engine.say("Ve una sombra moviendose rapidamente hacia una de las habitaciones.")
    engine.runAndWait()
    engine.say("Presione 1 para investigar la habitacion donde fue la silueta o presione 2 para ignorar y continuar buscando la salida.")
    engine.runAndWait()
    opcion = int(input("1-- Investigar la habitacion donde fue la silueta. 2 -- Ignorarla y continuar buscando la salida. "))
    if opcion == 1:
        print("Decides seguir la sombra, intrigado por descubrir quién o qué está merodeando por la mansión. Con pasos cautelosos, te diriges hacia la habitación donde la sombra desapareció. Al abrir la puerta, te encuentras con una escena sorprendente: un antiguo estudio lleno de polvo y libros cubiertos de telarañas. Pero lo más impactante es lo que encuentras en el centro de la habitación: una figura encapuchada de pie frente a un antiguo escritorio")
        engine.say("Decides seguir la sombra, intrigado por descubrir quién o qué está merodeando por la mansión. Con pasos cautelosos, te diriges hacia la habitación donde la sombra desapareció. Al abrir la puerta, te encuentras con una escena sorprendente: un antiguo estudio lleno de polvo y libros cubiertos de telarañas. Pero lo más impactante es lo que encuentras en el centro de la habitación: una figura encapuchada de pie frente a un antiguo escritorio")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=200
    elif opcion == 2:
        print("Decides ignorar la sombra y continuar explorando la mansión en busca de otras pistas sobre su misterioso pasado. Sin embargo, a medida que avanzas por los pasillos oscuros, una sensación de malestar comienza a crecer en el fondo de tu mente.")
        engine.say("Decides ignorar la sombra y continuar explorando la mansión en busca de otras pistas sobre su misterioso pasado. Sin embargo, a medida que avanzas por los pasillos oscuros, una sensación de malestar comienza a crecer en el fondo de tu mente.")
        engine.runAndWait()
        miedo += 100
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Ingrese una opcion valida! ")
        engine.say("Ingrese una opcion valida! ")
        engine.runAndWait()
        onceava_decision()


def finales():
    global miedo 
    print(miedo)
    if miedo < 600:
        print( centrar_texto("              ,;;;,"))
        print( centrar_texto("             ;;;;;;;"))
        print(centrar_texto( "          .-'`\, '/_"))
        print(centrar_texto( "        .'   \ (\"`(_)"))
        print(centrar_texto( "       / `-,.'\ \_/"))
        print(centrar_texto( "       \  \/\\  `--`"))
        print(centrar_texto( "        \  \ \ "))
        print(centrar_texto( "         / /| |"))
        print(centrar_texto( "        /_/ |_|"))
        print(centrar_texto( "  jgs  ( _\ ( _\  #:##        #:##        #:##         #:##"))
        print(centrar_texto( "                        #:##        #:##        #:##"))
        print(f"{nombre} utiliza inteligentemente los objetos que ha recolectado para descubrir la verdad detrás de los fenómenos paranormales en la casa y encontrar una forma de liberación.")
        engine.say(f"{nombre} utiliza inteligentemente los objetos que ha recolectado para descubrir la verdad detrás de los fenómenos paranormales en la casa y encontrar una forma de liberación.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        print( centrar_texto( "$$$$$$$$\       "))
        print( centrar_texto("$$  _____|      "))
        print( centrar_texto( "$$ |            "))
        print( centrar_texto( "$$$$$\          "))
        print(  centrar_texto("$$  __|         "))
        print(  centrar_texto("$$ |            "))
        print( centrar_texto( "$$ |            "))
        print(  centrar_texto("\__|            "))
        print( centrar_texto( "                "))
        print( centrar_texto( "                "))
        time.sleep(1)
        print( centrar_texto("$$\\ "))
        print(centrar_texto( "\\__|"))
        print(centrar_texto( "$$\\ "))
        print(centrar_texto( "$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("\\__|"))
        print("    ")
        print("    ")
        time.sleep(1)
        print(centrar_texto("$$\\   $$\\ "))
        print(centrar_texto("$$$\\  $$ |"))
        print(centrar_texto("$$$$\\ $$ |"))
        print(centrar_texto("$$ $$\\$$ |"))
        print(centrar_texto("$$ \\$$$$ |"))
        print(centrar_texto("$$ |\\$$$ |"))
        print(centrar_texto("$$ | \\$$ |"))
        print(centrar_texto("\\__|  \\__|"))
        print("           ")
        print("           ")

        time.sleep(40)

       

    elif miedo > 600 and miedo < 800:
        print(f"Después de enfrentarse a múltiples desafíos dentro de la casa abandonada, {nombre} finalmente logra desentrañar parte del misterio que la rodea. Descubre que la casa fue testigo de un antiguo pacto oscuro entre sus antiguos habitantes y seres sobrenaturales. Finalmente lo obligan a mantener la verdad en secreto y formar parte del pacto robandole su alma.")
        engine.say(f"Después de enfrentarse a múltiples desafíos dentro de la casa abandonada, {nombre} finalmente logra desentrañar parte del misterio que la rodea. Descubre que la casa fue testigo de un antiguo pacto oscuro entre sus antiguos habitantes y seres sobrenaturales. Finalmente lo obligan a mantener la verdad en secreto y formar parte del pacto robandole su alma.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        print( centrar_texto( "$$$$$$$$\       "))
        print( centrar_texto("$$  _____|      "))
        print( centrar_texto( "$$ |            "))
        print( centrar_texto( "$$$$$\          "))
        print(  centrar_texto("$$  __|         "))
        print(  centrar_texto("$$ |            "))
        print( centrar_texto( "$$ |            "))
        print(  centrar_texto("\__|            "))
        print( centrar_texto( "                "))
        print( centrar_texto( "                "))
        time.sleep(1)
        print( centrar_texto("$$\\ "))
        print(centrar_texto( "\\__|"))
        print(centrar_texto( "$$\\ "))
        print(centrar_texto( "$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("\\__|"))
        print("    ")
        print("    ")
        time.sleep(1)
        print(centrar_texto("$$\\   $$\\ "))
        print(centrar_texto("$$$\\  $$ |"))
        print(centrar_texto("$$$$\\ $$ |"))
        print(centrar_texto("$$ $$\\$$ |"))
        print(centrar_texto("$$ \\$$$$ |"))
        print(centrar_texto("$$ |\\$$$ |"))
        print(centrar_texto("$$ | \\$$ |"))
        print(centrar_texto("\\__|  \\__|"))
        print("           ")
        print("           ")


        

    elif miedo > 800:
        print(f"{nombre} decide tomar las pastillas encontradas al inicio  y seguir explorando la casa, sumergiéndose en un estado de miedo y paranoia extremo que lo consume por completo.  ")
        engine.say(f"{nombre} decide tomar las pastillas encontradas al inicio  y seguir explorando la casa, sumergiéndose en un estado de miedo y paranoia extremo que lo consume por completo.  ")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        print("           ")
        print("           ")
        print("           ")
        print("           ")
        print("           ")
        print("           ")
        print("           ")
        print("           ")
        print("           ")

        print( centrar_texto( "$$$$$$$$\       "))
        print( centrar_texto("$$  _____|      "))
        print( centrar_texto( "$$ |            "))
        print( centrar_texto( "$$$$$\          "))
        print(  centrar_texto("$$  __|         "))
        print(  centrar_texto("$$ |            "))
        print( centrar_texto( "$$ |            "))
        print(  centrar_texto("\__|            "))
        print( centrar_texto( "                "))
        print( centrar_texto( "                "))
        time.sleep(1)
        print( centrar_texto("$$\\ "))
        print(centrar_texto( "\\__|"))
        print(centrar_texto( "$$\\ "))
        print(centrar_texto( "$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("$$ |"))
        print( centrar_texto("\\__|"))
        print("    ")
        print("    ")
        time.sleep(1)
        print(centrar_texto("$$\\   $$\\ "))
        print(centrar_texto("$$$\\  $$ |"))
        print(centrar_texto("$$$$\\ $$ |"))
        print(centrar_texto("$$ $$\\$$ |"))
        print(centrar_texto("$$ \\$$$$ |"))
        print(centrar_texto("$$ |\\$$$ |"))
        print(centrar_texto("$$ | \\$$ |"))
        print(centrar_texto("\\__|  \\__|"))
        print("           ")
        print("           ")


        


def introduccion():
    # print( centrar_texto("                *         .              *            _.---._      "))
    print( centrar_texto("                              ___   .            ___.'       '.   *"))
    print( centrar_texto("        .              _____[LLL]______________[LLL]_____     \\"))
    print( centrar_texto("                      /     [LLL]              [LLL]     \     |"))
    print( centrar_texto("                     /____________________________________\    |    ."))
    print( centrar_texto("                      )==================================(    /"))
    print( centrar_texto("     .      *         '|I .-. I .-. I .--. I .-. I .-. I|'  .'"))
    print( centrar_texto("                  *    |I |+| I |+| I |. | I |+| I |+| I|-'`       *"))
    print( centrar_texto("                       |I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I|      ."))
    print( centrar_texto("              .       /_I_____I_____I______I_____I_____I_\""))
    print( centrar_texto("                       )================================(   *"))
    print( centrar_texto("       *         _     |I .-. I .-. I .--. I .-. I .-. I|          *"))
    print( centrar_texto("                |u|  __|I |+| I |+| I |<>| I |+| I |+| I|    _         ."))
    print( centrar_texto("           __   |u|_|uu|I |+| I |+| I |~ | I |+| I |+| I| _ |U|     _"))
    print( centrar_texto("       .  |uu|__|u|u|u,|I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I||n|| |____|u|"))
    print( centrar_texto("          |uu|uu|_,.-' /I_____I_____I______I_____I_____I\`'-. |uu u|u|__"))
    print( centrar_texto("          |uu.-'`      #############(______)#############    `'-. u|u|uu|"))

   
    print( centrar_texto("  ~'^'~    _,'~'^'~    _( )_                         _( )_   `'-.        ~'^'~"))
    print( centrar_texto("      _  .'            |___|                         |___|      ~'^'~     _"))
    print( centrar_texto("    _( )_              |_|_|          () ()          |_|_|              _( )_"))
    print( centrar_texto("    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|"))
    print( centrar_texto("    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|"))
    print( centrar_texto("    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|"))
    print( centrar_texto("    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/[===]\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|"))
    print( centrar_texto("    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|"))
    print( centrar_texto("~'^'~|_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_lc|~'^'~"))
    print( centrar_texto("   [_____]            [_____]                       [_____]            [_____] ") )

    print(centrar_texto(f"\n En una fría noche de invierno. {nombre} caminaba por un bosque cuando se topó con una casa abandonada. Movido por la curiosidad y el deseo de resguardarse del frío, decidió entrar en ella. Al explorar sus oscuros pasillos, encontró una mesa con varias pastillas sobre ella...  "))
    engine.say(f"\n En una fría noche de invierno,{nombre} caminaba por un bosque cuando se topó con una casa abandonada. Movido por la curiosidad y el deseo de resguardarse del frío, decidió entrar en ella. Al explorar sus oscuros pasillos, encontró una mesa con varias pastillas sobre ella...  ")
    engine.runAndWait()
    limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')


        
    


def historia():
    global nombre
    global limpiar_consola
    limpiar_consola
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(centrar_texto("/$$$$$$$  /$$$$$$ /$$$$$$$$ /$$   /$$ /$$    /$$ /$$$$$$$$ /$$   /$$ /$$$$$$ /$$$$$$$   /$$$$$$"))                          
    print(centrar_texto("| $$__  $$|_  $$_/| $$_____/| $$$ | $1$| $$   | $$| $$_____/| $$$ | $$|_  $$_/| $$__  $$ /$$__  $$"))
    print(centrar_texto("| $$  \ $$  | $$  | $$      | $$$$| $$| $$   | $$| $$      | $$$$| $$  | $$  | $$  \ $$| $$  \ $$"))
    print(centrar_texto("| $$$$$$$   | $$  | $$$$$   | $$ $$ $$|  $$ / $$/| $$$$$   | $$ $$ $$  | $$  | $$  | $$| $$  | $$"))
    print(centrar_texto("| $$__  $$  | $$  | $$__/   | $$  $$$$ \  $$ $$/ | $$__/   | $$  $$$$  | $$  | $$  | $$| $$  | $$"))
    print(centrar_texto("| $$  \ $$  | $$  | $$      | $$\  $$$  \  $$$/  | $$      | $$\  $$$  | $$  | $$  | $$| $$  | $$"))
    print(centrar_texto("| $$$$$$$/ /$$$$$$| $$$$$$$$| $$ \  $$   \  $/   | $$$$$$$$| $$ \  $$ /$$$$$$| $$$$$$$/|  $$$$$$/"))
    print(centrar_texto("|_______/ |______/|________/|__/  \__/    \_/    |________/|__/  \__/|______/|_______/  \______/"))
    print("")
    print("")
    print("")
    print("")
    print("")
    print(centrar_texto("Bienvenido A Elige tu propia  aventura! ")) 
    print(centrar_texto("Comencemos!"))
    engine.say(f"Bienvenido a Elige tu propia aventura! \nComencemos! ")
    engine.runAndWait()
    print("")
    print("")
    print("")
    print("")
    engine.say("Ingrese el nombre de su personaje")
    engine.runAndWait()
    nombre = input("Ingrese el nombre de su personaje: ").capitalize()
    limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
    introduccion()
    comienzo = True
    while comienzo: 
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        primera_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        segunda_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        tercera_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        cuarta_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        quinta_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        sexta_decision()        
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        septima_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        octava_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        novena_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(1)
        decima_decision()
        time.sleep(1)
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        onceava_decision()
        print("-"*consola_ancho)
        print(centrar_texto(f"Miedo =  {miedo}                         Inventario = {inventario}"))
        print("-"*consola_ancho)
        time.sleep(3)
        finales()
        engine.say("Desea repetir la historia para descubrir un nuevo final? Presione 1 para si o 2 para no. ")
        engine.runAndWait()
        seguir = int(input("Desea volver a repetir la historia para descubrir un nuevo final? [ 1 -- Si , 2 -- No ]"))
        if seguir != 1:
            comienzo = False



def menu():
    global limpiar_consola
    limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
    print(centrar_texto("                   _.-,"))
    print(centrar_texto("              _ .-'  / .._"))
    print(centrar_texto("           .-:'/ - - \\:::::-."))
    print(centrar_texto("         .::: '  e e  ' '-::::."))
    print(centrar_texto("        ::::'(    ^    )_.::::::"))
    print(centrar_texto("       ::::.' '.  o   '.::::'.'/_"))
    print(centrar_texto("   .  :::.'       -  .::::'_   _.:"))
    print(centrar_texto(" .-''---' .'|      .::::'   '''::::"))
    print(centrar_texto("'. ..-:::'  |    .::::'        ::::"))
    print(centrar_texto(" '.' ::::    \\ .::::'          ::::"))
    print(centrar_texto("      ::::   .::::'           ::::"))
    print(centrar_texto("       ::::.::::'._          ::::"))
    print(centrar_texto("        ::::::' /  '-      .::::"))
    print(centrar_texto("         '::::-/__    __.-::::'")     )
    print(centrar_texto("           '-::::::::::::::-'"))
    print(centrar_texto("                '''::::'''"))
    print(" ")
    print(" ")
    animacion(centrar_texto("Bienvenido a 'Elige tu propia' aventura.")) 
    engine.say(f"Bienvenido !¿ Estas listo para introducirte en un mundo lleno de aventuras?")
    engine.runAndWait()
    print("")
    print("")
    print("")
    print("") 
    print(centrar_texto("  /__________________________________________________/"))
    print(centrar_texto(" /_____________________________________________________/"))
    print(centrar_texto(" |                                                  ||"))
    print(centrar_texto(" |                                                  ||"))
    print(centrar_texto(" |                    1-- COMENZAR                  ||"))
    print(centrar_texto(" |                                                  ||"))
    print(centrar_texto(" |____________                           ___________||"))
    print(centrar_texto(" |                                                  ||"))
    print(centrar_texto(" |                     2--  SALIR                   ||"))
    print(centrar_texto(" |                                                  ||"))
    print(centrar_texto(" |                                                  ||"))
    print(centrar_texto(" | ________________________________________________ ||"))
    print(centrar_texto(" |__________________________________________________||"))

    engine.say("Presione 1 para comenzar o presione 2 para salir")
    engine.runAndWait()
    opcion = int(input(" "))
    if opcion == 1:
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        historia()
    else:
        pass
    
    
menu()