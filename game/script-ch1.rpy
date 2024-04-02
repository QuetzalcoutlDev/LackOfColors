
image infoTXT = ParameterizedText(xalign=0.5, yalign=0.5, style="infoText")
default infoValue = _("")

style infoText:
    size 30
    color "#ffffff"
    font "URWBookman-Light.otf"
    textalign 0.5

label ch_1:
    
    scene black
    pause 2.0
    window auto
    $ quick_menu = True
    "Puedo decir que este día será fatal."
    "O quizás esperar a ver que me deparara este día."
    "Creo que sería lo más indicado..."
    pause 1.0
    "Creo..."
    window hide(Dissolve(.2))
    pause 1.0
    scene bg station_platform with Dissolve(1.5)
    pause 1.4
    window auto
    play music station_ambience fadein 2.0
    "Al entrar a la estación, solo logro soltar un gran suspiro..."
    ai "{i}*Suspiro.....*{/i}"
    "Como siempre la estación esta repleta..."
    "Personas caminando de un lado a otro, alguien esperando el siguiente tren para ir a su destino..."
    "Tanto movimiento...."
    "Y..."
    pause 2.0
    ai "¿Cuanto tardara el tren en llegar?"
    "Al ver mi reloj, me surge el pensamiento de que puedo llegar tarde si no llega el tren..."
    pause 1.0
    ai "Vamos, ¿Por qué se tarda tanto?"
    "Ahora recuerdo que...."
    "El tren siempre llega a una hora en especifico..."
    "..."
    "Esto simplemente no me deja pensar correctamente."
    ai "{i}*Suspiro*{/i}"
    ai "Deberia llegar en cualquier momento."
    ai "Mientras pasare el rato escuchando música con mi teléfono."
    "Solo ver la pantalla de mi telefono me deja un poco confundida."
    "Verlo sin colores es bastante raro, no es dificil interactuar como siempre con el."
    "Pero verlo así, lo hace parecer que está congelado..."
    "Dejando de pensar en eso, solo me pongo los auriculares en los oidos y me pongo a escuchar mi música favorita..."
    stop music fadeout 1.0
    pause 1.0
    play music song1
    window hide(Dissolve(.2))
    pause 3.0
    scene bg station_platform with hgradient_left_scene_full
    $ renpy.notify(__("Pasaron unos minutos y el tren habia llegado..."))
    pause 4.0
    window auto
    "Tan concentrada en lo que estaba escuchando, que apenas me doy cuenta de que el tren acaba de llegar."
    ai "Por fin..."
    stop music fadeout 1.0
    pause 1.0
    play music trainAnnouncement fadein 2.0
    "Guardo mi telefono y comienzo a caminar hacia la puerta del tren..."
    pause 1.0
    "Quiz-{nw}"
    stop music fadeout 0.5
    show vignette2 onlayer effects
    show black2 onlayer effects2
    with dissolve
    play music terrorGround fadein 2.0
    pause 1.0
    ai "{cps=16}Otra vez...{/cps}"
    ai "{cps=16}Otra vez está pasando...{/cps}"
    "Esa sensación extraña de hace rato a regresado...."
    "Siento una presión en mi pecho que no me permite respirar correctamente..."
    "Pero...."
    "No estoy sintiendo ningún tipo de dolor...."
    ai "{i}*Suspiro.....*{/i}"
    "Como puedo camino a dentro del tren y busco un asiento..."
    window hide(Dissolve(.2))
    scene bg inside_train with hgradient_left_scene_full
    pause 1.0
    window auto
    ai "{i}*Suspiro.....*{/i}"
    pause 1.0
    "Algunos pasajeros se quedaron observando mientras que otros simplemente no hicieron caso a lo que pasaba..."
    "Preferi mostrarme de lo más tranquila para no llamar la atención...."
    pause 1.0
    ai "{i}*Suspiro.....*{/i}"
    pause 3.0
    hide vignette2 onlayer effects
    hide black2 onlayer effects2
    with Dissolve(1.6)
    stop music fadeout 2.0
    pause 1.0
    "Pasaron unos minutos y esa sensación se fue."
    ai "{i}*Suspiro*{/i}"
    ai "Al parecer también tendré que lidiar con eso ahora..."
    "Que mala suerte tengo..."
    pause 1.0
    "Solo me quedara esperar a ver que más pasara en este día..."
    pause 2.0
    ai "Solo esperar..."
    "He repetido ya varias veces esa palabra que hasta pierde su significado..."
    "Solo tengo que esperar que pasará hoy, ¿no?"
    "..."
    "La volvi a decir..."
    ai "{i}*Suspiro*{/i}"
    window hide(Dissolve(.2))
    pause 2.0
    scene bg inside_train at train_move
    with hgradient_left_scene_full
    play music insideTrain fadein 2.0
    pause 2.0
    window auto
    "Durante mi recorrido, mi mente solo divagaba en cosas sin sentido alguno..."
    "Imaginandome posibles situaciones por las cuales deje de ver los colores..."
    "Ninguna me convencia y realmente estaba pensando cosas extrañas.."
    ai "Vamos no pienses estupideces."
    "Cuando mi mente divaga simplemente comienza a pensar en cosas realmente extrañas."
    "Es algo que nos pasa a todos, ¿No?"
    "Aunque hablar de eso no es importante por ahora..."
    ai "Creo que no falta mucho para llegar a la parada."
    "Al ver mi reloj, puedo ver que me queda tiempo para llegar."
    "El tren se toma como 30 minutos en llegar a su destino."
    "LLendo en camión tardaria casi 50 minutos en llegar a donde voy, esto por las paradas constantes que hace este."
    "Bueno, ahora solo me queda esperar..."
    window hide(Dissolve(.2))
    pause 2.0
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 1.0
    play music trainStop fadein 1.0
    pause 4.0
    window auto
    "Al llegar a mi parada, comienzo a caminar hacia la escuela..."
    "Me queda tiempo suficiente para llegar temprano..."
    stop music fadeout 2.0
    pause 2.0
    scene bg school_entrance with hgradient_left
    pause 2.0
    ai "{i}*Jadeo*{/i}{w=1.0}{i}*Jadeo*{/i}{w=1.0}{i}*Jadeo*{/i}{w=1.0}"
    ai "Uff, por poco y no llego..."
    "Subestime un poco el tiempo que me quedaba..."
    "Así que durante el camino desde la estación hasta aquí, aumente bastante mi paso."
    ai "Estoy un poco cansada..."
    ai "Pero llegue a tiempo..."
    "Comienzo a caminar hacia dentro de la escuela para dirigirme hacia mi salón de clase..."
    window hide(Dissolve(.2))
    pause 3.0
    scene bg front_classroom with hgradient_left_scene_full
    pause 1.0
    "Al entrar al salón soy recibida por el profesor..."
    show tetsuo 2 at cso11
    play music m4 fadein 1.5
    tetsuo "Pasa adelante Ai."
    tetsuo "Veo que llegas un poco tarde."
    show tetsuo 1
    "¡¡¿Queé?!!"
    ai "Pero si mi reloj me dice lo contrario."
    ai "So-{nw}"
    show tetsuo 6 at j11
    tetsuo "Descuida, descuida."
    tetsuo "Solo estoy jugando."
    tetsuo "Pasa adelante jeje."
    show tetsuo 5 at cso11
    "El es Tetsuo Satoo."
    "El profesor de arte."
    $ _tetsuo_name = _("Tetsuo")
    "Siempre se la pasá haciendo bromas como está."
    "Normalmente siempre caigo en ellas."
    hide tetsuo
    pause 1.0
    "Caminando por el salón de clases, puedo sentir sin ninguna duda la mirada de mis compañeros..."
    "Recordandome que soy la ultima en llegar..."
    "Solo las ignoro y camino hasta mi asiento."
    azumi "Hola Ai, por poco y no llegas a tiempo."
    show azumi 1 at cso11
    ai "Si, subestime el tiempo que me quedaba"
    ai "Aún me siento agotada de tanto correr."
    azumi 2 "Bueno, al menos pudiste llegar a tiempo jeje."
    azumi 5 "Ahora puedes descansar un poco."
    ai "Si jeje."
    "Ella es mi amiga Azumi Kobayashi."
    $ _azumi_name = _("Azumi")
    "Ella se sienta a mi lado desde que inicie la universidad..."
    "Antes simplemente no nos hablabamos."
    "Pero de un día a otro comenzamos a hablar y posteriormente nos hicimos buenas amigas."
    "Tenemos gustos en común, así que era inevitable el hecho de que nos hicieramos amigas."
    azumi 2 "Deberias levantarte más temprano."
    show azumi 1
    ai "Es que lo hago, solo que está vez pues..."
    ai "Subestime el tiempo que me quedaba."
    azumi 8 "Si como no, entonces, ¿Por qué llevas días en los que siempre llegas con tan poco tiempo?"
    show azumi 7
    ai "Pues..."
    ai "Solo pasa..."
    azumi 8 "Bueno, lo que tu digas..."
    azumi 1 "Por cierto, vis-{nw}"
    show azumi 3 at cso21
    show tetsuo 2 at cso22
    tetsuo "Bueno estudiantes, preparense porque la clase está por comenzar."
    tetsuo "Hoy tenemos un ejercicio de composición."
    tetsuo "Preparense..."
    hide tetsuo
    pause 1.0
    show azumi 1 at cso11
    azumi 2 "Hablamos mejor más tarde, estate atenta a la clase."
    azumi 8 "No querrás que el profesor te regañe de nuevo como la ultima vez."
    show azumi 7
    ai "¡Oye!"
    show azumi 6 at j11
    azumi "Jajaja."
    azumi 2 "Ya enserio, hablamos más tarde."
    show azumi 1 at cso11
    ai "Vale."
    hide azumi
    stop music fadeout 2.0
    pause 2.0
    "Bueno..."
    "Solo me queda intentar realizar los ejercicios que el profesor diga."
    "Vamos a ver si puedo hacer algo como estoy ahora..."
    window hide(Dissolve(.2))
    pause 2.0
    scene bg front_classroom with hgradient_left_scene_full
    pause 1.0
    window auto
    show tetsuo 1 at cso11
    play music m5 fadein 2.0
    pause 1.0
    tetsuo 2 "Bueno estudiantes, como les dije, hoy tendremos un ejercicio."
    tetsuo "Como pueden notar, están estos objetos aqui al frente..."
    show figuras at objectShow
    tetsuo "El ejercicio de hoy, consiste en realizar una composición en base a lo que hemos estado viendo estás ultimas semanas."
    hide figuras
    show tetsuo 1
    "Al menos hoy toca algo que si disfruto hacer."
    "Aunque el profesor a veces repite este ejercicio...."
    "Bueno, solo queda sacar de mi bolso lo necesario para dibujar..."
    pause 1.0
    window hide(Dissolve(.2)) 
    scene bg front_classroom with hgradient_left_scene_full
    pause 1.0
    show tetsuo 2 at cso11
    tetsuo "Seguro muchos de ustedes pensaran {i}'¿Por qué otra vez este ejercicio?'{/i}"
    tetsuo 1 "Bueno, como les he dicho muchas veces..."
    tetsuo 2 "Quiero que sean creativos a la hora de hacerlo."
    tetsuo "No se limiten."
    hide tetsuo
    pause 1.0
    "..."
    "Vamos a ver que si hago algo bueno para este ejercicio..."
    stop music fadeout 1.0
    pause 1.0
    scene cg mesa_1 with Dissolve(1.0)
    play music m1 fadein 1.0
    pause 1.0
    scene cg mesa_2 with Dissolve(1.0)
    "Para comenzar el ejercicio, comenzaré dibujando la estructura de los objetos."
    "Es algo que el profesor siempre nos dice que hagamos, así que lo hare como siempre."
    play sound drawing
    scene cg mesa_3 with Dissolve(3.5)
    pause 1.0
    scene cg mesa_5 with Dissolve(.6)
    "Creo que está es la forma correcta de dibujar la estructura de los objetos..."
    pause 1.0
    scene cg mesa_3 with Dissolve(1.0)
    play audio drawing volume 0.5
    pause 3.0
    "Mientras dibujo me olvido de mi alrededor."
    "Creo que es normal..."
    "¿No?"
    "Solo pienso en lo que estoy haciendo en este momento y me olvido de todo a mi alrededor..."
    window hide(Dissolve(.2))
    pause 2.0
    scene black with Dissolve(1.0)
    $ infoValue = __("Unos minutos después...")
    show infoTXT "[infoValue]"
    pause 3.0
    scene cg mesa_4 with Dissolve(3.5)
    window auto
    pause 1.0
    "Bueno, con este boceto basta..."
    scene cg mesa_6 with Dissolve(.5)
    "Hmm..."
    azumi "Vas bien Ai."
    ai "Gracias Azumi."
    ai "Aunque solo es el boceto."
    azumi "Vale, vale."
    azumi "Tú continua jeje."
    pause 1.0
    "Creo que dejar todo plano no sería lo indicado."
    "¿Quizás si lo resuelvo por color?"
    "..."
    stop music fadeout 1.5
    "¿Por color?"
    "..."
    pause 0.5
    show layer master at zoomCam
    show layer screens at zoomCam
    show vignette2 onlayer effects
    show black2 onlayer effects2
    # with dissolve
    play music terrorGround fadein 2.0
    pause 1.0
    show layer master at Nothing
    show layer screens at Nothing
    ai "{i}*Agh*{/i}"
    "{cps=16}No de nuevo...{/cps}"
    "{cps=16}{i}*Suspiro*{/i}{/cps}"
    "{cps=16}{i}*Suspiro*{/i}{/cps}"
    ""

    return