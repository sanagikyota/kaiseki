import matplotlib.pyplot as plt

# データ
values = [79.60526315789474, 76.99115044247787, 96.0, 93.93939393939394]
labels = ['sk402_0.05mM', 'sk402_0.1mM', 'sk402', 'sk398']

# 棒グラフの作成
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='blue', width=0.4)
#plt.xlabel('Sample')
plt.ylabel('Death rate (%)')
plt.title('Death rate 240713')
plt.ylim(0, 100)
#plt.grid(axis='y', linestyle='-', linewidth=0.5)
plt.gca().yaxis.grid(False)
# グラフの保存
plt.savefig("fig_bta_398402_240713", dpi=300)
plt.show()