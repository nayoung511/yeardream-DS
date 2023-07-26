import pickle

with open("test.pk1", "rb") as fd:
    obj = pickle.load(fd)

print(obj)