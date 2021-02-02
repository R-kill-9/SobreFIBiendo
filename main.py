rooms = {
    'start': [{'next_room':'girl'}, {'next_room':'virgo'}, {'next_room':'game_over','reason': "Ponte a estudiar Magisterio." }],
    'play_again': [{'next_room':'start'}, {'next_room':'exit'}, {'next_room':'start'}],
    'girl': [{'next_room':'love'}, {'next_room':'class'}, {'next_room':'class'}],
    'virgo': [{'next_room':'lol'}, {'next_room':'class'}, {'next_room':'class'}],
    'love': [{'next_room':'cupido'}, {'next_room':'study'}, {'next_room':'study'}],    
    'class': [{'next_room':'game_over','reason': "Gracias por jugar, pero porfavor no te acerques a mi por la calle que me das miedo." }, {'next_room':'sub_class'}, {'next_room':'sub_class'}], 
    'sub_class': [{'next_room':'study'}, {'next_room':'gaming'}, {'next_room':'cupido'}],
    'lol': [{'next_room':'gaming'}, {'next_room':'study'}, {'next_room':'study'}],
    'study': [{'next_room':'depression2'}, {'next_room':'exam'}, {'next_room':'sub_study'}],
    'sub_study': [{'next_room':'depression2'}, {'next_room':'exam'}, {'next_room':'game_over','reason': "No todo el mundo nace con los cromosomas correctos." }],
    'gaming': [{'next_room':'depression1'}, {'next_room':'exam'}, {'next_room':'exam'}],
    'cupido': [{'next_room':'sex'}, {'next_room':'exam'}, {'next_room':'exam'}],
    'depression2': [{'next_room':'game_over','reason': "Por culpa de tu enfermedad mental dejaste de acudir a clase y no te presentaste a ningún examen." }],
    'depression1': [{'next_room':'game_over','reason': "Por culpa de la depresión dejaste de acudir a clase y no te presentaste a ningún examen." }],
    'sex': [{'next_room':'exam'}, {'next_room':'sub_sex'}, {'next_room':'game_over','reason': "Hay un colapso en el espacio tiempo y se crea una brecha espacial que te absorbe por exceso de estilo." }],
    'sub_sex': [{'next_room':'game_over','reason': "Debido a tu repentino cambio decides dejar la carrera" }, {'next_room':'game_over','reason': "Debido a tu repentino cambio decides dejar la carrera" }, {'next_room':'game_over','reason': "Debido a tu repentino cambio decides dejar la carrera" }],
    'exam': [{'next_room':'neumann'}, {'next_room':'neumann'}, {'next_room':'game_over','reason': "Pobre iluso, no sabes poner una lavadora y vas a saber comofunciona un procesador pringao." }],
    'neumann': [{'next_room':'game_over','reason': "Resultaste ser alérgico al agua, con lo que el té te provcó un coma de tres años y dos días." }, {'next_room':'snorlax'}, {'next_room':'weed'}],
    'weed': [{'next_room':'game_over','reason': "No hace falta explicación." }, {'next_room':'meet'}, {'next_room':'meet'}],
    'snorlax': [{'next_room':'game_over','reason': "No descifraste correctamente el código en hexa." }, {'next_room':'heroe'}, {'next_room':'game_over','reason': "No descifraste correctamente el código en hexa." }],
    'meet': [{'next_room':'game_over','reason': "Nunca intentes mentir a un maestro jedi." }, {'next_room':'sub_meet'}, {'next_room':'plan'}],
    'sub_meet': [{'next_room':'game_over','reason': "Eres demasiado poca cosa para convertir contra la grandeza de Pakistán." }, {'next_room':'plan'}, {'next_room':'plan'}],
    'heroe': [{'next_room':'jl'}, {'next_room':'game_over','reason': "Tu rebeldia hacia el juego ha causado daños cerebrales a su creador." }, {'next_room':'putin'}],
    'plan': [{'next_room':'sub_plan'}, {'next_room':'sub_plan'}, {'next_room':'game_over','reason': "Quién te crees para rechazar a semejante obra de arte." }],
    'sub_plan': [{'next_room':'jl2'}, {'next_room':'putin'}, {'next_room':'game_over','reason': "Pero si te lo he dicho cabezón." }],
    'jl': [{'next_room':'sub_jl'}, {'next_room':'putin_love'}, {'next_room':'game_over','reason': 'sub_elif_jl' }],
    'sub_jl': [{'next_room':'final'}, {'next_room':'final'}, {'next_room':'game_over','reason': "Todo en este mundo tiene un porqué y ahora tu pierdes por listo." }],
    'jl2': [{'next_room':'sub_jl2'}, {'next_room':'else_sub_jl2'}, {'next_room':'game_over','reason': 'sub_elif_jl2' }],
    'sub_jl2': [{'next_room':'final'}, {'next_room':'final'}, {'next_room':'game_over','reason': "Todo en este mundo tiene un porqué y ahora tu pierdes por listo." }],
    'else_sub_jl': [{'next_room':'final'}, {'next_room':'final'}, {'next_room':'game_over','reason': "Todo en este mundo tiene un porqué y ahora tu pierdes por listo." }],
    'putin_love': [{'next_room':'final'}, {'next_room':'final'}, {'next_room':'game_over','reason': "Todo en este mundo tiene un porqué y ahora tu pierdes por listo." }]

}

def read_room(room): 
    route = './rooms/'+ room + '.txt'
    file = open(route, 'r', encoding = "utf-8")
    print(file.read())

def access_room(room_name):
    read_room(room_name)
    
    #TODO:add trycatch
    answer = input(">")
    room = rooms[room_name][int(answer)]
    next_room = room['next_room']
    if next_room == 'game_over':
        print("\n" + room['reason'])
        print("Game over, quedas expulsado de la FIB!")
        play_again()

    elif next_room == 'final_room':
        read_room(next_room)
        exit()
    elif next_room == 'putin_room':
        print("Has causado un bucle de amor a Rusia.")
        while True:
            print("Родина Россия")
    else:
        access_room(next_room)

def play_again():
    route = './rooms/play_again.txt'
    file = open(route, 'r')
    print(file.read())
    
    answer = input(">")
     
    if (answer == "1"):
    # if player typed "1" lead him to start()
        exit()
    else:
    # if user types anything besides "0" or "2", exit() the program        
        access_room('start')
access_room('start')