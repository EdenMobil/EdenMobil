class TestSensory:
    def __init__(self, color_sensor, gyro_sensor, ev3):
        self.color_sensor = color_sensor
        self.gyro_sensor = gyro_sensor
        self.ev3 = ev3
        self.text = ["", "", ""]  # Placeholder for Color, Angle, and Speed

    def color(self):
        color_value = self.color_sensor.color()
        self.text[0] = str(color_value)

    def angle(self):
        angle_value = self.gyro_sensor.angle()
        self.text[1] = "Angle: " + str(angle_value) + "°"

    def speed(self):
        speed_value = self.gyro_sensor.speed()
        self.text[2] = "Speed: " + str(speed_value) + " deg/s"

    def show(self):
        self.ev3.screen.clear()  # Clear the screen
        for line in self.text:
            if line:  # Only print lines that are not empty
                self.ev3.screen.print(line)
                self.ev3.screen.print("---")
