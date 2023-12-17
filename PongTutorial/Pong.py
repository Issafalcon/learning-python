import turtle

ball_dx = 0.02
ball_dy = 0.02

win = turtle.Screen()
win.title("Pong by Issafalcon")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Speed of animation, not paddle
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Default is 20x20
paddle_a.penup()
paddle_a.goto(-340, 0)  # Starting position

win.onkeypress(lambda: paddle_up(paddle_a), "w")
win.onkeypress(lambda: paddle_down(paddle_a), "s")

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Speed of animation, not paddle
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Default is 20x20
paddle_b.penup()
paddle_b.goto(340, 0)  # Starting position

win.onkeypress(lambda: paddle_up(paddle_b), "Up")
win.onkeypress(lambda: paddle_down(paddle_b), "Down")

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Speed of animation, not paddle
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # Starting position

# Border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-400, 300)
border.pendown()
border.goto(-400, -300)
border.goto(400, -300)
border.goto(400, 300)
border.goto(-400, 300)
border.hideturtle()


def paddle_up(paddle: turtle.Turtle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def paddle_down(paddle: turtle.Turtle):
    y = paddle.ycor()
    y += -20
    paddle.sety(y)


def calculate_paddle_collision(paddle: turtle.Turtle, ball_dx):
    paddle_top = paddle.ycor() + 40
    paddle_bottom = paddle.ycor() - 40
    paddle_left = paddle.xcor() - 5
    paddle_right = paddle.xcor() + 5

    if (paddle_left < ball.xcor() < paddle_right) and (
        paddle_bottom < ball.ycor() < paddle_top
    ):
        return True

    return False


win.listen()

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1

    if calculate_paddle_collision(paddle_a, ball_dx):
        ball_dx *= -1

    if calculate_paddle_collision(paddle_b, ball_dx):
        ball_dx *= -1
