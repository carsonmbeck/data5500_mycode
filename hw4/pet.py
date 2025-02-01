# Pet.py



class Pet:
    species = "Unknown"

    # Class variable: Dictionary mapping species to their average lifespans.
    lifespans = {
        "dog": 13,
        "cat": 15,
        "parrot": 50
    }
    
    # Class variable: Dictionary mapping species to a conversion factor for calculating human years.
    # (For example, 1 dog year is roughly equivalent to 7 human years.)
    conversion_factors = {
        "dog": 7,
        "cat": 6,
        "parrot": 5
    }

    def __init__(self, name, age, species):
        # Prompt: "Should I assign species as an instance attribute even if there's a class variable?"
        # ChatGPT response: "Yes, assign species as an instance attribute so that each Pet can have its own species,
        # even though a default is defined at the class level."
        self.name = name
        self.age = age
        self.species = species

    def calculate_human_years(self):
        # Prompt: "How can I convert the pet's age into equivalent human years using a species-specific factor?"
        # ChatGPT response: "Retrieve the conversion factor from the conversion_factors dictionary.
        # Use a default factor (e.g., 7) if the species is not found."
        factor = Pet.conversion_factors.get(self.species.lower(), 7)
        return self.age * factor

    @classmethod
    def get_average_lifespan(cls, species):
        # Prompt: "How do I implement a method that returns the average lifespan for a given species?"
        # ChatGPT response: "Use the lifespans dictionary. Look up the species (in lowercase) and return the lifespan,
        # or return 'Unknown' if the species isn't in the dictionary."
        return cls.lifespans.get(species.lower(), "Unknown")

# Prompt: "Instantiate three Pet objects with different names, ages, and species.
# Then, calculate and print each pet's human-equivalent age and the average lifespan for their species."
if __name__ == '__main__':
    pet1 = Pet("Buddy", 5, "dog")
    pet2 = Pet("Whiskers", 3, "cat")
    pet3 = Pet("Polly", 2, "parrot")

    pets = [pet1, pet2, pet3]

    for pet in pets:
        human_age = pet.calculate_human_years()
        avg_lifespan = Pet.get_average_lifespan(pet.species)
        print(f"{pet.name} the {pet.species} is {pet.age} pet years old, which is equivalent to {human_age} human years.")
        print(f"Average lifespan of a {pet.species}: {avg_lifespan} years.\n")
