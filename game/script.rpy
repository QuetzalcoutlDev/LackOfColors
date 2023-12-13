
image chapterTXT = ParameterizedText(xalign=0.5, yalign=0.5, style="chapterText")
default chapterInfo = _("")

style chapterText:
    size 42
    color "#ffffff"
    font "URWBookman-Light.otf"
    textalign 0.5

label start:

    window hide(None)
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ quick_menu = False

    $ _shiori_name = "???"
    $ _yu_name = "???"
    $ _hideaki_name = "???"

    stop music fadeout 2.0
    with Dissolve(2.0)
    
    scene black
    show vignette onlayer effects
    pause 1.0

    if persistent.FirstInit:
        $ persistent.chapter = 0
        $ chapterInfo = _("{size=-15}Prologo:{/size}\nAmanecer descolorido")
        show chapterTXT "[chapterInfo]" with Dissolve(1.5)
        pause 2.0
        hide chapterTXT with Dissolve(1.5)
        pause 2.0
    
    $ persistent.FirstInit = False

    $ chapter = 0
    call ch_0
    
    if persistent.demo:
        call demo

    return

label demo:

    window hide(Dissolve(.4))

    $ allow_skipping = True
    $ config.allow_skipping = True
    $ quick_menu = False
    
    stop music fadeout 2.0
    with Dissolve(2.0)
    
    scene black
    pause 1.0

    $ chapterInfo = _("Esto es solo una demo\nGracias por jugar Lack Of Colors\nUn juego hecho para la Github GameOFF 2023, para más información puedes leer el archivo 'LEEME.txt'")
    show chapterTXT "[chapterInfo]" with Dissolve(1.5)
    pause 2.0
    hide chapterTXT with Dissolve(1.5)
    pause 2.0
    
    return