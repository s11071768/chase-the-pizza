controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setPosition(0, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    info.changeScoreBy(2)
    meem.setPosition(randint(10, 100), randint(10, 100))
    info.startCountdown(2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    pizza.setPosition(randint(10, 100), randint(10, 100))
    info.startCountdown(5)
})
let meem: Sprite = null
let pizza: Sprite = null
let mySprite: Sprite = null
scene.setBackgroundColor(1)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
pizza = sprites.create(img`
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
    `, SpriteKind.Food)
meem = sprites.create(img`
    . . 6 6 6 6 . . 
    . 6 d 4 4 4 b . 
    . c b 1 1 4 4 b 
    . c b b 4 4 d b 
    . . c b b d 1 c 
    . . . c c b b . 
    `, SpriteKind.Projectile)
