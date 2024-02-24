"""grip controller."""


from controller import Robot, LightSensor

import time


TIME_STEP = 64

MAX_SPEED = 6.28

robot = Robot()
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)




CAMERA_NAME = "camera1"
camera = robot.getDevice(CAMERA_NAME)
camera.enable(TIME_STEP)
    

ir_sensor2 = robot.getDevice('ir_sensor2')
ir_sensor2.enable(TIME_STEP)




color_sensor = robot.getDevice('colords')
color_sensor.enable(TIME_STEP)

ds_sensor = robot.getDevice('ds')
ds_sensor.enable(TIME_STEP)


ds1_sensor = robot.getDevice('ds1')
ds1_sensor.enable(TIME_STEP)

light_sensor = robot.getDevice("light_sensor")

light_sensor.enable(TIME_STEP)

ir_sensor = robot.getDevice('ir_sensor')
ir_sensor.enable(TIME_STEP)

ir_sensor_right = robot.getDevice('ir_sensor_right')
ir_sensor_right.enable(TIME_STEP)

ir_sensor_left = robot.getDevice('ir_sensor_left')
ir_sensor_left.enable(TIME_STEP)

ps = [robot.getDevice(f'ps{i}') for i in range(8)]
for sensor in ps:
    sensor.enable(TIME_STEP)
    
    
      
gs = []
gsNames = ['gs0', 'gs1', 'gs2']
for i in range(3):
    gs.append(robot.getDevice(gsNames[i]))
    gs[i].enable(TIME_STEP)
    
    
    
    
ls=[]
for i in range(8):
    ls.append(robot.getDevice('ls'+str(i)))
    ls[-1].enable(TIME_STEP)
   
   
   

kp =   0.04# 0.00000001
ki =  0.0001
kd =      0.0005

kp_line =   0.0006# 0.00000001
ki_line =  0.00001
kd_line =      0.001

target_distance = 80  # Adjust the target distance as needed
target_line = 900
integral = 0
integral_line = 0

last_error = 0
last_line_error =0



def limit_speed(speed):
    if speed > MAX_SPEED:
        return MAX_SPEED
    elif speed < -MAX_SPEED:
        return -MAX_SPEED
    return speed


       
rotation_duration = 2
rotation_start_time = None

is_rotating = False


      

