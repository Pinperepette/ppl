#!/usr/bin/env python

from ppl  import start, stop
import time

processo = start('python demone.py')
time.sleep(10)

stop(processo)
