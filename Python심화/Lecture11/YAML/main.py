import yaml

with open("yaml/test.yaml", "r") as fd:
    data = yaml.load(fd, Loader=yaml.FullLoader)

print(data)


data['수정됨'] = 9999999
data['feeling'] = 'sad'
with open("yaml/output.yaml", "w") as fd:
    data = yaml.dump(data, fd)
