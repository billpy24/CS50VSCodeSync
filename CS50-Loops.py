
"""
#conditionals

x  = int(input("what's x? "))
y = int(input("what's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


#lists

students = ["Hermione", "Ron", "Harry"]

print(students[0])
#alternate code 
#for student in students:
#    print(student)


#dicts
students = [Hermione, Ron, Harry]
houses = [Gryffindor, Slytherin, Hufflepuff]


students = {
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Harry": "Gryffindor",
    "Draco": "Slytherin:",

}
for student in students:
    print(student, students[student], sep=", ")


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

#talking about mario stuff

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()


def main():
    print_square(5)

def print_square(size):

    for i in range(size):
        print("#" * size)

main()


#currently on loops 2nd video
#pretend i have a code called sample which measures moisture in soil for my plant so Iget a reminder to water. While loop
from soil import sample

def main():
    moisture = sample()
    days = 0
    print(f"Day {days}:Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture}%")

    print("Water the plant")

main()
"""
#currently on loops 3rd video
