# https://matplotlib.org/stable/api/pyplot_summary.htmlimport 
import matplotlib.pyplot as plt

# x=["Baby","Toddler", "Teen", "Adult"]
# y=[10,15,18,5]

# plt.xlabel("Age")
# plt.ylabel("Score")

# plt.bar(x,y, color=["m", "g","r","b"])
# plt.plot(x,y)

# plt.show()
# -------------------------------------------------------------------

# x = ("Lithuania", "Romania", "Poland", "Bangladesh","Brazil","Colombia", "Others")

# data=[2,17,1,2,2,2,6]
# plt.pie(data,labels=x, explode=[0.03,0.05,0.03,0.03,0.03,0.03,0.03])
# plt.show()
# ----------------------------------------------------------

fig, axes = plt.subplots(2,2)

x=["Lithuania", "Romania", "Poland", "Bangladesh","Brazil","Colombia", "Others"]
y=[2,17,1,2,2,2,6]
y2=[14,12,5,6,8,26,14]
y3=[32,45,23,45,15,36,12]

axes[0,0].bar(x,y)
axes[0,1].plot(x,y2)
axes[1,1].pie(y3,labels=x)

plt.tight_layout()
plt.show()

