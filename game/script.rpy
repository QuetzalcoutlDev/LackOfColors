﻿
image chapterTXT = ParameterizedText(xalign=0.5, yalign=0.5, style="chapterText")
default chapterInfo = _("")

style chapterText:
    size 30
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
        $ chapterInfo = _("{size=-12}Prólogo:{/size}\nAmanecer descolorido")
        show chapterTXT "[chapterInfo]" with Dissolve(1.5)
        pause 2.0
        hide chapterTXT with Dissolve(1.5)
        pause 2.0
    
    $ persistent.FirstInit = False

    $ chapter = 0
    $ persistent.chapter = 0
    $ rpc.set_status(details=_("Prólogo: Amanecer descolorido"), state=_("Jugando..."))
    call ch_0 from _call_ch_0
    
    if persistent.demo:
        call demo from _call_demo
        
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

    $ chapterInfo = _("Está versión del juego es solo una demo\nGracias por jugar Lack Of Colors\nNo olvides dar tu opinión sobre el mismo\nMe ayudarás mucho con tu comentario\n:)")
    show chapterTXT "[chapterInfo]" with Dissolve(1.5)
    pause 5.0
    hide chapterTXT with Dissolve(1.5)
    pause 2.0
    
    return