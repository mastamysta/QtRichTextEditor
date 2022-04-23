import sys
import PySide6
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6 import QtCore
from PySide6 import QtWidgets, QtGui

import fugue

def is_bold_complete(window):

    ted = window.ted0
    cursor = ted.textCursor()
    ret = True

    # if the user has no selection, we just want to toggle the bold cursor

    if cursor.hasSelection():
        start = cursor.selectionStart() + 1
        end = cursor.selectionEnd()
    else:
        start = cursor.selectionStart()
        end = start + 1

    for position in range(start, end):

        cursor.setPosition(position)
        format = cursor.charFormat()

        if format.fontWeight() != QtGui.QFont.Bold:
            ret = False
            break

    return ret

def is_ital_complete(window):

    ted = window.ted0
    cursor = ted.textCursor()
    ret = True

    # if the user has no selection, we just want to toggle the bold cursor

    if cursor.hasSelection():
        start = cursor.selectionStart() + 1
        end = cursor.selectionEnd()
    else:
        start = cursor.selectionStart()
        end = start + 1

    for position in range(start, end):

        cursor.setPosition(position)
        format = cursor.charFormat()

        if format.fontItalic() != QtGui.QFont.StyleItalic:
            ret = False
            break

    return ret

def bold_clicked_handler(window):

    ted = window.ted0

    if not is_bold_complete(window):
        ted.setFontWeight(QtGui.QFont.Bold)
    else:
        ted.setFontWeight(QtGui.QFont.Normal)

def ital_clicked_handler(window):

    ted = window.ted0

    if not is_ital_complete(window):
        ted.setFontItalic(QtGui.QFont.StyleItalic)
    else:
        ted.setFontItalic(QtGui.QFont.StyleNormal)

def canInsertFromMimeData(self, source):

    if (source.hasImage()):
        return True
    else:
        return QtWidgets.QTextEdit.canInsertFromMimeData(source)

if __name__ =="__main__":

    app = QApplication(sys.argv)

    ui_file_name = "qtTest/mainwindow.ui"
    ui_file = QFile(ui_file_name)

    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    butBold = window.butBold
    butItal = window.butItal

    butBold.clicked.connect(lambda: bold_clicked_handler(window))
    butItal.clicked.connect(lambda: ital_clicked_handler(window))

    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())