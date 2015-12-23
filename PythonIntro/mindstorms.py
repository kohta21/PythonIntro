# -*- coding: utf-8 -*-

# Udacity URL
# https://www.udacity.com/course/viewer#!/c-ud036/l-1004409226/m-1013388833

import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(3):
        some_turtle.forward(80)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(10)

    for i in range(36):
        draw_square(brad)
        brad.right(10)


    ##Create the turtle Angie - Draw a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    ##Create the turtle Tri - Draw a triangle
    #Tri = turtle.Turtle()
    #Tri.shape("arrow")
    #Tri.color("green")
    #draw_triangle(Tri)

    window.exitonclick()

draw_art()