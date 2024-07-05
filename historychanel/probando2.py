import random
import time 
import pyttsx3
import pygame
import shutil
import os
import dibujos as dib
import dibujos as dib
import micro as mic
import threading

##ACLARACIONES
#Para correr el juego es necesario instalar en consola las librerias pygame y pyttsx3 con un pip install nombre_libreria . 

global limpiar_consola
limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
nombre = ""

global miedo
miedo = 0
global objetos_random
objetos_random = ["paquete de cigarrillos vacio", "Frasco", "Diario", "Jeringa", "Cuchillo ensangrentado", "Muñeca", "Reloj", "Máscara", "Radio", "ouija", "Collar", "Ojo", "Manchas", "Dientes", "muñeco budu", "carta", "un pajaro podrido", "cucarachas", "veneno"]

inventario = []

#Inicializador de motor de voz. 
engine = pyttsx3.init()
voices=  engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # los [ numero] se deben cambiar acuerdo a las necesidades de su sistema, si su lenguaje predeterminado es distinto al espaniol debera ajustar el numero 
engine.setProperty('language', 'es')
engine.setProperty('rate', 199)     # Velocidad de habla (palabras por minuto)
engine.setProperty('volume', 0.9)
engine.runAndWait()


#aIniciamos la musica especificando la ruta. 
pygame.init()
#Ruta del archivo de música e Iniciar la reproducción de la música de fondo
ruta_musica = "fondo.mp3"
pygame.mixer.music.load(ruta_musica)
pygame.mixer.music.play(-1)
pygame.mixer_music.set_volume(0.1)
engine = pyttsx3.init()

#cambiar el color de las letras de la consola
os.system("color 0" + "4") 
#os.system('mode con:fullscreen')


def encontrar_objeto(objeto):
    global inventario 
    return inventario.append(objeto)
    
consola_ancho = shutil.get_terminal_size().columns



def hablar(texto):
    talk = engine.say(texto)
    engine.runAndWait()


def animacion(texto, velocidad=0.03):
    
    for letra in texto:
        print(letra,end="", flush=True)
        time.sleep(velocidad)


def centrar_texto(texto):
    consola_ancho = shutil.get_terminal_size().columns
    espacios = (consola_ancho - len(texto)) // 2
    texto_centralizado = ' ' * espacios + texto
        
    return texto_centralizado





def encontrar_cigarrillo():
    print(f"{nombre} encuentra un cigarrillo")

## en caso que diga que si,  hacer un print de que tu nivel de miedo bajo
## el cigarrillo tien que bajar 50 pts¿



def primera_decision():
    global nombre 
    global miedo  
    print(f"En la penumbra de la casa abandonada, {nombre} avanzaba con cuidado por los pasillos polvorientos y crujientes. Cada paso resonaba ominosamente, aumentando su sensación de intriga y temor.  En el centro de una vieja mesa de madera, cubierta de una fina capa de polvo gris, descansaba un conjunto de objetos olvidados por el tiempo. Entre los objetos se destacaba una linterna oxidada, cuyo destello de metal y cristal parecía susurrarle al protagonista una promesa de seguridad en la oscuridad.")
    print("Linterna se ha agregado a tu inventario. ")
    dib.primer_dibujo()
    hablar(f"En la penumbra de la casa abandonada, {nombre} avanzaba con cuidado por los pasillos polvorientos y crujientes. Cada paso resonaba ominosamente, aumentando su sensación de intriga y temor.  En el centro de una vieja mesa de madera, cubierta de una fina capa de polvo gris, descansaba un conjunto de objetos olvidados por el tiempo. Entre los objetos se destacaba una linterna oxidada, cuyo destello de metal y cristal parecía susurrarle al protagonista una promesa de seguridad en la oscuridad.")
    hablar("-- Diga Encender prender linterna o diga seguir en Oscuridad para Seguir en la oscuridad")
    encontrar_objeto("linterna")
    opcion = mic.hablar()

    if "encender" in opcion:
        print("Al encender la linterna, ilumina un pasillo oscuro y descubre una puerta secreta que conduce a una habitación oculta llena de antigüedades. Cuando entra a la habitacion, siente que algo lo toca ")
        hablar("Al encender la linterna, ilumina un pasillo oscuro y descubre una puerta secreta que conduce a una habitación oculta llena de antigüedades. Cuando entra a la habitacion, siente que algo lo toca")

        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo += 50
    elif "oscuridad" in opcion:
        print(f"Decidió seguir en la oscuridad, pero tropezó con un objeto que hizo ruido, alertando a algo en la casa. Sintió que algo lo persiguió.")
        hablar(f"Decidió seguir en la oscuridad, pero tropezó con un objeto que hizo ruido, alertando a algo en la casa. Sintió que algo lo persiguió.")
        #engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo += 100
    else:
        print("Ingrese una opción correcta.")
        #engine.say("Ingrese una opción correcta.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        primera_decision( )
