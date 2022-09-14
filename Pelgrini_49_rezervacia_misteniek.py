import tkinter
canvas=tkinter.Canvas(width=600, height=300, bg='white')
canvas.pack() #spravil som okno

pocetradov=10
VEL=40
obsadene=0
busx, busy=50, 50

def zafarbi(sedadlo, farba): #funkcia na farbi
        canvas.itemconfig('sedadlo_'+str(sedadlo), fill=farba)

def kresli(x,y,pocet):#spravil som 10 na 4 polícka s číslami od 1 do 40 zvislo
        cislo=0
        for i in range(pocet):
                for j in range(4):
                        cislo+=1
                        canvas.create_rectangle(x+i*VEL, y+j*VEL,
                                                x+(i+1)*VEL-10, y+(j+1)*VEL-10, fill='lime green',
                                                tags='sedadlo_'+str(cislo))
                        canvas.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo)

def klik(event):#nastavil som lave tlačidlo na miške
    global obsadene
    if(busx<event.x<busx+VEL*pocetradov and
        busy<event.y<busy+VEL*4):
            ix=(event.x-busx) // VEL
            iy=(event.y-busy) // VEL
            sedadlo=ix*4+iy+1
            zafarbi(sedadlo, 'red')
            print(sedadlo)
            obsadene+=1
            pocitadlo()

def klik2(event): #nastavil som prave tlačidlo na miške
    global obsadene
    if(busx<event.x<busx+VEL*pocetradov and
        busy<event.y<busy+VEL*4):
            ix=(event.x-busx) // VEL
            iy=(event.y-busy) // VEL
            sedadlo=ix*4+iy+1
            zafarbi(sedadlo, 'lime green')
            print(sedadlo)
            obsadene-=1
            pocitadlo()

def pocitadlo():#počítam obsadené miesta
    canvas.delete('zig')
    canvas.create_text(250,250,text='obsadene '+str(obsadene),tag='zig')

kresli(busx, busy, pocetradov) #pomaloval som plátno
canvas.bind('<Button>',klik) #nastavil som lave tlačidlo na miške
canvas.bind('<Button-3>',klik2) #nastavil som prave tlačidlo na miške