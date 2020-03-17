# -*- coding: utf-8 -*-
"""py_util.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ajason08/py_util/blob/master/py_util.ipynb
"""

import time
class stopwatch:
  def __init__(self):
    self._started = time.time()
    self._last_started = self._started
    self._laps = []
    self._totaltime = "please call stop() first!"    

  def _humanizetime(self,elapsed_time):
    mins = int(elapsed_time / 60)
    secs = int(elapsed_time - (mins * 60))
    return f'Time: {mins}m {secs}s'    

  def stop(self, verbose=True):
    stoptimer = time.time()
    elapsed_time = stoptimer - self._started
    self._totaltime = self._humanizetime(elapsed_time)
    
    # calculating lap time
    elapsed_time = stoptimer - self._last_started    
    lap = self._humanizetime(elapsed_time)
    self._laps.append(lap)    
    if verbose: print(lap)        
    self._last_started = time.time()

  # read-only properties
  @property
  def laps(self):
   return self._laps
  @property
  def totaltime(self):
   return self._totaltime

def testing_stopwatch():
  mywatch = stopwatch()
  time.sleep(2)
  mywatch.stop()
  print(mywatch.laps)
  time.sleep(3)
  mywatch.stop()
  print(mywatch.laps)
  print(mywatch.totaltime)