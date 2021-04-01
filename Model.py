import graphics as gr
from tkinter import *
import math

#Class of astronomic objects
class AstObj:
    def __init__(self, radius, mass, color, coords, velocity):
        self.r = radius
        self.m = mass
        self.color = color
        self.coords = coords
        self.v = velocity
        self.a = gr.Point(0, 0)
        self.circle = None
        self.pref_coords = coords

#фунция, возвращающая сумму двух векторо-точек библиотеки Graphics
def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point

#фунция, возвращающая разность двух векторо-точек библиотеки Graphics
def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point

#Функция, отрисовывающая окно с серым фоном разрешеним SIZE_X x SIZE_Y
def draw_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('grey')
    rectangle.draw(window)


#Функция, отрисовывающая круг в заданной точке, заданного цвета и радиуса
def draw_ball(coords, radius, color):
    circle = gr.Circle(coords, radius)
    circle.setFill(color)
    circle.draw(window)
    return circle


#Функция, отрисовывающая все астрономические объекты из массива astobjs
def draw_all(astrobjs):
    draw_window()
    for astrobj in astrobjs:
        astrobj.circle = draw_ball(astrobj.coords,
                                   astrobj.r,
                                   astrobj.color)

#Функция, обновляющая координаты путем сложения старых координат и новых скоростей
def update_coords(coords, velocity):
    return add(coords, velocity)

#Функция, обновляющая скорости путем сложения старых скоростей и новых ускорений
def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


#Функция, обновляющая ускорение одного объекта к другому
def update_acceleration_for2(AstObj1, AstObj2):
    diff = sub(AstObj1.coords, AstObj2.coords)
    distance_3 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)
    if distance_3 != 0:
        G = 2500
        #G = 0.00000000000667
        return gr.Point((-diff.x * G * AstObj2.m) / distance_3,
                        (-diff.y * G * AstObj2.m) / distance_3)

#Функция, обновляющая итоговые ускорения всех объектов
def update_acceleration(Astroobjects):
    for i in range(0, len(Astroobjects)):
        Astroobjects[i].a = gr.Point(0, 0)
        for j in range(0, len(Astroobjects)):
                if i < j and int(Matrix[i][j].get()) == 1:
                    Astroobjects[i].a = add(Astroobjects[i].a,
                                            update_acceleration_for2(Astroobjects[i],
                                                                     Astroobjects[j]))
                if j < i and int(Matrix[j][i].get()) == 1:
                    Astroobjects[i].a = add(Astroobjects[i].a,
                                            update_acceleration_for2(Astroobjects[i],
                                                                     Astroobjects[j]))

#Фукнция, решающая проблему налета объектов друг на друга
def collision_check(Astroobjects):
    for i in range(0, len(Astroobjects)):
        for j in range(0, len(Astroobjects)):
            if i != j and i < len(Astroobjects) and j < len(Astroobjects):
                diff = sub(Astroobjects[i].coords, Astroobjects[j].coords) #вектор-разность между координатами двух объектов
                distance = (diff.x ** 2 + diff.y ** 2) ** (1 / 2) #расстояние между объектами
                if (distance <= (Astroobjects[i].r + Astroobjects[j].r)): #проверка "наезда" одной планеты на другую
                    M = Astroobjects[i].m + Astroobjects[j].m #масса нового тела

                    #цвет нового тела определяется массой самого тяжелого объекта:
                    if (Astroobjects[i].m >= Astroobjects[j].m):
                        Astroobjects[i].color = Astroobjects[i].color

                    if (Astroobjects[i].m < Astroobjects[j].m):
                        Astroobjects[i].color = Astroobjects[j].color
                        Astroobjects[i].coords = Astroobjects[j].coords

                    #координаты нового тела определяются из центра масс двух объектов перед столкновением

                   #Astroobjects[i].coords = gr.Point((Astroobjects[i].coords.x * Astroobjects[i].m
                    #                                   + Astroobjects[j].coords.x * Astroobjects[j].m) / M,
                     #                                 (Astroobjects[i].coords.y * Astroobjects[i].m
                      #                                 + Astroobjects[j].coords.y * Astroobjects[j].m) / M)

                    #скорость нового тела из закона сохранения импульса
                    Astroobjects[i].v.x = (Astroobjects[i].m * Astroobjects[i].v.x
                                                  + Astroobjects[j].m * Astroobjects[j].v.x) / M
                    Astroobjects[i].v.y = (Astroobjects[i].m * Astroobjects[i].v.y
                                                  + Astroobjects[j].m * Astroobjects[j].v.y) / M

                    #масса нового тела, равная сумме масс двух старых тел
                    Astroobjects[i].m = M

                    #радиус нового тела такой, чтобы его объём был равен сумме объёмов двух старых тел
                    Astroobjects[i].r = (Astroobjects[i].r ** 3 + Astroobjects[j].r ** 3) ** (1 / 3)

                    #удаление старых тел с экрана
                    Astroobjects[j].circle.undraw()
                    Astroobjects[i].circle.undraw()
                    #рисование нового тела
                    Astroobjects[i].circle = draw_ball(Astroobjects[i].coords,
                                                       Astroobjects[i].r,
                                                       Astroobjects[i].color)

                    #удаление одного старого тела из массива Астрообъектов
                    del Astroobjects[j]


