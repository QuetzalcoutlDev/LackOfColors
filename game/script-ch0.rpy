
label ch_0:
    
    scene black
    pause 2.0
    window auto
    $ quick_menu = True
    "¿Imaginan levantarse y ver que lo más notorio en este mundo simplemente ya no está?"
    "O simplemente carece de ese tono característico que ayuda a ver este qué lugar no es un-"
    pause 1.5
    "Realmente no se como describirlo."
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
    "A excepción de los fines de semana claro está."
    "Todo normal."
    "¿Verdad?"
    pause 1.0
    ai hmm4 "A veces no se si quiero ir a la universidad."
    ai hmm2 "¿Por qué los lunes en la mañana tienen que ser las clases?"
    show ai hmm1
    "Si, estoy como cierto gato que odia los lunes."
    "A veces es muy molesto levantarse temprano para ir a la universidad después de un día de descanso."
    ai agh5 "{i}*Suspiro*{/i}"
    ai hmm2 "No debí dormirme tan tarde."
    ai "Siento como si no hubiera dormido nada."
    show ai hmm1
    "Normalmente evito mis responsabilidades jugando o dibujando o haciendo otra actividad que no sea hacer mi tarea primero."
    "Si, sueno bastante patética."
    "Pero oye, siempre pasa que de un día para otro termino haciendo las tareas."
    "¿Eso está bien?"
    "Sinceramente no."
    ai normal2 "Bueno, será mejor que vaya a la sala."
    ai "¿Qué hora será?"
    hide ai
    pause 0.5
    "Caminando a la puerta de mi cuarto me doy cuenta de algo."
    ai "¿Por qué todo se ve tan descolorido?"
    stop music fadeout 2.0
    "Mirando mi alrededor puedo notar que todo mi cuarto carece de algún tipo de color."
    show ai surprise1 at lio11
    ai "¡¿Qué car#j04?!"
    "¿Por qué mi cuarto está tan descolorido?"
    "¿Lo pintaron sin darme cuenta?"
    ai normal6 "Vamos, esto debe ser una broma de mal gusto."
    ai normal2 "Pero..."
    show ai hmm1
    "Un sentimiento de que algo raro está pasando comienza a apoderarse de mi."
    "No se porque pero solo comienzo a sentirme bastante insegura."
    ai happy4 "Vamos Ai, solo calmate."
    ai "Esto tiene que ser normal, ¿verdad?"
    show ai happy3
    pause 1.5
    "¿Verdad?"
    pause 2.0
    hide ai
    "Queriendo buscar una razón, solo me cruza la idea de caminar hacia a la ventana de mi cuarto..."
    "Solo para buscar una razón..."
    pause 1.0
    "Para darme cuenta de que-{w=2.0}{nw}"
    show ai surprise1 at lio11
    ai "¡¿QUE CAR#J04?!"
    ai "No no no no no, esto no puede estar pasando."
    play music m1 fadein 1.5
    show ai surprise1 at j11
    ai "¿Por qué todo está gris?"
    show ai surprise1 at j11
    ai "¿Donde están los colores?"
    show ai surprise1 at j11
    ai "Cuan- {nw=1}"
    show ai surprise1 at j11
    extend "cuando, ¿Cuando paso esto?"
    show ai surprise1 at j11
    ai "¿Por qué pasó?"
    pause 1.0
    show ai happy5 at cso11
    with Dissolve(0.6)
    ai "Vamos Ai, calmate."
    ai "Esto debe ser normal, ¿Verdad?"
    pause 1.0
    show ai happy4 at j11
    ai "¿Verdad?"
    ai "...."
    show ai happy3 at cso11
    "Jajaja, seguro esto debe ser un sueño."
    "Si, seguro lo es."
    "¿O estaré bajo la influencia de alguna droga?"
    "..."
    "Pero si yo no-"
    "..."
    "Mejor descarto eso, no soy de hacer eso."
    "Mmm..."
    ai happy4 "Seguro no soy la unica que ve todo gris, ¿verdad?"
    pause 1.0
    "Creo que debería pensar si mi máma también está pasando por este problema."
    ai hmm1 "Espero no ser la única que pasa por esto."
    ai "Aunque si esto es una pesadilla seguro despertare en algún momento."
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
    shiori idle "Procura buscar un horario de sueño óptimo, asi dormiras bien."
    shiori normal1 "Bueno, antes de que te vayas a la universidad necesito un favor tuyo."
    show shiori idle
    ai "¿Y que necesitas?"
    shiori normal1 "Necesito que vayas a la tienda."
    shiori "Quiero que me compres algunas cosas."
    show shiori idle
    ai "Claro."
    ai "Solo dime que quieres que compre."
    "Se está tomando con calma esto de que todo está gris..."
    "¿Soy la única que ve todo así acaso?"
    "..."
    "No se si preguntarle."
    pause 1.5
    "Veo en la mesa del comedor un objeto que no recuerdo haber visto antes."
    show caja at objectShow
    "Parece una caja de algún color que ahora no puedo notar."
    "Seguro es un regalo o solo una caja común y corriente que no había notado antes."
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
            "Claro, porque es ridículo preguntar el color de algo."
            shiori "Es del color favorito de tu tía."
            show shiori idle
            ai "¿Y cuál es su color favorito?"
            shiori normal2 "Mm, su color favorito es el rosado."
            shiori "Creí que lo recordabas."
            shiori "Es bastante raro que también preguntes el color de la caja."
            ai "Perdón, es que mi pregunta era para saber cuál era el color favorito de mi tía."
            ai "Es que lo había olvidado."
        "Dejarlo pasar.":
            ai "Mejor no."
            ai "Ya se me olvido que te iba a preguntar."
            shiori normal2 "Hmm..."
            shiori "¿Enserio no me ibas a preguntar nada?"
            ai "No descuida, no era nada importante."
            "Creo que preguntarle eso directamente sería muy estupido."
            ai "Solo iba a preguntarte sobre esa caja que está en la mesa."
            shiori hmm0 "Tu debes saber para qué es esa caja."
            ai "No sé para qué es."
            shiori normal1 "Esa caja contiene un regalo para tu tía, recuerda que hoy es su cumpleaños."
            show shiori idle
            ai "Vaya se me había olvidado."

    shiori idle "Mientras tu tía no lo sepa esta bien."
    shiori sad2 "Hasta yo a veces lo olvido."
    shiori "No se lo cuentes."    
    pause 1.0
    shiori normal1 "Bueno, en lo que estaba."
    shiori "Necesito que vayas a la tienda."
    show shiori idle
    ai "Sí verdad, ¿Qué necesitas que compre?"
    shiori normal1 "Bueno, son algunos víveres que faltan para los pastelillos que haré para el evento de encendido de luces de hoy."
    show shiori idle
    "Hoy es el encendido de luces en la plaza de la ciudad por navidad, mi mamá todos los años participa en el evento cocinando algunos pastelillos y otros postres."
    shiori normal1 "Necesito 2 kilos de harina de trigo y un kilo de azúcar, los demás ingredientes ya los tengo."
    shiori normal3 "Por cierto, la harina de trigo tiene que ser de una marca en específico."
    shiori normal1 "La ultima que compre era bastante buena, {nw=1.0}"
    extend normal3 "aunque no recuerdo su nombre."
    shiori "El color del paquete de la que compre era de color rojo,"
    shiori normal1 "En la mesa está el dinero."
    shiori "Apresúrate porque no querrás llegar tarde a la universidad."
    show shiori idle at cso11
    ai "Vale, ya regreso."
    shiori normal1 "Te estare esperando."
    hide shiori
    stop music fadeout 2.0
    pause 2.5
    "¡¡¿¿PORQUE ME TIENE QUE PASAR ESTO??!!"
    "¿Por qué tiene que ser una harina en específico?"
    "¿No puede ser una harina común y corriente?"
    "{i}*Suspiro*{/i}"
    pause 2.0
    "Voy a tener que intentar comprar en está situación."
    "¿Será muy complicado sabiendo que no puedo ver los colores?"
    "Voy a tener que averiguarlo."
    "{i}*Suspiro*{/i}"
    "Que situación tan complicada y extraña."
    pause 1.4
    play audio open_door
    scene bg ai_house with hgradient_left_scene_full
    pause 1.0
    "Lo bueno es que la tienda está prácticamente a la vuelta de la esquina."
    "Lo malo es que no sé si será difícil poder comprar sin ver los colores."
    "Lo he vuelto a decir, pero es super extraño esto que está pasando."
    "Así que simplemente no se que pensar o decir."
    pause 2.0
    scene bg convenience_store with hgradient_left_scene_full
    pause 3.0
    play audio store_ring
    scene bg store with hgradient_left
    pause 1.0
    show yu idle at cso11
    play music m2 fadein 2.0
    yu "Bienvenido/a a la tienda."
    yu normal1 "Oh{w=1.0}{nw}"
    show yu normal1 at j11
    extend ", hola Ai, ¿En qué te puedo ayudar?"
    show yu idle
    ai "Hola Yu, vine a comprar algunas cosas para los pastelillos que hara mi máma para el evento de encendido de luces."
    $ _yu_name = _("Yu")
    "Ella es Yu Ishikawa."
    "Trabaja en está tienda de conveniencia."
    "También es una amiga y vecina."
    yu happy2 "Que bien, llevo esperando mucho tiempo el evento."
    yu "Quiero probar los pastelillos que tu máma prepara."
    show yu happy2 at j11
    yu "Es una de las cosas que más me gusta del evento."
    show yu happy1 at cso11
    ai "Está vez no le faltan muchos ingredientes."
    ai "También cambió la receta de los mismos."
    yu idle "Eso es una buena noticia."
    yu normal1 "Imagino que ahora son mejores de lo que ya los eran."
    show yu idle
    ai "Claro, te sorprenderá lo buenos que son ahora."
    yu normal1 "Bueno, aunque no te distraigo más."
    yu idle "Si necesitas mi ayuda estoy aquí."
    ai "Claro, lo tendre en cuenta."
    pause 1.0
    show yu idle at cso11
    hide yu
    "¿Será necesario que le pida ayuda?"
    "..."
    "Mejor intento a ver si puedo comprar así como estoy ahora."
    pause 1.0
    scene bg store with hgradient_left_scene_full
    pause 1.0
    show ai hmm1 at cso11
    ai "Mi máma quiere dos kilos de harina de trigo."
    ai hmm2 "Y un kilo de azúcar."
    show ai hmm1
    "Se me hará más fácil comprar el azúcar, eso claro está."
    hide ai
    pause 1.0
    "Mirando en uno de los estantes logro ver el azúcar."
    show azucar at objectShow
    "¿Con un kilo de azúcar se puede hacer todo lo que mi máma hace?"
    "..."
    "Seguro ya tiene más azúcar y pues solo le falta un kilo."
    hide azucar
    pause 1.0
    show ai hmm1 at cso11
    "Caminando alrededor del estante veo la harina de trigo."
    ai "Okey..."
    ai hmm2 "Lo que me faltaba."
    hide ai
    show harina1 at objectShow
    "Las únicas harinas que puedo distinguir son prácticamente del mismo color."
    hide harina1
    "O al menos de lo que puedo distinguir como color."
    show harina2 at objectShow
    "Solo logro ver que la de la izquierda es un poco más clara que la de la derecha."
    "¡¿Cómo rayos voy a saber cual es la que quiere mi máma?!"
    "¿Por qué tenía que ser específica?"
    hide harina2
    pause 1.0
    "¿Le pido ayuda a Yu?"
    "Hmm..."
    "Quizás decirle directamente lo del color sería un poco absurdo."
    "..."
    "Ya se."
    "Tomo las dos harinas y me dirijo a donde está Yu."
    pause 2.0
    ai "Yu, necesito hacerte una pregunta."
    show yu normal1 at cso11
    yu "Dime Ai, ¿Qué pasa?"
    show yu idle
    ai "¿Sabes cual es la harina que mi máma compro la ultima vez que vino aquí?"
    yu normal1 "Claro, ¿Ella te pidió una en específico?"
    show yu idle
    ai "Si, no se cual fue la que compro."
    yu normal1 "Compró la que tienes en la mano izquierda."
    yu "Yo misma se la recomende."
    show yu idle
    show harina2 at objectShow
    "Así que era la más oscura."
    "Que bueno que Yu recordaba cual era."
    "Me salvo."
    hide harina2
    ai "Muchas gracias Yu."
    ai "Me salvaste de que mi máma se enojara jeje."
    yu happy2 "Descuida, para eso estoy aquí."
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
    "Este día será fatal, lo sé."
    "Si no logro descubrir porque me paso esto, no se que haré."
    stop music fadeout 2.0
    pause 2.4
    scene bg convenience_store with hgradient_left_scene_full
    pause 1.0
    "Saliendo de la tienda comienzo a sentir algo extraño."
    show vignette2 onlayer effects
    show black2 onlayer effects2
    with dissolve
    play music terrorGround fadein 2.0
    "Me siento..."
    "¿Decaída?"
    "Es una sensación súper rara."
    "La puedo describir como un sentimiento de pesadez extraño."
    "Pero a la vez es como si algo me oprimiera el pecho."
    "Es realmente indescriptible."
    hide vignette2 onlayer effects
    hide black2 onlayer effects2
    with Dissolve(1.6)
    stop music fadeout 2.0
    pause 2.0
    "Pasaron unos momentos y esa sensación se fue..."
    ai "{i}*Suspiro*{/i}"
    ai "Eso nunca antes había pasado."
    ai "Espero que no sea nada malo."
    pause 1.6
    show bg ai_house with hgradient_left_scene_full
    pause 2.0
    "Sinceramente no se que fue esa sensación de hace rato."
    "Nunca la había experimentado antes."
    "Espero que no se vuelva a repetir."
    pause 1.0
    play audio open_door
    show bg ai_livingroom with hgradient_left
    pause 1.0
    play music m1 fadein 2.0
    pause 0.25
    show shiori idle at cso11
    shiori "Hola de nuevo hija."
    ai "Hola de nuevo máma..."
    ai "Aqui traigo lo que pediste."
    shiori normal1 "Excelente."
    shiori "Ahora si podré terminar los pastelillos."
    shiori reflexive1 "Se que ha todos les sorprenderá mi nueva receta."
    ai "¿Para eso era la harina que querías?"
    show shiori normal1 at j11
    shiori "Pues claro."
    shiori "Esa harina, dejo los últimos pastelillos que hice con una consistencia realmente agradable."
    shiori idle "Es realmente buena."
    "Hace como dos semanas mi mamá hizo unos pastelillos para probar su nueva receta."
    "No lo recordaba, pero ahí está el dato."
    ai "¿Y cuantos pastelillos pretendes hacer?"
    shiori hmm0 "Los que pueda hacer."
    shiori normal1 "Jeje."
    shiori "Hare los que pueda..."
    shiori idle "Por cierto...{w=1.0}{nw}"
    shiori "Se te va a hacer tarde para ir a la universidad, será mejor que desayunes de una vez."
    ai "Es cierto."
    ai "Casi lo olvidaba."
    stop music fadeout 1.5
    window hide(Dissolve(.2))
    show shiori idle at cso11
    hide shiori
    pause 1.0
    scene black with Dissolve(2.0)
    pause 1.0
    window auto
    "Mi máma y yo nos sentamos a comer."
    "Mientras comíamos me comenzó a hacer preguntas que siempre hace."
    "¿Qué si tengo novio? o si ¿Por qué no salgo mucho?"
    "En fin, preguntas que toda mamá hace..."
    "A veces me incomodan, pero sinceramente..."
    "No me molesta que las haga."
    "Sería malo que no me las haga."
    "¿Me entienden?"
    window hide(Dissolve(.2))
    pause 2.0
    scene bg ai_livingroom with hgradient_left
    pause 1.0
    window auto
    "Casi terminando de comer, le hice una pregunta a mi máma."
    show shiori idle at cso11
    play music m2 fadein 1.5
    pause 1.0
    ai "Máma, ¿Te puedo hacer una pregunta?"
    shiori normal1 "Claro hija, no tienes porque preguntarme."
    show shiori idle
    ai "Bueno, es que solo para que lo supieras."
    ai "Bueno..."
    ai "¿Si alguna vez despertarás sin poder ver los colores que harias?"
    shiori normal2 "Hmm..."
    shiori normal4 "Bueno..."
    shiori "Es un poco extraña la pregunta."
    shiori normal1 "Pero te respondere con esto..."
    shiori "Rojo, verde y azul son los colores de la luz, si ellos no están pues los reemplazarán el blanco y el negro."
    ## Nota de Quetzalcoutl: Yo me sorprendí al enterarme de eso jeje
    $ renpy.notify(_("El blanco, negro y gris no son colores, ellos son 'Acromaticos' que significa literalmente 'Sin color'\nEsto porque carecen de tono o saturación, pero comumente los seguimos llamando colores."))
    shiori "Estos últimos no son colores por ende todo se verá gris."
    shiori idle "Si en el hipotetico caso que dejara de ver los colores, primero me sorprenderia..."
    shiori normal1 "Seria una situación que me dejaria realmente confundida y asustada..."
    shiori "Solo me preguntaria.. ¿Por qué?"
    shiori normal2 "Bueno..."
    shiori "Pensar en las razones porque me paso también seria lo indicado..."
    "Todo lo que hice."
    shiori normal4 "Aunque...{w=1.0}{nw}"
    extend normal3 "Pues también pensaria en...{w=2.0}{nw}"
    shiori sad2 "Disculpa hasta yo misma me confundi."
    shiori idle "Bueno..."
    shiori "Si yo me despertara sin poder ver los colores,{nw}" 
    extend normal1 " solo estaria confundida jeje."
    shiori "Aunque eso de ver todo gris es algo que no puede pasar realmente."
    shiori idle "Pero si, si me pasara eso me dejaria realmente confundida y asustada."
    shiori normal1 "¿Eso responde tu pregunta?"
    shiori sad2 "Aunque no creas que no estoy un poco confundida con tu pregunta y mi respuesta."
    shiori idle "Pensaré en una mejor después."
    shiori normal1 "Así que dime...{w=1.0}{nw}"
    extend "¿Eso responde tu pregunta?"
    ai "Bueno..."
    "Dijo exactamente lo que he hecho."
    "Está es una situación realmente confusa."
    "Pero puedo confirmar que mi mamá no está pasando por esto."
    ai "Si, si la responde"
    shiori normal1 "Me alegro."
    shiori normal2 "Aunque es realmente rara."
    shiori "¿Tienes algo que quieras contarme?"
    shiori "Si algo te pasa no dudes en decirme."
    shiori sad3 "Soy tu madre.."
    shiori "Recuerda que puedes confiar en mi."
    ai "No no, no me pasa nada."
    show shiori normal2
    ai "Jeje."
    ai "Solo es algo que quería preguntarte desde hace rato."
    shiori normal1 "Bueno, espero haber resolvido tu duda."
    shiori sad2 "Aunque cuando encuentre una mejor respuesta te dire."
    shiori normal1 "Por cierto, te recuerdo que ahora si puedes llegar tarde a la universidad si no te apresuras."
    show shiori idle
    ai "Ah, es cierto."
    ai "Ire a cambiarme."
    shiori normal1 "Vale te espero."
    hide shiori
    window hide(Dissolve(.2))
    stop music fadeout 1.5
    scene bg ai_room with hgradient_left_scene_full
    pause 1.0
    window auto
    "Mi máma respondió lo mismo que he hecho."
    "Bueno, al menos puedo saber que hasta ella quedaria confundida con algo asi."
    play music m1 fadein 2.0
    show ai meh1 at cso11
    ai "Aunque me gustaria saber la razón por la cual me ocurrio esto."
    pause 1.0
    ai meh2 "Realmente no puedo pensar en algo que lo explique."
    show ai meh1
    "Espero poder ver los colores nuevamente."
    "Ojala esto sea momentaneo..."
    "La unica razón que puedo pensar que haya causado esto es que esta bajo la influencia de una droga.."
    "Aunque..."
    "Mejor la descarto, no soy de hacer eso."
    "..."
    pause 1.0
    ai angry2 "Mejor me apresuro..."
    ai "Si me quedo aquí parada pensando en nada voy a llegar tarde."
    ai idle "Asi que ire a cambiarme."
    ai hmm1 "Aunque..."
    "Si se que me estoy olvidando de algo.."
    pause 2.0
    show ai hmm4
    "Si, debería ir a bañarme primero."
    ai agh4 "{i}*Suspiro*{/i}"
    ai angry2 "Voy a llegar súper tarde."
    show ai angry2 at cso11
    hide ai
    window hide(Dissolve(.5))
    pause 1.0
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 1.0
    play sound shower
    pause 9.0
    $ print("Si, Ai ya se baño")
    pause 1.0
    stop sound
    scene bg ai_room with hgradient_left
    window auto
    pause 1.0
    play music m3 fadein 2.0
    "Bueno, ahora me vestiré."
    ai "Viendo la hora, me queda tiempo."
    "Creo."
    ai "Si me apresuro si llegare temprano."
    ai "Bueno..."
    ai "¿Donde está mi ropa?"
    "Buscando en lo que puedo decir que es como un armario, me doy cuenta de algo..."
    ai "¡¡¡¡TODO ESTÁ GRIS!!!!!!{w=1.5}{nw}"
    ai "¡¡¡¡¿COMO VERE QUE ROPA PONERME?!!!!{w=1.5}{nw}"
    ai "¡¡¡C4R4J0OOO!!!!"
    ai "Aho-{nw}"
    "Me acabo de dar cuenta que acabo de gritar eso en voz alta."
    pause 1.0
    shiori "Hija, ¿Todo bien?"
    shiori "Oí un grito..."
    ai "¡No pasó nada!"
    ai "¡Descuida!"
    shiori "¿En Serio estás bien?"
    ai "¡Si si, estoy bien!"
    shiori "Bueno..."
    shiori "Si tu lo dices."
    ai "¡Descuida, no te preocupes!"
    shiori "Está bien.."
    shiori "Apresúrate si no quieres llegar tarde."
    ai "¡Vale, ya salgo!"
    pause 2.0
    "Eso estuvo cerca."
    "Que bueno que no escucho lo que dije."
    "Al menos eso creo..."
    pause 1.0
    "..."
    ai "Bueno..."
    ai "¿Ahora que hago?"
    pause 2.0
    "..."
    "Viendo mi 'armario', puedo recordar la ropa que me he puesto."
    "{i}Como toda persona...{/i}"
    ai "{i}*Suspiro*{/i}"
    ai "Vere que ropa me puedo poner..."
    window hide(Dissolve(.5))
    pause 1.0
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 2.0
    scene bg ai_room with Dissolve(1.0)
    pause 1.0
    window auto
    pause 1.0
    show ai casual idle at cso11
    ai "Bueno, ya estoy lista."
    "No soy una experta cuando se trata de escoger ropa."
    "Pero en está situación simplemente no me puedo poner a pensar en esas cosas."
    ai casual normal4 "No es la mejor elección, pero recuerdo como iban sus colores."
    ai "Asi que mal no me veo."
    show ai casual meh1
    "A veces me critico a mi misma por mi aspecto."
    "Quizás es algo normal..."
    "Aunque lo dudo, pero simplemente pienso de esa manera a veces."
    "No puedo evitar tener pensamientos intrusivos."
    "Aunque me pasa cada cierto tiempo, lo mejor que hago es ignorarlos."
    play music m3 fadein 1.7
    ai casual normal2 "Creo que mejor salgo del cuarto."
    show ai casual normal2 at cso11
    hide ai
    pause 1.0
    "Después de recoger mis cosas me dirijo a la sala."
    pause 1.0
    scene bg ai_livingroom with hgradient_left
    pause 1.0
    show shiori idle at cso11
    shiori "Hola de nuevo hija, ¿Ya te vas?"
    ai "Si, espero poder llegar temprano."
    shiori normal1 "No seas pesimista, aun te queda tiempo."
    shiori "Si sales ahora llegaras temprano."
    show shiori idle
    ai "Bueno, entonces..."
    ai "Me iré ahora jeje."
    shiori normal1 "No te detengo más."
    show shiori idle
    ai "Adiós máma."
    shiori normal1 "Que te vaya bien."
    shiori normal3 "Recuerda que si necesitas hablar de algo..."
    shiori "No dudes en hablarme."
    show shiori normal2
    ai "Descuida máma, no pasa nada."
    "¿Qué tan extraña fue mi pregunta?"
    "La verdad no lo sé..."
    "...."
    ai "Ahora si me voy."
    shiori normal1 "Adiós hija."
    show shiori idle at cso11
    hide shiori
    stop music fadeout 1.6
    pause 2.0
    "Mientras camino hacia la puerta solo logró intentar pensar en que me puede deparar este día tan extraño."
    pause 1.0
    scene bg ai_house with hgradient_left_scene_full
    pause 1.0
    ai "Siento que me estoy tomando con mucha calma esto de no poder ver los colores."
    ai "¿Verdad?"
    ai "Jaja."
    pause 1.0
    "Mejor dejo de hablar conmigo misma y comienzo a caminar."
    pause 1.0
    scene bg crossing_city with hgradient_left_scene_full
    pause 1.0
    play music m1 fadein 2.0
    pause 1.0
    "Me tengo que dirigir a la estación de trenes para cruzar la ciudad e ir a la universidad."
    "A veces voy en camión, pero creo que no es importante hablar de eso ahora..."
    pause 2.0
    "Caminando por la calle, hacia el cruce peatonal para ir hacia la calle que me lleva a la estación..."
    "Valga la redundancia..."
    "Me doy cuenta de algo que realmente puede ser muy malo en este preciso momento..."
    ai "Entonces se pone cada vez más raro..."
    show semaforo at objectShow
    pause 1.0
    "Ahora no puedo ver si el semáforo está en rojo para poder caminar."
    hide semaforo
    ai "{i}*Suspiro*{/i}"
    pause 1.0
    "Aunque..."
    "No todo está perdido."
    ai "Ahora me siento estupida..."
    "Si la forma de saber que está en rojo es viendo si los autos están detenidos."
    ai "Solo tengo que esperar un rato..."
    pause 1.0
    window hide(Dissolve(.4))
    scene bg crossing_city with hgradient_left_scene_full
    pause 1.0
    window auto
    "Pasó alrededor de un minuto cuando por fin el semáforo se puso en rojo."
    "Mejor dicho, que los autos se detuvieron..."
    "Por ende pues el semáforo está en rojo."
    ai "Por fin..."
    "Comienzo a caminar hacia la otra acera para dirigirme hacia la calle donde está la estación de trenes."
    "No está muy lejos de mi casa, por eso voy caminando todos los días hacia ella..."
    pause 2.0
    scene bg city_station with hgradient_left_scene_full
    pause 1.0
    ai "Bueno, por fin llegue..."
    ai "Aun me queda tiempo para llegar."
    "A veces llego tarde pero pues hoy no será el caso..."
    "..."
    ai "Solo me queda abordar el tren e ir..."
    pause 1.0
    stop music fadeout 2.0
    pause 2.0
    ai "Hoy realmente será un día extraño..."
    ai "No se como estar todo el día sin poder ver los colores..."
    window hide(Dissolve(.3))
    pause 1.0
    scene black with Dissolve(2.0)
    pause 1.0
    window auto
    pause 0.5
    "Al subirme al tren, comienzo a pensar en una razón de porqué pasó esto..."
    "Simplemente no se que pensar de todo está situación..."
    "¿Qué harían si de la nada dejaran de ver los colores?"
    "¿Cómo actuarían?"
    "Yo al menos no sé cómo actuar."
    "Esto me ha dejado súper confundida."
    "Solo tendré que esperar..."
    "A que me llegue una respuesta..."
    "O despertar de esto, que puedo o no..."
    "Llamar pesadilla..."
    window hide(Dissolve(.3))
    pause 2.0
    $ persistent.capListComplete["cap0"] = True

    return