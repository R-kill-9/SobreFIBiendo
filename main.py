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
        route = './rooms/sub_jl2.txt'
        file = open(route, 'r')
        print(file.read())
        final_room()
    elif (attack == "3"):
    # if player typed "3" lead him to game_over()
        route = './rooms/sub_elif_jl2.txt'
        file = open(route, 'r')
        print(file.read())
        final_room()
        game_over("Nunca debiste recordarle a JL que tiene el cora partido.")
    else:
        # if player typed "2" lead him to final_room()
        route = './rooms/else_sub_jl2.txt'
        file = open(route, 'r')
        print(file.read())
        final_room()

def jl_room():
    route = './rooms/jl.txt'
    file = open(route, 'r')
    print(file.read())

    attack = input(">")

    if (attack == "1"):
        # if player typed "1" lead him to final_room()
        route = './rooms/sub_jl.txt'
        file = open(route, 'r')
        print(file.read())
        final_room()
    elif (attack == "3"):
    # if player typed "3" lead him to game_over()
        route = './rooms/sub_elif_jl.txt'
        file = open(route, 'r')
        print(file.read())
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
        route = './rooms/if_plan.txt'
        file = open(route, 'r')
        print(file.read())
    
    else:
        game_over("Pero muy guapo.")

    route = './rooms/sub_plan.txt'
    file = open(route, 'r')
    print(file.read())
    
    answer = input(">")

    if (answer == "1"):
        # if player typed "1" lead him to JL_room()
        jl2_room()
    elif (answer == "2"):
        route = './rooms/putin.txt'
        file = open(route, 'r')
        print(file.read())
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
        route = './rooms/sub_meet.txt'
        file = open(route, 'r')
        print(file.read())
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
    route = './rooms/exam.txt'
    file = open(route, 'r')
    print(file.read())
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
        route = './rooms/sub_sex.txt'
        file = open(route, 'r')
        print(file.read())
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
        route = './rooms/sub_study.txt'
        file = open(route, 'r')
        print(file.read())   
        
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
        route = './rooms/sun_class.txt'
        file = open(route, 'r')
        print(file.read())
        
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
    route = './rooms/play_again.txt'
    file = open(route, 'r')
    print(file.read())
    
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

    