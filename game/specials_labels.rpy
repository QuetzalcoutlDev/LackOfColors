
image SplashInfo = ParameterizedText(xalign=0.5, yalign=0.5,style="splashInfo")
style splashInfo:
    size 30
    color "#ffffff"
    font "URWBookman-Light.otf"
    textalign 0.5

style splashInfo:
    variant "small"
    
    size 35

label splashscreen:

    $ rpc.rpc_start()
    $ rpc.set_status(details=__("Iniciando..."))

    if not persistent.FirstGame:

        scene black 
        stop music
        menu:
            "Selecciona tú idioma / Select your language"
            "Español.":
                $ persistent.language = None
                $ renpy.change_language(None)
            "English.":
                $ persistent.language = "english"
                $ renpy.change_language("english")

        window hide(None)
        pause 1.0
        show SplashInfo __("¡Este juego es una demo!\nEl juego puede someterse a cambios a medida que se actualice\nDiálogos, imágenes, sonidos y música pueden llegar a cambiar.") with Dissolve(1.0)
        pause 6
        hide SplashInfo with Dissolve(1.0)
        pause 1.0
        $ persistent.FirstGame = True

    if persistent.FirstGame:
        scene black 
        show SplashInfo __("{size=-6}Usa audífonos para disfrutar de una mejor experiencia.{/size}")
        pause 3.0
        hide SplashInfo with Dissolve(1.0)
        pause 1.0
        
    pause 1.0
    play audio IamQuetzalcoatl
    show QuetzalLogo with Dissolve(1.0)
    pause 2.0
    hide QuetzalLogo with Dissolve(1.0)
    pause 1.0
    
    return

label after_load:

    if persistent.chapter == 0:
        $ rpc.set_status(details=__("Prólogo: Amanecer descolorido"), state=__("Jugando..."))
    elif persistent.chapter == 1:
        $ rpc.set_status(details=__("Capitulo 1: Colores apagados"), state=__("Jugando..."))
    return

label before_main_menu:
    
    $ rpc.set_status(details=__("En menú principal"))

    return

label quit:
    $ rpc.stop()
    
    return