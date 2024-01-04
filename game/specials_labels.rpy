
image SplashInfo = ParameterizedText(xalign=0.5, yalign=0.5,style="splashInfo")
style splashInfo:
    size 30
    color "#ffffff"
    font "URWBookman-Light.otf"
    textalign 0.5

label splashscreen:

    $ rpc.rpc_start()
    $ rpc.set_status(details=_("Iniciando..."))

    if not persistent.FirstGame:
        scene black 
        pause 1.0
        show SplashInfo _("¡Este juego es una demo!\nEl juego puede someterse a cambios a medida que se actualice\nDialogos, imagenes, sonidos y música pueden llegar a cambiar.") with Dissolve(1.0)
        pause 6
        hide SplashInfo with Dissolve(1.0)
        pause 1.0
        scene white with Dissolve(1.0)
        $ persistent.FirstGame = True

    if persistent.FirstGame:
        scene black 
        show SplashInfo _("{size=-9}Usa audifonos para tener una mejor experiencia.{/size}")
        pause 3.0
        hide SplashInfo with Dissolve(1.0)
        pause 1.0

    if not persistent.FirstGame:    
        scene black
    else:    
        scene white with Dissolve(0.7)
    pause 1.0
    play audio IamQuetzalcoatl

    if not persistent.FirstGame:
        show QuetzalLogoInvert with Dissolve(1.0)
        pause 2.0
        hide QuetzalLogoInvert with Dissolve(1.0)
        pause 1.0
    else:
        show QuetzalLogo with Dissolve(1.0)
        pause 2.0
        hide QuetzalLogo with Dissolve(1.0)
        pause 1.0

    return

label after_load:

    if persistent.chapter == 0:
        $ rpc.set_status(details=_("Prologo: Amanecer descolorido"), state=_("Jugando..."))
    return

label before_main_menu:
    
    $ rpc.set_status(details=_("En menú principal"))

    return

label quit:
    $ rpc.stop()
    
    return