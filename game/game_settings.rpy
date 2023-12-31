
init -1 python:

    _dismiss_pause = config.developer
    config.keymap["game_menu"].remove("mouseup_3")
    config.keymap["hide_windows"].append("mouseup_3")

    config.has_autosave = False
    config.has_quicksave = False

default persistent.capListComplete = {
    "cap0": False, # Prologo 
    "cap1": False, # Capitulo 1 (Aun no disponible en esta versión)
    "cap2": False, # Capitulo 2 (Aun no disponible en esta versión)
    "cap3": False  # Capitulo 3 (Aun no disponible en esta versión)
}

default chapter = 0
define config.gl2 = False
define config.has_sync = False
default persistent.chapter = 0
default persistent.FirstInit = True
default persistent.FirstGame = False
default persistent.demo = True
default persistent.notifyTime = 5

image black = "#000000"
image white = "#ffffff"
image vignette:
    "gui/vignette.png"
    xpos 0.5
    ypos 1.0
    alpha 0.7

image vignette2:
    "gui/vignette.png"
    xpos 0.5
    ypos 1.0
    block:
        alpha 1.0
        pause 0.1
        alpha 0.9
        pause 0.1
        repeat

image black2:
    "#000000"
    block:
        alpha 0.6
        pause 0.1
        alpha 0.55
        pause 0.1
        repeat

image cps:
    "gui/cps.png"
    zoom 0.4 alpha 0.0 xpos 1060 ypos 680
    block:
        linear 0.3 alpha 1.0 xoffset 5
        pause 0.4
        linear 0.3 alpha 0.0 xoffset 0
        pause 0.4
        repeat

image menuFlash:
    "white"
    menuFade

image menuFlashInvert:
    "black"
    menuFade

image menuBG:
    "images/menuBG/menuBG0000.png"
    pause 0.5
    "images/menuBG/menuBG0001.png"
    pause 0.5
    "images/menuBG/menuBG0002.png"
    pause 0.5
    repeat
    
transform menuFade:
    easeout 0.9 alpha 0.0

image QuetzalLogo = "images/QuetzalLogo.png"
image QuetzalLogoInvert = "images/QuetzalLogoInvert.png"

default _ai_name = _("Ai")
default _shiori_name = _("Shiori")
default _yu_name = _("Yu")
default _hideaki_name = _("Hideaki")

define narrator = Character(ctc="cps", ctc_position="fixed")
define ai = Character(name="[_ai_name]", image="ai", what_prefix='"', what_suffix='"',  who_color="#ffffff", ctc="cps", ctc_position="fixed")
define shiori = Character(name="[_shiori_name]", image="shiori", what_prefix='"', what_suffix='"',  who_color="#ffffff", ctc="cps", ctc_position="fixed")
define yu = Character(name="[_yu_name]", image="yu", what_prefix='"', what_suffix='"',  who_color="#ffffff", ctc="cps", ctc_position="fixed")
define hideaki = Character(name="[_hideaki_name]", image="hideaki", what_prefix='"', what_suffix='"',  who_color="#ffffff", ctc="cps", ctc_position="fixed")

### Sonido y música

# Sonido
define audio.clock_alarm = "audio/clock-alarm.ogg"
define audio.knock_1 = "audio/knock_1.ogg"
define audio.knock_2 = "audio/knock_2.ogg"
define audio.knock_3 = "audio/knock_3.ogg"
define audio.open_door = "audio/open_door.ogg"
define audio.store_ring = "audio/convenience_storering.ogg"
define audio.shower = "audio/shower.ogg"
define audio.IamQuetzalcoatl = "audio/IamQuetzalcoatl.ogg"

# Música
define audio.m1 = "audio/Faded_mornings.ogg"
define audio.m2 = "audio/In_my_mind.ogg"
define audio.m3 = "audio/Hikara.ogg"
define audio.terrorGround = "audio/terror_ground.ogg"
define audio.menuTheme = "audio/Lack.ogg"

### Sprites de personajes

