
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

features = np.load("dataset/features/features.npy")
labels = np.load("dataset/labels/labels.npy")

pca = PCA(n_components=2)
projected = pca.fit_transform(features)

plt.figure(figsize=(8, 6))
for label_value, color, label_name in zip([0, 1], ['green', 'red'], ['Alert', 'Drowsy']):
    idx = (labels == label_value)
    plt.scatter(projected[idx, 0], projected[idx, 1],
                c=color, label=label_name, s=50, alpha=0.7)

plt.title("PCA of Collected Features")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("dataset/pca_feature_plot_fixed.png")
plt.show()
