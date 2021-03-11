from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

cancer = load_breast_cancer()
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data, cancer.target, random_state=0)
svc = SVC()
#χωρις κανονικοποιηση
print("Before Normalization:")
svc.fit(X_train,Y_train)
print("Accuracy on train set: {:.2f}".format(svc.score(X_train, Y_train)))
print("Accuracy on test set: {:.2f}".format(svc.score(X_test, Y_test)))
#με κανονικοποιηση
min_on_training = X_train.min(axis=0)
range_on_training = (X_train - min_on_training).max(axis=0)
X_train_scaled = (X_train - min_on_training) / range_on_training
X_test_scaled = (X_test - min_on_training) / range_on_training
svc = SVC()
print("After Normalization:")
svc.fit(X_train_scaled,Y_train)
print("New Accuracy on train set: {:.3f}".format(svc.score(X_train_scaled, Y_train)))
print("New Accuracy on test set: {:.3f}".format(svc.score(X_test_scaled,Y_test)))



