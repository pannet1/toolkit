import logging
import logging.handlers
import queue
import atexit
import sys
from typing import Any
import os


class AsyncLogger:

    def __init__(self, level=logging.INFO, log_file: Any = None, use_journal: bool = True, show: bool = True):
        self._level = level
        self._log_file_path = log_file
        self._use_journal = use_journal
        self._show = show
        self._listener = None
        self._log_queue = queue.Queue(-1)

        self._formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - **%(name)s** - %(threadName)s - %(message)s"
        )

    def _log(self, msg: str) -> None:
        if self._show:
            print(msg)

    def start(self):
        if self._listener is not None:
            self._log("Async logging system is already running.")
            return

        slow_handlers = []

        if self._use_journal and os.path.exists('/dev/log'):
            try:
                journal_handler = logging.handlers.SysLogHandler(address='/dev/log')
                journal_handler.setFormatter(self._formatter)
                slow_handlers.append(journal_handler)
                self._log("Async logging enabled, outputting to systemd journal.")
            except Exception as e:
                self._log(f"Could not connect to systemd journal: {e}")

        if self._log_file_path:
            file_handler = logging.handlers.RotatingFileHandler(
                self._log_file_path, maxBytes=10 * 1024 * 1024, backupCount=5
            )
            file_handler.setFormatter(self._formatter)
            file_handler.setLevel(self._level)
            slow_handlers.append(file_handler)
            self._log(f"Async logging enabled, outputting to: {self._log_file_path}")

        if self._show and not self._log_file_path:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(self._formatter)
            slow_handlers.append(console_handler)
            self._log("Async logging enabled, outputting to console.")

        self._listener = logging.handlers.QueueListener(self._log_queue, *slow_handlers)
        self._listener.start()
        atexit.register(self.stop)

        root_logger = logging.getLogger()
        root_logger.setLevel(self._level)

        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)

        queue_handler = logging.handlers.QueueHandler(self._log_queue)
        root_logger.addHandler(queue_handler)

    def stop(self):
        if self._listener:
            self._listener.stop()
            self._listener = None
            self._log("\nAsync logger stopped and all logs flushed.")

    def get_logger_function(self):
        return logging.getLogger
