#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from functions.linefollower import LineFollower
from test_sensory import TestSensory

# Create your objects here.
ev3 = EV3Brick()

color_sensor = ColorSensor(Port.S3) # LineFollower only
gyro_sensor = GyroSensor(Port.S2)
#touch_sensor = TouchSensor(Port.S1) # StairClimber only

right_motor = Motor(Port.A) 
left_motor = Motor(Port.D)
Drive = DriveBase(right_motor, left_motor, wheel_diameter=56, axle_track=152)

# Needed for StairClimber else comment out
#lift_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#rear_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Configure Display
big_font = Font(size=24)
ev3.screen.set_font(big_font)

# Configure Speaker
ev3.speaker.set_speech_options(language='de',voice='m3',speed=None,pitch=50)

# Battery Info
print(ev3.battery.voltage(), "mV")
print(ev3.battery.current(), "mA")

ev3.speaker.beep()
#ev3.speaker.say('Edenmobil am Start')

#Line = LineFollower(Drive, color_sensor, ev3)
#Line.follow()
#climb = StairClimber(ev3, Drive, touch_sensor, lift_motor, rear_motor)
#steps = 10
#climb.climb(steps)

Test = TestSensory(color_sensor, gyro_sensor, ev3)
while True:
    Test.color()
    Test.angle()
    Test.show()
    wait(0.5)
