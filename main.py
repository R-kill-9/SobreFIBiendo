def final_room():
    route = './rooms/final.txt'
    file = open(route, 'r')
    print(file.read())

def putin_love_room():
    route = './rooms/putin_love.txt'
    file = open(route, 'r')
    print(file.read())

    final_room()


def jl2_room():
    route = './rooms/jl2.txt'
    file = open(route, 'r')
    print(file.read())
    
    attack = input(">")

    if (attack == "1"):
        # if player typed "1" lead him to final_room()
        print("Has fumado tantos porros con el RECTOR que tu nivel de fuerza ha igualado al de GOKU y el bong ha llegado a 2.99*10^8 m/s.")
        print("Jl intenta esquivar el bong con su velocidad de procesador VON NEUMANN usando la ALU, pero no es suficiente.")
        print("La velocidad es tal que el golpe desintegra a JL con el impacto, acción que le produce un gran placer a tu mente enferma.")
        print("Delante tuyo aparecen mágicamente dos objetos.")
        print("El primer objeto es un boli rojo en el que está escrito lo siguiente: 'Un boli para suspenderlos a todos'.")
        print("El otro objeto es un certificado de la asignatura de IC.")
        final_room()
    elif (attack == "3"):
    # if player typed "3" lead him to game_over()
        print("    JL: -No intentes eso, mi corazón está roto. Yo solo he sido capaz de amar a un hombre, Vladimir y la vida nos separó.")
        print("    JL: -Jamás deberías haberme hecho recordarlo maldito gusano.")     
        print("Tus palabras causaron tal cólera en JL que desprendió una onda binaria explosiva que separó tu cabeza de tu cuerpo en un t.p.")       
        game_over("Nunca debiste recordarle a JL que tiene el cora partido.")
    else:
        # if player typed "2" lead him to final_room()
        print("Invocas un MERCEDES BENZ FULL EQUIPED de color amarillo usando palabras no inteligíbles para un ser humano.")
        print("Posteriormente te subes y te das cuenta de que el acabado del interior es precioso, gracias a las matrículas de los de tardes.")
        print("Una vez has observado perfectamente el coche atropellas majestuosamente a JL, múltiples veces.")
        print("Cuando observas que ya lo has derrotado sigues atropellándolo porque estás loco, sino no habrías llegado hasta aquí.")
        print("Delante tuyo aparecen mágicamente dos objetos.")
        print("El primer objeto es un boli rojo en el que está escrito lo siguiente: 'Un boli para suspenderlos a todos'.")
        print("El otro objeto es un certificado de la asignatura de IC.")
        final_room()

def jl_room():
    route = './rooms/jl.txt'
    file = open(route, 'r')
    print(file.read())

    attack = input(">")

    if (attack == "1"):
        # if player typed "1" lead him to final_room()
        print("Tu poder es tal que has sido capaz de clavarle veinte puertas AND en cada ojo a tu enemigo.")
        print("Jl intenta ir a por ti pero por culpa de la ceguera se tropieza con una piedra del Colisseo y cae en una trampilla secreta.")
        print("En esa trampilla es devorado por dos leones, acción que le produce un gran placer a tu mente enferma.")
        print("Delante tuyo aparecen mágicamente dos objetos.")
        print("El primer objeto es un boli rojo en el que está escrito lo siguiente: 'Un boli para suspenderlos a todos'.")
        print("El otro objeto es un certificado de la asignatura de IC.")
        
        final_room()
    elif (attack == "3"):
    # if player typed "3" lead him to game_over()
        print("    JL: -No intentes eso, mi corazón está roto. Yo solo he sido capaz de amar a un hombre, Vladimir y la vida nos separó.")
        print("    JL: -Jamás deberías haberme hecho recordarlo maldito gusano.")     
        print("Tus palabras causaron tal cólera en JL que desprendió una onda binaria explosiva que separó tu cabeza de tu cuerpo en un t.p.")       
        game_over("Nunca debiste recordarle a JL que tiene el cora partido.")
    else:
        # if player typed "2" lead him to putin_love_room()
        putin_love_room()



