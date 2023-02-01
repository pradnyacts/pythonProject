#approach1
# import sys
# sys.path.append("C:/Users/pradn/PycharmProjects/pythonProject/day 8/package1")
# sys.path.append("C:/Users/pradn/PycharmProjects/pythonProject/day 8/package1/package2")
# import mod1
# import mod2
# mod1.display()
# mod2.show()

#approach2
import sys
sys.path.append("C:/Users/pradn/PycharmProjects/pythonProject/day 8/package1")
sys.path.append("C:/Users/pradn/PycharmProjects/pythonProject/day 8/package1/package2")
from mod1 import *
from mod2 import *
display()
show()