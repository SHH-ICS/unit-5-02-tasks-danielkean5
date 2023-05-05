# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

while True:
    word = input("enter any word:\n")
    if word == "exit":
      break
    else:
        print(len(word))