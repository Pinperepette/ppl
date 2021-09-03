<p align="center">
  <a href="" rel="noopener">
</p>
<h3 align="center">PPL Python Process Launch</h3>
<div align="center">
</div>

## 🧐 About <a name = "about"></a>
**it's a simple utility to do things the way I like to do them ... BAD and rapid**

**Have you ever had to kill a subprocess or a process launched by a script as a daemon?**
**with ppl you do it easy, greep process && kill. the end.**
## 🏁 Getting Started <a name = "getting_started"></a>

### Installing
`python setup.py`

## 🔧 Running the tests <a name = "tests"></a>
`python main.py`

## 🎈 Usage <a name="usage"></a>
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
