# run tests using doctest
import doctest

# filters folder
from rawls import scene
from rawls import rawls
from rawls import stats
from rawls import utils

print("==============================")
print("Runs test command...")

# pass test using doctest
doctest.testmod(scene)
doctest.testmod(rawls)
doctest.testmod(stats)
doctest.testmod(utils)