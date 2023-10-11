"""Të ndërtohet një funksion, i cili merr një numër dhe tregon nëse numri është tek
ose çift."""

def even_or_odd():
    num = int(input("Zgjedh nje number te plote: "))
    if num % 2 == 0:
        print(f"{num} eshte numer cift.")
    else:
        print(f"{num} eshte numer tek.")

even_or_odd()


# #ushtrimi 6
# """Të ndërtohet një funksion, i cili merr një string dhe një gërmë (një karakter string)
# dhe gjen sa herë përsëritet gërma tek string-u."""

def char_count():
    word = input("Shkruaj nje fjale: ")
    letter = input("Zgjedh nje shkronje nga fjala: ")
    num = word.count(letter)
    print(num)

char_count()


#ushtrimi 7


class Student:
    def __init__(self, name, surname, email, age, training):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.training = training


    def display(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Email: {self.email}, Training: {self.training}")







# Mbushja
student_1 = Student("Joe", "Doe", "Joe.Doe@gmail.com", 25, "designer")

student_1.display()