def plan_room():
    route = './rooms/plan.txt'
    file = open(route, 'r')
    print(file.read())

    answer1 = input(">")
    
    if (answer1 == "1"):
        print("Quién podría rechazar dicha oferta.")
    
    else:
        game_over("Pero muy guapo.")

    print("\nEn el bar te cuenta tener un malévolo plan con el que convertirá a la FIB en la mayor asociación de marihuana de ESPAÑITA.")
    print("Te confiesa que le has caído muy bien y que le gustaría que le ayudaras a cumplir su sueño.")
    print("Tu único trbajo sería retar a JL, su gran opositor, a una batalla a muerte.")
    print("Te promete que si ganas te regalrá el título de informática y un mercedes comprado con las cuotas de tus compañeros de clase.")
    print("¿Aceptas? (1 o 2)")
    print("\n1.) Voy a acabar con JL y vengar a aquellos soldados caídos en Noviembre.")
    print("2.) Aceituna.")
    print("3.) Yo cogería la 1.")
    
    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to JL_room()
        jl2_room()
    elif (answer == "2"):
        print("Al pronunciar dicha palabra has causado un bucle de amor a Rusia.")
        putin_room()
    else:
        # if player typed "3" lead him to putin_room()
        game_over("Te quedaba poco para ganar pero te pasáste de troll.")

def putin_room():
    while True:
        print("Родина Россия")

def heroe_room():
    route = './rooms/heroe.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to JL_room()
        jl_room()
    elif (answer == "2"):
    # if player typed "2" lead him to game_over()
        game_over("Tu rebeldia hacia el juego ha causado daños cerebrales a su creador.")
    else:
        # if player typed "3" lead him to putin_room()
        putin_room()
        

def meet_room():
    route = './rooms/meet.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to game_over()
        game_over("Nunca intentes mentir a un maestro jedi.")
    elif (answer == "2"):
    # if player typed "2" lead him to digimon_room()
        print("A todos nos pasaría lo mismo pero la respuesta correcta era la 3.")
        print("Vamos a hacer que no ha pasado nada y que has escogido la 3.")
        plan_room()
    else:
        # if player typed "3" lead him to plan_room()
        plan_room()

def snorlax_room():
    route = './rooms/snorlax.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to game_over()
        game_over("No descifraste correctamente el código en hexa.")
    elif (answer == "2"):
    # if player typed "2" lead him to digimon_room()
        heroe_room()
    else:
        # if player typed "3" lead him to game_over()
        game_over("No descifraste correctamente el código en hexa.")

def weed_room():
    route = './rooms/weed.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to game_over()
        game_over("No hace falta explicación.")
    else:
        # if player typed "2" lead him to meet_room()
        meet_room()

def neumann_room():
    route = './rooms/neumann.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to game_over()
        game_over("Resultaste ser alérgico al agua, con lo que el té te provcó un coma de tres años y dos días.")
    elif (answer == "2"):
        # if player typed "2" lead him to snorlax_room()
        snorlax_room()
    else:
        # if player typed "3" lead him to weed_room()
        weed_room()
    
def exam_room():
    print("\nTe presentas al primer examen y logras aprobar gracias a que tenías al gran Tomit delante.")
    neumann_room()

def sex_room():
    route = './rooms/sex.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        exam_room()
    elif (answer == "2"):
        # if player typed "2" lead him to exam1_room()
        print("Después de esta excelente elección descubres un mundo que solo habías percibido en el Hentai y descubres el sentido de la vida.")
        print("Posteriormente al llegar a tu casa se te presenta ante tus ojos un espíritu con gafas y  sobrepeso que te dice:")
        print("Espíritu:")
        print("    -Soy la represenación de los códigos del informático, los mismos que tú hoy has roto.")
        print("    -Pues está escrito en dichos códigos que todo informático debe mantenerse puro hasta recibir su grado.")
        print("    -Por romper el código debo privarte de tu esencia de infórmaitco y converirte en un sucio muggle.")
        print("Después de que el espíritu desaparezca empieza a desaparecer tu chepa y a arreglarse mágicamente tu vista.")
        print("Y de repente sientes unas ganas irrefrenables de apuntarte a ADE y ser tu propio jefe a la par que aprender 9 idiomas.")
        game_over("Debido a tu repentino cambio decides dejar la carrera.")
    else:
        # if player typed "3" lead him to game_room()
        game_over("Hay un colapso en el espacio tiempo y se crea una brecha espacial que te absorbe por exceso de estilo.")

def depression1_room():
    route = './rooms/depression1.txt'
    file = open(route, 'r')
    print(file.read())

    game_over("Por culpa de la depresión dejaste de acudir a clase y no te presentaste a ningún examen.")

def depression2_room():
    route = './rooms/depression2.txt'
    file = open(route, 'r')
    print(file.read())

    game_over("Por culpa de tu enfermedad mental dejaste de acudir a clase y no te presentaste a ningún examen.")


def cupido_room():
    route = './rooms/cupido.txt'
    file = open(route, 'r')
    print(file.read())   

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to sex_room()
        sex_room()
    else:
        # if player typed "2" lead him to exam_room()
        exam_room()

