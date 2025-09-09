from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from app.main_window import MainWindow


def main() -> int:

	app = QApplication(sys.argv)
	app.setApplicationName("PyQt6 Starter")

	window = MainWindow()
	window.show()

	return app.exec()


if __name__ == "__main__":
	sys.exit(main())

