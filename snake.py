from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.x_pos = 0
        self.snake_blocks = []
        self.create_snake()
        self.snake_head = self.snake_blocks[0]

    def create_snake(self):

        for block in STARTING_POSITIONS:
            self.add_block(block)

    def add_block(self, block):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(block)
        self.x_pos -= 20
        self.snake_blocks.append(new_block)

    def reset(self):
        for block in self.snake_blocks:
            block.hideturtle()
        self.snake_blocks.clear()
        self.create_snake()
        self.snake_head = self.snake_blocks[0]

    def grow(self):
        self.add_block(self.snake_blocks[-1].position())

    def move(self):
        for block_num in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[block_num - 1].xcor()
            new_y = self.snake_blocks[block_num - 1].ycor()
            self.snake_blocks[block_num].goto(new_x, new_y)

        self.snake_head.fd(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)




