from collections import defaultdict

text = "asgaasdjfhajehfjsndfjknwajefnjankdg"

character = {}

for char in text:
    # char이 있으면 가져오고 없으면 None
    count = character.get(char, None)

    if count is None:
        character[char] = 0

    character[char] += 1

print(character)


#-----------------------------
text = "asgaasdjfhajehfjsndfjknwajefnjankdg"

character = defaultdict(int)

for char in text:
    character[char] += 1

print(character)
