def setup():
    size(600, 400)
    background(255)

def draw():
    if mousePressed and mouseX > 200:
        line(pmouseX, pmouseY, mouseX, mouseY)
        
def mouseClicked():
    if mouseX < 200:
        if mouseY < 100:
            stroke(0, 0, 0)
        else:
            stroke(random(255), random(255), random(255))
