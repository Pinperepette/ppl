## PPL Python Process Launch

**it's a simple utility to do things the way I like to do them ... BAD and rapid**

**Have you ever had to kill a subprocess or a process launched by a script as a daemon?**
**with ppl you do it easy, greep process && kill. the end.**

**for install run:   `python setup.py`**
#### easy example in test folder, run main.py for launch daemon.py and kill it

``` python
#!/usr/bin/env python

""" example file main.py """

from ppl  import start, stop
import time

# start process name processo
processo = start('python demone.py')
""" 
if the script takes parameters, 
processo = start(f'python demone.py {parameters}')
"""
time.sleep(10)

# kill process name processo
stop(processo)
```
