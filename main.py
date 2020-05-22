from graphics import *
import tests.mainTester


def main():
        win = GraphWin("Test", 500, 500)
        win.setBackground("black");

        img = Image(Point(250, 250), "tst.png")
        img.draw(win)

        win.getMouse()
        win.close()

