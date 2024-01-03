
label quit:

    $ rpc.stop()
    
    return

image demoInfo = ParameterizedText(xalign=0.5, yalign=0.5,style="demoInfo")
style demoInfo:
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
        show demoInfo _("¡Este juego es una demo!\nEl juego puede someterse a cambios a medida que se actualice\nDialogos, imagenes, sonidos y música pueden llegar a cambiar.") with Dissolve(1.0)
        pause 6
        hide demoInfo with Dissolve(1.0)
        pause 1.0
        scene white with Dissolve(1.0)
        $ persistent.FirstGame = True

    scene white
    pause 1.0
    play audio IamQuetzalcoatl
    show QuetzalLogo with Dissolve(1.0)
    pause 2.0
    hide QuetzalLogo with Dissolve(1.0)
    pause 1.0

    return