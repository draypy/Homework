# Task 4.7*
# Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
# Try to change x to a list `[1,2,3]`. Explain the result.
# Try to change import to `from x import *` where x - module names. Explain the result.

"""
1.This code worked because the modules are found in the same directory.
In mod_c, the variable x = 5 was assigned import mod_b is ignored.
If they were in different directories, you would have to specify PythonPATH

2.
import mod_c
import mod_b
>>> 5

# import mod_c
import mod_b
>>> [1, 2, 3]

This is due to the fact that the variable mod_c was registered in mod_c. x = 5

3.
from mod_c import *
from mod_b import *

print(x)
>>> [1, 2, 3]
print(mod_c.x)
>>> [5]
two different variables
however, if we declare variables x in both modules
the variable x will be imported from the last import
from mod_b import * # 5
from mod_c import * # [1, 2, 3]
>>> [1, 2, 3]
from mod_c import *
from mod_d import *
>>> 5

 """

