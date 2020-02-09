import numpy as np
from scipy import stats

#no entry value, outside range
NO = -1

def process(vec):
    out = []
    for i in vec:
        if i != NO:
            out.append(i - stats.tmean(vec, (0, 100)))  # rating range
        else:
            out.append(0)
    return out


def norm_cos_sim(a, b):
    a = process(a)
    b = process(b)
    print(a)
    print(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# NO for no entry
a = [4, 3, 4, NO, NO, 1]
b = [4, 1, 2, 2, NO, 1]
c = [4, NO, NO, 3, 1, NO]

print(norm_cos_sim(a, b))
print(norm_cos_sim(a, c))
