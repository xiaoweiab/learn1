#   @author: 马朝威 1570858572@qq.com
#   @time: 2019-02-27 0:56

from sklearn import datasets
from sklearn import svm
from joblin

def frist_start():
    digits = datasets.load_digits()
    # print(digits.target)
    clf = svm.SVC(C=100., gamma=0.001)
    clf.fit(digits.data[:-1], digits.target[:-1])
    print(clf)
    print(type(clf))
    print(clf.predict(digits.data[:-1]))


def model_persistence():
    clf = svm.SVC(gamma='scale')
    iris = datasets.load_iris()
    x, y = iris.data, iris.target
    print(clf.fit(x, y))


def main():
    # frist_start()
    model_persistence()


if __name__ == "__main__":
    main()









