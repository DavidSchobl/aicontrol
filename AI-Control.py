#AI-Control_v1.14
import sys
import json
import socket
import os
import signal
import psutil
import datetime
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMenuBar, QAction, QInputDialog, QHBoxLayout
from PyQt5.QtCore import QTimer, QProcess, QDir, QUrl
from PyQt5.QtGui import QDesktopServices, QIcon

print('''[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[34m▄[0m[46m[34m▄[0m[46m[34m▄[0m[46m[34m▄[0m[46m[34m▄[0m[46m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[30m▄[0m[46m[30m▄[0m[46m[30m▄[0m[46m[30m▄[0m[46m[30m▄[0m[46m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[33m▄[0m[42m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[32m▄[0m[43m[32m▄[0m[43m[30m▄[0m[42m[30m▄[0m[42m[32m▄[0m[42m[33m▄[0m[42m[33m▄[0m[42m[33m▄[0m[46m[33m▄[0m[46m[33m▄[0m[42m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[33m▄[0m[46m[33m▄[0m[46m[36m▄[0m[46m[36m▄[0m
[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[36m▄[0m[42m[36m▄[0m[46m[36m▄[0m[42m[32m▄[0m[42m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[32m▄[0m[43m[32m▄[0m[43m[32m▄[0m[43m[32m▄[0m[43m[33m▄[0m[42m[33m▄[0m[42m[33m▄[0m[43m[33m▄[0m[42m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m
[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[36m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[30m▄[0m[42m[30m▄[0m[43m[32m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[30m▄[0m[42m[30m▄[0m[42m[32m▄[0m[46m[32m▄[0m[42m[32m▄[0m[43m[33m▄[0m[43m[33m▄[0m[41m[30m▄[0m[40m[30m▄[0m[43m[31m▄[0m[43m[32m▄[0m[43m[32m▄[0m[42m[32m▄[0m[46m[32m▄[0m[42m[31m▄[0m[43m[31m▄[0m[43m[31m▄[0m[43m[31m▄[0m[43m[33m▄[0m[43m[32m▄[0m[43m[32m▄[0m[43m[32m▄[0m[43m[30m▄[0m[42m[31m▄[0m[43m[31m▄[0m[43m[31m▄[0m[43m[33m▄[0m[43m[33m▄[0m[41m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m
[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[36m▄[0m[42m[32m▄[0m[46m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[46m[36m▄[0m[46m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[31m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[33m▄[0m[42m[31m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[31m▄[0m[42m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[44m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m
[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[42m[36m▄[0m[40m[30m▄[0m[40m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[33m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[31m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[43m[33m▄[0m[41m[31m▄[0m[40m[30m▄[0m[40m[32m▄[0m[42m[32m▄[0m[42m[33m▄[0m[41m[31m▄[0m[41m[31m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[35m▄[0m[45m[35m▄[0m[44m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[32m▄[0m[46m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[33m▄[0m[42m[33m▄[0m[42m[33m▄[0m[43m[33m▄[0m
[46m[32m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[42m[30m▄[0m[42m[30m▄[0m[42m[30m▄[0m[42m[30m▄[0m[46m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[42m[33m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[41m[31m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[43m[33m▄[0m[41m[31m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[43m[33m▄[0m[41m[31m▄[0m[41m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[45m[35m▄[0m[46m[32m▄[0m[42m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m
[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[32m▄[0m[40m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[46m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[36m▄[0m[42m[36m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[43m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[42m[33m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[31m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[43m[32m▄[0m[41m[31m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[43m[33m▄[0m[41m[31m▄[0m[43m[31m▄[0m[40m[30m▄[0m[40m[30m▄[0m[45m[35m▄[0m[42m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[46m[36m▄[0m
[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[46m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[42m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[42m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[43m[32m▄[0m[41m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[42m[33m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[41m[31m▄[0m[43m[33m▄[0m[42m[32m▄[0m[41m[32m▄[0m[41m[31m▄[0m[40m[30m▄[0m[40m[30m▄[0m[45m[35m▄[0m[46m[35m▄[0m[46m[32m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[36m▄[0m[43m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[46m[36m▄[0m
[42m[31m▄[0m[42m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[30m▄[0m[46m[30m▄[0m[46m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[36m▄[0m[42m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[42m[32m▄[0m[43m[32m▄[0m[43m[32m▄[0m[43m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[33m▄[0m[46m[33m▄[0m[40m[30m▄[0m[40m[30m▄[0m[41m[30m▄[0m[43m[30m▄[0m[43m[33m▄[0m[40m[33m▄[0m[40m[30m▄[0m[41m[32m▄[0m[43m[33m▄[0m[43m[33m▄[0m[42m[33m▄[0m[43m[32m▄[0m[40m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[44m[30m▄[0m[42m[30m▄[0m[42m[30m▄[0m[40m[30m▄[0m[40m[30m▄[0m[46m[36m▄[0m[42m[36m▄[0m[40m[30m▄[0m[40m[30m▄[0m[43m[30m▄[0m[43m[30m▄[0m[43m[33m▄[0m[46m[33m▄[0m
[41m[31m▄[0m[41m[31m▄[0m[40m[31m▄[0m[40m[31m▄[0m[43m[31m▄[0m[42m[31m▄[0m[42m[31m▄[0m[47m[33m▄[0m[40m[32m▄[0m[40m[30m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[32m▄[0m[40m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[42m[32m▄[0m[46m[32m▄[0m[46m[32m▄[0m[46m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[42m[36m▄[0m[42m[36m▄[0m[46m[36m▄[0m[40m[32m▄[0m[40m[32m▄[0m[40m[32m▄[0m[40m[32m▄[0m[40m[32m▄[0m[40m[32m▄[0m[40m[32m▄[0m[46m[36m▄[0m[46m[36m▄[0m[40m[36m▄[0m[40m[36m▄[0m[42m[36m▄[0m[42m[36m▄[0m[42m[32m▄[0m[42m[32m▄[0m[40m[32m▄[0m[40m[36m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m[40m[33m▄[0m[40m[33m▄[0m[40m[32m▄[0m[43m[32m▄[0m[43m[32m▄[0m[40m[33m▄[0m[42m[33m▄[0m[42m[33m▄[0m[43m[33m▄[0m[43m[32m▄[0m[43m[33m▄[0m[41m[33m▄[0m[40m[33m▄[0m[40m[32m▄[0m[40m[32m▄[0m[40m[31m▄[0m[40m[32m▄[0m[40m[36m▄[0m[42m[35m▄[0m[46m[36m▄[0m[42m[36m▄[0m[40m[36m▄[0m[40m[32m▄[0m[40m[32m▄[0m[43m[33m▄[0m[43m[33m▄[0m[43m[33m▄[0m
''')
print(f"\033[35mAI-Control for Windows v1.14 - {datetime.datetime.now()} - (AICW) \033[0m")  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AI Control for Windows')
        self.setWindowIcon(QIcon('ailogo.ico'))
        self.processes = {}
        self.app_settings = {'applications': []}
        self.settings_file = 'settings.json'
        self.lang_dir = 'lng'  # Language directory
        self.default_lang_file = 'en.json'  # Default language file
        self.lang_data = {}  # Stores UI and log messages
        self.load_settings()
        self.check_and_prepare_lang_files()
        self.load_language_data()
        self.setup_ui()
        self.app_status_last_state = {}
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_apps_status)
        
        QApplication.instance().aboutToQuit.connect(self.cleanup_before_exit)

    def initialize_app_buttons(self):
        """Initializes application buttons based on the loaded settings."""
        for app in self.app_settings.get('applications', []):
            self.add_app_button(app['name'], app['path'], app['port'])
        
    def check_and_prepare_lang_files(self):
        """Checks if the language directory and default language file exist, creates them if not."""
        if not os.path.exists(self.lang_dir):
            os.makedirs(self.lang_dir)
        default_lang_path = os.path.join(self.lang_dir, self.default_lang_file)
        if not os.path.isfile(default_lang_path):
            with open(default_lang_path, 'w') as file:
                # Initializing with default UI and log messages, including a default array of values
                json.dump({
                    "ui_messages": {
                        "add_app": "Add Application",
                        "select_batch": "Select .bat file",
                        "app_name": "Application Name",
                        "enter_app_name": "Enter application name:",
                        "app_port": "Application Port",
                        "enter_port": "Enter local port for application:",
                        "confirm_stop_title": "Confirm Application Stop",
                        "confirm_stop_message": "Are you sure you want to stop this application?",
                        "open_ui": "Open UI"
                    },
                    "log_messages": {
                        "app_started": "Starting application: {app_name}",
                        "app_terminated": "Terminating application: {app_name}",
                        "app_running_on_port": "Application {app_name} is running on port {port}.",
                        "app_running_port_not_available": "Application {app_name} is running, but port {port} is not available.",
                        "cleanup_before_exit": "Terminating all applications and stopping the timer...",
                        "app_action_completed": "Initialization completed.",
                        "settings_file_not_found": "Configuration file not found, creating a new one."
                    }
                }, file, indent=4)

    def add_app_button(self, app_name, file_name, port):
        button_container = QWidget()
        button_layout = QHBoxLayout()
        button_container.setLayout(button_layout)

        app_button = QPushButton(app_name)
        app_button.clicked.connect(lambda: self.toggle_application(app_name, file_name, port, app_button))
        button_layout.addWidget(app_button)

        open_ui_button = QPushButton(self.lang_data["ui_messages"]["open_ui"])
        open_ui_button.setStyleSheet("background-color: lightblue;")
        open_ui_button.setEnabled(False)  # Tlačítko bude inicializováno jako neaktivní
        open_ui_button.clicked.connect(lambda: self.open_application_ui(port))
        button_layout.addWidget(open_ui_button)

        self.layout.addWidget(button_container)
        self.processes[app_name] = {'process': None, 'port': port, 'button': app_button, 'ui_button': open_ui_button}

    def check_timer_necessity(self, starting=True):
        """Starts or stops the timer based on whether any applications are running."""
        active_processes = any(info['process'] is not None and info['process'].state() == QProcess.Running for info in self.processes.values())
        
        if starting and active_processes and not self.timer.isActive():
            self.timer.start(4000)  # Například každých 4000 milisekund
        elif not starting and not active_processes and self.timer.isActive():
            self.timer.stop()

    def check_timer_necessity(self, starting=True):
        active_processes = [info for info in self.processes.values() if info['process'] and info['process'].state() == QProcess.Running]
        if starting and active_processes:
            if not self.timer.isActive():
                self.timer.start(4000)  # Například každé 4 sekundy
        elif not starting and not active_processes:
            if self.timer.isActive():
                self.timer.stop()

    def is_port_open(self, port):
        """Checks if a given port is open."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Nastaví timeout pro testování portu
            result = sock.connect_ex(('127.0.0.1', port))
            return result == 0

    def open_application_ui(self, port):
        """Otevře webový prohlížeč na lokální adrese aplikace."""
        url = QUrl(f"http://127.0.0.1:{port}")
        QDesktopServices.openUrl(url)

    def load_language_data(self):
        """Loads the UI and log messages from the default language file."""
        default_lang_path = os.path.join(self.lang_dir, self.default_lang_file)
        try:
            with open(default_lang_path, 'r') as file:
                self.lang_data = json.load(file)
        except FileNotFoundError:
            print(f"\033[35m(AICW) {datetime.datetime.now()} - " + self.lang_data["log_messages"]["language_file_not_found"] + f"\033[0m")
            self.check_and_prepare_lang_files()

    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.menu = self.menuBar().addMenu("&Menu")
        self.add_action = QAction(self.lang_data.get("ui_messages", {}).get("add_app", "Add Application"), self)

        self.add_action.triggered.connect(self.add_application)
        self.menu.addAction(self.add_action)
        
        self.initialize_app_buttons()
    # Přidání aplikace, přidání tlačítka aplikace, a další metody zůstanou většinou stejné
    # Změny budou v logovacích zprávách a textech UI tlačítek
    
    def add_application(self):
        file_name, _ = QFileDialog.getOpenFileName(self, self.lang_data.get("ui_messages", {}).get("select_batch", "Select .bat file"), "", "Batch files (*.bat)")
        if file_name:
            app_name, ok_name = QInputDialog.getText(self, self.lang_data.get("ui_messages", {}).get("app_name", "Application Name"), self.lang_data.get("ui_messages", {}).get("enter_app_name", "Enter application name:"))
            port, ok_port = QInputDialog.getInt(self, self.lang_data.get("ui_messages", {}).get("app_port", "Application Port"), self.lang_data.get("ui_messages", {}).get("enter_port", "Enter local port for application:"))
            if ok_name and app_name and ok_port:
                self.app_settings['applications'].append({'name': app_name, 'path': file_name, 'port': port})
                self.save_settings()
                self.add_app_button(app_name, file_name, port)

    def toggle_application(self, app_name, file_name, port, app_button):
        process_info = self.processes[app_name]

        app_button.setEnabled(False)
        app_button.setStyleSheet("background-color: yellow;")

        if process_info['process'] is None or process_info['process'].state() == QProcess.NotRunning:
            print(f"\033[35m(AICW) {datetime.datetime.now()} - " + self.lang_data["log_messages"]["app_started"].format(app_name=app_name) + f"\033[0m")

            process = QProcess(self)
            process.readyReadStandardOutput.connect(lambda: self.read_output(process))
            process.readyReadStandardError.connect(lambda: self.read_error(process))

            process.setWorkingDirectory(QDir().absoluteFilePath(file_name).replace('/' + file_name.split('/')[-1], ''))
            process.start(file_name)

            self.processes[app_name]['process'] = process
            app_button.setStyleSheet("background-color: orange;")

            self.check_timer_necessity(starting=True)
        else:
            app_button.setStyleSheet("background-color: red;")
            
            self.kill_application_process(port)
            process_info['process'].terminate()
            print(f"\033[35m(AICW) {datetime.datetime.now()} - " + self.lang_data["log_messages"]["app_terminated"].format(app_name=app_name) + f"\033[0m")
            self.kill_application_process(port)
            process_info['process'] = None
            app_button.setStyleSheet("")  # Reset button appearance
            process_info['ui_button'].setEnabled(False)
            process_info['button'].setEnabled(True)
            self.check_timer_necessity(starting=False)
            
    # Metody check_apps_status, is_port_open, open_application_ui, a další pomocné metody zůstanou beze změn
    # Klíčové je, že všechny textové řetězce a zprávy budou nahrazeny hodnotami z jazykového souboru

    def save_settings(self):
        """Updates settings.json with the path to the used language file."""
        self.app_settings['lang_file'] = os.path.join(self.lang_dir, self.default_lang_file)  # Adding path to lang file
        with open(self.settings_file, 'w') as file:
            json.dump(self.app_settings, file, indent=4)

    def read_output(self, process):
        output = process.readAllStandardOutput()
        print(f"{datetime.datetime.now()} - " + output.data().decode('utf-8', errors='ignore'))

    def read_error(self, process):
        error = process.readAllStandardError()
        print(f"\033[35m(AICW) {datetime.datetime.now()} - " + error.data().decode('utf-8', errors='ignore') + f"\033[0m")

    def kill_application_process(self, port):
        """Ukončí procesy naslouchající na zadaném portu, kromě procesů s PID 0."""
        for proc in psutil.process_iter(attrs=['pid', 'connections']):
            try:
                for conn in proc.info['connections']:
                    if conn.laddr.port == port and proc.pid != 0:
                        proc.terminate()  # Ukončení pomocí terminate místo os.kill
                        proc.wait()  # Čeká, až proces skončí
                        break
            except psutil.AccessDenied:
                print(f"\033[35m(AICW) Access denied when trying to terminate process {proc.pid}. Skipping..." + f"\033[0m")
            except Exception as e:
                print(f"\033[35m(AICW) An error occurred when trying to terminate process {proc.pid}: {e}" + f"\033[0m")

    def check_apps_status(self):
        """Checks the status of applications and updates the UI accordingly."""
        for app_name, process_info in self.processes.items():
            if process_info['process'] is not None and process_info['process'].state() == QProcess.Running:
                is_port_open = self.is_port_open(process_info['port'])
                status_message = self.lang_data.get("log_messages", {}).get("app_running_on_port", "Application {app_name} is running on port {port}.") if is_port_open else self.lang_data.get("log_messages", {}).get("app_running_port_not_available", "Application {app_name} is running, but port {port} is not available.")
                status_message = status_message.format(app_name=app_name, port=process_info['port'])
                
                if self.app_status_last_state.get(app_name, None) != is_port_open:
                    print(f"\033[35m(AICW) {datetime.datetime.now()} - " + status_message + f"\033[0m")
                    self.app_status_last_state[app_name] = is_port_open
                
                process_info['button'].setStyleSheet("background-color: green;" if is_port_open else "background-color: yellow;")
                process_info['ui_button'].setEnabled(is_port_open)
                process_info['button'].setEnabled(True) if is_port_open else process_info['button'].setEnabled(False)
            else:
                process_info['button'].setStyleSheet("")
                process_info['button'].setEnabled(True)
                process_info['ui_button'].setEnabled(False)
                if app_name in self.app_status_last_state:
                    del self.app_status_last_state[app_name]

    def cleanup_before_exit(self):
        """Cleans up running applications and stops the timer before exiting."""
        print(f"\033[35m(AICW) {datetime.datetime.now()} - " + self.lang_data["log_messages"]["cleanup_before_exit"] + f"\033[0m")
        if self.timer.isActive():
            self.timer.stop()
        for app_name, process_info in self.processes.items():
            if process_info['process'] is not None:
                process = process_info['process']
                if process.state() == QProcess.Running:
                    process.terminate()
                    if not process.waitForFinished(6000):  # Čeká 10 sekund
                        process.kill()  # Pokud proces nekončí, zabije ho
                    
    def load_settings(self):
        """Loads the application settings from settings.json, creating a new one if necessary."""
        try:
            with open(self.settings_file, 'r') as file:
                self.app_settings = json.load(file)
        except FileNotFoundError:
            print(f"\033[35m(AICW) {datetime.datetime.now()} - " + self.lang_data.get("log_messages", {}).get("settings_file_not_found", "Configuration file not found, creating a new one.") + f"\033[0m")
            self.app_settings = {'applications': []}
            self.save_settings()

# Running the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
