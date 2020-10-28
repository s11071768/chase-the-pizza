def on_a_pressed():
    mySprite.set_position(0, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(-1)
    meem.set_position(randint(10, 150), randint(10, 150))
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    info.change_score_by(1)
    pizza.set_position(randint(10, 100), randint(10, 100))
    info.start_countdown(5)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

meem: Sprite = None
pizza: Sprite = None
mySprite: Sprite = None
scene.set_background_color(1)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 7 7 7 7 7 6 . . . . . 
            . . . . . 7 f 7 f 7 6 . . . . . 
            . . . . . 7 7 f 7 7 6 . . . . . 
            . . . . . 7 f f f 7 6 . . . . . 
            . . . . . 7 f 7 f 7 6 . . . . . 
            . . . . . 7 7 7 7 7 6 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
pizza = sprites.create(img("""
        . . . . . . b b b b . . . . . . 
            . . . . . . b 4 4 4 b . . . . . 
            . . . . . . b b 4 4 4 b . . . . 
            . . . . . b 4 b b b 4 4 b . . . 
            . . . . b d 5 5 5 4 b 4 4 b . . 
            . . . . b 3 2 3 5 5 4 e 4 4 b . 
            . . . b d 2 2 2 5 7 5 4 e 4 4 e 
            . . . b 5 3 2 3 5 5 5 5 e e e e 
            . . b d 7 5 5 5 3 2 3 5 5 e e e 
            . . b 5 5 5 5 5 2 2 2 5 5 d e e 
            . b 3 2 3 5 7 5 3 2 3 5 d d e 4 
            . b 2 2 2 5 5 5 5 5 5 d d e 4 . 
            b d 3 2 d 5 5 5 d d d 4 4 . . . 
            b 5 5 5 5 d d 4 4 4 4 . . . . . 
            4 d d d 4 4 4 . . . . . . . . . 
            4 4 4 4 . . . . . . . . . . . .
    """),
    SpriteKind.food)
meem = sprites.create(img("""
        . . 6 6 6 6 . . 
            . 6 d 4 4 4 b . 
            . c b 1 1 4 4 b 
            . c b b 4 4 d b 
            . . c b b d 1 c 
            . . . c c b b .
    """),
    SpriteKind.projectile)