# Ai
image ai idle = "images/sprites/ai/Ai idle.png"
image ai happy1 = "images/sprites/ai/Ai happy1.png"
image ai happy2 = "images/sprites/ai/Ai happy2.png"
image ai happy3 = "images/sprites/ai/Ai happy3.png"
image ai happy4 = "images/sprites/ai/Ai happy4.png"
image ai happy5 = "images/sprites/ai/Ai happy5.png"
image ai meh1 = "images/sprites/ai/Ai meh1.png"
image ai meh2 = "images/sprites/ai/Ai meh2.png"
image ai normal1 = "images/sprites/ai/Ai normal1.png"
image ai normal2 = "images/sprites/ai/Ai normal2.png"
image ai normal3 = "images/sprites/ai/Ai normal3.png"
image ai normal4 = "images/sprites/ai/Ai normal4.png"
image ai normal5 = "images/sprites/ai/Ai normal5.png"
image ai normal6 = "images/sprites/ai/Ai normal6.png"
image ai normal7 = "images/sprites/ai/Ai normal7.png"
image ai hmm1 = "images/sprites/ai/Ai hmm1.png"
image ai hmm2 = "images/sprites/ai/Ai hmm2.png"
image ai hmm3 = "images/sprites/ai/Ai hmm3.png"
image ai hmm4 = "images/sprites/ai/Ai hmm4.png"
image ai hmm5 = "images/sprites/ai/Ai hmm5.png"
image ai ha1 = "images/sprites/ai/Ai ha1.png"
image ai angry1 = "images/sprites/ai/Ai angry1.png"
image ai angry2 = "images/sprites/ai/Ai angry2.png"
image ai angry3 = "images/sprites/ai/Ai angry3.png"
image ai angry4 = "images/sprites/ai/Ai angry4.png"
image ai angry5 = "images/sprites/ai/Ai angry5.png"
image ai sad1 = "images/sprites/ai/Ai sad1.png"
image ai sad2 = "images/sprites/ai/Ai sad1.png"
image ai sad3 = "images/sprites/ai/Ai sad1.png"
image ai sad4 = "images/sprites/ai/Ai sad1.png"
image ai sad5 = "images/sprites/ai/Ai sad1.png"
image ai agh1 = "images/sprites/ai/Ai agh1.png"
image ai agh2 = "images/sprites/ai/Ai agh2.png"
image ai agh3 = "images/sprites/ai/Ai agh3.png"
image ai agh4 = "images/sprites/ai/Ai agh4.png"
image ai agh5 = "images/sprites/ai/Ai agh5.png"
image ai surprise1 = "images/sprites/ai/Ai surprise1.png"

image ai casual idle = "images/sprites/ai/casual/Ai idle.png"
image ai casual happy1 = "images/sprites/ai/casual/Ai happy1.png"
image ai casual happy2 = "images/sprites/ai/casual/Ai happy2.png"
image ai casual happy3 = "images/sprites/ai/casual/Ai happy3.png"
image ai casual happy4 = "images/sprites/ai/casual/Ai happy4.png"
image ai casual happy5 = "images/sprites/ai/casual/Ai happy5.png"
image ai casual meh1 = "images/sprites/ai/casual/Ai meh1.png"
image ai casual meh2 = "images/sprites/ai/casual/Ai meh2.png"
image ai casual normal1 = "images/sprites/ai/casual/Ai normal1.png"
image ai casual normal2 = "images/sprites/ai/casual/Ai normal2.png"
image ai casual normal3 = "images/sprites/ai/casual/Ai normal3.png"
image ai casual normal4 = "images/sprites/ai/casual/Ai normal4.png"
image ai casual normal5 = "images/sprites/ai/casual/Ai normal5.png"
image ai casual normal6 = "images/sprites/ai/casual/Ai normal6.png"
image ai casual normal7 = "images/sprites/ai/casual/Ai normal7.png"
image ai casual hmm1 = "images/sprites/ai/casual/Ai hmm1.png"
image ai casual hmm2 = "images/sprites/ai/casual/Ai hmm2.png"
image ai casual hmm3 = "images/sprites/ai/casual/Ai hmm3.png"
image ai casual hmm4 = "images/sprites/ai/casual/Ai hmm4.png"
image ai casual hmm5 = "images/sprites/ai/casual/Ai hmm5.png"
image ai casual ha1 = "images/sprites/ai/casual/Ai ha1.png"
image ai casual angry1 = "images/sprites/ai/casual/Ai angry1.png"
image ai casual angry2 = "images/sprites/ai/casual/Ai angry2.png"
image ai casual angry3 = "images/sprites/ai/casual/Ai angry3.png"
image ai casual angry4 = "images/sprites/ai/casual/Ai angry4.png"
image ai casual angry5 = "images/sprites/ai/casual/Ai angry5.png"
image ai casual sad1 = "images/sprites/ai/casual/Ai sad1.png"
image ai casual sad2 = "images/sprites/ai/casual/Ai sad1.png"
image ai casual sad3 = "images/sprites/ai/casual/Ai sad1.png"
image ai casual sad4 = "images/sprites/ai/casual/Ai sad1.png"
image ai casual sad5 = "images/sprites/ai/casual/Ai sad1.png"
image ai casual agh1 = "images/sprites/ai/casual/Ai agh1.png"
image ai casual agh2 = "images/sprites/ai/casual/Ai agh2.png"
image ai casual agh3 = "images/sprites/ai/casual/Ai agh3.png"
image ai casual agh4 = "images/sprites/ai/casual/Ai agh4.png"
image ai casual agh5 = "images/sprites/ai/casual/Ai agh5.png"
image ai casual surprise1 = "images/sprites/ai/casual/Ai surprise1.png"

