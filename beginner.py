import random
y=20
z=15
print(y*z)
v=5
w=5
print(w+w*w)
name="merriment"
age=17
occupation="banker"
print(age)
print(occupation)
print(name)
is_banker=True
print(is_banker)
print(name,age,occupation,is_banker)
c=50-20
print(c)


name:str=""
age:int= 40 
a=b=c=30
empty=None


print(empty)
decimaal =3.4
is_admin= True 
print(type(decimaal))
print(type(is_admin))
print(type(age))
listofNames=["MAry", "chisom", 60]
print(type(listofNames))
listofNames[0]="Ekpere"

print(listofNames)
listofNames[1]="peace"
print(listofNames)
my_favourite_country=("afghnistan", "iran", "somali")
print(my_favourite_country)

print(type(my_favourite_country))
students_info={"name":"Mary","age":16,"origin":"Abakaliki",  "name":"Timothy",  "origin":"Enugu"}
print(type(students_info["name"]))
print(students_info["origin"])
print(students_info["name"])
print(students_info)

listoffav=[{"name":"Amaka"}, {"name":"mgbeke"}]
print(listoffav[0])

print(students_info["name"])

print(students_info.get("origin"))

if "name" in students_info:
    print(students_info["name"])

has_car=False

if has_car:
    print(f"you have a car that is {has_car}")

()
[]
{}
scores=[2,4,6,8,10]
scores.append(100)
scores.insert(1,15)
a=50
b=20
print(a==b)
c=10
d=10
print(c==d)
c==d
print(c)
print(a!=b)
print(c!=d)


print(scores)
score = 70 
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("very Good")
else:
    print("Failed")



has_uniform = True
has_paid = False


if has_uniform and has_paid:
    print("you are qualified to attend the party")
else:
    print("is either you have not paid or you dont have a uniform")
has_blackshoe=True
has_watch=False
if has_blackshoe or has_watch:
    print("good to go")
else:
    ("vanish")
has_blackshoe=False
print(not has_blackshoe)
category=["transport","food","book"]
print(category =="transport" or category =="food" and category == "book" )
roundnum = round(0.1 + 0.2 , 2) 
roundit  =  round(3.36573653, 3)
print(roundnum)
print(roundit)
print(int(3.17))
print(abs((0.1 + 0.2 ) -  0.3 ) < 1e-9)

temperature =  10


if temperature >  30:
    print("the  day  is  hot")
elif temperature > 20:
    print("is  a nice day")
elif temperature >= 10 :
    print("the day is so cold ")

else:
    print("you  camne from  mars ")


fruits  =  ["apple",  "pinapple", "orange"]


for fruit in  fruits:
    print(f"i love {fruits[:]}")
bees="queen"
print("bees {[:4]}" )
male=[20, 15, 10, 5, 0]
print(male[0:4])
print(bees[0:3])
me="Ekpere"
for E in me:
    print(me[-1])

for num in range(200, 300, 2):
    if num % 2 == 0:
        print(f"even number {num ** 2}")
    else:
        print(f"odd {num}")
    
print(7 %  2)

print(len(scores))
for i in range(len(me)):
    if me[i] == "e":
        print(f"found  the letter {me[i]} at index {i}")


count =  0 

while  count  <  10:
    count +=2
    print(f"the count is now {count}")

"""
secretNumber  = random.randint(1, 100)
guess =  0
attmept =  0

while guess !=  secretNumber:
    guess =  int(input("Please guess a secret Number:"))
    attmept += 1

    if guess  < secretNumber :
        print(f"the number you guess {guess} is lower than the secret number")
    elif guess > secretNumber:
        print(f"the number you guess  is  higher continue trying")
print(f"your  guess {guess} is  our secret number & got it  in  {attmept} tries. bravo!")
"""
task=["clean the room", "sweep", "wipe the glasses"]
 
print(" starting  to  do  all my  chores now")

while task:
    current_task =  task.pop(0)
    print(f"doing  the {current_task} now")


print("all  my task  has been done horay!")

tasks=[3,5,7,8,0,9]
print(tasks.pop(3))

print(len(task))


num =  [2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 19]
stop = 0

while stop < len(num):
    number = num[stop]
    if number % 2 != 0:
      print(f" the  first  odd num {num[stop]}")
      break
    stop += 1

binary =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


counter =  0 

while counter < 10 :
    counter += 1

    if counter % 2 != 0:
        continue
    print(f"the  even  numbers  are {counter}")


index =  0 


while  index  <  len(binary):
    number =  binary[index]

    if number % 2 == 0:
      
       print(f"the is  the  even  {number} on  the  list")
      
    index +=1
user =  { "name":"Maryskiddo",  "age":30, "occupation":"Lawyer", "Sidehustle":"Armrobbery" }
while user:
    key = "name", "age", "occupation", "Sidehustle"
    print(f"the main game include {key}")
    break
while user:
    attachment = "Marysiddo", 30, "Lawyer", "Armrobbery"
    print(f"my info {attachment}")
    break


while count < 6:
    count += 1
    if count ==2:
       continue

for  key  in  user:
    print(f"{key}: {user[key]}")

for key in  user:
    print(f"this  is  the  values {user[key]}")

for value  in  user.values():
    print(value)


for keys,values in user.items():
    print(f"{keys}:{values}")

cart = {"apple" : 4, "banana" : 2, "watermelon" :7 }
total=0
for fruits, quantity in cart.items():
    total += quantity


print(f"the total of what you bought is {total}")
inventory = {"laptop" : 4, "phone" :  7, "keyboard" : 2, "monitor" : 0 }
plus = 0
for product, remender in inventory.items():
    if remender == 0:
        print(f"f the  {product } is  out of stock  remainig:{remender}")

movies = {"karatekids":8.5, "durnkardmaster":8.0,  "littlerascles":9.6, "richer":7.5  }

for movie, rating in movies.items():
    print(f"{movie}:{rating}")
    if rating >=8.0:
        print (f"you must watch")
    else:
        print("just okay")

       
movie_rating = 0 

for movie, rating in movies.items():
    movie_rating +=rating
    average_rating = movie_rating / len(movies)

print(movie_rating)
print(f"average rating of all movies: {average_rating}")

for i in range(3):
    for j in range(3):
        print(f"{i}, {j}")
for num in range (20):  
    if num  == 5:
        break
    print(num)
for num in range (20):
    if num % 2 == 0:
        continue
    print(num)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
