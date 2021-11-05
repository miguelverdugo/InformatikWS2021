import sys
import numpy as np
"""
args = sys.argv

s = int(args[1]) + int(args[2]) + int(args[3])

print(args)
print("Summe:", s)
"""

print("Summe:", sum(np.array(sys.argv[1:]).astype(int)))
