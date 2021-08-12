@namespace
class SpriteKind:
    Button = SpriteKind.create()
def redPress():
    red.set_image(assets.image("""
        redButtonPush
    """))
    red.start_effect(effects.fountain, 500)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    pause(500)
    red.set_image(assets.image("""
        redButton
    """))
    pause(500)

def on_up_pressed():
    global currentGuess, userTurn
    if userTurn:
        if lights[currentGuess] == 0:
            redPress()
            currentGuess += 1
        else:
            wrongGuess()
    if currentGuess == len(lights):
        currentGuess = 0
        userTurn = False
        addLight()
        lightUp()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def bluePress():
    blue.set_image(assets.image("""
        blueButtonPush
    """))
    blue.start_effect(effects.fountain, 500)
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    pause(500)
    blue.set_image(assets.image("""
        blueButton
    """))
    pause(500)
def setButton():
    global red, green, blue, yellow
    red = sprites.create(assets.image("""
        redButton
    """), SpriteKind.player)
    red.set_position(80, 40)
    green = sprites.create(assets.image("""
        greenButton
    """), SpriteKind.player)
    green.set_position(80, 80)
    blue = sprites.create(assets.image("""
        blueButton
    """), SpriteKind.player)
    blue.set_position(60, 60)
    yellow = sprites.create(assets.image("""
        yellowButton
    """), SpriteKind.player)
    yellow.set_position(100, 60)

def on_left_pressed():
    global currentGuess, userTurn
    if userTurn:
        if lights[currentGuess] == 0:
            bluePress()
            currentGuess += 1
        else:
            wrongGuess()
    if currentGuess == len(lights):
        currentGuess = 0
        userTurn = False
        addLight()
        lightUp()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def lightUp():
    global userTurn, currentGuess
    for value in lights:
        if value == 0:
            redPress()
        elif value == 1:
            greenPress()
        elif value == 2:
            bluePress()
        else:
            yellowPress()
    userTurn = True
    currentGuess = 0
def yellowPress():
    yellow.set_image(assets.image("""
        yellowButtonPush
    """))
    yellow.start_effect(effects.fountain, 500)
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    pause(500)
    yellow.set_image(assets.image("""
        yellowButton
    """))
    pause(500)
def addLight():
    global randLight
    randLight = randint(0, 3)
    lights.append(randLight)

def on_right_pressed():
    global currentGuess, userTurn
    if userTurn:
        if lights[currentGuess] == 0:
            yellowPress()
            currentGuess += 1
        else:
            wrongGuess()
    if currentGuess == len(lights):
        currentGuess = 0
        userTurn = False
        addLight()
        lightUp()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def wrongGuess():
    game.over(False, effects.melt)

def on_down_pressed():
    global currentGuess, userTurn
    if userTurn:
        if lights[currentGuess] == 0:
            greenPress()
            currentGuess += 1
        else:
            wrongGuess()
    if currentGuess == len(lights):
        currentGuess = 0
        userTurn = False
        addLight()
        lightUp()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def greenPress():
    green.set_image(assets.image("""
        greenButtonPush
    """))
    green.start_effect(effects.fountain, 500)
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    pause(500)
    green.set_image(assets.image("""
        greenButton
    """))
    pause(500)
randLight = 0
yellow: Sprite = None
green: Sprite = None
blue: Sprite = None
currentGuess = 0
red: Sprite = None
userTurn = False
lights: List[number] = []
scene.set_background_color(1)
setButton()
lights = []
userTurn = False
addLight()
lightUp()