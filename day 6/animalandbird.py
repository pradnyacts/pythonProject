#approach 1
# import Animal
# import bird
# Animal.fly()
# Animal.color()
# bird.fly()
# bird.color()

#approach2
from Animal import *
from bird import *             #same name functions will be called from latest imported module
fly()
color()
# to mitigate this issue refer below
from Animal import *
color()
fly()
from bird import *
color()
fly()
