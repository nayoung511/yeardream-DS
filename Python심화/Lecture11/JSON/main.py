import json

obj = {
    "ID" : 3,
    "소지물" : [
        "휴대폰",
        4e-3,
        12468285,
        None,
        []
    ]
}


with open("output.json", "w") as fd:
    json.dump(obj, fd)