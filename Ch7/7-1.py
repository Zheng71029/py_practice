class Window:
    def __init__(self,w=10,h=5):
        self.width=w
        self.height=h


#(a)
w0=Window()
print(w0.width)  
print(w0.height) 

#(b)
w1=Window(12,8)
print(w1.width)  
print(w1.height) 

#(c)
setattr(w1,'width',16)
setattr(w1,'height',7)
print(w1.width)  
print(w1.height) 

#(d)
a = w0.width * w0.height 
b = w1.width * w1.height 
if a>b :
    print(a)
else:
    print(b)