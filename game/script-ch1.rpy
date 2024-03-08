
label ch_1:
    
    scene black
    pause 2.0
    window auto
    $ quick_menu = True
    "Puedo decir que este día será fatal."
    "O quizás puedo esperar a ver que me deparara este día."
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
    window hide(Dissolve(.2))
    stop music fadeout 2.0
    pause 2.0
    scene bg station_platform with hgradient_left_scene_full
    play music trainAnnouncement fadein 2.0
    pause 4.0
    window auto
    "Tan concentrada en lo que estaba escuchando, que apenas me doy cuenta de que el tren acaba de llegar."
    ai "Por fin..."
    pause 1.0
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

    return