primera_decision()

def segunda_decision():
    global miedo
    print("")
    print("")
    print("")
    print("")
    print("")
    dib.segundoDibujo()
    print("")
    print("")
    print("")
    print("")
    print(f"--Corriendo por su vida, {nombre} se mete en un pasillo y ve una puerta cerrada:")
    encontrar_objeto(random.choice(objetos_random))
    print("Has encontrado un objeto, mìra tu inventario . ")
    engine.say(f"--Corriendo por su vida, {nombre} se mete en un pasillo y ve una puerta cerrada:")
    engine.runAndWait()
    engine.say("Diga abrir la puerta o diga 'otra salida' para buscar otra salida")
    engine.runAndWait()
    opcion = mic.hablar()
    if "abrir" in opcion:
        print(f"Al abrir la puerta, descubre una habitación sellada con símbolos extraños en las paredes. Dentro, encuentra un mapa que revela la ubicación de una posible salida pero donde estaria la salida la hoja se encuentra rota.")
        engine.say(f"Al abrir la puerta, descubre una habitación sellada con símbolos extraños en las paredes. Dentro, encuentra un mapa que revela la ubicación de una posible salida pero donde estaria la salida la hoja se encuentra rota.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=150
    elif "salida" in opcion:
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
    dib.tercerDibujo()
    print("")
    print("")
    print("")

    print(f"Recorriendo la casa {nombre}se encuentra una fotografía") 
    engine.say(f"Recorriendo la casa {nombre}se encuentra una fotografía") 
    engine.runAndWait()
    engine.say("Diga 'Examinar fotografia' para examinarla o 'tirar fotografia' para dejar a un lado")
    engine.runAndWait()
    opcion = mic.hablar()
    if "examinar" in opcion :
        print("Fotografia fue agregada a inventario")
        encontrar_objeto("Fotografìa ")
        print("Al examinar la fotografía, descubre pistas sobre el pasado de la casa y la identidad de aquellos que la habitaban. Esto le ayuda a entender mejor el misterio que rodea al lugar.")
        engine.say("Al examinar la fotografía, descubre pistas sobre el pasado de la casa y la identidad de aquellos que la habitaban. Esto le ayuda a entender mejor el misterio que rodea al lugar.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=50    
    elif "tirar" in opcion:
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
    dib.cuarto_dibujo()
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
    engine.say("Diga 'examinar' para buscar pistas o diga 'deshacer diario' para dejar a un lado ")
    engine.runAndWait()
    opcion =mic.hablar()
    if "examinar" in opcion :
        print(f"{nombre} busca pistas en las páginas restantes y descubre la verdad sobre una tragedia que ocurrió en la casa, lo que le permite resolver el misterio y liberar a las almas atormentadas que la habitaban.  ")
        engine.say(f"{nombre} busca pistas en las páginas restantes y descubre la verdad sobre una tragedia que ocurrió en la casa, lo que le permite resolver el misterio y liberar a las almas atormentadas que la habitaban.  ")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=100
    elif "deshacer" in opcion:
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

        cuarta_decision()

def quinta_decision():
    global miedo
    dib.quinto_dibujo()
    encontrar_objeto(random.choice(objetos_random))
    print("Has encontrado un objeto, mìra tu inventario . ")
    print(f"{nombre} Escucha pasos en el piso de arriba:") 
    engine.say(f"{nombre} Escucha pasos en el piso de arriba:")
    engine.runAndWait()
    engine.say("diga 'investigar ruido' para investigar o diga 'esconderse del ruido'  para esconderse")
    engine.runAndWait()
    opcion = mic.hablar()
    if "investigar" in opcion :
        print(f"Decide investigar y descubre que los pasos eran de un animal herido que necesitaba ayuda. Al ayudarlo, el animal lo guía de regreso a la seguridad.")
        engine.say(f"Decide investigar y descubre que los pasos eran de un animal herido que necesitaba ayuda. Al ayudarlo, el animal lo guía de regreso a la seguridad.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')

        miedo+=50
    elif "esconderse" in opcion:
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
    dib.sexto_dibujo()
    encontrar_objeto(random.choice(objetos_random))
    print("Has encontrado otro objeto, mìra tu inventario . ")

    print("Encuentra un espejo empañado:") 
    engine.say("Encuentra un espejo empañado:")
    engine.runAndWait()
    engine.say("Diga 'limpiar espejo' para  limpiar el espejo o diga 'ignorar espejo ' para ignorarlo ")
    engine.runAndWait()
    opcion = mic.hablar()
    if "limpiar" in opcion:
        print("Al limpiar el espejo, se enfrenta a su propio reflejo distorsionado y descubre que el espejo es una entrada a otro mundo donde debe enfrentar sus miedos internos para escapar.")
        engine.say("Al limpiar el espejo, se enfrenta a su propio reflejo distorsionado y descubre que el espejo es una entrada a otro mundo donde debe enfrentar sus miedos internos para escapar.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif "ignorar" in opcion:
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
    dib.septimo_dibujo()
    print("Encuentra una llave oxidada. ") 
    engine.say("Encuentra una llave oxidada. ")
    engine.runAndWait()
    engine.say("Diga 'guardar llave' para guardarla o diga 'tirar llave' para tirarla")
    engine.runAndWait()
    opcion = mic.hablar()
    if "guardar" in opcion:
        print("Llave ha sido agregada a su inventario. ")
        encontrar_objeto("Llave")
        print("Guarda la llave y más tarde descubre que abre una caja fuerte que contiene información vital para resolver el misterio de la casa.")
        engine.say("Guarda la llave y más tarde descubre que abre una caja fuerte que contiene información vital para resolver el misterio de la casa.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif "tirar" in opcion:
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
    dib.octavo_dibujo()
    global miedo
    print("Encuentra un mapa dibujado a mano") 
    engine.say("Encuentra un mapa dibujado a mano")
    engine.runAndWait()
    engine.say("Diga 'seguir mapa 'para seguirlo  o diga 'tirar mapa' para descartarlo")
    engine.runAndWait()
    opcion = mic.hablar()
    if "seguir" in opcion:
        encontrar_objeto("Mapa")
        print("Mapa se ha agregado a tu inventario . ")
        print("Sigue el mapa y encuentra una salida segura del bosque, sin embargo se encuentra obstruída por escombros, pero también descubre un lugar secreto donde puede encontrar ayuda")
        engine.say("Sigue el mapa y encuentra una salida segura del bosque, sin embargo se encuentra obstruída por escombros, pero también descubre un lugar secreto donde puede encontrar ayuda")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif "tirar" in opcion :
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
    dib.noveno_dibujo()
    global miedo
    print("Encuentra un sótano oscuro") 
    engine.say("Encuentra un sótano oscuro")
    engine.runAndWait()
    engine.say("Diga 'investigar sotano' para bajar a investigar el sotano o diga 'evitar sotano' para evitarlo.")
    engine.runAndWait()
    opcion = mic.hablar()
    if "investigar" in opcion:
        print("Decide bajar y descubre un laboratorio abandonado donde se llevaban a cabo experimentos peligrosos. Allí encuentra una solución para deshacer una maldición que afectaba a la casa.")
        engine.say("Decide bajar y descubre un laboratorio abandonado donde se llevaban a cabo experimentos peligrosos. Allí encuentra una solución para deshacer una maldición que afectaba a la casa.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=100
    elif "evitar" in opcion:
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
    dib.decimo_dibujo()
    print("Fosforos y vela se han agregado a tu inventario")
    encontrar_objeto("Fosforo")
    encontrar_objeto("Vela")
    print("Encuentra una vela y fósforos") 
    engine.say("Encuentra una vela y fósforos")
    engine.runAndWait()
    engine.say("Diga 'encender' para encender la vela con los fosforos o diga 'guardar' para guardarla ")
    engine.runAndWait()
    opcion = mic.hablar()
    if "encender" in opcion :
        print("Enciende la vela y los fósforos, lo que le permite explorar más a fondo la casa y encontrar una salida segura.")
        engine.say("Enciende la vela y los fósforos, lo que le permite explorar más a fondo la casa y encontrar una salida segura.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=50
    elif "guardar" in opcion:
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
    print("Ve una sombra moviendose rapidamente hacia una de las habitaciones.") 
    dib.onceava_decision()
    engine.say("Ve una sombra moviendose rapidamente hacia una de las habitaciones.")
    engine.runAndWait()
    engine.say("Diga  'investigar silueta' para investigar la habitacion donde fue la silueta o diga 'ignorar silueta' para ignorar y continuar buscando la salida.")
    engine.runAndWait()
    opcion = mic.hablar()
    if "investigar" in opcion:
        print("Decides seguir la sombra, intrigado por descubrir quién o qué está merodeando por la mansión. Con pasos cautelosos, te diriges hacia la habitación donde la sombra desapareció. Al abrir la puerta, te encuentras con una escena sorprendente: un antiguo estudio lleno de polvo y libros cubiertos de telarañas. Pero lo más impactante es lo que encuentras en el centro de la habitación: una figura encapuchada de pie frente a un antiguo escritorio")
        engine.say("Decides seguir la sombra, intrigado por descubrir quién o qué está merodeando por la mansión. Con pasos cautelosos, te diriges hacia la habitación donde la sombra desapareció. Al abrir la puerta, te encuentras con una escena sorprendente: un antiguo estudio lleno de polvo y libros cubiertos de telarañas. Pero lo más impactante es lo que encuentras en el centro de la habitación: una figura encapuchada de pie frente a un antiguo escritorio")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        miedo+=200
    elif "ignorar" in opcion:
        print("Decides ignorar la sombra y continuar explorando la mansión en busca de otras pistas sobre su misterioso pasado. Sin embargo, a medida que avanzas por los pasillos oscuros, una sensación de malestar comienza a crecer en el fondo de tu mente.")
        engine.say("Decides ignorar la sombra y continuar explorando la mansión en busca de otras pistas sobre su misterioso pasado. Sin embargo, a medida que avanzas por los pasillos oscuros, una sensación de malestar comienza a crecer en el fondo de tu mente.")
        engine.runAndWait()
        miedo += 100
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Ingrese una opción válida! ")
        engine.say("Ingrese una opción válida! ")
        engine.runAndWait()
        onceava_decision()


def finales():
    global miedo 
    print(miedo)
    if miedo < 600:
        dib.espia()
        print(f"{nombre} utiliza inteligentemente los objetos que ha recolectado para descubrir la verdad detrás de los fenómenos paranormales en la casa y encontrar una forma de liberación.")
        engine.say(f"{nombre} utiliza inteligentemente los objetos que ha recolectado para descubrir la verdad detrás de los fenómenos paranormales en la casa y encontrar una forma de liberación.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        dib.fin()

    elif miedo > 600 and miedo < 800:
        print(f"Después de enfrentarse a múltiples desafíos dentro de la casa abandonada, {nombre} finalmente logra desentrañar parte del misterio que la rodea. Descubre que la casa fue testigo de un antiguo pacto oscuro entre sus antiguos habitantes y seres sobrenaturales. Finalmente lo obligan a mantener la verdad en secreto y formar parte del pacto robandole su alma.")
        engine.say(f"Después de enfrentarse a múltiples desafíos dentro de la casa abandonada, {nombre} finalmente logra desentrañar parte del misterio que la rodea. Descubre que la casa fue testigo de un antiguo pacto oscuro entre sus antiguos habitantes y seres sobrenaturales. Finalmente lo obligan a mantener la verdad en secreto y formar parte del pacto robandole su alma.")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        dib.fin()
    elif miedo > 800:
        print(f"{nombre} decide tomar las pastillas encontradas al inicio  y seguir explorando la casa, sumergiéndose en un estado de miedo y paranoia extremo que lo consume por completo.  ")
        engine.say(f"{nombre} decide tomar las pastillas encontradas al inicio  y seguir explorando la casa, sumergiéndose en un estado de miedo y paranoia extremo que lo consume por completo.  ")
        engine.runAndWait()
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        dib.fin()




def introduccion():
    print(centrar_texto(f"\n En una fría noche de invierno. {nombre} caminaba por un bosque cuando se topó con una casa abandonada. Movido por la curiosidad y el deseo de resguardarse del frío, decidió entrar en ella. Al explorar sus oscuros pasillos, encontró una mesa con varias pastillas sobre ella...  "))
    print("")
    dib.dibujo_introduccion()
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
    dib.bienvenida()
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
        (primera_decision())
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
    dib.fantasmita()
    animacion(centrar_texto("Bienvenido a 'Elige tu propia aventura'")) 
    engine.say(f"Bienvenido en e")
    engine.runAndWait()
    limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
    dib.menu()
    engine.say(f" diga para ' Quiero Empezar' para comenzar o Diga 'Quiero Salir' para salir")
    engine.runAndWait()
    opcion = mic.hablar()
    if "empezar" in opcion:
        limpiar_consola = os.system('cls' if os.name == 'nt' else 'clear')
        historia()
    else:
        pass
    
menu()
