from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """ Constructor"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):   # reinitialize the snake back at the center
        for seg in self.segments:
            seg.goto(1000, 1000)  # previous segments go off the screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Method design to move the snake object"""
        for seg_num in range(len(self.segments) - 1, 0, -1):  # loops across the list of segments
            next_x = self.segments[seg_num - 1].xcor()  # stores the x coordinate of the segment before the current one
            next_y = self.segments[seg_num - 1].ycor()  # stores the y coordinate of the segment before the current one
            self.segments[seg_num].goto(next_x, next_y)  # assigns the previous coordinates to the the current segment

        self.head.forward(MOVE_DISTANCE)  # moves forward the first segment, the others will follow afterwards

    def up(self):
        if self.head.heading() != DOWN:  # checks to see if the the current direction is not down
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # checks to see if the the current direction is not up
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # checks to see if the the current direction is not right
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # checks to see if the the current direction is not left
            self.head.setheading(RIGHT)
