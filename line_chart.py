from matplotlib import pyplot as plt
#print(plt.style.available)
#plt.style.use('fivethirtyeight')
plt.xkcd()
ages_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[38496,42000,46757,49562,53232,56584,62125,64253,67125,68611,73556]
plt.plot(ages_x,dev_y,color="#444444",linestyle="--", label="All dev")
py_dev_y=[43454,48659,53154,57845,63925,65124,70003,70000,71458,75469,83565]
plt.plot(ages_x,py_dev_y,color="#5a7d9a",linewidth=3,label="python dev")
js_dev_y=[37845,43562,46987,49564,53624,56421,62452,66674,68745,68746,74568]
plt.plot(ages_x,js_dev_y,color="#adad3b",linewidth=3,label="javascript")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by Age")
plt.legend()
#plt.grid(True)
plt.tight_layout()
plt.savefig("line.png")
plt.show()
