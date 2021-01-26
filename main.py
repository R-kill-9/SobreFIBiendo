
def lol_room():
    print("\nSin darte cuenta has pasado toda la clase hablando de LOL con tus nuevos amigos y no has hecho caso a JL.")
    print("\nLlegas a casa y recibes una llamada de uno de tus amigos preguntandote si quieres jugar ¿Qué decides hacer? (1 o 2)")
    print("\n1.) Jugar para socializar porque nunca has tenido amigos, sino no serías informático.")
    print("\n2.) No jugar y repasar. Total para que quieres amigos reales cuando puedes tener todos los imaginarios que quieras")   

    answer = input(">")

    if (answer == 1):
        # if player typed "1" lead him to lol_room()
        lol_room()
    else:
        # if player typed "2" lead him to class_room()
        class_room()


def class_room():
    print("\nHas atendido sabiamente a toda la clae del gran JL aprendiendo cosas que nunca vas a usar porque no te gusta el hardware") 
    print(" ¿verdad?")
    print("\n1.) Si que me gusta, soy un psicópata.")
    print("\n2.) No, no me ducho pero soy normal.")   
    print("\n3.) Furbo")   

    answer = input(">")

    if (answer == 1):
        # if player typed "1" lead him to lol_room()
        game_over("Gracias por jugar, pero porfavor no te acerques a mi por la calle que me das miedo.")
    else:
        # if player typed "2" or "3" lead him to class_room()
        print("\nLlegas a casa después de tremendo tostón de clase, ¿Qué decides hacer?") 
        print("\n1.) Repasar un poquito, menos vida social no puedo tener.")
        print("\n2.) Entrar al Discord del curso para ver si alguien juega al LOL.")   
        print("\n3.) Buscar el insta de la chica que se sienta atrás, la mala racha de 18 años se puede acabar.")


def love_room():
    print("\nSin darte cuenta has pasado toda la clase hablando con la chica y no has hecho caso a JL.")
    print("\nLlegas a casa y recibes una llamada de la chica de clase ¿Qué decides hacer? (1 o 2)")
    print("\n1.) Coger el teléfono.")
    print("\n2.) No coger el teléfono y repasar lo que se ha repasado")   

    answer = input(">")

    if (answer == 1):
        # if player typed "1" lead him to lol_room()
        lol_room()
    else:
        # if player typed "2" lead him to class_room()
        class_room()
    

def virgo_room():
    print("\nUna vez te sientas los chicos que estaban hablando se callan de repente.")
    print("\n¿Qué decides hacer? (1 o 2)")
    print("\n1.) Saludar a tus compañeros con un -Hola.")
    print("\n2.) No decir nada y esperar a que inicie la clase.")

    answer = input(">")

    if (answer == 1):
        # if player typed "1" lead him to lol_room()
        lol_room()
    else:
        # if player typed "2" lead him to class_room()
        class_room()

def girl_room():
    print("\nLa chica en la que te habías fijado resulta ser un tio, amigo despierta esto es informática.")
    print("\nAún así parecesestar en tu día de suerte, ya que una chica se sienta a tu lado y te saluda")
    print("\n¿Qué decides hacer? (1 o 2 o 3)")
    print("\n1.) Saludarle de vuelta con un -Hola")
    print("\n2.) Asentir con la cabeza sin llegar a decir nada.")
    print("\n3.) Agachar la cabeza y no responder, nunca antes has hablado con una mujer y la situación te sobrepasa.")

    answer = input(">")

    if (answer == 1):
        # if player typed "1" lead him to love_room()
        love_room()
    else:
        # if player typed "2" or "3" lead him to class_room()
        class_room()




# function to ask play again or not
def play_again():
    print("Se te ha hecho una revisión de expediente y se te ha otorgado una última oportunidad, ¿Quieres aprovecharla?")
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
    print("    Nombre: Manolo")
    print("    Apellidos: García, García") 
    print("Acabas de entrar a tu primera clase de IC.")
    print("\nSentados delante del todo hay un grupo de chicos que huelen a jugadores de LOL.")
    print("\nSentada al final de clase hay lo que parece ser una chica.")
    print("\n¿Dónde decides sentarte? (principio = p o final = f)")
    
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

    