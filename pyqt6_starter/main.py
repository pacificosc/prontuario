from __future__ import annotations

import sys
import threading
import time
import urllib.error
import urllib.request

from PyQt6.QtWidgets import QApplication

from app.main_window import MainWindow
from app.server import create_app


def _run_flask_app(host: str = "127.0.0.1", port: int = 5000) -> None:
	flask_app = create_app()
	flask_app.run(host=host, port=port, debug=False, use_reloader=False)


def _wait_for_server(url: str, timeout_seconds: float = 10.0) -> bool:
	deadline = time.time() + timeout_seconds
	while time.time() < deadline:
		try:
			with urllib.request.urlopen(url, timeout=1.5) as response:  # nosec B310
				if response.status == 200:
					return True
		except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
			pass
		time.sleep(0.2)
	return False


def main() -> int:
	# Start Flask server in background thread
	server_thread = threading.Thread(target=_run_flask_app, kwargs={"host": "127.0.0.1", "port": 5000}, daemon=True)
	server_thread.start()

	# Wait for server readiness
	server_ready = _wait_for_server("http://127.0.0.1:5000/", timeout_seconds=12.0)

	qt_app = QApplication(sys.argv)
	qt_app.setApplicationName("PyQt6 Starter")

	window = MainWindow()
	if server_ready:
		window.load_url("http://127.0.0.1:5000/")
	else:
		window.load_url("about:blank")
	window.show()

	return qt_app.exec()


if __name__ == "__main__":
	sys.exit(main())

