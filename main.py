from pet import Pet

# Create pet object
my_pet = Pet("Buddy", "Golden Retriever", "Playful")

print(f"\n🎉 Welcome your new pet: {my_pet}\n")
my_pet.get_status()

# Interactions
my_pet.eat()
my_pet.sleep()
my_pet.play()
my_pet.train("roll over")
my_pet.train("fetch")
my_pet.train("fetch")  # Try teaching again
my_pet.show_tricks()

# Check status again
print()
my_pet.get_status()
