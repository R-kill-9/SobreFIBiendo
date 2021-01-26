def exam1_room():
    print("Te presentas al priner examen y logras aprobar gracias a que tenías al gran Tomit delante.")

def sex_room():
    print("\nUna vez llegas a su casa la chica te pregunta que si quieres ir ya a estudiar o prefieres ver Netflixa un rato.")
    print("¿Qué respondes? (1 o 2 o 3)")
    print("\n1.) Mejor nos ponemos a estudiar que el examen es muy difícil.")
    print("2.) Vemos Netflix un rato y luego estudiamos.")
    print("3.) No puedo tengo furbo.")

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        exam1_room()
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
    print("\nAl final te pasaste toda la semana practicando para impresionar a tus amigos.")
    print("En el examen solo fuiste capaz de responder una de las siete preguntas.")
    print("Aún así tu única esperanza era impresionar a tus amigos con tu gran habilidad para tocar teclas en el momento exacto.")
    print("Por desgrácia tus panas decidieron no jugar contigo porque les parecías extremadamente raro.")
    print("Por otra parte dijeron no querer volver a verte desprendías un hedor que les hacía estar incómodos cuando te veían")
    print("Debido al trauma que te causó dichas palabras caíste en una gran depresión")
    game_over("Por culpa de la depresión dejaste de acudir a clase y no te presentaste a ningún examen")

def depression2_room():
    print("\nDebido al exceso de estudio empezaste a sufrir alucinaciones.")
    print("Solo eras capaz de comunicarte en binario y ya no querías ver Hentai, preferías ver las sensuales curvas de una puerta OR")
    print("Ya no comías, puesto que te alimentabas de los carry que quedaban en las operaciones de suma binaria.")
    print("Días después fuiste ingresado en un hospital de psiquiatría con muchos otros informáticos.")
    game_over("Por culpa de tu enfermedad mental dejaste de acudir a clase y no te presentaste a ningún examen")


def love2_room():
    print("\nYa ha pasado un mes y medio y no has aprendido nada por estar hablando todo el día con la chica.")
    print(" En una semana tienes el primer parcial y ella te invita a su casa a estuiar. ¿Qué decides hacer? (1 o 2)")
    print("\n1.) Ir a su casa a 'estudiar', hay oportunidades que solo se presentan una vez en la vida.")
    print("2.) Ser responsable y estudiar mucho porque sabes que te van a funar en el examen.")   

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        sex_room()
    else:
        # if player typed "2" lead him to class_room()
        exam1_room()

def lol2_room():
    print("\nYa ha pasado un mes y medio y no has aprendido nada por estar jugando con tus nuevos compas todo el día.")
    print(" En una semana tienes el primer parcial, pero hay torneo de LOL el próximo finde. ¿Qué decides hacer? (1 o 2)")
    print("\n1.) Entrenar jugando al LOL, necesitas demostrarles que eres el mejor en un juego de ordenador para recibir la aprovación externa que tus padres nunca te dieron.")
    print("2.) Ser responsable y estudiar mucho porque sabes que te van a funar en el examen.")   

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        depression1_room()
    else:
        # if player typed "2" lead him to class_room()
        exam1_room()

def class2_room():
    print("\nYa ha pasado un mes y medio y llevas perfectamente el temario.")
    print(" En una semana tienes el primer parcial, pero tienes una gran fatiga mental. ¿Qué decides hacer? (1 o 2 o 3)")
    print("\n1.) Seguir estudiando, no pain no gain, mentalidad de tiburao.")
    print("2.) Estudiar un rato y luego descansar viendo tu anime favorito.")   
    print("3.) Beber un chupito de legía.")   
    
    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        depression2_room()
    elif (answer == "2"):
        # if player typed "2" lead him to class_room()
        class2_room()
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
        print("3.) Beber un chupito de legía.")   
        
        answer = input(">")

        if (answer == "1"):
            # if player typed "1" lead him to lol_room()
            depression2_room()
        elif (answer == "2"):
            # if player typed "2" lead him to class_room()
            exam1_room()
        else: 
            game_over("No todo el mundo nace con los cromosomas correctos")

def lol_room():
    print("\nSin darte cuenta has pasado toda la clase hablando de LOL con tus nuevos amigos y no has hecho caso a JL.")
    print("Llegas a casa y recibes una llamada de uno de tus amigos preguntandote si quieres jugar ¿Qué decides hacer? (1 o 2)")
    print("\n1.) Jugar para socializar porque nunca has tenido amigos, sino no serías informático.")
    print("2.) No jugar y repasar. Total para que quieres amigos reales cuando puedes tener todos los imaginarios que quieras")   

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        lol2_room()
    else:
        # if player typed "2" lead him to class_room()
        class2_room()


def class_room():
    print("\nHas atendido sabiamente a toda la clae del gran JL aprendiendo cosas que nunca vas a usar porque no te gusta el hardware") 
    print(" ¿verdad?")
    print("\n1.) Si que me gusta, soy un psicópata.")
    print("2.) No, no me ducho pero soy normal.")   
    print("3.) Viva el betis")   

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
            class2_room()
        elif (answer == "2"):
            # if player typed "2" lead him to lol_room()
            lol2_room()
        else:
            # if player typed "3" lead him to class_room()
            love2_room()

def love_room():
    print("\nSin darte cuenta has pasado toda la clase hablando con la chica y no has hecho caso a JL.")
    print("Llegas a casa y recibes una llamada de la chica de clase ¿Qué decides hacer? (1 o 2)")
    print("\n1.) Coger el teléfono.")
    print("2.) No coger el teléfono y repasar lo que se ha repasado")   

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        love2_room()
    else:
        # if player typed "2" lead him to class_room()
        class2_room()
    

def virgo_room():
    print("\nUna vez te sientas los chicos que estaban hablando se callan de repente.")
    print("\n¿Qué decides hacer? (1 o 2)")
    print("\n1.) Saludar a tus compañeros con un -Hola.")
    print("2.) No decir nada y esperar a que inicie la clase.")

    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to lol_room()
        lol_room()
    else:
        # if player typed "2" lead him to class_room()
        class_room()

def girl_room():
    print("\nLa chica en la que te habías fijado resulta ser un tio, amigo despierta esto es informática.")
    print("Aún así pareces estar en tu día de suerte, ya que una chica se sienta a tu lado y te saluda")
    print("¿Qué decides hacer? (1 o 2 o 3)")
    print("\n1.) Saludarle de vuelta con un -Hola")
    print("2.) Asentir con la cabeza sin llegar a decir nada.")
    print("3.) Agachar la cabeza y no responder, nunca antes has hablado con una mujer y la situación te sobrepasa.")

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
    print("\nFicha técnica:")
    print("    Nombre: Mariano")
    print("    Apellidos: García, García") 
    print("    Edad: ln(65659969.14)")
    print("    Hobbies: jugar al LOL, espiar a la vecina del cuarto, ver Hentai.")
    print("    Nº de relaciones afectivas: cos 90.")
    print("    Signo zodiacal: virgo.")
    print("\nAcabas de entrar a tu primera clase de IC.")
    print("Sentados delante del todo hay un grupo de chicos que huelen a jugadores de LOL.")
    print("Sentada al final de clase hay lo que parece ser una chica.")
    print("¿Dónde decides sentarte? (principio = p o final = f)")
    
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

    