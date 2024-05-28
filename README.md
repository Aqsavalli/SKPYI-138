#Task-1A-1
#PROGRAM
from itertools import product

s = ["I", "You"]
v = ["Play", "Love"]
o = ["Cricket", "Ludo"]

combinations = product(s, v, o)

for combination in combinations:
    print(" ".join(combination) + ".")



#OUTPUT
I Play Cricket.
I Play Ludo.
I Love Cricket.
I Love Ludo.
You Play Cricket.
You Play Ludo.
You Love Cricket.
You Love Ludo.


#Task-1A-2
#Program

def convert_emojis_to_text(text):

    emoji_dict = {
        "😊": ":)",
        "😂": "Laugh",
        "❤️": "Love",
        "🍕":"Pizza",
        "🍦":"Ice-Cream",  
        "😥":"Sad",
        "😜":"Crazy",
        "🎶":"Music",
        "🎂":"Cake",
        "🚗":"Driving Car",
        "💐":"Congratulations",
    }
    
    for emoji, text_rep in emoji_dict.items():
        text = text.replace(emoji, text_rep)
        
    return text

text_with_emojis = "I love 🍕 and 🍦! 😊"
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis="i'm in ❤️ with this!!! "
text_without_emojis=convert_emojis_to_text(text_with_emojis)
print("Text Without emojis:",text_without_emojis)
text_with_emojis = "I ❤️ 🎶"
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "You're 😜 "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "Are you 🚗"
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "Hearty 💐 "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "She feeling 😥 "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "He is 😂ing "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)



#OUTPUT
Text without emojis: I love Pizza and Ice-Cream! :)
Text Without emojis: i'm in Love with this!!! 
Text without emojis: I Love Music
Text without emojis: You're Crazy 
Text without emojis: Are you Driving Car
Text without emojis: Hearty Congratulations 
Text without emojis: She feeling Sad 
Text without emojis: He is Laughing 



#Task-1B-2
#PROGRAM

class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._author_royalty = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def author_royalty(self):
        return self._author_royalty

    @author_royalty.setter
    def author_royalty(self, value):
        self._author_royalty = value

    def royalty(self, copies_sold):
        royalty = 0
        if copies_sold <= 500:
            royalty = 0.1 * self._price * copies_sold
        elif copies_sold <= 1500:
            royalty = (0.1 * 500 * self._price) + (0.125 * self._price * (copies_sold - 500))
        else:
            royalty = (0.1 * 500 * self._price) + (0.125 * 1000 * self._price) + (0.15 * self._price * (copies_sold - 1500))
        self._author_royalty = royalty
        return royalty


book1 = Book("Python Programming", "GUIDO VAN ROSSUM", "Publisher Aqsa", 25)
print("The name of the Book is",book1.title)
print("The AUTHOR of the book is",book1.author)
print("The PUBLISHER of the book is",book1.publisher)
print("The PRICE of the book is",book1.price)
print("10% of the retail price on the first 500 copies is",book1.royalty(700))  
print("12.5% for the next 1,000 copies sold is",book1.author_royalty)  
class Ebook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self._ebook_format = ebook_format

    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, value):
        self._ebook_format = value

    def royalty(self, copies_sold):
        royalty = super().royalty(copies_sold)
        if self._ebook_format:  
            royalty -= 0.12 * royalty
        return royalty


ebook1 = Ebook("Python Programming (ebook)", "GUIDO VAN ROSSUM", "Publisher Aqsa", 20, "PDF")
print("The TITLE of the ebooks is",ebook1.title)
print("The AUTHOR of the ebooks is",ebook1.author)
print("The PUBLISHER of the ebooks is",ebook1.publisher)
print("The PRICE of the ebooks is",ebook1.price)
print("The FORMAT of ebooks is",ebook1.ebook_format)
print("12% of GST on ebooks is",ebook1.royalty(700))  



#OUTPUT
The name of the Book is Python Programming
The AUTHOR of the book is GUIDO VAN ROSSUM
The PUBLISHER of the book is Publisher Aqsa
The PRICE of the book is 25
10% of the retail price on the first 500 copies is 1875.0
12.5% for the next 1,000 copies sold is 1875.0
The TITLE of the ebooks is Python Programming (ebook)
The AUTHOR of the ebooks is GUIDO VAN ROSSUM
The PUBLISHER of the ebooks is Publisher Aqsa
The PRICE of the ebooks is 20
The FORMAT of ebooks is PDF
12% of GST on ebooks is 1320.0


#Task-1B-2
#PROGRAM

def calculate_flames(name1, name2):
    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    
    
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    name1_list = list(name1)
    name2_list = list(name2)
    
    
    for char in name1:
        if char in name2_list:
            name2_list.remove(char)
            name1_list.remove(char)
    
    
    remaining_chars = name1_list + name2_list
    
    
    count = len(remaining_chars)
    print("The number of remaining  CHARs in 2 names is",count)
    
    while len(flames) > 1:
        index = (count % len(flames) - 1)
        if index >= 0:
            right = flames[index + 1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]


name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = calculate_flames(name1, name2)
print("Relationship between", name1, "and", name2, "is:", result)




#OUTPUT
Enter the first name: Aqsa
Enter the second name: Chinnu
The number of remaining  CHARs in 2 names is 10
Relationship between Aqsa and Chinnu is: Love
