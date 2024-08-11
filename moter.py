import pyfirmata
 
comport = 'COM3'
board = pyfirmata.Arduino(comport)

# Define motor control pins
motor_direction_1 = board.get_pin('d:8:o')  # Digital pin for motor direction 1
motor_direction_2 = board.get_pin('d:9:o')  # Digital pin for motor direction 2
motor_speed = board.get_pin('d:10:p')       # PWM pin for motor speed

def led(fingerUp):
    if fingerUp == [0, 0, 0, 0, 0]:
        motor_direction_1.write(0)
        motor_direction_2.write(0)
        motor_speed.write(0)  # Motor off

    elif fingerUp == [1, 0, 0, 0, 0]:
        motor_direction_1.write(1)
        motor_direction_2.write(0)
        motor_speed.write(0.2)  # Motor on at low speed

    elif fingerUp == [0, 1, 0, 0, 0]:
        motor_direction_1.write(1)
        motor_direction_2.write(0)
        motor_speed.write(0.5)  # Motor on at medium speed

    elif fingerUp == [0, 0, 1, 0, 0]:
        motor_direction_1.write(1)
        motor_direction_2.write(0)
        motor_speed.write(1)  # Motor on at high speed

    elif fingerUp == [1, 1, 1, 1, 1]:
        motor_direction_1.write(0)
        motor_direction_2.write(1)
        motor_speed.write(0.5)  # Motor on in reverse at medium speed

# Example usage
fingerUp = [1, 0, 0, 0, 0]
led(fingerUp)
