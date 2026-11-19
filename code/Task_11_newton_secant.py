"""BIT 2118 Scientific Computing — Task 11\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np

cashflows = np.array([-10000,3000,3500,4000,2500], dtype=float)
def npv(r):
    return sum(c/(1+r)**t for t,c in enumerate(cashflows))
def dnpv(r):
    return sum(-t*c/(1+r)**(t+1) for t,c in enumerate(cashflows) if t)
r = 0.10
for _ in range(50):
    r -= npv(r)/dnpv(r)
print("Newton-Raphson IRR:", r)
