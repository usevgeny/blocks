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


groupe = [a, d, b, c, g, e, f, g]

xt1 = 800
xt2 = 800
yt1 = 720
yt2 = 0

master = Tk()
root = Canvas(master, width=800, height=720)
root.pack()

#drawing blocks
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

def update_tag():
    untouched = "blue"
    being_touched = "red"
    touched = "gray"
    block_color=untouched

    for i in range(len(groupe)):
        x_block = xt1
        print(i)
        if groupe[i]['xl_item'] >= x_block and groupe[i]['xo_item'] <= x_block:
            root.itemconfig(rects[i], tag="being_touched")
        elif groupe[i]['xl_item'] > x_block and groupe[i]['xo_item'] > x_block:
            root.itemconfig(rects[i], tag="touched")

        print(groupe[i]['xl_item'], groupe[i]['xo_item'], x_block, root.itemcget(rects[i],"tag"))
    update_color()

def update_color():
    for r in rects:
        if root.itemcget(r, "tag") == "untouched" : 
            root.itemconfig(r, fill="blue")
        elif root.itemcget(r, "tag") == "being_touched" : 
            root.itemconfig(r, fill="red")
        elif root.itemcget(r, "tag") == "touched" : 
            root.itemconfig(r, fill="gray")
#Moving RedLine
def deplacer():
    global xt1, yt1, xt2, yt2
    xt1-=5
    xt2-=5
    root.coords(laser_print, xt1, yt1, xt2,yt2)
    update_tag()
    
    root.after(50, deplacer)

    return



#draw vertical redline
laser_print=root.create_line(xt1, yt1, xt2, yt2, fill="red")
rects=[]

#draw rects
for ensemble in groupe:
    drawing_block = root.create_rectangle(ensemble['xo_item'], ensemble['yo_item'],
                                 ensemble['xl_item'], ensemble['yl_item'], tag="untouched")
    rects.append(drawing_block)

deplacer()

mainloop()

  
