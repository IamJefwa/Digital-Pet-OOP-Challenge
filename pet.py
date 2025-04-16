class Pet:
    def __init__(self, name, breed="Unknown", personality="Friendly"):
        self.name = name
        self.breed = breed
        self.personality = personality
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.health = 10
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} 🍗 ate and feels happier!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} 💤 took a nap and is recharged!")

    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play. 🥱 Let them rest!")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} 🐾 played and had a great time!")

    def train(self, trick):
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}!")
        else:
            self.tricks.append(trick)
            print(f"{self.name} 🧠 learned a new trick: {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet. 😢")
        else:
            tricks_str = ', '.join(self.tricks)
            print(f"{self.name} knows: {tricks_str} 🐶")

    def get_mood(self):
        if self.happiness >= 8:
            return "😊 Happy"
        elif self.happiness >= 5:
            return "😌 Content"
        elif self.happiness >= 3:
            return "😟 Sad"
        else:
            return "😢 Depressed"

    def check_health(self):
        if self.hunger >= 9:
            self.health = max(0, self.health - 2)
        if self.energy <= 1:
            self.health = max(0, self.health - 1)

    def get_status(self):
        self.check_health()
        print(f"--- 🐾 {self.name}'s Status ---")
        print(f"Breed      : {self.breed}")
        print(f"Personality: {self.personality}")
        print(f"Hunger     : {self.hunger}/10")
        print(f"Energy     : {self.energy}/10")
        print(f"Happiness  : {self.happiness}/10")
        print(f"Health     : {self.health}/10")
        print(f"Mood       : {self.get_mood()}")
        print("-------------------------------")

    def __str__(self):
        return f"{self.name} the {self.breed} ({self.personality})"
