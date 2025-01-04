from ButtonClass import Button


width, height = 1500, 1000
scene = 'mainMenu'

def actionScene(lvl):  # функция, меняющая переменную сцены
    global scene
    scene = lvl

button1 = Button(width / 2 - 600, height / 2 - 300, "images/UI/lvl/lvl1.png", 300, 300, actionScene)
button2 = Button(width / 2 - 200, height / 2 - 300, "images/UI/lvl/lvl2.png", 300, 300, actionScene)
button3 = Button(width / 2 + 200, height / 2 - 300, "images/UI/lvl/lvl3.png", 300, 300, actionScene)
button4 = Button(width / 2 - 600, height / 2 + 100, "images/UI/lvl/lvl4.png", 300, 300, actionScene)
button5 = Button(width / 2 - 200, height / 2 + 100, "images/UI/lvl/lvl5.png", 300, 300, actionScene)
button6 = Button(width / 2 + 200, height / 2 + 100, "images/UI/lvl/lvl6.png", 300, 300, actionScene)
def draw_buttons(screen):
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    button5.draw(screen)
    button6.draw(screen)

def handle_event(event):
    isStarted = button1.is_pressed(event)
    if button1.is_pressed(event):
        button1.handle_event_parameter('lvl1')
    if button2.is_pressed(event):
        button2.handle_event_parameter('lvl2')
    if button3.is_pressed(event):
        button3.handle_event_parameter('lvl3')
    if button4.is_pressed(event):
        button4.handle_event_parameter('lvl4')
    if button5.is_pressed(event):
        button5.handle_event_parameter('lvl5')
    if button6.is_pressed(event):
        button6.handle_event_parameter('lvl6')
    return isStarted