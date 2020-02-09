import numpy as np
from scipy import stats

def process(vec):
    out = []
    for i in vec:
        if i != -1:
            out.append(i - stats.tmean(vec, (0, 100))) # rating range
        else:
            out.append(0)
    return out


def norm_cos_sim(a, b):
    a = process(a)
    b = process(b)
    print(a)
    print(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# value outside range for no entry
a = [4, 3, 4, -1, -1, 1]
b = [4, 1, 2, 2, -1, 1]
c = [4, -1, -1, 3, 1, -1]

print(norm_cos_sim(a, b))
print(norm_cos_sim(a, c))
