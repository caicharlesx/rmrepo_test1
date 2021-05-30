X_centered = X - X.mean(axis=0)
U, s, V = np.linalg.svd(X_centered)
c1=V.T[:,0]
c2=V.T[:,1]

