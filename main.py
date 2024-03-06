twd_characters = ["Rick Grimes", "Daryl Dixon", "Michonne"]

for i in twd_characters:
    print(i, "\n")




twd_dict = [{'Character': i} for i in twd_characters]


for i in twd_dict:
    print(i)    


class Character:

    def __init__(self, name, hp, resolve) -> None:
        self.name = name
        self.hp = int(hp)
        self.resolve = int(resolve)

    def callout(self, target):
        print("Hey, you!")
        target.resolve += 100

        

rick = Character("Rick Grimes", 100, 1000)
michonne = Character("Michonne", 100, 1000)
rick.callout(michonne)
print(michonne.resolve)