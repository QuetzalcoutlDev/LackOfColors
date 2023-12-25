
init -1 python:

    _dismiss_pause = config.developer
    config.keymap["game_menu"].remove("mouseup_3")
    config.keymap["hide_windows"].append("mouseup_3")

    config.has_autosave = False
    config.has_quicksave = False

define config.gl2 = False
default persistent.chapter = 0
default persistent.FirstInit = True
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

# Música
define audio.m1 = "audio/Faded_mornings.ogg"
define audio.m2 = "audio/In_my_mind.ogg"
define audio.m3 = "audio/Hikara.ogg"
define audio.terrorGround = "audio/terror_ground.ogg"

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
image bg ai_departament = "images/bg/ai-apartament.png"
image bg convenience_store = "images/bg/convenience-store.png"

### Objetos
image caja = "images/objects/caja.png"
image azucar = "images/objects/azucar.png"
image harina1 = "images/objects/harina_1.png"
image harina2 = "images/objects/harina_2.png"


