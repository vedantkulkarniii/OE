import pickle

class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")


# Write content to file
with open("document.txt", "w") as f:
    f.write("This is a sample document content.\n")

# Read content from file
with open("document.txt", "r") as f:
    print("File Content:")
    print(f.read())


# Create object
doc = Document("AI Notes", "Vedant")

# Serialize (save object)
with open("doc_meta.pkl", "wb") as f:
    pickle.dump(doc, f)

# Deserialize (load object)
with open("doc_meta.pkl", "rb") as f:
    loaded_doc = pickle.load(f)

print("\nDeserialized Object:")
loaded_doc.display()