import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS

im = Image.new("RGB", (640,480))
draw = ID.Draw(im)

#Optimised code for DDA algorithm
def lineDDA(x1,y1,x2,y2):

    if(x1 == x2): #Vertical Line, Here we know that x-coordinate is not changing therefore there is no need to increment x in for loop.it will reduce the time 
        difference = abs(y1 - y2)
        if(y1>y2):
            yy = y2
        else:
            yy = y1
        for i in range(0,int(difference)):
            draw.point((x1, yy),(255,0,0))
            yy=yy+1
    elif(y1 == y2):  #Horizontal Line, same goes with y-coordinate
        difference=abs(x1-x2) 
        if(x1>x2):
            xx = x2
        else:
            xx = x1
        for i in range(0,int(difference)):
            draw.point((xx,y1),(255,0,0))
            xx=xx+1        
	
    else:
        dx = x2-x1
        dy = y2-y1
        x=x1
        y=y1
        slope = float(dy)/float(dx)
        if(y1>y2):
            yy = y2
        else:
            yy = y1
        if(x1>x2):
            xx = x2
        else:
            xx = x1    
        if(slope == -1): #Diagonal line, Here we have reduce some steps by eliminating fews steps like xincremnet and yincremnet etc.
            while(xx != x2 and yy != y2):
                draw.point((xx,yy),(255,0,0))
                xx=xx+1
                yy=yy+1    
        elif(slope == 1):  #Diagonal line
            while(xx != x2 and yy != y2):
                draw.point((xx,yy),(255,0,0))
                xx=xx+1
                yy=yy+1

        else:
            if(abs(dx)>abs(dy)):
                steps = abs(dx)
            else:
                steps = abs(dy)
	 			
            xincrement = float(dx)/float(steps)
            yincrement = float(dy)/float(steps)
            draw.point((round(x),round(y)),(255,0,0))
            for k in range(0,steps):
                x= x + xincrement
                y= y + yincrement
                draw.point(round(x),round(y),(255,0,0))
	    
 	

maxx = 450/640
maxy = 349/480;

lineDDA((174/maxx),(254/maxy), (174/maxx), (294/maxy))   
lineDDA((204/maxx), (254/maxy), (204/maxx), (300/maxy))
lineDDA((242/maxx), (254/maxy), (242/maxx), (300/maxy))
lineDDA((271/maxx), (254/maxy), (271/maxx), (294/maxy))
lineDDA((153/maxx), (327/maxy), (216/maxx), (327/maxy))
lineDDA((230/maxx), (327/maxy), (293/maxx), (327/maxy))

draw.polygon((((160/maxx),(134/maxy)),((160/maxx),(186/maxy)),((135/maxx),(186/maxy)),((135/maxx),(134/maxy))),fill=128,outline=255)
draw.polygon((((135/maxx),(143/maxy)),((91/maxx),(143/maxy)),((91/maxx),(178/maxy)),((135/maxx),(178/maxy))),fill=128,outline=255)
draw.polygon((((287/maxx),(134/maxy)),((287/maxx),(186/maxy)),((313/maxx),(186/maxy)),((313/maxx),(134/maxy))),fill=128,outline=255)
draw.polygon((((313/maxx),(143/maxy)),((313/maxx),(178/maxy)),((358/maxx),(178/maxy)),((358/maxx),(143/maxy))),fill=128,outline=255)
draw.polygon((((175/maxx),(127/maxy)),((273/maxx),(127/maxy)),((273/maxx),(23/maxy)),((175/maxx),(23/maxy))),fill=64,outline=255)
draw.polygon((((160/maxx),(127/maxy)),((287/maxx),(127/maxy)),((287/maxx),(254/maxy)),((160/maxx),(254/maxy))),fill=255,outline=255)

draw.arc(((188/maxx), (48/maxy), (212/maxx), (77/maxy)), 0, 360, fill = (255,0,0))
draw.arc(((233/maxx), (48/maxy), (259/maxx), (77/maxy)), 0, 360, fill = 255)
draw.arc(((153/maxx), (293/maxy), (216/maxx), (362/maxy)), 180, 0, fill = (255,0,0))
draw.arc(((230/maxx), (293/maxy), (293/maxx), (362/maxy)), 180, 0, fill = (255,0,0))

im.show()