#Функция, сдвигающая все объекты согласно вычисленным ускорениям и скоростям
def moving(Astroobjects):
    update_acceleration(Astroobjects)
    for i in range(0, len(Astroobjects)):
        #Trajectory = Astroobjects[i].coords
        #Trajectory.setFill(Astroobjects[i].color)
        #Trajectory.draw(window)
        #вычисляем новые координаты
        Astroobjects[i].v = update_velocity(Astroobjects[i].v,
                                            Astroobjects[i].a)
        Astroobjects[i].coords = update_coords(Astroobjects[i].coords,
                                               Astroobjects[i].v)
        if (Astroobjects[i].coords.x != Astroobjects[i].pref_coords.x or
                Astroobjects[i].coords.y != Astroobjects[i].pref_coords.y):
            w = sub(Astroobjects[i].coords, Astroobjects[i].pref_coords)
            #двигаемся на эту разницу
            Astroobjects[i].circle.move(w.x, w.y)
            #устареваем новые координаты
            Astroobjects[i].pref_coords = gr.Point(Astroobjects[i].coords.x,
                                                   Astroobjects[i].coords.y)
    gr.time.sleep(0.01)


#Создание окна интерфейса
root = Tk()
root.title('Model settings')
root.geometry("1200x800")


#Список всех используемых цветов объектов
COLORS = [
"orange",
"yellow",
"red",
"blue",
"green",
"gray",
"black"
]


#Выпадающее меню выбора цвета
label_color = Label(root, text='Color', font='bold')
label_color.place(x=115, y=25)

variable_color = StringVar(root)
variable_color.set(COLORS[0]) # default value
color_menu = OptionMenu(root, variable_color, *COLORS,)
color_menu.place(x=105, y=45)



#Поле ввода массы
label_mass = Label(root, text='Mass', font='bold')
label_mass.place(x=210, y=25)
entry_mass = Entry(root, width=10)
entry_mass.place(x=205, y=50)

#Поле ввода радиуса
label_radius = Label(root, text='Radius', font='bold')
label_radius.place(x=310, y=25)
entry_radius = Entry(root, width=10)
entry_radius.place(x=305, y=50)


#Поля ввода коорднат
label_mass = Label(root, text='Coordinates', font='bold')
label_mass.place(x=185, y=100)

label_x = Label(root, text='X')
label_x.place(x=120, y=130)
entry_x = Entry(root, width=10)
entry_x.place(x=135, y=130)

label_y = Label(root, text='Y')
label_y.place(x=245, y=130)
entry_y = Entry(root, width=10)
entry_y.place(x=260, y=130)

#Поля ввода скоростей
label_velocity = Label(root, text='Velocity', font='bold')
label_velocity.place(x=190, y=200)

label_v_x = Label(root, text='Vx')
label_v_x.place(x=115, y=230)
entry_v_x = Entry(root, width=10)
entry_v_x.place(x=135, y=230)

label_v_y = Label(root, text='Vy')
label_v_y.place(x=240, y=230)
entry_v_y = Entry(root, width=10)
entry_v_y.place(x=260, y=230)


#Sun1 = AstObj(30, 1.1, 'yellow', gr.Point(750, 500), gr.Point(0, 3))
#Sun2 = AstObj(30, 1.1, 'orange', gr.Point(630, 500), gr.Point(0, -3))
#Venus = AstObj(10, 0.000007, 'orange', gr.Point(470, 500), gr.Point(0, 5))
#Earth = AstObj(10, 0.00001, 'green', gr.Point(350, 500), gr.Point(0, 4))
#Mars = AstObj(10, 0.00000001, 'red', gr.Point(300, 500), gr.Point(0, 4))
#Jupiter = AstObj(20, 0.00005, 'orange', gr.Point(200, 500), gr.Point(2, 6))
#Astroobjects_Example = [Sun1, Sun2, Venus, Earth, Mars, Jupiter]


Sun = AstObj(30, 1.1, 'yellow', gr.Point(650, 500), gr.Point(0, 0))
Mercury = AstObj(2, 0.000001, 'orange', gr.Point(600, 500), gr.Point(0, 7))
Venus = AstObj(5, 0.000007, 'orange', gr.Point(550, 500), gr.Point(0, 5))
Earth = AstObj(8, 0.00001, 'blue', gr.Point(500, 500), gr.Point(0, 4))
Mars = AstObj(7, 0.000008, 'red', gr.Point(425, 500), gr.Point(0, 3))
Jupiter = AstObj(15, 0.00005, 'orange', gr.Point(300, 500), gr.Point(0, 2.7))
Asteroid = AstObj(1, 0.000000001, 'brown', gr.Point(0, 0), gr.Point(5, 5))

