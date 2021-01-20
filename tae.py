from turtle import *
import random
import playsound
def make_ball(size):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = random.choice(["red", "green", "blue", "yellow", "pink", "purple"])
    while True:
        dx = random.randint(-1, 1)  # 이동벡터
        dy = random.randint(-1, 1)  # 이동벡터
        if dx != 0 or dy != 0:
            break
    return [x, y, size, color, dx, dy]
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5


def key_left():
    if stage == 0:
        my.seth(180)  # turtle.seth(to_angle) 거북이 각도 설정
        my.fd(onestep)  # fd: 향한 방향으로 onestep 만큼 이동
        if(my.xcor()< -300): # xcor()  x 좌표 반환 
            my.setx( -300) # 맵 탈출 제어

#오른쪽 이동
def key_right():
    if stage == 0:
        my.seth(0) 
        my.fd(onestep)
        if(my.xcor() > 300):
            my.setx(300)    

#위쪽 이동
def key_up():
    global stage
    my.seth(90)
    my.fd(onestep)
    if(my.ycor()>300):
        my.sety(300)
    if stage == 2:
        title.reset()
        title.ht()
        my.setpos(0,-200)
        my.seth(90)
        title.up()
        title.setpos(-20,-300)
        title.down()
        title.setpos(-20,80)
        title.up()
        title.setpos(20,-300)
        title.down()
        title.setpos(20,80)
        title.up()
        title.setpos( -250,180)
        title.write("[ 1 ]", font = ("맑은고딕", 18, "bold"))
        title.up()
        title.setpos( -25,250)
        title.write("[ 2 ]", font = ("맑은고딕", 18, "bold"))
        title.up()
        title.setpos( 210,180)
        title.write("[ 3 ]", font = ("맑은고딕", 18, "bold"))
        stage = 1    

#아래쪽 이동
def key_down():
    my.seth(270)
    my.fd(onestep)
    if(my.ycor()< -290):
        my.sety( -290)
def draw(ballpen, ball_list):
    global stage
    alive = True
    tracer(0)
    while (alive):
        listen()
        
        if stage == 0:
            if my.xcor() > -130 and my.xcor()< 110 and my.ycor() > -90 and my.ycor() <0:
                title.reset()
                title.ht()
                my.setpos(0,-200)
                my.seth(90)
                title.up()
                title.setpos(-20,-300)
                title.down()
                title.setpos(-20,80)
                title.up()
                title.setpos(20,-300)
                title.down()
                title.setpos(20,80)
                title.up()
                title.setpos( -250,180)
                title.write("[ 1 ]", font = ("맑은고딕", 18, "bold"))
                title.up()
                title.setpos( -25,250)
                title.write("[ 2 ]", font = ("맑은고딕", 18, "bold"))
                title.up()
                title.setpos( 210,180)
                title.write("[ 3 ]", font = ("맑은고딕", 18, "bold"))
                
                stage = 1
        elif stage == 1:
            if my.ycor() > 170 :
                ballpen.clear()
                i = random.randint(1,4)
                if i==1:
                    my.setpos(-250,180)
                elif i ==2 :
                    my.setpos(-25,250)
                else:
                    my.setpos(210,180)
                stage = 2
            tracer(180-my.ycor())
             #공 그리기 ( 1 프레임 마다 지우고 다시그리기 )
            ballpen.clear()
            for i in range( len( ball_list )):
                
                x, y, size, color, dx, dy = ball_list[ i ] 
                
                #공 이동
                x += dx
                y += dy


                #check 2 : 공이 맵을 나가려고 하는가
                if (x<-300) or (x > 300): dx *= -1
                if (y<-300) or (y > 300): dy *= -1

                #check 3 : 공끼리 부딪혔는가
                for j in range( len( ball_list ) ) :

                    if not i==j :
                        target_x = ball_list[j][0]
                        target_y = ball_list[j][1]

                        if(distance(x, y, target_x, target_y)<=20):
                            #공 방향 바꾸기
                            dx *= -1
                            dy *= -1
                            ball_list[j][4] = ball_list[j][4] * -1
                            ball_list[j][5] = ball_list[j][5] * -1

                            # 공 떨어뜨리기
                            x += dx *2
                            y += dy *2
                    
                ball_list[i] = [x, y, size, color, dx, dy]
                ballpen.setpos(x, y)
                ballpen.dot(size, color)
                
        elif stage == 2:
            ballpen.clear()
        update()

def main():
    
    playsound.playsound("start.mp3",block=False)
    
    global stage
    stage =0
    global onestep
    onestep = 20

    setup(600, 600) #600 * 600 
    
    global my
    my = Turtle()
    my.shape("turtle")
    my.up() # up : 펜을 올려서 그림을 그리지 않음. up 이 없으면 그림그림
    my.setpos(-250,250)

    onkey(key_right, "Right")
    onkey(key_left, "Left")
    onkey(key_up, "Up")
    onkey(key_down, "Down")


    global title
    title = Turtle()
    title.up()
    title.setpos(-150,200)
    title.down()
    title.write("김태우 생일 외", font = ("맑은고딕", 18, "bold"))
    title.up()
    title.setpos(-150,170)
    title.down()
    title.write("지나가버린 모두의 생일", font = ("맑은고딕", 18, "bold"))
    title.up()
    title.setpos(-150,140)
    title.down()
    title.write("다가오는 나의 생일 기념", font = ("맑은고딕", 18, "bold"))
    title.up()
    title.setpos(-150,110)
    title.down()
    title.write("이벤트", font = ("맑은고딕", 18, "bold"))

    title.up()
    title.setpos(-100,-80)
    title.down()
    title.write("시작하기", font = ("맑은고딕", 33, "bold"))
    title.up()
    title.setpos( -130,-90 )
    title.down()
    title.setpos( -130,0 )
    title.setpos( 110,0 )
    title.setpos( 110,-90 )
    title.setpos( -130,-90 )
    title.ht()
     #공 그릴 펜
    ballpen = Turtle()
    ballpen.up()
    ballpen.ht()
    #공 담을 리스트
    ball_list = [ ]
    ball_size = 10
    #공 생성 정보를 받아와 리스트에 추가
    for i in range(20):
        ball = make_ball(ball_size)
        ball_list.append(ball)
        
    draw( ballpen, ball_list)



if __name__ == "__main__":
    main()
