# -*- coding: utf-8 -*-

from logging import Handler
from portalocker import unlock
from cloghandler import ConcurrentRotatingFileHandler

class RotatingFileHandler(ConcurrentRotatingFileHandler):
  def release(self):
    try:
      self.stream.flush()
      if self._rotateFailed:
        self.stream.close()
    except Exception:
      # suppress annoyed exception
      pass
    finally:
      try:
        unlock(self.stream_lock)
      finally:
        # release thread lock
        Handler.release(self)