Astroobjects_Example = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Asteroid]



#Задание матрица смежности взаимодействий для примера системы
Matrix = [[None for x in range(len(Astroobjects_Example))] for y in range(len(Astroobjects_Example))]
for i in range(0, len(Astroobjects_Example)):
    for j in range(0, len(Astroobjects_Example)):
        Matrix[i][j] = IntVar(root)
        Matrix[i][j].set(1)


Astroobjects = []


#Функция, создающая объект с параметрами, введенными в поля
def object_parameters_entry():
    New_Object = AstObj(float(entry_radius.get()), float(entry_mass.get()),
                        variable_color.get(), gr.Point(float(entry_x.get()),
                        float(entry_y.get())), gr.Point(float(entry_v_x.get()),
                                                        float(entry_v_y.get())))
    return New_Object






#Функция, отрисовывающая матрицу смежности
def draw_matrix():
    canvas = Canvas(root, width=800, height=800)
    canvas.pack(side='right')
    # отрисовка номеров строк и столбцов матрицы смежности:
    for i in range(0, len(Astroobjects)):
        # по горизонтали:
        Label_Object = Label(canvas, text=str(i + 1), font='Bold 14')
        Label_Object.place(x=250 + i * 50, y=100)

        # по вертикали:
        Label_Object = Label(canvas, text=str(i + 1), font='Bold 14')
        Label_Object.place(x=210, y=130 + i * 50)
    #Задание матрицы смежности
    global Matrix
    Matrix = [[None for x in range(len(Astroobjects))] for y in range(len(Astroobjects))]

    for i in range(0, len(Astroobjects)):
        for j in range(0, len(Astroobjects)):
            Matrix[i][j] = IntVar(root)
            Matrix[i][j].set(1)

    #массив CheckButton'ов
    inter_condition = [[None for x in range(len(Astroobjects))] for y in range(len(Astroobjects))]
    #Отрисовка CheckButton'ов
    for i in range(0, len(Astroobjects)):
        for j in range(0, len(Astroobjects)):
            if i < j:
                inter_condition[i][j] = Checkbutton(canvas, variable=Matrix[i][j], font='bold 10')
                inter_condition[i][j].place(x=250 + i * 50, y=130 + j * 50)

            if j < i:
                inter_condition[j][i] = Checkbutton(canvas, variable=Matrix[j][i], font='bold 10')
                inter_condition[j][i].place(x=250 + j * 50, y=130 + i * 50)

    



#Кнопка для добавления объекта
btn_addobj = Button(root, text='Add object', font="Bold")
btn_addobj.place(x=150, y=300)
btn_addobj.bind('<Button-1>', lambda event: (Astroobjects.append(object_parameters_entry()), btn_example.destroy(), drawlist()))

#Функция, выводящая добавленных объект и его параметры в список
def drawlist():
    i = len(Astroobjects)
    Astroobjects_list = Label(root, text='Planet ' + str(i) + ': Radius = ' + str(Astroobjects[i - 1].r) +
                                         ' Coords: (' + str(Astroobjects[i - 1].coords.x) + ', ' +
                                         str(Astroobjects[i - 1].coords.y) + ')' + ' Velocity: (' +
                                         str(Astroobjects[i - 1].v.x) + ', ' + str(Astroobjects[i - 1].v.y) +
                                         ')', font='Bold 12', fg=str(Astroobjects[i - 1].color))

    Astroobjects_list.place(x=20, y=400 + i * 30)


#Кнопка для запуска
def launchbutton():
    launchbutton = Button(root, text='Run model', font="Bold 16")
    launchbutton.bind('<Button-1>', lambda event: (root.quit()))
    launchbutton.place(x=700, y=150 + len(Astroobjects) * 50)
    label_interaction = Label(root, text='Uncheck the boxes on the interactions you want to disable:', font="Bold 14")
    label_interaction.place(x=500, y=40)

#Кнопка для настройки взаимодействия
btn_interaction_sttngs = Button(root, text='Configure interaction', font="Bold")
btn_interaction_sttngs.bind('<Button-1>', lambda event: (draw_matrix(), launchbutton(), btn_example.destroy()))
btn_interaction_sttngs.place(x=120, y=370)

#Функция для слияния двух массивов
def merge_arrays(Array1, Array2):
    for i in range(0, len(Array2)):
        Array1.append(Array2[i])

#Кнопка, по нажатию на которую запускающется пример системы
btn_example = Button(root, text='Run the sample model', font='Bold')
btn_example.bind('<Button-1>', lambda event: (merge_arrays(Astroobjects, Astroobjects_Example), root.quit()))
btn_example.place(x=100, y=450, width=300)

root.mainloop()





#Задание параметров окна
SIZE_X = 1500
SIZE_Y = 800
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)




#Отрисовка всех объктов
draw_all(Astroobjects)


#Бесконечый цикл
while True:
    moving(Astroobjects)
    collision_check(Astroobjects)
    gr.time.sleep(0.01)



