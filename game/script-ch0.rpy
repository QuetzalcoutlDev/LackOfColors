
label ch_0:
    scene black
    pause 2.0
    window auto
    $ quick_menu = True
    "¿Os imagináis levantaros y ver que lo más destacado en este mundo simplemente ya no está?"
    "O simplemente le falta ese tono característico que ayuda a ver que este lugar no es un-"
    pause 1.5
    "Podría decirse que es difícil de poner en palabras."
    "Pero simplemente eso ya no existía."
    "Sin motivo alguno."
    "O al menos ninguno que pudiera encontrar al principio."
    window hide(dissolve)
    pause 2.0
    scene bg ai_room with dissolve
    play audio clock_alarm
    pause 2.0
    ai "{i}*bostezo*{/i}"
    show ai agh2 at cso11
    ai "Vale, ya voy."
    play music m1 fadein 1.5
    show ai agh3
    "Me llamo Ai Tanaka."
    "Una chica de 21 años normal que se levanta todos los días para ir a la universidad."
    "Excepto los fines de semana, por supuesto."
    "Todo normal."
    "¿Verdad?"
    pause 1.0
    ai hmm4 "A veces no estoy segura si quiero ir a la universidad."
    ai hmm2 "¿Por qué tienen que ser las clases los lunes por la mañana?"
    show ai hmm1
    "Sí, estoy como cierto gato que odia los lunes."
    "Es bastante molesto levantarse temprano para ir a la universidad después de un día de descanso."
    ai agh5 "{i}*Suspiro*{/i}"
    ai hmm2 "Quizás no debí acostarme tan tarde."
    ai "Me siento como si no hubiera dormido en absoluto."
    show ai hmm1
    "Por lo general, evito mis responsabilidades jugando, dibujando u haciendo otra actividad en lugar de hacer mi tarea primero."
    "Si, sueno bastante patética."
    "Pero ¿sabes qué? Siempre termino haciendo las tareas de un día para otro."
    "¿Eso está bien?"
    "Sinceramente, no."
    ai normal2 "Bueno, será mejor que vaya a la sala."
    ai "¿Qué hora será?"
    hide ai
    pause 0.5
    "Caminando hacia la puerta de mi habitación, me doy cuenta de algo."
    ai "¿Por qué todo se ve tan descolorido?"
    stop music fadeout 2.0
    "Al mirar a mi alrededor, noto que mi habitación carece de algún tipo de color."
    show ai surprise1 at lio11
    ai "¡¿Qué diablos?!"
    "¿Por qué mi habitación está tan desteñida?"
    "¿Lo han pintado sin que me diera cuenta?"
    ai normal6 "Vamos, esto tiene que ser una broma de mal gusto."
    ai normal2 "Pero..."
    show ai hmm1
    "Empiezo a sentir que algo extraño está sucediendo y me está invadiendo."
    "No sé por qué, pero empiezo a sentirme bastante insegura."
    ai happy4 "Vamos, Ai, simplemente cálmate."
    ai "Esto tiene que ser normal, ¿no?"
    show ai happy3
    pause 1.5
    "¿Verdad?"
    pause 2.0
    hide ai
    "Buscando una razón, solo se me ocurre acercarme a la ventana de mi habitación..."
    "Solo para intentar encontrar una razón..."
    pause 1.0
    "Para darme cuenta de que-{w=2.0}{nw}"
    show ai surprise1 at lio11
    ai "¡¿Qué diablos?!"
    ai "¡No, no, no, no, esto no puede estar ocurriendo!"
    play music m1 fadein 1.5
    show ai surprise1 at j11
    ai "¿Por qué todo está en tonos grises?"
    show ai surprise1 at j11
    ai "¿Dónde están los colores?"
    show ai surprise1 at j11
    ai "Cuan- {nw=1}"
    show ai surprise1 at j11
    extend "Cuándo, ¿cuándo pasó esto?"
    show ai surprise1 at j11
    ai "¿Por qué ha pasado?"
    pause 1.0
    show ai happy5 at cso11
    with Dissolve(0.6)
    ai "Vamos, Ai, cálmate."
    ai "Esto debe ser normal, ¿verdad?"
    pause 1.0
    show ai happy4 at j11
    ai "¿Verdad?"
    ai "..."
    show ai happy3 at cso11
    "Jajaja, seguro que esto debe ser un sueño."
    "Puede que sí, seguro que lo es."
    "¿O estaré bajo la influencia de alguna droga?"
    "..."
    "Pero si yo no-"
    "..."
    "Mejor descarto eso, no soy de hacer ese tipo de cosas."
    "Mmm..."
    ai happy4 "Seguro que no soy la única que ve todo gris, ¿verdad?"
    pause 1.0
    "Creo que debería pensar si mi mamá también está pasando por este problema."
    ai hmm1 "Espero no ser la única que está pasando por esto."
    ai "Aunque si esto es una pesadilla seguro despertare en algún momento."
    window hide(Dissolve(.2))
    hide ai
    pause 1.5
    scene bg ai_livingroom with hgradient_right
    pause 1.5
    window auto
    show shiori normal1 at cso11
    shiori "Buenos días, hija"
    show shiori idle
    ai "Buenos días, mamá."
    "Ella es mi madre, Shiori Tanaka"
    $ _shiori_name = _("Mamá")
    "Tiene 40 años."
    "Es muy protectora conmigo y suele ser muy tranquila en lo que dice y hace."
    "También es bastante sabia, un dato interesante de ella que pueden tener en cuenta."
    shiori normal1 "¿Has dormido bien?"
    show shiori idle
    ai "Si, algo."
    ai "Solo que estoy un poco cansada."
    shiori hmm4 "No tener un control sobre tus horas de sueño conlleva estos problemas."
    show shiori hmm3
    ai "Lo sé, mamá, me lo dices a menudo."
    shiori hmm0 "Si, es correcto, pero no veo que hagas caso a eso."
    ai "Sí, perdón."
    shiori idle "Intenta encontrar un horario de sueño óptimo, así dormirás bien."
    shiori normal1 "Vale, antes de que te vayas a la universidad, necesito pedirte un favor."
    show shiori idle
    ai "¿Y qué necesitas?"
    shiori normal1 "Me hace falta que vayas a la tienda."
    shiori "Quiero que me compres algunas cosas."
    show shiori idle
    ai "Claro."
    ai "Sólo dime qué quieres que compre."
    "Se está tomando con calma el hecho de que todo esté gris..."
    "¿Soy la única que ve las cosas de esta manera?"
    "..."
    "No estoy segura de si debería preguntarle."
    pause 1.5
    "Veo en la mesa del comedor un objeto que no recuerdo haber visto antes."
    show caja at objectShow
    "Se parece a una caja de algún color que ahora mismo no puedo identificar."
    "Seguro que es una caja normal que no había notado antes."
    hide caja
    "..."
    ai "Ma, ¿Puedo preguntarte algo?"
    shiori normal1 "Claro."
    shiori idle "¿Qué ocurre?"
    ai "Pues..."
    menu:
        "¿Le pregunto si puede ver el color de la caja?"
        "Preguntar.":
            ai "¿Qué es esa caja que está en la mesa?"
            shiori normal1 "Es un regalo para tu tía."
            shiori "Recuerda que hoy es su cumpleaños."
            show shiori idle
            ai "¿Y cuál es el color de esa caja?"
            show shiori normal1 at j11
            shiori "¡Ja! Me divierte que lo preguntes."
            "Vale, porque preguntar por el color de algo es absurdo."
            shiori "Es el color favorito de tu tía."
            show shiori idle
            ai "¿Y cuál es su color favorito?"
            shiori normal2 "Ah, su color favorito es el rosa."
            shiori "Pensé que lo recordabas."
            shiori "Es bastante raro que también preguntes por el color de la caja."
            ai "Disculpa, es que mi pregunta era para saber cuál es el color favorito de mi tía."
            ai "Es que lo había olvidado."
        "Dejarlo pasar.":
            ai "Mejor no."
            ai "Ya se me olvidó que te iba a preguntar algo."
            shiori normal2 "Hmm..."
            shiori "¿En serio no me ibas a preguntar nada?"
            ai "No te preocupes, no era nada importante."
            "Creo que preguntarle eso directamente sería muy estúpido."
            ai "Solo iba a preguntarte sobre esa caja que está en la mesa."
            shiori hmm0 "Tú debes saber para qué es esa caja."
            ai "No sé para qué es."
            shiori normal1 "Esa caja contiene un regalo para tu tía, recuerda que hoy es su cumpleaños."
            show shiori idle
            ai "Vaya, se me había olvidado."

    shiori idle "Mientras tu tía no lo sepa está bien."
    shiori sad2 "Hasta yo a veces lo olvido."
    shiori "No se lo cuentes."
    pause 1.0
    shiori normal1 "Bueno, en lo que estaba."
    shiori "Necesito que vayas a la tienda."
    show shiori idle
    ai "Sí verdad, ¿qué necesitas que compre?"
    shiori normal1 "Bueno, son algunos víveres que faltan para los pastelitos que haré para el evento de encendido de luces de hoy."
    show shiori idle
    "Hoy es el encendido de luces en la plaza de la ciudad por Navidad, mi mamá todos los años participa en el evento cocinando algunos pastelitos y otros postres."
    shiori normal1 "Necesito 2 kilos de harina de trigo y un kilo de azúcar, los demás ingredientes ya los tengo."
    shiori normal3 "Por cierto, la harina de trigo tiene que ser de una marca en específico."
    shiori normal1 "La última que compré era bastante buena, {nw}"
    extend normal3 "aunque no recuerdo su nombre."
    shiori "El color del paquete de la que compré era de color rojo,"
    shiori normal1 "En la mesa está el dinero."
    shiori "Apresúrate porque no querrás llegar tarde a la universidad."
    show shiori idle at cso11
    ai "Vale, ya regreso."
    shiori normal1 "Te estaré esperando."
    hide shiori
    stop music fadeout 2.0
    pause 2.5
    "¡¿Por qué me tiene que pasar esto?!?"
    "¿Por qué tiene que ser una harina en específico?"
    "¿No puede ser una harina común y corriente?"
    "{i}*Suspiro*{/i}"
    pause 2.0
    "Voy a tener que intentar comprar en esta situación."
    "¿Será muy complicado sabiendo que no puedo ver los colores?"
    "Voy a tener que averiguarlo."
    "{i}*Suspiro*{/i}"
    "Qué situación tan complicada y extraña."
    pause 1.4
    play audio open_door
    scene bg ai_house with hgradient_left_scene_full
    pause 1.0
    "Lo bueno es que la tienda está prácticamente a la vuelta de la esquina."
    "Lo malo es que no sé si será difícil poder comprar sin ver los colores."
    "He vuelto a decirlo, pero es muy extraño esto que está pasando."
    "Así que simplemente no sé qué pensar o decir."
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
    extend ", hola Ai, ¿En qué puedo ayudarte?"
    show yu idle
    ai "Hola Yu, vine a comprar algunas cosas para los pastelitos que hará mi mamá para el evento de hoy."
    $ _yu_name = _("Yu")
    "Ella es Yu Ishikawa."
    "Trabaja en esta tienda de conveniencia."
    "También es una amiga y vecina."
    yu happy2 "Qué bien, llevo esperando mucho tiempo."
    yu "Quiero probar los pastelitos que tu mamá prepara."
    show yu happy2 at j11
    yu "Es una de las cosas que más me gusta del evento."
    show yu happy1 at cso11
    ai "Esta vez no le faltan muchos ingredientes."
    ai "También cambió la receta de los mismos."
    yu idle "Eso es una buena noticia."
    yu normal1 "Imagino que ahora son mejores de lo que ya los eran."
    show yu idle
    ai "Claro, te sorprenderá lo buenos que son ahora."
    yu normal1 "Bueno, aunque no te distraigo más."
    yu idle "Si necesitas mi ayuda estoy aquí."
    ai "Claro, lo tendré en cuenta."
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
    ai "Mi mamá quiere dos kilos de harina de trigo."
    ai hmm2 "Y un kilo de azúcar."
    show ai hmm1
    "Se me hará más fácil comprar el azúcar, eso claro está."
    hide ai
    pause 1.0
    "Mirando en uno de los estantes logro ver el azúcar."
    show azucar at objectShow
    "¿Con un kilo de azúcar se puede hacer todo lo que mi mamá hace?"
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
    "¡¿Cómo rayos voy a saber cuál es la que quiere mi mamá?!"
    "¡¿Por qué tenía que ser específica?!"
    hide harina2
    pause 1.0
    "¿Le pido ayuda a Yu?"
    "Hmm..."
    "Quizás decirle directamente lo del color sería un poco absurdo."
    "..."
    "Ya sé."
    "Tomo las dos harinas y me dirijo a donde está Yu."
    pause 2.0
    ai "Yu, necesito hacerte una pregunta."
    show yu normal1 at cso11
    yu "Dime Ai, ¿Qué pasa?"
    show yu idle
    ai "¿Sabes cuál es la harina que mi mamá compró la última vez que vino aquí?"
    yu normal1 "Claro, ¿ella te pidió una en específico?"
    show yu idle
    ai "Sí, no sé cuál fue la que compró."
    yu normal1 "Compró la que tienes en la mano izquierda."
    yu "Yo misma se la recomendé."
    show yu idle
    show harina2 at objectShow
    "Así que era la más oscura."
    "Qué bueno que Yu recordaba cuál era."
    "Me salvó."
    hide harina2
    ai "Muchas gracias Yu."
    ai "Me salvaste de que mi mamá se enojara jeje."
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
    "Si no logro descubrir por qué me pasó esto, no sé qué haré."
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
    pause 2.0
    hide vignette2 onlayer effects
    hide black2 onlayer effects2
    with Dissolve(1.6)
    stop music fadeout 2.0
    pause 1.0
    "Pasaron unos momentos y esa sensación se fue..."
    ai "{i}*Suspiro*{/i}"
    ai "Eso nunca antes había pasado."
    ai "Espero que no sea nada malo."
    pause 1.6
    show bg ai_house with hgradient_left_scene_full
    pause 2.0
    "Sinceramente no sé qué fue esa sensación de hace rato."
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
    ai "Hola de nuevo mamá..."
    ai "Aquí traigo lo que pediste."
    shiori normal1 "Excelente."
    shiori "Ahora sí podré terminar los pastelitos."
    shiori reflexive1 "Sé que a todos les sorprenderá mi nueva receta."
    ai "¿Para eso era la harina que querías?"
    show shiori normal1 at j11
    shiori "Pues claro."
    shiori "Esa harina, dejó los últimos pastelitos que hice con una consistencia realmente agradable."
    shiori idle "Es realmente buena."
    "Hace como dos semanas mi mamá hizo unos pastelitos para probar su nueva receta."
    "No lo recordaba, pero ahí está el dato."
    ai "¿Y cuántos pastelitos pretendes hacer?"
    shiori hmm0 "Los que pueda hacer."
    shiori normal1 "Jeje."
    shiori "Haré los que pueda..."
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
    "Mamá y yo nos sentamos a comer."
    "Mientras comíamos, ella comenzó a hacerme las preguntas de siempre."
    "¿Tengo novio? ¿Por qué no salgo muy a menudo?"
    "En fin, las preguntas que toda madre hace..."
    "A veces me incomodan, pero la verdad..."
    "Es que no me molesta que las haga."
    "Sería peor si no me las hiciera."
    "¿Me entienden?"
    window hide(Dissolve(.2))
    pause 2.0
    scene bg ai_livingroom with hgradient_left
    pause 1.0
    window auto
    "Casi terminando de comer, le hice una pregunta a mi mamá."
    show shiori idle at cso11
    play music m2 fadein 1.5
    pause 1.0
    ai "Ma, ¿te puedo hacer una pregunta?"
    shiori normal1 "Claro hija, no tienes que preguntarme."
    show shiori idle
    ai "Bueno, es que solo para que lo supieras."
    ai "Bueno..."
    ai "¿Si alguna vez despertaras sin poder ver los colores, qué harías?"
    shiori normal2 "Hmm..."
    shiori normal4 "Bueno..."
    shiori "Es una pregunta un poco extraña."
    shiori normal1 "Pero te responderé con esto..."
    shiori "Rojo, verde y azul son los colores de la luz, si ellos no están, pues los reemplazarán el blanco y el negro."

    ## Nota de Quetzalcoutl: Yo me sorprendí al enterarme de eso jeje
    $ renpy.notify(_("El blanco, negro y gris no son colores, ellos son 'Acromáticos' que significa literalmente 'Sin color'\nEsto porque carecen de tono o saturación, pero comúnmente los seguimos llamando colores."))

    shiori "Estos últimos no son colores, por ende todo se verá gris."
    shiori idle "Si en el hipotético caso que dejara de ver los colores, primero me sorprendería..."
    shiori normal1 "Sería una situación que me dejaría realmente confundida y asustada..."
    shiori "Solo me preguntaría.. ¿Por qué?"
    shiori normal2 "Bueno..."
    shiori "Pensar en las razones por las que me pasó también sería lo indicado..."
    "Todo lo que hice."
    shiori normal4 "Aunque...{w=1.0}{nw}"
    extend normal3 "Pues también pensaría en...{w=2.0}{nw}"
    shiori sad2 "Disculpa, hasta yo misma me confundí."
    shiori idle "Bueno..."
    shiori "Si yo me despertara sin poder ver los colores,{nw}" 
    extend normal1 " solo estaría confundida jeje."
    shiori "Aunque eso de ver todo gris es algo que no puede pasar realmente."
    shiori idle "Pero sí, si me pasara eso me dejaría realmente confundida y asustada."
    shiori normal1 "¿Eso responde tu pregunta?"
    shiori sad2 "Aunque no creas que no estoy un poco confundida con tu pregunta y mi respuesta."
    shiori idle "Pensaré en una mejor después."
    shiori normal1 "Así que dime...{w=1.0}{nw}"
    extend "¿Eso responde tu pregunta?"
    ai "Bueno..."
    "Dijo exactamente lo que he hecho."
    "Esta es una situación realmente confusa."
    "Pero puedo confirmar que mi mamá no está pasando por esto."
    ai "Sí, sí la responde."
    shiori normal1 "Me alegro."
    shiori normal2 "Aunque es realmente rara."
    shiori "¿Tienes algo que quieras contarme?"
    shiori "Si algo te pasa no dudes en decirme."
    shiori sad3 "Soy tu madre."
    shiori "Recuerda que puedes confiar en mí."
    ai "No, no, no me pasa nada."
    show shiori normal2
    ai "Jeje."
    ai "Solo es algo que quería preguntarte desde hace rato."
    shiori normal1 "Bueno, espero haber resuelto tu duda."
    shiori sad2 "Aunque cuando encuentre una mejor respuesta te diré."
    shiori normal1 "Por cierto, te recuerdo que ahora sí puedes llegar tarde a la universidad si no te apresuras."
    show shiori idle
    ai "Ah, es cierto."
    ai "Iré a cambiarme."
    shiori normal1 "Vale, te espero."
    hide shiori
    window hide(Dissolve(.2))
    stop music fadeout 1.5
    scene bg ai_room with hgradient_left_scene_full
    pause 1.0
    window auto
    "Mi mamá respondió lo mismo que he hecho."
    "Bueno, al menos puedo saber que hasta ella quedaria confundida con algo así."
    play music m1 fadein 2.0
    show ai meh1 at cso11
    ai "Aunque me gustaria saber la razón por la cual me ocurrio esto."
    pause 1.0
    ai meh2 "Realmente no puedo pensar en algo que lo explique."
    "Espero poder ver los colores nuevamente."
    "Ojala esto sea momentaneo..."
    "La unica razón que puedo pensar que haya causado esto es que este bajo la influencia de una droga.."
    "Aunque..."
    "Mejor la descarto, porque no soy de hacer eso."
    pause 1.0
    ai angry2 "Mejor me apresuro..."
    ai "Si me quedo aquí parada pensando en nada voy a llegar tarde."
    ai idle "Así que ire a cambiarme."
    ai hmm1 "Aunque..."
    "Sí, se que me estoy olvidando de algo.."
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
    ai "Bueno, ahora me vestiré."
    ai "Viendo la hora, me sobra tiempo."
    "Creo."
    ai "Si me apresuro llegare temprano."
    ai "Bueno..."
    ai "¿Dónde está mi ropa?"
    "Buscando en lo que puedo decir que es como un armario, me doy cuenta de algo..."
    ai "¡¡¡¡TODO ESTÁ GRIS!!!!!!{w=1.5}{nw}"
    ai "¡¡¡¡¿COMO VERE QUE ROPA PONERME?!!!!{w=1.5}{nw}"
    ai "¡¡¡MI3RD444AAAAA!!!!"
    ai "¡¡¡Aho-{nw}"
    "Me acabo de dar cuenta que acabo de gritar eso en voz alta."
    shiori "Hija, ¿Todo bien?"
    shiori "Oí un grito..."
    ai "¡No pasó nada!"
    ai "¡Descuida!"
    shiori "¿En serio estás bien?"
    ai "¡Si si, estoy bien!"
    shiori "Bueno..."
    shiori "Si tu lo dices."
    ai "¡Descuida, no te preocupes!"
    shiori "Está bien.."
    shiori "Apresúrate si no quieres llegar tarde."
    ai "¡Vale, ya salgo!"
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
    hide ai
    pause 1.0
    scene bg ai_livingroom with hgradient_left
    pause 0.4
    show shiori idle at cso11
    shiori "Hola de nuevo hija, ¿Ya te vas?"
    ai "Si, espero poder llegar temprano."
    shiori normal1 "No seas pesimista, aún te queda tiempo."
    shiori "Si sales ahora, llegarás temprano."
    ai "Bueno, entonces..."
    ai "Me iré ahora."
    shiori normal1 "No te detengo más."
    ai "Adiós mamá."
    shiori normal1 "Que te vaya bien."
    shiori normal3 "Recuerda que si necesitas hablar..."
    shiori "Recuerda que estoy aquí."
    ai "Descuida, no pasa nada."
    "¿Qué tan extraña fue mi pregunta?"
    "La verdad no lo sé..."
    "...."
    ai "Ahora si me voy."
    shiori normal1 "Adiós hija."
    show shiori idle at cso11
    hide shiori
    stop music fadeout 1.6
    pause 2.0
    "Mientras camino hacia la puerta solo logró pensar en que me puede deparar este día tan extraño."
    pause 1.0
    scene bg ai_house with hgradient_left_scene_full
    pause 1.0
    ai "Creo me estoy tomando con mucha calma esto de no poder ver los colores."
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
    "La forma de saber que está en rojo es viendo si los autos están detenidos."
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
    ai "Aún me queda tiempo para llegar."
    "A veces llego tarde pero hoy no será el caso..."
    "..."
    ai "Solo me queda abordar el tren..."
    pause 1.0
    stop music fadeout 2.0
    pause 2.0
    ai "Hoy realmente será un día extraño..."
    ai "No se como será este día sin poder ver los colores..."
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