# Shiori
image shiori idle = "images/sprites/shiori/Shiori idle.png"
image shiori normal1 = "images/sprites/shiori/Shiori normal1.png"
image shiori normal2 = "images/sprites/shiori/Shiori normal2.png"
image shiori normal3 = "images/sprites/shiori/Shiori normal3.png"
image shiori normal4 = "images/sprites/shiori/Shiori normal4.png"
image shiori reflexive1 = "images/sprites/shiori/Shiori reflexive?1.png"
image shiori sad1 = "images/sprites/shiori/Shiori sad1.png"
image shiori sad2 = "images/sprites/shiori/Shiori sad2.png"
image shiori sad3 = "images/sprites/shiori/Shiori sad3.png"
image shiori sad4 = "images/sprites/shiori/Shiori sad4.png"
image shiori sad5 = "images/sprites/shiori/Shiori sad5.png"
image shiori angry1 = "images/sprites/shiori/Shiori angry1.png"
image shiori hmm1 = "images/sprites/shiori/Shiori hmm1.png"
image shiori hmm2 = "images/sprites/shiori/Shiori hmm2.png"
image shiori hmm3 = "images/sprites/shiori/Shiori hmm3.png"
image shiori hmm4 = "images/sprites/shiori/Shiori hmm4.png"
image shiori hmm5 = "images/sprites/shiori/Shiori hmm5.png"
image shiori hmm0 = "images/sprites/shiori/Shiori hmm?.png"

# Yu
image yu idle = "images/sprites/yu/Yu idle.png"
image yu normal1 = "images/sprites/yu/Yu normal1.png"
image yu normal2 = "images/sprites/yu/Yu normal2.png"
image yu normal3 = "images/sprites/yu/Yu normal3.png"
image yu normal4 = "images/sprites/yu/Yu normal4.png"
image yu sad1 = "images/sprites/yu/Yu sad1.png"
image yu sad2 = "images/sprites/yu/Yu sad2.png"
image yu sad3 = "images/sprites/yu/Yu sad3.png"
image yu sad4 = "images/sprites/yu/Yu sad4.png"
image yu sad5 = "images/sprites/yu/Yu sad5.png"
image yu hmm1 = "images/sprites/yu/Yu hmm1.png"
image yu hmm2 = "images/sprites/yu/Yu hmm2.png"
image yu hmm3 = "images/sprites/yu/Yu hmm3.png"
image yu hmm4 = "images/sprites/yu/Yu hmm4.png"
image yu hmm5 = "images/sprites/yu/Yu hmm5.png"
image yu hmm6 = "images/sprites/yu/Yu hmm6.png"
image yu hmm7 = "images/sprites/yu/Yu hmm7.png"
image yu happy1 = "images/sprites/yu/Yu happy1.png"
image yu happy2 = "images/sprites/yu/Yu happy1.png"
image yu happy3 = "images/sprites/yu/Yu happy1.png"
image yu happy4 = "images/sprites/yu/Yu happy1.png"

### Fondos

image bg ai_room = "images/bg/ai-room.png"
image bg ai_livingroom = "images/bg/ai-livingroom.png"
image bg store = "images/bg/store.png"
image bg departament = "images/bg/departament.png"
image bg ai_house = "images/bg/ai-house.png"
image bg convenience_store = "images/bg/convenience-store.png"
image bg crossing_city = "images/bg/crossing_city.png"
image bg city_station = "images/bg/city_station.png"

### Objetos
image caja = "images/objects/caja.png"
image azucar = "images/objects/azucar.png"
image harina1 = "images/objects/harina_1.png"
image harina2 = "images/objects/harina_2.png"
image semaforo_apagado = "images/objects/semaforo_apagado.png"
image semaforo_encendido_1 = "images/objects/semaforo_encendido_1.png"
image semaforo_encendido_2 = "images/objects/semaforo_encendido_2.png"
image semaforo_encendido_3 = "images/objects/semaforo_encendido_3.png"

image semaforo:
    "semaforo_apagado"
    pause 0.6
    "semaforo_encendido_1"
    pause 6.0
    "semaforo_apagado"
    pause 0.6
    "semaforo_encendido_2"
    pause 6.0
    "semaforo_apagado"
    pause 0.6
    "semaforo_encendido_3"
    pause 6.0
    "semaforo_apagado"
    repeat