while robot.step(TIME_STEP) != -1 :
    gs2=gs[0].getValue()
    gs0=gs[2].getValue()
    gs1 = gs[1].getValue()
    left2 = ps[5].getValue()
    left1 = ps[6].getValue() 
    front_wall = ps[0].getValue() 
    front_wall2 = ps[7].getValue() 
    right1 = ps[1].getValue() 
    ds =ds_sensor.getValue()
    image = camera.getImage()
    light= light_sensor.getValue()
    ds1 = ds1_sensor.getValue()



    ir_front_right = ir_sensor.getValue()
    ir_front_left = ir_sensor2.getValue()
    
    ir_left = ir_sensor_left.getValue()
    ir_right = ir_sensor_right.getValue()
    right2 = ps[2].getValue() 
    ds = ds_sensor.getValue()
    error = target_distance - ir_right 
    error_line = target_line - (gs0+gs1+gs2)
    integral += error
    integral_line +=error_line
    derivative = error - last_error
    derivative_line=error_line - last_line_error
    PID = kp_line * error_line + ki_line * integral_line + kd_line * derivative_line
    correction = kp * error + ki * integral + kd * derivative
    left_speed = limit_speed( 0.5*MAX_SPEED + correction)
    right_speed = limit_speed( 0.5*MAX_SPEED - correction)
    leftSpeed_line = limit_speed(0.5*MAX_SPEED  + PID)
    rightSpeed_line = limit_speed(0.5*MAX_SPEED  - PID)
    left2 = ps[5].getValue()
    left1 = ps[6].getValue() 
    front_wall = ps[0].getValue() 
    front_wall2 = ps[7].getValue() 
    right1 = ps[1].getValue() 

    ir_front_right = ir_sensor.getValue()
    ir_front_left = ir_sensor2.getValue()
    
    ir_left = ir_sensor_left.getValue()
    ir_right = ir_sensor_right.getValue()
    
    print("ir_front_right:", ir_front_right)
    print("ir_front_left:", ir_front_left)
    print("ir_left",ir_left )
    print("ir_right",ir_right )
    print("front_wall:", ps[0].getValue())
    print("front_wall2:", ps[7].getValue())
    print("right1",ps[1].getValue() )
    print("right2",ps[2].getValue()  )
    print("left1",ps[6].getValue() )
    print("left2",ps[5].getValue() )
    print("gs0",gs[0].getValue() )
    print("ds",ds)
    print("gs1",gs[1].getValue() )
    
    print("gs2",gs[2].getValue() )
    print("ds", ds)
    print("ds1", ds1)
        # Check if there is an obstacle on the right
    ir_fr_bool = ir_sensor.getValue() >80
    ir_fl_bool = ir_sensor2.getValue() > 80
    right1_bool = ps[1].getValue() > 80
    right2_bool = ps[2].getValue()> 80 
    ir_lbool = ir_sensor_left.getValue()>80
    ir_rbool = ir_sensor_right.getValue()>80
    left2_bool = ps[5].getValue()>80
    left1_bool = ps[6].getValue() >80
    front_wall_bool = ps[7].getValue() >80
    front_wall_bool2= ps[0].getValue() >80
    
    if gs[1].getValue() < 600  or gs[0].getValue() < 600  or gs[2].getValue() < 600 :
            print("PIDLINE")
            left_speed = leftSpeed_line
            right_speed = rightSpeed_line
        # Additional condition to check if ir_front_right and ir_front_left are decreasing


    elif (ir_fl_bool or ir_fr_bool):
        print("If")
        if ds > 80 and ds1 >80:
            print("block")
            if not is_rotating:
                # Initiate rotation only if not already rotating
                rotation_start_time = time.time()
                is_rotating = True
                print("Rotation initiated")


            elapsed_time = time.time() - rotation_start_time
            print("Elapsed time:", elapsed_time)

            if elapsed_time < rotation_duration:
                # Continue rotating until the rotation is complete
                left_speed = -MAX_SPEED
                right_speed = MAX_SPEED
                print("Continuing rotation")
            else:
                # Stop the robot after the rotation duration
                left_speed = 0
                right_speed = 0
                rotation_start_time = None
                is_rotating = False
                print("Rotation complete. Stopping.")     
                
        elif ds >80  or ir_fr_bool  :
            print("turn left")
            left_speed = -left_speed
            right_speed =right_speed
        elif ds1 >80 :
            print("turn right")
            left_speed = left_speed
            right_speed =-right_speed
       
    elif front_wall_bool or front_wall_bool2:
        if right1_bool or  right2_bool  :
            print("turn left elif")
            left_speed = -left_speed
            right_speed =right_speed
        if left1_bool or  left2_bool  :
            print("turn right elif")
            left_speed = left_speed
            right_speed =-right_speed

    
    

    
    
    elif gs[1].getValue()> 859 and gs[1].getValue()<860:

        leftMotor.setVelocity(0)
        rightMotor.setVelocity(0)
        break
  
    else:
        if is_rotating:
            elapsed_time = time.time() - rotation_start_time
            if elapsed_time < rotation_duration:
                # Continue rotating until the rotation is complete
                left_speed = -MAX_SPEED
                right_speed = MAX_SPEED
                print("else iff")
            else:
                # Stop the robot after the rotation duration
                left_speed = 0
                right_speed = 0
                rotation_start_time = None
                is_rotating = False 
                print("else not iff")
            
        else:
            left_speed = left_speed
            right_speed = right_speed
            print("else  ")
        
    leftMotor.setVelocity(left_speed)
    rightMotor.setVelocity(right_speed)
    last_error = error
    last_line_error = error_line
    pass

# Enter here exit cleanup code.
