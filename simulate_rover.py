import argparse
import turtle as t 
import random
import math

argp = argparse.ArgumentParser(description='rover movement calculation')
argp.add_argument('filepath',type=str,help='path to the instruction file')
argp.add_argument('--graphical',action='store_true',help='graphical representation')
args = argp.parse_args()

rover = {
    'x': 0,
    'y': 0,
    'orientation': 0
}

def isValid(instruction):
    
    if instruction['action']== 'move' and instruction['unit'] == 'degrees':
        return False
    elif instruction['action'] == 'turn' and instruction['unit'] == 'meters':
        return False
    return True

def generateInstruction(file):
    instructions = []
    lines = file.readlines()
    valid_lines = [line.strip().lower() for line in lines if line.strip()]
    for i, line in enumerate(valid_lines):
        props = line.split()
        valid = len(props) == 4 and props[2] in ['meters', 'degrees'] and props[3] in ['forward', 'backward', 'clockwise', 'counterclockwise']
        if len(props) <=3 or len(props)>4 :
            instructions.append({
            'valid': False,
            'num': i + 1,    
        })
        else:
            instructions.append({
                'valid': valid,
                'num': i + 1,
                'action': props[0],
                'value': float(props[1]),
                'unit': props[2],
                'direction': props[3]
            })
    return instructions

def isValid(instruction):
    # print(instruction['action'])
    if instruction['action'] == 'move' and instruction['unit'] == 'degrees':
        return False
    elif instruction['action'] == 'turn' and instruction['unit'] == 'meters':
        return False
    return True

def setOrientation():
     if rover['orientation'] < 270 and rover['orientation'] > 180 :
            rover['orientation'] = rover['orientation']-180
     if rover['orientation'] < 180 and rover['orientation'] > 90 :
            rover['orientation'] = 180 - rover['orientation']
     if rover['orientation'] < 270 and rover['orientation'] > 180 :
            rover['orientation'] = rover['orientation']-180
     if rover['orientation'] > 270:
            rover['orientation'] = 360 - rover['orientation']

def executeInstructions(instructions):
    for i in instructions:
            if args.graphical:
                for obstacle  in obstacles:
                    if checkCollision(mainturtle,obstacle,i['num']):
                        return
            
            print(f"I'm at ({rover['x']},{rover['y']}) facing {rover['orientation']} degrees")
            # if not isValid(i): 
            #     print(f"I've encountered an instruction I don't understand, aborting (instruction :{i['num']} )") 
            #     return 
            if not i['valid']:
                    print(f"I've encountered an instruction I don't understand, aborting (instruction :{i['num']} )") 
                    return      
            if i['action'] == 'turn':
                print(f"Turning  {i['value']} {i['unit']} {i['direction']} (instruction {i['num']})")
            
                if i['direction'] == 'clockwise' :
                    rover['orientation'] = (  i['value'])%360 
                    mainturtle.right(rover['orientation']) if args.graphical else "" 
                else: 
                    rover['orientation'] =  (rover['orientation'] - i['value'])%360 
                    mainturtle.right(rover['orientation']) if args.graphical else ""

            if i['action'] == 'move':
                print(f"Moving   {i['value']}  {i['unit']}  {i['direction']} (instruction {i['num']})")
                setOrientation()
                angle = rover['orientation']
                radian = math.radians(angle)
                if i['direction'] == 'forward':
                    rover['x'] = rover['x'] +  round(math.sin(radian)*i['value'])
                    rover['y'] = rover['y'] + round(math.cos(radian)*i['value'])
                    
                    mainturtle.forward(i['value']*10) if args.graphical else ""
                if i['direction'] == 'backward':
                    rover['x'] = rover['x'] -  round(math.sin(radian)*i['value'])
                    rover['y'] = rover['y'] - round(math.cos(radian)*i['value'])
                    
                    mainturtle.backward(i['value']*10) if  args.graphical else " "
            if args.graphical:
                for obstacle  in obstacles:
                    if checkCollision(mainturtle,obstacle,i['num']):
                        return
                 

def checkCollision(mainturtle,obstacle:t,num):
     expression = (((mainturtle.xcor() - obstacle.xcor())**2) + ((mainturtle.ycor() - obstacle.ycor())**2))
     distance =math.sqrt(expression)
     if distance < 25 :
          obstacle.fillcolor('red')
          obstacle.shape('triangle')
          return True
     else : 
          return False

  
def generateObstacles():
     x = random.randint(-300,300)
     y = random.randint(-300,300)
     return (x,y)

if args.graphical:
     t.mode('logo')
     t.delay(10)
     mainturtle = t.Turtle()
     mainturtle.fillcolor('blue')
     obstacles =[]
     screen = t.Screen()
     t.Screen()
     mainturtle.shape('turtle')
     mainturtle.pendown()
     num_of_obstacles = random.randint(5,25)
     for i in range(num_of_obstacles):
          myturtle = t.Turtle()
          myturtle.penup()
          myturtle.shape('circle')
          myturtle.setpos(generateObstacles())
          obstacle = myturtle
          obstacles.append(obstacle)
    
with open(args.filepath) as file:
    instructions = generateInstruction(file)   
    executeInstructions(instructions)

if args.graphical :
     t.done()



   

	
