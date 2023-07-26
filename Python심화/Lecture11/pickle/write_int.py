import pickle

with open("test_int.pkl", "rb") as fd:
    out = pickle.load(fd)

print(out)