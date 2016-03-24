import signal
import sys
from PyMata.pymata import PyMata
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton,QVBoxLayout, QWidget, QTextEdit
app = QApplication([])
mainwindow = QMainWindow()
mainwindow.setWindowTitle("My Rebo")
button_go = QPushButton("Go Go Go")
button_dancing = QPushButton("Dancing now")
button_right = QPushButton("Right")
button_left = QPushButton("Turn left")
button_exit = QPushButton("Stop")
button_distance = QPushButton("Show the Distance")
vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addWidget(button_exit)
vbox.addWidget(button_go)
vbox.addWidget(button_dancing)
vbox.addWidget(button_right)
vbox.addWidget(button_left)
vbox.addWidget(button_distance)
textedit = QTextEdit("")
vbox.addWidget(textedit)
# This is some silly Qt-ism
container = QWidget()
container.setLayout(vbox)
mainwindow.setCentralWidget(container)
mainwindow.show()
def distance_handler(self):
    value = board.analog_read(1)
    distance = 6762 / (value -9) -4
    textedit.append("{:06.2f}".format(distance))
    print (distance)
    print("distance", board.analog_read(1))
def exit_handler(sig):
    if board is not None: board.reset()
    sys.exit(0)
def go_handler(Go):
    for i in range(0, 100):
     board.analog_write(5, i)
     board.analog_write(6, i)
    for i in range(6, 10):
        board.analog_write(5, i)
        board.analog_write(6, i)
def dancing_handler(dancing):
    for i in range(0, 255):
     board.analog_write(5, i)
     board.analog_write(6, i)
    for i in range(6, 10):
        board.analog_write(5, i)
        board.analog_write(6, i)
def left_handler(back):
    for i in range(1, 10):
     board.analog_write(5, i)
     board.analog_write(6, i)
    for i in range(1, 10):
     board.analog_write(5, i)
     board.analog_write(6, i)
button_left.clicked.connect(left_handler)
button_distance.clicked.connect(distance_handler)
button_exit.clicked.connect(exit_handler)
button_dancing.clicked.connect(dancing_handler)
button_go.clicked.connect(go_handler)
signal.signal(signal.SIGINT, exit_handler)
board = PyMata()
board.set_pin_mode(5, board.PWM, board.DIGITAL)
board.set_pin_mode(6, board.PWM, board.DIGITAL)
board.set_pin_mode(1, board.INPUT, board.ANALOG)
sys.exit(app.exec_()) # This is basically infinite loop here, it blocks everything else!