def gaming_room():
    route = './rooms/gaming.txt'
    file = open(route, 'r')
    print(file.read())   

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        depression1_room()
    else:
        # if player typed "2" lead him to class_room()
        exam_room()

def study_room():
    route = './rooms/study.txt'
    file = open(route, 'r')
    print(file.read())
    
    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to depression_room()
        depression2_room()
    elif (answer == "2"):
        # if player typed "2" lead him to exam_room()
        exam_room()
    else:
        # if player typed "3" lead him to class_room()
        print("Te despiertas debido a un calor abrasador y te das cuenta de que estás en un descampado infinitamente grande.")
        print("En la lejanía se escucha Bohemian Rhapsody y delante tuyo aparece Maradona, que te ayuda a levantarte.")
        print("Caminas junto a él hasta llegar delante de un hombre colosal, que te dice lo siguiente:")
        print("Satán: ")
        print("    -Muchos me conocen como el Diablo, Satán, procesador Von Nuemann, Lucifer, pero tu puedes llamarme Manolo.")
        print("    -Estás destinado a vivir en el castigo eterno, pero que peor castigo hay para alguien como tu que la vida misma.")
        print("Justo después de que ese coloso recitara la última palabra vuelves a aprecer en tu habitación con el vaso de detergente en la mano.")
        print("¿Qué decides hacer? (1 o 2 o 3)")
        print("\n1.) Seguir estudiando, no pain no gain, mentalidad de tiburao.")
        print("2.) Estudiar un rato y luego descansar viendo tu anime favorito.")   
        print("3.) Beber un chupito de lejía.")   
        
        answer = input(">")

        if (answer == "1"):
            # if player typed "1" lead him to lol_room()
            depression2_room()
        elif (answer == "2"):
            # if player typed "2" lead him to class_room()
            exam_room()
        else: 
            game_over("No todo el mundo nace con los cromosomas correctos.")

def lol_room():
    route = './rooms/lol.txt'
    file = open(route, 'r')
    print(file.read())   

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        gaming_room()
    else:
        # if player typed "2" lead him to class_room()
        study_room()


def class_room():
    route = './rooms/class.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        game_over("Gracias por jugar, pero porfavor no te acerques a mi por la calle que me das miedo.")
    else:
        # if player typed "2" or "3" lead him to class_room()
        print("\nLlegas a casa después de tremendo tostón de clase, ¿Qué decides hacer?") 
        print("\n1.) Repasar un poquito, menos vida social no puedo tener.")
        print("2.) Entrar al Discord del curso para ver si alguien juega al LOL.")   
        print("3.) Buscar el insta de la chica que se sienta atrás, la mala racha de 18 años se puede acabar.")
        
        answer = input(">")

        if (answer == "1"):
            # if player typed "1" lead him to lol_room()
            study_room()
        elif (answer == "2"):
            # if player typed "2" lead him to lol_room()
            gaming_room()
        else:
            # if player typed "3" lead him to class_room()
            cupido_room()

def love_room():
    route = './rooms/love.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        cupido_room()
    else:
        # if player typed "2" lead him to class_room()
        study_room()
    

def virgo_room():
    route = './rooms/virgo.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        lol_room()
    else:
        # if player typed "2" lead him to class_room()
        class_room()

def girl_room():
    route = './rooms/girl.txt'
    file = open(route, 'r')
    print(file.read())

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to love_room()
        love_room()
    else :
        # if player typed "2" or "3" lead him to class_room()
        class_room()


# function to ask play again or not
def play_again():
    print("\n\nSe te ha hecho una revisión de expediente y se te ha otorgado una última oportunidad, ¿Quieres aprovecharla?")
    print(" (si = s o no = n)")
    
    answer = input(">")
     
    if (answer == "s" or answer == "si"):
    # if player typed "si" or "s" lead him to start()
        start()
    else:
    # if user types anything besides "yes" or "y", exit() the program        
        exit()


def game_over(reason):
    print("\n" + reason)
    print("\nGame over, quedas expulsado de la FIB!")
    play_again()

def start(): 
    
    route = './rooms/start.txt'
    file = open(route, 'r')
    print(file.read())
    
    answer = input(">").lower()
    
    if (answer == "p" or answer == "principio"):
        # if player typed "principio" or "p" lead him to virgo_room()
        virgo_room()

    elif (answer == "f" or answer == "final"):
        # else if player typed "final" or "f" lead him to girl_room()
        girl_room()

    # else call game_over() function with the "reason" argument
    else:
        game_over("No supiste ni introducir bien una letra en un juego pocho")
        
start()

    