import os
def read_notes():
    try:
        with open("notes.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def display_notes():
    notes = read_notes()
    if notes:
        print("Your notes:")
        for index, note in enumerate(notes, start=1):
            print(str(index) + ") " + note.strip())
    else:
        print("No notes found.")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

def delete_note():
    display_notes()
    try:
        notes = read_notes()
        if not notes:
            print("No notes to delete.")
            return
        
        note_index = int(input("Enter the index of the note to delete: "))
        
        if note_index < 1 or note_index > len(notes):
            print("Invalid index.")
            return
        
        with open("notes.txt", "w") as file:
            for index, note in enumerate(notes, start=1):
                if index != note_index:
                    file.write(note)
        print("Note deleted successfully.")
    except ValueError:
        print("Invalid index.")

while True:
    print("\nOptions:")
    print("1. Display notes")
    print("2. Add a note")
    print("3. Delete a note")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
