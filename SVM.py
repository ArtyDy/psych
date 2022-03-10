#%% SVM
from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =pd.read_excel('../../../03_03_22_analysis.xlsx')
df.reset_index()
TPVDN=np.asarray(df['TPVDN'][:41])
TPVUN=np.asarray(df['TPVUN'][:41])

clf=svm.SVC(kernel="linear")

clf.fit([TPVDN, TPVUN], [0, 1])
# %%
ax=plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)
plt.scatter(TPVDN,TPVUN)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
ax.contour(
    XX, YY, Z, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"]
)
plt.show()
# %%
