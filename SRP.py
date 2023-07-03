# ------------- SRP ------------- #

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # this is bad practice
    def save(self):
        pass

    def load(self):
        pass



# It is better to separate the area of responsibility of saving from the journal class
class PersistenceManage:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I always busy.")

print(f"Journal entries:\n{j}")
