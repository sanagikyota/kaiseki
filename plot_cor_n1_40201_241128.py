import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import seaborn as sns

def multiply_by_100(data):
    return [x * 100 for x in data]

sns.set()
c = multiply_by_100([0.05, 0.07083333333333333, 0.7593360995850622, 0.7876106194690266, 0.6636771300448431, 0.5061224489795918])
f = multiply_by_100([0.04950495, 0.223404255, 0.984924623, 1, 1, 1])

# c2 = multiply_by_100([0.05, 0.2708333333333333, 0.4811320754716981, 0.5878378378378378, 0.9880239520958084, 0.9739130434782609])
# f2 = multiply_by_100([0, 0.113924051, 0.231404959, 0.6328125, 1, 1])
# c3 = multiply_by_100([0.05, 0.125, 0.47244094488188976, 0.5328467153284672, 0.9338842975206612, 0.9435483870967742])
# f3 = multiply_by_100([0, 0.162011173, 0.380165289, 0.624113475, 1, 1])

fig, ax = plt.subplots(figsize=(6,6))

# グラフを描画
# ax.scatter(c, f, marker='o')

ax.scatter(c[0],f[0],color = 'cyan', label = '0%')
# ax.scatter(c2[0],f2[0],color = 'cyan')
# ax.scatter(c3[0],f3[0],color = 'cyan')
ax.scatter(c[1],f[1],color = 'deepskyblue', label = '0.7%')
# ax.scatter(c2[1],f2[1],color = 'deepskyblue')
# ax.scatter(c3[1],f3[1],color = 'deepskyblue')
ax.scatter(c[2],f[2],color = 'dodgerblue', label = '1.0%')
# ax.scatter(c2[2],f2[2],color = 'dodgerblue')
# ax.scatter(c3[2],f3[2],color = 'dodgerblue')
ax.scatter(c[3],f[3],color = 'mediumslateblue', label = '1.3%')
# ax.scatter(c2[3],f2[3],color = 'mediumslateblue')
# ax.scatter(c3[3],f3[3],color = 'mediumslateblue')
ax.scatter(c[4],f[4],color = 'slateblue', label = '1.5%')
# ax.scatter(c2[4],f2[4],color = 'slateblue')
# ax.scatter(c3[4],f3[4],color = 'slateblue')
ax.scatter(c[5],f[5],color = 'darkviolet', label = '1.8%')
# ax.scatter(c2[5],f2[5],color = 'darkviolet')
# ax.scatter(c3[5],f3[5],color = 'darkviolet')

ax.grid(True)

ax.set_xlabel('formation rate(%)')
ax.set_ylabel('dead cell rate(%)')
ax.set_ylim(-5,105)
ax.set_xlim(-5,105)

slope, _ = np.polyfit(c, f, 1)

line_of_best_fit = slope * np.array(c)

correlation_coefficient, _ = pearsonr(c, f)
fit_equation = f'f(x) = {slope:.4f} * x'
fit_equation_f = f'{fit_equation}\n(R²= {correlation_coefficient:.4f})'

x = np.linspace(0, 100, 100)
ax.plot(x, x, color='black', linestyle='--', linewidth=0.8, label='x = y')

ax.plot(c, line_of_best_fit, color='black', linewidth=0.1, label=fit_equation_f)
ax.legend(loc='lower right', fontsize='8')
fig.savefig("fig_bta_cor_40201_241128_2.png")

plt.show()