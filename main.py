import sys
import QtGUI

if __name__ == "__main__":
    app = QtGUI.QApplication(sys.argv)
    window = QtGUI.Window()
    window.show()
    sys.exit(app.exec())