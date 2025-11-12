print("Welcome User! How Can I Help You")
print("1 For Continue")
print("2 For Exit")
def book():
    print("Enter 1 for To Kill a Mockingbird by Harper Lee ")
    print("Enter 2 for 1984 by George Orwell")
    print("Enter 3 for The Alchemist by Paulo Coelho")
    print("Enter 4 for The Great Gatsby by F. Scott Fitzgerald")
    print("Enter 5 for Harry Potter and the Sorcerer’s Stone by J.K. Rowling")
    b = int(input("Enter a Book for as shown above: "))
    if b == 1:
        print("To Kill a Mockingbird by Harper Lee -> \n-------- Description -------- \n A timeless classic exploring racial injustice and moral growth in the Deep South. Told through the eyes of young Scout Finch, it teaches empathy, courage, and integrity.")
    elif b == 2:
        print("1984 by George Orwell -> \n-------- Description -------- \n A dystopian novel about a totalitarian regime that controls truth, history, and thought. It’s a powerful warning about surveillance, propaganda, and loss of freedom.")
    elif b == 3:
        print("The Alchemist by Paulo Coelho -> \n-------- Description -------- \n A philosophical tale about following one’s dreams and listening to the heart. It follows Santiago, a shepherd, on his journey to find his personal legend")
    elif b == 4:
        print("The Great Gatsby by F. Scott Fitzgerald -> \n-------- Description -------- \n Set in the roaring 1920s, it depicts love, wealth, and the illusion of the American Dream. Jay Gatsby’s tragic pursuit of Daisy Buchanan reflects the emptiness of materialism.")
    elif b == 5:
        print("Harry Potter and the Sorcerer’s Stone by J.K. Rowling -> \n-------- Description -------- \n The first book in the magical Harry Potter series. It introduces a boy wizard discovering friendship, courage, and destiny at Hogwarts. ")
    else:
        print("Invalid Input \n ---------- No Book Found ----------")
def run():
    a = int(input("Enter Any no. as per given above: "))
    if a == 1:
        book()
    elif a == 2:
        print("Thanks for visiting us: ")
    else:
        print("Invalid Input given")
run()

