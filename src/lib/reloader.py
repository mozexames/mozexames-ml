import os
import sys
import subprocess

class Reloader(object):
  RELOADING_CODE = 3

  def start_process(self):
    """
    Spawn a new Python interpreter with the same arguments as this one,
    but running the reloader thread.
    """
    while True:
      print('Starting ...')

      args = [sys.executable] + sys.argv
      env = os.environ.copy()
      env['TKINTER_MAIN'] = 'true'

      exit_code = subprocess.call(args, env=env, close_fds=False)
      if exit_code != self.RELOADING_CODE:
        return exit_code

  def trigger_reload(self):
    print('Reloading ...')
    sys.exit(self.RELOADING_CODE)


def run_with_reloader(root, *hotkeys):
  """
  Run the given application in an independent python interpreter
  to allow for reloading using `Reloader`.
  """
  import signal
  signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
  reloader = Reloader()
  try:
    if os.environ.get('TKINTER_MAIN') == 'true':
      # Reload a TKinter environment
      for hotkey in hotkeys:
        root.bind_all(hotkey, lambda event: reloader.trigger_reload())

      root.mainloop()
    else:
      sys.exit(reloader.start_process())
  except KeyboardInterrupt:
    pass
