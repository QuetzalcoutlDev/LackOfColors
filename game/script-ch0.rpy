
label ch_0:
    
    scene black
    pause 2.0
    window auto
    $ quick_menu = True
    "¿Imaginan levantarse y ver que lo más notorio en este mundo simplemente ya no está?"
    "O simplemente carece de ese tono caracteristico que ayuda a ver este que lugar no es-"
    pause 1.5
    "No se como describirlo."
    "Pero simplemente eso ya no estaba."
    "Sin razón alguna."
    "O no una que pudiera encontrar al principio."
    window hide(dissolve)
    pause 2.0
    scene bg ai_room with dissolve
    play audio clock_alarm
    pause 2.0
    ai "{i}*bostezo*{/i}"
    show ai agh2 at cso11
    ai "Si, ya voy."
    play music m1 fadein 1.5
    show ai agh3
    "Mi nombre es Ai Tanaka."
    "Una chica de 21 años común y corriente que se levanta todos los días para ir a la universidad."
    "A excepción de los fines de semana claro esta."
    "Todo normal."
    "¿Verdad?"
    pause 1.0
    ai hmm4 "A veces no se si quiero ir o no a la universidad."
    ai hmm2 "¿Por qué los lunes en la mañana tienen que ser las clases?"
    show ai hmm1
    "Se lo que se siente."
    "Estoy como cierto gato que odia los lunes."
    ai agh5 "{i}*suspiro*{/i}"
    ai "Agh."
    ai hmm2 "No debi dormirme tan tarde."
    ai "Siento como si no hubiera dormido."
    show ai hmm1
    "Normalmente evito mis responsabilidades jugando o dibujando o haciendo otra actividad que no sea hacer mi tarea primero."
    "Si, sueno bastante patetica."
    "Pero oye, siempre pasa que de un día para otro termino haciendo las tareas."
    "¿Eso esta bien?"
    "Sinceramente no."
    ai normal2 "Bueno, será mejor que vaya a la sala."
    ai "No se que hora es."
    hide ai
    "Caminando a la puerta de mi cuarto me doy cuenta de algo."
    ai "¿Por qué todo se ve tan descolorido?"
    stop music fadeout 2.0
    "Mirando a los lados veo que todo mi cuarto carece de algún tipo de color."
    show ai surprise1 at lio11
    ai "¡¿Qué car#j04?!"
    "¿Por qué mi cuarto esta tan descolorido?"
    "¿Lo pintaron sin yo darme cuenta?"
    ai normal6 "Vamos, esto debe ser una broma de mal gusto."
    ai normal2 "Pero..."
    show ai hmm1
    "Un sentimiento de que algo no esta bien comienza a apoderarse de mi."
    "No se porque pero solo comienzo a sentirme bastante insegura."
    "¿Qué pasa?"
    ai happy4 "Vamos Ai solo calmate."
    ai "Esto tiene que ser normal, ¿verdad?"
    show ai happy3
    "¿Verdad?"
    pause 2.0
    hide ai
    "Sin razón alguna comienzo a caminar hacia la ventana de mi cuarto."
    pause 1.0
    "Para darme cuenta de que-"
    show ai surprise1 at lio11
    ai "¡¿QUE CAR#J04?!"
    ai "No no no no no, esto no puede estar pasando."
    play music m1 fadein 1.5
    show ai surprise1 at j11
    ai "¿Por qué todo esta gris?"
    show ai surprise1 at j11
    ai "¿Donde están los colores?"
    show ai surprise1 at j11
    ai "Cuan- {nw=1}"
    show ai surprise1 at j11
    extend "cuando, ¿Cuando paso esto?"
    show ai surprise1 at j11
    ai "¿Por qué paso?"
    ai happy5 "Vamos Ai, calmate."
    ai "Esto debe ser normal, ¿Verdad?"
    pause 1.0
    show ai happy4 at j11
    ai "¿Verdad?"
    ai "...."
    show ai happy3 at cso11
    "Jajaj, seguro esto debe ser un sueño."
    "Si seguro."
    "¿O estare bajo la influencia de algún quimico?"
    "..."
    "Pero si yo no-"
    "..."
    "Mejor descarto eso, no soy de hacer eso."
    "Mmm..."
    ai happy4 "Seguro no soy la unica que ve todo gris, ¿verdad?"
    pause 1.0
    "Creo que deberia pensar si mi máma también esta pasando por este problema."
    ai hmm1 "Seguro, mi máma también esta pasando por esto."
    window hide(Dissolve(.2))
    hide ai
    pause 1.5
    scene bg ai_livingroom with hgradient_right
    pause 1.5
    window auto
    show shiori normal1 at cso11
    shiori "Buenos dias hija."
    show shiori idle
    ai "Buenos dias máma."
    "Ella es mi madre Shiori Tanaka."
    $ _shiori_name = _("Shiori")
    "Tiene 40 años."
    "Es muy protectora conmigo y suele ser muy calmada en lo que dice y hace."
    "También es bastante sabia, un dato interesante de ella que pueden tener en cuenta."
    shiori normal1 "¿Dormiste bien?"
    show shiori idle
    ai "Si, algo."
    ai "Aunque me siento un poco cansada."
    shiori hmm4 "No tener un control de tu hora de sueño, trae consigo estos problemas."
    show shiori hmm3
    ai "Si lo se máma, me lo dices a menudo."
    shiori hmm0 "Si es correcto, pero no veo que hagas caso a eso."
    ai "Si, perdón."
    shiori idle "Procura buscar un horario de sueño optimo, asi dormiras bien."
    shiori normal1 "Bueno, antes de que te vayas a la universidad, ¿Puedes ir a la tienda?"
    shiori "Necesito algunas cosas."
    show shiori idle
    ai "Claro."
    "No se si es que ella se está tomando con calma esto de que todo está gris..."
    "No se si preguntarle."
    pause 1.5
    "Veo en la mesa del comedor un objeto que no recuerdo haber visto antes."
    show caja at objectShow
    "Parece una caja de algún color que ahora no puedo notar."
    "Seguro es un regalo o solo una caja común y corriente que no habia notado antes."
    hide caja
    "..."
    ai "Máma, ¿Puedo preguntarte algo?"
    shiori normal1 "Claro."
    shiori idle "¿Qué sucede?"
    ai "Bueno..."
    menu:
        "¿Le pregunto si ella puede ver el color de la caja?"
        "Preguntar.":
            ai "¿Qué es esa caja que está en la mesa?"
            shiori normal1 "Bueno, es un regalo para tu tía."
            shiori "Recuerda que hoy es su cumpleaños."
            show shiori idle
            ai "¿Y cual es el color de esa caja?"
            show shiori normal1 at j11
            shiori "Me hace gracia que preguntes eso."
            shiori "Es del color favorito de tu tía."
            show shiori idle
            ai "¿Y Cuál es color su favorito?"
            shiori normal2 "Hmm, su color favorito es el rosado."
            shiori "Crei que lo recordabas."
            ai "Perdon, se me habia olvidado."
            
        "Dejarlo pasar.":
            ai "Mejor no."
            ai "Ya se me olvido que te iba a preguntar."
            shiori normal2 "Hmm..."
            shiori "¿Enserio no me ibas a preguntar nada?"
            ai "No descuida, no era nada importante."
            "Creo que preguntarle eso directamente seria muy estupido."
            ai "Solo iba a preguntarte sobre esa caja que está en la mesa."
            shiori hmm0 "Tu debes saber para que es esa caja."
            ai "No se para que es."
            shiori normal1 "Esa caja contiene un regalo para tu tía, recuerda que hoy es su cumpleaños."
            show shiori idle
            ai "Vaya se me habia olvidado."
    shiori idle "Mientras tu tía no lo sepa esta bien."
    shiori sad2 "Hasta yo a veces lo olvido."
    shiori "No se lo cuentes."        
    pause 1.0
    shiori normal1 "Bueno, en lo que estaba."
    shiori "Necesito que vayas a la tienda."
    show shiori idle
    ai "Si verdad, ¿Qué necesitas que compre?"
    shiori normal1 "Bueno, son algunos ingredientes para algunos pastelillos que hare para el evento de encendido de luces de hoy."
    show shiori idle
    "Hoy es el encendido de luces en la plaza de la ciudad por el més de diciembre, mi máma todos los años ayuda en el evento cocinando algunos pastelillos y otros postres."
    "Me tenia que pasar hoy."
    shiori normal1 "Necesito 2 kilos de harina de trigo y un kilo de azúcar, los demás ingredientes ya los tengo."
    shiori normal3 "Por cierto, la harina de trigo tiene que ser de una marca en especifico."
    shiori normal1 "La ultima que compre era bastante buena, {nw=1.0}"
    extend normal3 "aunque no recuerdo su nombre."
    shiori "La bolsa es de color rojo,"
    shiori normal1 "En la mesa está el dinero."
    shiori "Apresurate porque no querrás llegar tarde a la universidad."
    show shiori idle
    ai "Vale, ya regreso."
    shiori normal1 "Te estare esperando."
    hide shiori
    stop music fadeout 2.0
    pause 2.5
    "¡¡¿¿PORQUE ME TIENE QUE PASAR ESTO??!!"
    "¿Por qué tenia que ser una harina en especifico?"
    "{i}*Suspiro{/i}"
    pause 2.0
    "¿Será muy complicado comprar sin poder ver los colores?"
    "Voy a tener que averiguarlo."
    pause 1.4
    play audio open_door
    scene bg ai_departament with hgradient_left_scene_full
    pause 1.0
    "Lo bueno es que la tienda está al lado del edificio en donde vivo."
    "Lo malo es que no se si sera dificil poder comprar sin ver los colores."
    "Que extraño es todo esto."
    pause 2.0
    scene bg store with hgradient_left_scene_full
    pause 3.0
    play audio store_ring
    scene bg convenience_store with hgradient_left
    pause 1.0
    show yu idle at cso11
    play music m2 fadein 2.0
    yu "Hola Ai, ¿En qué te puedo ayudar?"
    ai "Hola Yu, vine a comprar algunas cosas para los pastelillos que hara mi máma para el evento de encendido de luces."
    "Ella es Yu Ishikawa."
    "Trabaja en esta tienda de conveniencia."
    "Es una amiga y vecina."
    yu happy2 "Oh si, llevo esperando mucho tiempo el evento."
    yu "Quiero probar los pastelillos que tu máma prepara."
    show yu happy2 at j11
    yu "Es una de las cosas que más me gusta del evento."
    show yu happy1
    ai "Está vez no le faltan muchos ingredientes."
    yu idle "Eso es una buena noticia."
    yu normal1 "Asi está un poco más tranquila."
    yu "Bueno aunque no te distraigo más."
    yu idle "Si necesitas mi ayuda estoy aqui."
    ai "Claro, te pedire ayuda si necesito."
    "¿Será necesario que le pida ayuda?"
    "..."
    "Mejor intento a ver si puedo comprar asi como estoy ahora."
    hide yu
    pause 1.0
    scene bg convenience_store with hgradient_left_scene_full
    pause 1.0
    show ai hmm1 at cso11
    ai "Mi máma quiere dos kilos de harina de trigo."
    ai hmm2 "Y un kilo de azúcar."
    show ai hmm1
    "Se me hará más facil comprar la azúcar, eso claro está."
    hide ai
    pause 1.0
    "Mirando en uno de los estantes logro ver la azúcar."
    show azucar at objectShow
    "¿Con un kilo de azúcar se puede hacer todo lo que mi máma hace?"
    "..."
    "Seguro ya tiene más azúcar y pues solo le falta un kilo."
    hide azucar
    pause 1.0
    show ai hmm1 at cso11
    "Caminando alrededor del estante veo a la harina de trigo."
    ai "Okey..."
    ai hmm2 "Lo que me faltaba."
    hide ai
    show harina1 at objectShow
    "Las unicas harinas que puedo distinguir son practicamente del mismo color."
    hide harina1
    "O al menos de lo que puedo distinguir como color."
    show harina2 at objectShow
    "Solo logro ver que la de la izquierda es un poco más clara que la de la derecha."
    "¡¿Comó rayos voy a saber cual es la que quiere mi máma?!"
    "¿Por qué tenia que ser especifica?"
    hide harina2
    pause 1.0
    "¿Le pido ayuda a Yu?"
    "Hmm..."
    "Quizás decirle directamente lo del color seria un poco absurdo."
    "..."
    "Ya se."
    "Tomo las dos harinas y me dirijo a donde está Yu."
    pause 2.0
    ai "Yu, necesito hacerte una pregunta."
    show yu normal1 at cso11
    yu "Dime Ai, ¿Qué pasa?"
    show yu idle
    ai "¿Sabes cual es la harina que mi máma compro la ultima vez que vino aquí?"
    yu normal1 "Claro, ¿Ella te pidio una en especifico?"
    show yu idle
    ai "Si, no se cual fue la que compro."
    yu normal1 "Compro la que tienes en la mano izquierda."
    yu "Yo misma se la recomende."
    show yu idle
    show harina2 at objectShow
    "Asi que era la más oscura."
    "Que bueno que Yu recordaba cual era."
    "Me salvo."
    hide harina2
    ai "Muchas gracias Yu."
    ai "Me salvaste de que mi máma se enojara jeje."
    yu happy2 "Descuida, para eso estoy aqui."
    yu normal1 "¿Eso es todo lo que vas a llevar?"
    show yu idle
    ai "Si, es todo."
    "Procedo a darle el dinero a Yu."
    pause 1.0
    yu normal1 "Muchas gracias por venir Ai."
    yu happy2 "Ten un lindo día."
    show yu happy1
    ai "Igualmente."
    pause 0.5
    "Este día será fatal, lo se."
    "Si no logro descubrir porque me paso esto, no se que hare."
    stop music fadeout 2.0
    pause 2.4
    scene bg store with hgradient_left_scene_full
    pause 1.0
    "Saliendo de la tienda comienzo a sentir algo extraño."
    show vignette2 onlayer effects 
    with dissolve 
    "Me siento..."
    "¿Decaida?"
    "Es una sensación super rara."
    "La puedo describir como un sentimiento de pesadez extraño."
    "Pero a la vez es como si algo me oprimiera el pecho."
    hide vignette2 with Dissolve(1.6)
    pause 2.0
    "Pasaron unos momentos y esa sensación se fue..."
    ai "{i}*Suspiro*{/i}"
    ai "Eso nunca antes habia pasado."
    ai "Espero que no sea nada malo."
    pause 1.6
    show bg ai_departament with hgradient_left_scene_full
    pause 2.0
    ""

    return