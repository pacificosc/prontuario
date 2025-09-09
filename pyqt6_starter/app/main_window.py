from __future__ import annotations

from PyQt6.QtCore import QSize, pyqtSlot, QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
	QMainWindow,
	QStatusBar,
	QToolBar,
	QWidget,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
	"""Main window that hosts a QWebEngineView pointing to the local Flask app."""

	def __init__(self) -> None:
		super().__init__()
		self.setWindowTitle("PyQt6 Starter")
		self.resize(800, 500)

		central_widget = QWidget(self)
		self.web_view = QWebEngineView(central_widget)
		self.setCentralWidget(self.web_view)

		# Toolbar
		toolbar = QToolBar("Main Toolbar", self)
		toolbar.setIconSize(QSize(16, 16))
		self.addToolBar(toolbar)

		action_reload = QAction("Reload", self)
		action_reload.setStatusTip("Reload page")
		action_reload.triggered.connect(self.on_reload)
		toolbar.addAction(action_reload)

		action_home = QAction("Home", self)
		action_home.setStatusTip("Go to dashboard")
		action_home.triggered.connect(self.on_home)
		toolbar.addAction(action_home)

		action_quit = QAction("Quit", self)
		action_quit.setStatusTip("Exit application")
		action_quit.triggered.connect(self.close)
		toolbar.addAction(action_quit)

		# Status bar
		status_bar = QStatusBar(self)
		self.setStatusBar(status_bar)
		status_bar.showMessage("Ready")

	def load_url(self, url: str) -> None:
		self.web_view.setUrl(QUrl(url))

	@pyqtSlot()
	def on_reload(self) -> None:
		self.web_view.reload()

	@pyqtSlot()
	def on_home(self) -> None:
		self.load_url("http://127.0.0.1:5000/")

