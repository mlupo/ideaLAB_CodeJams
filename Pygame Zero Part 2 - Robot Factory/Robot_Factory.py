import random

player = Actor('alien')
robot_list = []

WIDTH = 768
HEIGHT = 768

colour = (90,10,200)

def draw():
    screen.clear()
    screen.fill(colour)
    for actor in robot_list:
        actor.draw()
    player.draw()

def update():
    for actor in robot_list.copy():
        actor.left += 3
        if actor.left > WIDTH:
            robot_list.remove(actor)

def on_mouse_move(pos):
    player.center = pos

def make_robot():
    y_start = random.randint(0,6)
    robot = Actor("robot_idle")
    robot.topright = 0, y_start * 128
    robot_list.append(robot)

clock.schedule_interval(make_robot, 0.5)

def set_robot_hurt(robo):
    robo.image = 'alien_hurt'
    sounds.eep.play()
    print('ouch')

def on_mouse_down(pos):
    for actor in robot_list:
        if actor.collidepoint(pos):
            set_robot_hurt(actor)
        else:
            print("you missed!")