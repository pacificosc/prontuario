from __future__ import annotations

from PyQt6.QtCore import QSize, pyqtSlot
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
	QLabel,
	QMainWindow,
	QPushButton,
	QStatusBar,
	QToolBar,
	QVBoxLayout,
	QWidget,
)


class MainWindow(QMainWindow):
	"""Main application window with a simple label and button."""

	def __init__(self) -> None:
		super().__init__()
		self.setWindowTitle("PyQt6 Starter")
		self.resize(800, 500)

		central_widget = QWidget(self)
		layout = QVBoxLayout(central_widget)

		self.message_label = QLabel("Hello, PyQt6!", parent=central_widget)
		self.primary_button = QPushButton("Click me", parent=central_widget)
		self.primary_button.clicked.connect(self.on_primary_button_clicked)

		layout.addWidget(self.message_label)
		layout.addWidget(self.primary_button)
		self.setCentralWidget(central_widget)

		# Toolbar
		toolbar = QToolBar("Main Toolbar", self)
		toolbar.setIconSize(QSize(16, 16))
		self.addToolBar(toolbar)

		action_quit = QAction("Quit", self)
		action_quit.setStatusTip("Exit application")
		action_quit.triggered.connect(self.close)
		toolbar.addAction(action_quit)

		# Status bar
		status_bar = QStatusBar(self)
		self.setStatusBar(status_bar)
		status_bar.showMessage("Ready")

	@pyqtSlot()
	def on_primary_button_clicked(self) -> None:
		self.message_label.setText("Clicked!")

