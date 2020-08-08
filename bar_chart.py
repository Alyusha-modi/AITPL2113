import numpy as np
from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
ages_x=[25,26,27,28,29,30,31,32,33,34,35]
x_indexes=np.arange(len(ages_x))
width=0.25
dev_y=[38496,42000,46757,49562,53232,56584,62125,64253,67125,68611,73556]
plt.bar(x_indexes-width, dev_y,width=width,color="#444444",linestyle="--", label="All dev")
py_dev_y=[43454,48659,53154,57845,63925,65124,70003,70000,71458,75469,83565]
plt.bar(x_indexes, py_dev_y,width=width,color="#5a7d9a",linewidth=3,label="python dev")
js_dev_y=[37845,43562,46987,49564,53624,56421,62452,66674,68745,68746,74568]
plt.bar(x_indexes+width,js_dev_y,width=width,color="#adad3b",linewidth=3,label="javascript")
plt.legend()
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")

plt.xticks(ticks=x_indexes,label=ages_x)
plt.tight_layout()

plt.show()
