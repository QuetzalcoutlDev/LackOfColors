
define fadefast = Fade(0.5, 0.5, 0.5, color="#000000")
define fade = Fade(1.0, 0.5, 1.0, color="#000000")
define fadeslow = Fade(2.0, 0.5, 2.0, color="#000000")
define fadeveryslow = Fade(3.0, 0.5, 3.0, color="#000000")

define dissolvefast = Dissolve(0.5)
define dissolve = Dissolve(1.0)
define dissolveslow = Dissolve(2.0)
define dissolveveryslow = Dissolve(3.0)

transform character_show_out(x=640):
    yanchor 1.0 subpixel True

    on show:
        ypos 1.71 zoom 0.9
        xcenter x alpha 0.0
        ease .3 ypos 1.70 alpha 1.0 zoom 0.96
    on replace:
        alpha 1.0
        parallel:
            ease .3 xcenter x zoom 0.96
    on hide:
        ease .3 alpha 0.0 ypos 1.71 zoom 0.90
        
transform cso11:
    character_show_out(x=640)
transform cso21:
    character_show_out(x=320)
transform cso22:
    character_show_out(x=960)

transform left_right_in_out(x1=640, x2=-300):
    yanchor 1.0 subpixel True

    on show:
        ypos 1.70 zoom 0.96 xcenter x2 
        ease .9 xcenter x1
    on hide:
        ease .9 xcenter x2

transform lio11:
    left_right_in_out(640, -300)
transform lio21:
    left_right_in_out(320, -300)
transform lio22:
    left_right_in_out(960, -300)

transform rio11:
    left_right_in_out(640, 1490)
transform rio21:
    left_right_in_out(320, 1490)
transform rio22:
    left_right_in_out(960, 1490)

transform character_jump(x=640):
    yanchor 1.0 subpixel True ypos 1.70 zoom 0.96 xcenter x
    linear .1 ypos 1.67
    ease .1 ypos 1.70
    
transform j11:
    character_jump(x=640)
transform j21:
    character_jump(x=320)
transform j22:
    character_jump(x=960)

define hgradient_left = ImageDissolve("images/horizontal_gradient.png", 0.5, 64, reverse=False)
define hgradient_right = ImageDissolve("images/horizontal_gradient.png", 0.5, 64, reverse=True)

define hgradient_left_scene_full = MultipleTransition([
    False, ImageDissolve("images/horizontal_gradient.png", 0.5, 64, reverse=False),
    Solid("#000000"), Pause(0.5),
    Solid("#000000"),ImageDissolve("images/horizontal_gradient.png", 0.5, 64, reverse=False),
    True])

define hgradient_right_scene_full = MultipleTransition([
    False, ImageDissolve("images/horizontal_gradient.png", 0.5, 64, reverse=True),
    Solid("#000000"), Pause(0.5),
    Solid("#000000"),ImageDissolve("images/horizontal_gradient.png", 0.5, 64, reverse=True),
    True])

transform objectShow:
    yanchor 1.0 subpixel True xpos 0.0
    on show:
        alpha 0.0 ypos 1.1
        ease .8 alpha 1.0 ypos 1.0
    on hide:
        ease .8 alpha 0.0 ypos 1.1
    
transform blur_effect(v=1.0):
    blur v

transform train_move():
    yanchor 1.0 subpixel True xpos -0.1 ypos 1.0 zoom 1.1
    block:
        linear 0.1 ypos 1.002
        pause 0.05
        linear 0.1 ypos 1.0
        pause 0.05
        linear 0.1 ypos 1.005
        pause 0.05
        linear 0.1 ypos 1.002
        pause 0.05
        linear 0.1 ypos 1.005
        pause 0.05
        repeat

transform zoomCam():
    zoom 2.0 xcenter 0.5 ycenter 0.5
    ease 0.4 zoom 1.0 
    repeat 2

transform Nothing():
    ease 0.2 zoom 1.0

transform zoomCam2():
    xcenter 0.5 ycenter 0.5
    block:
        ease 0.1 zoom 1.003
        ease 0.1 zoom 1.006
        ease 0.1 zoom 1.003
        ease 0.1 zoom 1.005
        ease 0.1 zoom 1.0
        repeat

transform zoomCam3(z, t):
    xcenter 0.5 ycenter 0.5
    linear t zoom z