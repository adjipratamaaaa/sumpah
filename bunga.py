import turtle
import math

# Fungsi untuk menggambar satu kelopak bunga
def petal():
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)

# Fungsi untuk menggambar bunga
def flower():
    turtle.color("red")
    for _ in range(6):  # Jumlah kelopak
        petal()
        turtle.right(60)  # Rotasi untuk posisi kelopak selanjutnya

# Fungsi untuk menggambar tangkai bunga
def stem():
    turtle.right(90)  # Menghadap ke bawah
    turtle.color("green")
    turtle.pensize(5)  # Ukuran pensil untuk tangkai
    turtle.forward(300)  # Menggambar tangkai

# Fungsi untuk menggambar daun
def leaf():
    turtle.color("green")
    turtle.begin_fill()
    turtle.circle(50, 90)  # Daun setengah lingkaran
    turtle.left(90)
    turtle.circle(50, 90)  # Daun setengah lingkaran
    turtle.end_fill()

# Fungsi utama
def main():
    turtle.speed(50)  # Kecepatan menggambar
    turtle.bgcolor("lightblue")  # Latar belakang
    turtle.penup()
    turtle.goto(0, -200)  # Posisi awal bunga
    turtle.pendown()
    
    flower()  # Menggambar bunga
    
    # Menggambar tangkai dan daun
    stem()
    turtle.right(45)
    leaf()
    turtle.left(180)
    leaf()
    
    turtle.hideturtle()  # Sembunyikan kursor turtle
    turtle.done()  # Selesai menggambar

if __name__ == "__main__":
    main()
