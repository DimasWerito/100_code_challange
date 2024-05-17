import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)

    t = turtle.Turtle()
    t.speed(0)

    # Встановлення початкової позиції
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Визначення рівня рекурсії та розміру відрізка
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    length = 300

    # Малювання трьох сторін сніжинки Коха
    for _ in range(3):
        koch_snowflake(t, level, length)
        t.right(120)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
