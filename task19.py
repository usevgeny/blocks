from tkinter import *

a = {
    "y":2,
    "len" : 4
    }


b = {
    "y":5,
    "len" : 7
    }


c = {
    "y":6,
    "len" : 8
    }


d = {
    "y":2,
    "len" : 4
    }


e = {
    "y":4,
    "len" : 12
    }


f = {
    "y":3,
    "len" : 10
    }


g = {
    "y":7,
    "len" : 10
    }


groupe = [a,d, b, c, g, e, f]

xt1 = 800
xt2= 800
yt1=720
yt2=0

master = Tk()
root = Canvas(master, width=800, height=720)
root.pack()

#Moving RedLine
def deplacer():
    global xt1, yt1, xt2, yt2
    xt1-=5
    xt2-=5
    root.coords(laser_print, xt1, yt1, xt2,yt2)
    root.after(50,deplacer)

    return

#drawing blocks
drawing_blocks = []
item = {}

graf_dist = 0
dist_betw=0
untouched = "blue"
being_touched = "red"
touched= "gray"
block_color=untouched

for ensemble in groupe:

    graf_dist+=60
    dist_betw+=10

    xo=graf_dist+dist_betw
    yo=int(ensemble['y']*50)
    xl=xo+60
    yl=int(ensemble['len']*50)
    ensemble['xo_item']=xo
    ensemble['yo_item']=yo
    ensemble['xl_item']=xl
    ensemble['yl_item']=yl
    # if xo<=xt1 and xl>xt1:
    #     block_color=being_touched
    # elif xo<xt1 and xl<=xt1:
    #     block_color=untouched



    # drawing_block = root.create_rectangle(xo, yo, xl, yl, fill=block_color, tag="blocks")

    # drawing_blocks.append(drawing_blocks)


#draw vertical redline
laser_print=root.create_line(xt1, yt1, xt2, yt2, fill="red")
i=0
for ensemble in groupe:
    i+=2
    print(ensemble['xo_item']+i)

deplacer()

for ensemble in groupe:
    print(ensemble)
    x_block=xt1
    if ensemble['xo_item']<x_block and ensemble['xl_item']>x_block:
        block_color=being_touched
    elif ensemble['xo_item']>=x_block and ensemble['xl_item']>x_block:
        block_color=touched
    drawing_block = root.create_rectangle(ensemble['xo_item'], ensemble['yo_item'], ensemble['xl_item'], ensemble['yl_item'], fill=block_color, tag="blocks")
  

   

def update_color():
    untouched = "blue"
    being_touched = "red"
    touched= "gray"
    block_color=untouched

    for i in range(len(groupe)):
        x_block = xt1
        bbb=groupe[i]
        if bbb['xo_item'] <x_block and bbb['xl_item'] >=x_block:
            block_color=being_touched
        elif bbb['xo_item']>=x_block and bbb['xl_item'] <=x_block:
            block_color=touched

        print(bbb['xo_item'])
        print(bbb['xl_item'])
    
    root.itemconfig('blocks', fill=block_color)
    root.after(50,update_color)

update_color()




mainloop()