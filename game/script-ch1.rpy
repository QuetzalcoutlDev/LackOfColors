
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
    "O quizás esperar a ver que me deparará este día."
    "Creo que sería lo más indicado..."
    pause 1.0
    "Creo..."
    window hide(Dissolve(.2))
    pause 1.0
    scene bg station_platform with Dissolve(1.5)
    pause 1.4
    window auto
    play music station_ambience fadein 2.0
    "Al entrar a la estación, solo logró soltar un gran suspiro..."
    ai "{i}*Suspiro.....*{/i}"
    "Como siempre la estación está repleta..."
    "Personas caminando de un lado a otro, alguien esperando el siguiente tren para ir a su destino..."
    "Tanto movimiento...."
    "Y..."
    pause 2.0
    ai "¿Cuanto tardará el tren en llegar?"
    "Al ver mi reloj, me surge el pensamiento de que puedo llegar tarde si no llega el tren..."
    pause 1.0
    ai "Vamos, ¿Por qué se tarda tanto?"
    "Ahora recuerdo que...."
    "El tren siempre llega a una hora en específico..."
    "..."
    "Esto simplemente no me deja pensar correctamente."
    ai "{i}*Suspiro*{/i}"
    ai "Debería llegar en cualquier momento."
    ai "Mientras pasaré el rato escuchando música con mi teléfono."
    "Solo ver la pantalla de mi teléfono me deja un poco confundida."
    "Verlo sin colores es bastante raro, no es difícil interactuar como siempre con el."
    "Pero verlo así, hace parecer que está congelado..."
    "Dejando de pensar en eso, solo me pongo los auriculares en los oidos y me pongo a escuchar mi música favorita..."
    stop music fadeout 1.0
    pause 1.0
    play music song1
    window hide(Dissolve(.2))
    pause 3.0
    scene bg station_platform with hgradient_left_scene_full
    $ renpy.notify(__("Pasaron unos minutos y el tren había llegado..."))
    pause 4.0
    window auto
    "Tan concentrada en lo que estaba escuchando, que apenas me doy cuenta de que el tren acaba de llegar."
    ai "Por fin..."
    stop music fadeout 1.0
    pause 1.0
    play music trainAnnouncement fadein 2.0
    "Guardo mi teléfono y comienzo a caminar hacia la puerta del tren..."
    pause 1.0
    "Quiz-{nw}"
    stop music fadeout 0.5
    show vignette2 onlayer effects
    show black2 onlayer effects2
    with dissolve
    show layer master at zoomCam2
    show layer screens at zoomCam2
    play music terrorGround fadein 2.0
    pause 1.0
    ai "{cps=16}Otra vez...{/cps}"
    ai "{cps=16}Otra vez está pasando...{/cps}"
    "Esa sensación extraña de hace rato ha regresado...."
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
    "Prefiero mostrarme de lo más tranquila a llamar la atención...."
    pause 1.0
    ai "{i}*Suspiro.....*{/i}"
    pause 3.0
    hide vignette2 onlayer effects
    hide black2 onlayer effects2
    with Dissolve(1.6)
    show layer master at Nothing
    show layer screens at Nothing
    stop music fadeout 2.0
    pause 1.0
    "Pasaron unos minutos y esa sensación se fue."
    ai "{i}*Suspiro*{/i}"
    ai "Al parecer también tendré que lidiar con eso ahora..."
    "Que mala suerte tengo..."
    pause 1.0
    "Solo me quedará esperar a ver qué más pasará en este día..."
    pause 2.0
    ai "Solo esperar..."
    "He repetido ya varias veces esa palabra que hasta pierde su significado..."
    "Solo tengo que esperar que pasará hoy, ¿no?"
    "..."
    "La volví a decir..."
    ai "{i}*Suspiro*{/i}"
    window hide(Dissolve(.2))
    pause 2.0
    scene bg inside_train at train_move
    with hgradient_left_scene_full
    play music insideTrain fadein 2.0
    pause 2.0
    window auto
    "Durante mi recorrido, mi mente solo divagaba en cosas sin sentido alguno..."
    "Imaginando posibles situaciones por las cuales deje de ver los colores..."
    "Ninguna me convencía y realmente estaba pensando cosas extrañas.."
    ai "Vamos no pienses estupideces."
    "Cuando mi mente divaga simplemente comienza a pensar en cosas realmente extrañas."
    "Es algo que nos pasa a todos, ¿No?"
    "Aunque hablar de eso no es importante por ahora..."
    ai "Creo que no falta mucho para llegar a la parada."
    "Al ver mi reloj, puedo ver que me queda tiempo para llegar."
    "El tren se toma como 30 minutos en llegar a su destino."
    "Yendo en camión tardaría casi 50 minutos en llegar a donde voy, esto por las paradas constantes que hace este."
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
    "¡¡¿Qué?!!"
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
    "Ella se sienta a mi lado desde que inicié la universidad..."
    "Antes simplemente no nos hablábamos."
    "Pero de un día a otro comenzamos a hablar y posteriormente nos hicimos buenas amigas."
    "Tenemos gustos en común, así que era inevitable el hecho de que nos hiciéramos amigas."
    azumi 2 "Deberías levantarte más temprano."
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
    tetsuo "Bueno estudiantes, prepárense porque la clase está por comenzar."
    tetsuo "Hoy tenemos un ejercicio de composición."
    tetsuo "Preparense..."
    hide tetsuo
    pause 1.0
    show azumi 1 at cso11
    azumi 2 "Hablamos mejor más tarde, estate atenta a la clase."
    azumi 8 "No querrás que el profesor te regañe de nuevo como la última vez."
    show azumi 7
    ai "¡Oye!"
    show azumi 6 at j11
    azumi "Jajaja."
    azumi 2 "Ya en serio, hablamos más tarde."
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
    tetsuo "Como pueden notar, están estos objetos aquí al frente..."
    show figuras at objectShow
    tetsuo "El ejercicio de hoy, consiste en realizar una composición en base a lo que hemos estado viendo estás últimas semanas."
    hide figuras
    show tetsuo 1
    "Al menos hoy toca algo que sí disfruto hacer."
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
    "Vamos a ver si hago algo bueno para este ejercicio..."
    stop music fadeout 1.0
    pause 1.0
    scene cg mesa_1 with Dissolve(1.0)
    play music m1 fadein 1.0
    pause 1.0
    scene cg mesa_2 with Dissolve(1.0)
    "Para comenzar el ejercicio, comenzaré dibujando la estructura de los objetos."
    "Es algo que el profesor siempre nos dice que hagamos, así que lo haré como siempre."
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
    azumi "Tú continúa jeje."
    pause 1.0
    "Creo que dejar todo plano no sería lo indicado."
    "¿Quizás si lo resuelvo por color?"
    "..."
    stop music fadeout 1.5
    "¿Por{w=1.0} color?{w=1.5}{nw}"
    pause 0.5
    show layer master at zoomCam2
    show layer screens at zoomCam2
    show vignette2 onlayer effects
    show black2 onlayer effects2
    with dissolve
    play music terrorGround fadein 2.0
    pause 1.0
    ai "{i}*Agh*{/i}"
    "{cps=16}No de nuevo...{/cps}"
    ai "{cps=16}{i}*Suspiro*{/i}{/cps}{w=1.0}{nw}"
    ai "{cps=16}{i}*Suspiro*{/i}{/cps}{w=1.0}{nw}"
    "Mi respiración otra vez la siento limitada..."
    "Siento una presión en el pecho..."
    ai "{cps=16}{i}*Suspiro*{/i}{/cps}{w=1.0}{nw}"
    "Como si se tratara de un movimiento involuntario solo coloco mi mano izquierda sobre mi pecho..."
    "En un intento de calmar lo que siento..."
    ai "{cps=16}{i}*Suspiro*{/i}{/cps}{w=1.0}{nw}"
    "No siento dolor..."
    "No siento ni algo parecido a ello..."
    "O al menos sigo sin poder describir lo que me sucede..."
    pause 2.0
    "Alzo mi mirada para ver si no he llamado la atención de nadie..."
    scene bg front_classroom with Dissolve(.2)
    show layer master at zoomCam2
    pause 1.0
    "Mirando a mi alrededor, veo que nadie se ha-{nw}"
    show azumi 4 at cso11
    azumi "Ai, ¿Te sientes bien?"
    show azumi 3
    "Mierda..."
    "Se dio cuenta..."
    "No quiero decirle para no preocuparla..."
    "Pero..."
    ai "{cps=16}{i}*Suspiro*{/i}{/cps}{w=1.0}{nw}"
    azumi 4 "¿En Serio estás bien?"
    show azumi 3
    ai "Yo..."
    ai "Estoy algo mareada..."
    ai "No se porque de la nada me comencé a sentir así..."
    azumi 4 "¿Quieres que te lleve a la enfermería?"
    show azumi 3
    ai "{cps=16}Si...{/cps}"
    ai "{cps=16}Gracias...{/cps}"
    azumi 4 "Vale, deja le digo al profesor."
    hide azumi
    pause 1.0
    "{cps=26}¿Por qué ahora me tenia que pasar esto?{/cps}"
    "{cps=26}¿Qué me sucede?{/cps}"
    pause 2.0
    show azumi 3 at cso21
    show tetsuo 3 at cso22
    tetsuo "¿Como te sientes Ai?"
    show tetsuo 4
    "Por favor, no quiero llamar la atención de los demás..."
    "Solo...{nw}"
    ai "{cps=16}Me siento... Mareada...{/cps}"
    "Por favor, no quiero llamar la atención de los demás..."
    hide black2 onlayer effects2
    show black3 onlayer effects2
    ai "{cps=16}{i}*Suspiro*{/i}{/cps}{w=1.0}{nw}"
    tetsuo 3 "Si, llevala a la enfermería para que se recueste..."
    tetsuo "Si se siente mejor no dudes en avisarme."
    show tetsuo 4
    azumi 4 "Vamos Ai."
    pause 1.0
    play audio open_door
    scene bg school_hallway with hgradient_left_scene_full
    show layer master at zoomCam2
    show layer screens at zoomCam2
    pause 1.0
    "Azumi y yo salimos del salón de clases..."
    "Pude notar que varios de mis compañeros fijaban su mirada en mí..."
    "No quería llamar tanto la atención..."
    show azumi 3 at cso11
    azumi "Vamos Ai, ya vamos a llegar a la enfermería."
    hide azumi
    pause 2.0
    play audio open_door
    scene bg nursing with hgradient_left_scene_full
    show layer master at zoomCam2
    show layer screens at zoomCam2
    pause 1.0
    "Al llegar a la enfermería me recuesto en una de las camas más cercanas a la entrada..."
    show azumi 4 at cso11
    azumi "Solo recuestate tranquila."
    azumi "Ya se te debe de pasar..."
    show azumi 3 at cso11
    "Yo espero que si..."
    ai "{cps=16}Gracias por traerme hasta aquí Azumi...{/cps}"
    azumi 4 "Tú no te preocupes, si te sientes mal tenias que decirlo."
    azumi "Por ahora solo intenta descansar a ver si te sientes mejor."
    show azumi 3 at cso11
    ai "{cps=16}Eso intentaré...{/cps}"
    ai "{cps=16}{i}*Suspiro*{/i}{/cps}{w=1.0}{nw}"
    azumi 4 "Estaré aquí a tu lado hasta que te sientas mejor..."
    show azumi 3
    show black onlayer front:
        alpha 0.1
    ai "{cps=16}{i}Muchas gracias Azumi...{/i}{/cps}{w=1.0}{nw}"
    show black onlayer front:
        alpha 0.2
    azumi 6 "Descuida, soy tú amiga y tengo que preocuparme por ti."
    show black onlayer front:
        alpha 0.4
    azumi 4 "Si te sientes mal, no me lo ocultes."
    show black onlayer front:
        alpha 0.5
    azumi "No quiero que te llegue a pasar nada malo."
    show black onlayer front:
        alpha 0.6
    azumi "Me sentiría muy mal si algo malo te llegase a pasar."
    show black onlayer front:
        alpha 0.7
    azumi 6 "Estoy aquí para escucharte."
    show black onlayer front:
        alpha 0.8
    azumi 9 "Si necesitas hablar dime."
    "Me siento cada vez más cansada..."
    azumi 10 "Sabes que me preocupo mucho por ti."
    show black onlayer front:
        alpha 0.9
    azumi "Solo descansa Ai, piensa en lo que te digo..."
    show black onlayer front:
        alpha 1.0
    pause 2.0
    $ quick_menu = False
    window hide(None)
    scene black
    stop music fadeout 2.0
    window hide(Dissolve(.2))
    hide vignette2 onlayer effects
    hide black3 onlayer effects2
    hide black onlayer front
    show layer master at Nothing
    show layer screens at Nothing
    pause 6.0
    window auto
    $ quick_menu = True
    "¿Eso fue todo?"
    "No entiendo que pasa..."
    "Solo recuerdo que entre a la enfermería y..."
    "¿Qué pasó después?"
    window hide(Dissolve(.2))
    pause 2.0
    scene bg nursing with Dissolve(1.0)
    pause 1.0
    ai "¿Qué pasó?"
    "No se cuanto tiempo ha pasado desde que entré a la enfermería..."
    "¿Me quede dormida?"
    show azumi 2 at cso11
    azumi "Hola Ai, por fin despertaste."
    azumi "Te quedaste dormida al rato que llegamos a la enfermería."
    azumi "¿Te sientes mejor?"
    show azumi 1
    play music m1 fadein 2.0
    ai "Si, me siento mejor."
    "Creo."
    azumi 6 "Muy bien jeje."
    azumi 10 "La verdad me habías preocupado."
    show azumi 9
    ai "No quería preocuparte..."
    azumi 8 "No comiences con que no debo preocuparme por ti."
    show azumi 7
    ai "Si si, mejor no digo más nada."
    pause 2.0
    ai "Por cierto..."
    show azumi 1
    ai "¿Cuanto tiempo me quede dormida?"
    azumi 2 "Como unas 2 horas."
    azumi 8 "¿Realmente dormiste bien?"
    azumi "Porque quedarte dormida por tanto tiempo es una aclaratoria de que no habías dormido bien."
    show azumi 7
    ai "Pues..."
    "La verdad no es que duerma bien siempre..."
    ai "La verdad no se..."
    azumi 8 "Lo que tu digas."
    azumi 2 "Intenta dormir bien."
    azumi 4 "No se si sea eso lo que te causó el mareo o lo que sea que te sucedió."
    azumi 2 "Pero intenta dormir mejor."
    show azumi 1
    ai "Si, lo intentare..."
    pause 1.0
    azumi 2 "¿Regresamos al salón de clases?"
    show azumi 1
    ai "Tú adelántate, yo voy en un rato."
    azumi 2 "Vale, de acuerdo."
    azumi "Le diré al profesor que ya te sientes mejor."
    azumi 6 "Nos vemos en un rato."
    show azumi 5
    ai "De acuerdo."
    hide azumi
    stop music fadeout 2.0
    pause 1.0
    play audio open_door
    pause 3.0
    "Veo a Azumi salir de la habitación..."
    "La soledad en la habitación ahora se hace notar..."
    ai "{i}*Suspiro*{/i}"
    "Me recuesto en la cama nuevamente para pensar un rato."
    scene cg en_cama_1 with Dissolve(0.3)
    pause 1.0
    scene cg en_cama_2 with Dissolve(0.2)
    play music m6 fadein 1.5
    ai "¿Por qué me pasa esto?"
    scene cg en_cama_1 with Dissolve(0.3)
    "Creo que por ahora no obtendré una respuesta a esa pregunta..."
    "¿Quizás dormir mal sea el causante de esto?"
    "¿Debería considerar ir al médico?"
    scene cg en_cama_2 with Dissolve(0.2)
    ai "No quiero que nadie se entere..."
    scene cg en_cama_1 with Dissolve(0.3)
    "Me doy cuenta que no pensé en lo de considerar ir al médico..."
    "Todo esto no me ha dejado pensar correctamente."
    scene cg en_cama_2 with Dissolve(0.2)
    ai "¿Valdría la pena arriesgarse a eso?"
    scene cg en_cama_1 with Dissolve(0.3)
    "No siento que lo valga."
    scene cg en_cama_2 with Dissolve(0.2)
    ai "Nada vale la pena el riesgo."
    scene cg en_cama_1 with Dissolve(0.3)
    "¿Riesgo de qué?"
    "No quiero imaginarme que tenga algo extraño..."
    "¿Pero cómo sabría que tengo si no voy al médico?"
    "¿Cómo sabría si lo que tengo es causado por algo malo?"
    scene cg en_cama_2 with Dissolve(0.2)
    ai "¿Cómo sabría si lo que tengo es causado por algo malo?"
    scene cg en_cama_1 with Dissolve(0.3)
    "¿Cómo sabría si lo que tengo es causado por algo malo?"
    pause 2.0
    "Ahora no puedo dejar de pensar en eso..."
    scene cg en_cama_2 with Dissolve(0.2)
    ai "Debería ir entonces..."
    scene cg en_cama_1 with Dissolve(0.3)
    "Para quitarme mis dudas..."
    "..."
    scene cg en_cama_2 with Dissolve(0.2)
    ai "{i}*Suspiro*{/i}"
    scene cg en_cama_1 with Dissolve(0.3)
    stop music fadeout 2.0
    window hide(Dissolve(.2))
    pause 2.0
    scene black with Dissolve(.5)
    pause 1.0
    window auto
    "Estuve ya el tiempo suficiente en la enfermería..."
    "Me levanté de la cama para dirigirme de nuevo al salón de clases..."
    window hide(Dissolve(.2))
    pause 2.0
    scene bg nursing with Dissolve(0.4)
    pause 1.0
    window auto
    ai "Tanto tiempo que pasé aquí..."
    "No se cuando fue la última vez que estuve en la enfermería por tanto tiempo..."
    ai "{i}*Suspiro*{/i}"
    "Sin más, solo salgo de la enfermería..."
    pause 1.0
    play audio open_door
    scene bg school_hallway with hgradient_left_scene_full
    pause 1.0
    "Al salir de la enfermería, solo puedo notar la monocromía del pasillo de la universidad."
    ai "Se ve tan apagado..."
    ai "Sin vida..."
    ai "Tan parecido y a la vez tan..."
    ai "¿Desigual?"
    "No se que pensar..."
    "Simplemente es bastante extraño verlo así."
    "Los colores al menos le daban una vibra más..."
    "¿Viva?"
    "Creo que puedo decirlo de esa manera."
    pause 1.0
    scene bg school_hallway with hgradient_left_scene_full
    play music m4 fadein 2.0
    pause 1.0
    "Caminando por el pasillo, veo algo que llama mi atención..."
    ai "¿Un cartel?"
    scene cg talents_show with Dissolve(0.5)
    "..."
    "Nunca lo había visto."
    "Al parecer el club de música quiere hacer un show de talentos..."
    ai "Entraría a algo así pero..."
    "Pero no creo tener ningún tipo de talento..."
    "Me gusta la música, pero creo que intentar algo así solo me dejaría en ridículo frente a los demás..."
    ai "No vale la pena el riesgo..."
    "Ya he dicho mucho esa frase..."
    "¿No vale la pena el riesgo?"
    "{i}¿Qué riesgo?{/i}"
    "{i}¿Tienes miedo a hacer algo que pueda dejarte en ridículo frente a los demás?{/i}"
    "{i}¿No quieres llamar la atención de los demás?{/i}"
    "La verdad si..."
    "¿O puedo llamarlo pena ajena?"
    "..."
    "La verdad no se..."
    "Solo sé que no quiero entrar en algo así."
    "Y que no hay una muestra mía de interés en cosas así..."
    ai "{i}*Suspiro*{/i}"
    "Mejor no sigo perdiendo el tiempo..."
    scene bg school_hallway with hgradient_left_scene_full
    stop music fadeout 2.0
    pause 1.0
    "Acercándome a la puerta del salón, me comienzo a poner un poco nerviosa..."
    "Estuve mucho tiempo en la enfermería..."
    ai "{i}*Suspiro*{/i}"
    "Solo entro sin más..."
    "Esperando la respuesta de los demás..."
    play audio open_door
    scene bg front_classroom with hgradient_left_scene_full
    pause 1.0
    show tetsuo 3 at cso11
    tetsuo "¿Como te sientes Ai?"
    tetsuo "¿Estás mejor?"
    show tetsuo 4 at cso21
    show azumi 4 at cso22
    azumi "Tardaste un poco en venir aquí."
    azumi "¿Te sentiste mal de nuevo?"
    show azumi 3
    ai "Solo me distraje mientras caminaba hasta aquí."
    ai "Y si, me siento mejor jeje."
    show azumi 1
    play music m5 fadein 1.0
    tetsuo 2 "Me alegro."
    tetsuo "Fui a la enfermería mientras estabas dormida."
    tetsuo 3 "Si te sientes mal de nuevo no dudes en decirlo..."
    tetsuo "No te impedire ir a la enfermería si así lo necesitas."
    show tetsuo 1
    ai "Lo tendré en cuenta."
    tetsuo 2 "¿Continuaras con el ejercicio?"
    show tetsuo 1
    ai "Si, si lo continuare."
    tetsuo 6 "Excelente."
    tetsuo 2 "Que lo que acaba de pasar no te limite."
    tetsuo "Ten eso en cuenta."
    tetsuo "Bueno, pueden tomar asiento, que la clase aún continúa."
    hide tetsuo
    pause 1.0
    show azumi 2 at cso11
    azumi "Vayamos a nuestros asientos."
    azumi "Continuemos en donde nos quedamos."
    show azumi 1
    ai "¿Tu no terminaste el ejercicio?"
    azumi 6 "No jeje."
    azumi "Estuve acompañándote hasta que despertaste."
    show azumi 5
    "Vaya..."
    ai "Gracias por eso."
    azumi 2 "Tu descuida, es lo que hacen las amigas."
    azumi 6 "Ya continuemos con los ejercicios."
    azumi 13 "Porque la verdad no quiero pensar en la idea de hacer enojar al profesor jeje."
    show azumi 12
    ai "Si jeje."
    "Nos sentamos en nuestros asientos y continuamos en donde nos quedamos."
    azumi 2 "Hablamos más tarde."
    azumi 4 "Aunque si te llegas a sentir mal me dices, ¿De acuerdo?"
    show azumi 3
    ai "Si..."
    azumi 6 "Perfecto."
    azumi "Ahora si, continuemos en donde nos quedamos."
    show azumi 1
    ai "Vale."
    hide azumi
    stop music fadeout 2.0
    pause 2.0
    "Bueno..."
    "Continuemos en donde lo deje..."
    window hide(Dissolve(.2))
    pause 1.0
    scene black with Dissolve(2.0)
    pause 1.0
    play audio drawing
    pause 3.0
    scene bg front_classroom with Dissolve(1.0)
    pause 1.0
    "Han pasado varias horas..."
    "Terminamos los ejercicios de composición que el profesor había dicho..."
    "Después de eso, el profesor nos continuó hablando de formas en las que podemos mejorar, así como en otras cosas relacionadas a su materia."
    "Es interesante escucharlo."
    "¿Interesante? claro."
    "Por algo estudió está materia."
    "..."
    "Aunque a veces no ponga de mi parte en realizar lo que él dice."
    "O si acaso en indagar más en la materia."
    "..."
    show tetsuo 2 at cso11
    play music m3 fadein 2.0
    tetsuo "Bueno estudiantes, la clase de hoy ha terminado."
    tetsuo "Espero les haya gustado lo que hemos visto hoy."
    show tetsuo 1
    girl_1 "Estuvo excelente."
    tetsuo 2 "Recuerden que nos veremos la semana que viene."
    tetsuo "Que es nuestra última semana que estaremos en Diciembre."
    tetsuo 6 "Pero no olviden realizar más ejercicios y practicar."
    tetsuo "Y traer algo para compartir entre todos jeje."
    tetsuo 2 "Con esto dicho, nos vemos la siguiente semana."
    tetsuo "Pueden retirarse."
    hide tetsuo
    pause 1.0
    "Bueno, ya no hay más clases..."
    "Hoy en si era el último día de clases."
    "Debido a que tendremos vacaciones en Diciembre."
    "El profesor quiso realizar una reunión de despedida la siguiente semana."
    "..."
    show azumi 6 at cso11
    azumi "Por fin, no más clase jeje."
    azumi "Podremos descansar un poco."
    show azumi 5
    ai "Si jeje."
    azumi 8 "Y eso incluye dormir mejor, ¿verdad?"
    show azumi 7
    ai "Bueno..."
    ai "Lo intentare."
    azumi 8 "Eso espero."
    azumi 2 "Se me olvido preguntarte si irás al evento de encendido de luces de la plaza."
    show azumi 1
    ai "Pues..."
    ai "No se."
    azumi 6 "Vamos tienes que ir."
    azumi "No has asistido desde hace como 2 años."
    azumi 10 "Asiste hoy, por favor."
    show azumi 9
    ai "Voy a pensarlo."
    azumi 10 "Espero que si vayas."
    azumi "Aunque no te sientas obligada por mi."
    show azumi 9
    ai "Descuida..."
    "La verdad no se si ir o no."
    "Ahora menos tiene sentido ir con todo esto que está pasando."
    "¿Para qué iría si todo se vería gris?"
    "Carente de algún tipo de color."
    "Deje de ir porque me aburre un poco el evento."
    "No puedo prometerle a Azumi que iré..."
    "A mi madre tampoco."
    "..."
    ai "Dejame pensarlo."
    azumi 2 "Bueno, con eso basta."
    azumi 6 "Espero que si vayas."
    show azumi 5
    pause 1.0
    azumi 2 "Ya vayámonos."
    azumi "Quiero ir a comer jeje."
    show azumi 1
    ai "Si, yo también."
    hide azumi
    pause 1.0
    "Azumi y yo recogimos nuestras cosas, y comenzamos a caminar hasta la puerta del salón para retirarnos."
    "No sin antes despedirnos del profesor."
    azumi_ai "Adiós profesor."
    azumi "Nos vemos la próxima semana."
    show tetsuo 2 at cso11
    tetsuo "Adiós muchachas."
    tetsuo "Nos vemos."
    tetsuo "No olviden practicar."
    show tetsuo 1
    azumi "Claro jeje."
    tetsuo 2 "Bueno, que les vaya bien."
    hide tetsuo
    pause 1.0
    show tetsuo 2 at cso11
    tetsuo "Ai, antes de que te vayas quiero hablar contigo un momento."
    show tetsuo 1
    ai "Claro..."
    ai "¿Qué sucede?"
    tetsuo 3 "Es sobre lo que te paso."
    tetsuo "¿Estás bien?"
    show tetsuo 4
    ai "Pues si..."
    tetsuo 3 "Bueno, es un poco preocupante lo que te sucedió."
    tetsuo "Son mis estudiantes, y debo preocuparme por ustedes."
    tetsuo "¿Crees saber por qué te sucedió eso?"
    show tetsuo 4
    menu:
        ai "Pues..."
        "La verdad no duermo bien.":
            ai "Pasa que a veces no puedo dormir bien."
            ai "Creo que se debe a eso."
            "La verdad no se si sea por eso."
            tetsuo 3 "Bueno..."
            tetsuo "Puedes ponerlo como una posibilidad."
            tetsuo "Entonces pues intenta dormir mejor."
            tetsuo "Y si te vuelve a suceder algo así, hazlo saber a quien tengas más cerca."
            show tetsuo 4
            ai "Claro..."
            "La verdad no quiero que algo así me pase enfrente a mi madre."
            "No quiero que se preocupe."
            $ persistent.decissions['estas_bien0'] = True
        "La verdad no se.":
            ai "La verdad no tengo idea del porque me paso."
            tetsuo 3 "Es un poco preocupante que te pase sin más."
            tetsuo "¿Duermes bien?"
            tetsuo "¿Comes bien?"
            tetsuo "Hay muchas razones por la cual pudo sucederte eso."
            tetsuo "Esperemos que no sea causado por nada malo."
            tetsuo "Claro, mejor pensar que no es por algo malo."
            ai "Si, quiero pensarlo de esa manera."
            $ persistent.decissions['estas_bien1'] = True
    pause 1.0
    ai "Bueno..."
    show tetsuo 1
    ai "Nos vemos profesor."
    ai "Gracias por preocuparse."
    tetsuo 2 "Son mis estudiantes, es mi deber estar al tanto de ustedes."
    tetsuo "No solo académicamente, sino también cuidar de que estén bien."
    tetsuo 3 "Se que son adultos, pero igualmente tengo que preocuparme por todos."
    show tetsuo 4
    ai "Si, lo entiendo."
    ai "Nos vemos."
    tetsuo 2 "Cuidate."
    hide tetsuo
    stop music fadeout 1.5
    pause 1.0
    "Después de esta charla con el profesor, salgo del salón."
    play audio open_door
    scene bg school_hallway with hgradient_left_scene_full
    pause 1.0
    show azumi 2 at cso11
    azumi "¿Todo bien?"
    show azumi 1
    ai "Si, solo me estaba preguntando cómo estaba."
    azumi 2 "No creas que no se preocupo por lo que te paso."
    azumi 4 "Y no solo él, varios de nuestros compañeros también estaban preocupados."
    show azumi 3
    ai "Ya veo."
    pause 1.0
    play music m2 fadein 2.0
    azumi 2 "Aunque dejemos ese tema."
    azumi "Ya estás mejor qué es lo importante."
    show azumi 1
    ai "Si..."
    "Espero que no se vuelva a repetir..."
    pause 1.0
    "Espero..."
    scene bg school_hallway with hgradient_left_scene_full
    "Azumi y yo comenzamos a caminar para salir de la escuela."
    "Mientras lo hacemos comenzamos a platicar."
    "Comenzó a compartir ideas para un proyecto que quiere realizar."
    "Así como yo también le compartí mis ideas..."
    scene bg school_entrance with hgradient_left_scene_full
    "Al salir de la escuela, nos toca dirigirnos a la estación de trenes nuevamente para ir a nuestras casas."
    "No está lejos de aquí tampoco."
    "Pero hablar nos distrae durante el recorrido hasta allí."
    window hide(Dissolve(.2))
    pause 2.0
    scene black with Dissolve(1.5)
    pause 1.0
    window auto
    "Caminamos por la ciudad para dirigirnos a la estación de trenes."
    "En el camino se nos antojó comprar unos helados."
    "Le dije a Azumi que los escogiera."
    "Aunque no le dije el porque..."
    ai "Solo escogelos jeje."
    azumi "Bueno, espero te guste el sabor que escojas para ti."
    pause 1.0
    stop music fadeout 1.0
    "Al llegar a la estación de trenes y esperar nuestro tren."
    "Nos subimos y esperamos nuevamente..."
    play music inside_train fadein 2.0
    pause 6.0
    stop music fadeout 1.0
    play sound trainStop
    pause 2.0
    stop sound fadeout 1.0
    "Al llegar a nuestra parada nos bajamos y comenzamos a caminar a nuestras casas."
    "Vivimos cerca y por eso tomamos el mismo tren."
    window hide(Dissolve(.2))
    pause 1.0
    show bg ai_house with Dissolve(1.5)
    pause 1.0
    "Llegamos a mi casa..."
    "Azumi vive unas 2 cuadras arriba en la calle en donde vivo."
    "Así que por eso me acompaña."
    play music m1 fadein 2.0
    show azumi 2 at cso11
    azumi "Bueno Ai, nos vemos."
    azumi 13 "Hoy no podré entrar a tu casa, porque tengo cosas que hacer."
    azumi 2 "Aunque mañana puedo venir si quieres."
    show azumi 1
    ai "Claro."
    ai "Tú descuida."
    azumi 6 "Perfecto."
    azumi 2 "Ten en cuenta lo que te dije hoy."
    azumi "¿De acuerdo?"
    show azumi 1
    ai "Si si."
    ai "No te preocupes."
    azumi 6 "Vale vale."
    azumi 2 "Bueno, nos vemos."
    azumi "Quizás de la casualidad que vaya hoy a tu casa antes del evento."
    azumi 6 "Aunque espero verte por haya."
    azumi 13 "Si, se que lo vas a pensar."
    azumi "Pero me quiero hacer la idea de que si iras."
    azumi 12 "Aunque si no puedes no importa."
    pause 1.0
    azumi 6 "Ahora si, nos vemos Ai."
    show azumi 5
    ai "Adios Azumi."
    hide azumi
    stop music fadeout 2.0
    pause 2.0
    "Después de despedirme de Azumi solo me queda entrar a mi casa."
    "No sé para que sobre pienso eso."
    pause 1.0
    play audio open_door
    scene bg ai_livingroom with hgradient_left_scene_full
    pause 1.0
    play music m4 fadein 2.0
    show shiori normal1 at cso11
    shiori "Hola hija, bienvenida de nuevo."
    show shiori idle
    ai "Hola ma."
    shiori normal1 "¿Como te fue?"
    shiori "¿Estuvo bien la clase de hoy?"
    show shiori idle
    ai "Si, estuvo bien."
    ai "Como siempre jeje."
    shiori normal1 "Casi termino los pastelitos."
    shiori sad2 "Después de que almuerces necesito que vayas a la tienda de nuevo jeje."
    shiori "Hubo algo que me faltó que compraras."
    show shiori sad1
    ai "Claro yo voy, tu descuida."
    "Espero que no sea algo específico nuevamente."
    "No quiero tener que adivinar de nuevo."
    shiori normal1 "No puedo ir a comprarlo yo, es que no quiero descuidar por mucho tiempo los pastelitos."
    shiori "Iré a revisarlos nuevamente, ve a cambiarte para que almuerces."
    shiori "La comida está recién hecha, así que no habrá que calentarla."
    show shiori idle
    ai "Vale."
    hide shiori
    pause 1.0
    "Después de terminar de conversar con mi madre, me dirijo a mi cuarto."
    scene bg ai_room with hgradient_left_scene_full
    pause 1.0
    "Al entrar dejo mi mochila en donde va y me cambio de ropa..."
    pause 2.0
    ai "Ya estoy lista."
    stop music fadeout 1.0
    "Al girar mi mirada, algo llama mi atención..."
    "Es el espejo que tengo en una mesa..."
    scene cg frente_al_espejo_1
    show layer master at zoomCam3(1.1, 20)
    show vignette2 onlayer effects
    show black2 onlayer effects2
    with Dissolve(0.3)
    pause 1.0
    $ renpy.music.set_volume(0.4)
    play music terrorGround fadein 1.0
    pause 1.0
    scene cg frente_al_espejo_2 with Dissolve(.2)
    ai "Vaya..."
    ai "Si..."
    ai "Me veo mal..."
    scene cg frente_al_espejo_1 with Dissolve(.2)
    "Quien lo diría..."
    scene cg frente_al_espejo_2 with Dissolve(.2)
    ai "¿Estoy bien, verdad?"
    scene cg frente_al_espejo_1 with Dissolve(.2)
    "¿Verdad?"
    scene cg frente_al_espejo_2 with Dissolve(.2)
    ai "¿Qué tengo?"
    ai "¿Realmente estoy bien?"
    scene cg frente_al_espejo_1 with Dissolve(.2)
    "No hay una respuesta a esas preguntas..."
    "No hay una..."
    "Respuesta..."
    scene cg frente_al_espejo_2 with Dissolve(.2)
    ai "¿Estare bien?"
    ai "¿Verdad?"
    scene cg frente_al_espejo_1 with Dissolve(.2)
    "¿Verdad?"
    scene cg frente_al_espejo_2 with Dissolve(.2)
    ai "Solo el tiempo lo dirá..."
    scene cg frente_al_espejo_1 with Dissolve(.2)
    "Solo el tiempo..."
    "Lo dirá..."
    window hide(Dissolve(.3))
    show layer master at zoomCam3(1.05, 10)
    pause 2.0
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause 2.0
    hide vignette2 onlayer effects
    hide black2 onlayer effects2
    $ persistent.capListComplete['cap1'] = True

    return