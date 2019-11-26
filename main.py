import random
class person:
  def __init__(self,name,age,gender,hair_color,accessory):
    self.name = name
    self.age = age
    self.gender=gender
    self.hair_color=hair_color
    self.accessory = accessory
p1 = person("chantal","24","female","brown","earrings")
p2 = person("eric","30","male","bald","earrings")
p3 = person("alex","28","male","blonde","cigar")
p4 = person("bob","21","male","blonde","hat")
p5 = person("paul","29","male","brown","hat")
p6 = person("frank","22","male","black","earrings")
p7 = person("zoe","19","female","brown","glasses")
p8 = person("joe","19","male","white","glasses")
p9 = person("buba","20","female","black","earrings")
p10 = person("rita","28","female","purple","glasses")
p11 = person("rick","30","male","blonde","glasses")
p12 = person("antoine","34","female","brown","none")
p13 = person("john","22","male","black","glasses")
p14 = person("chap","20","male","bald","glasses")
p15 = person("evelyn","33","female","pink","none")
p16 = person("lady","29","female","brown","glasses")
p17 = person("samantha","25","female","blonde","hat")
p18 = person("jenny","34","female","pink","glasses")
p19 = person("javier","23","male","pink","hat")
p20 = person("evan","25","male","blonde","none")
p21 = person("mathias","25","male","bald","glasses")
p22 = person("michael","23","male","blonde","none")
p23 = person("hank","25","male","pink","hat")
p24 = person("vito","32","male","bald","none")
people =[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24]
ourguy=people[random.randint(0,24)]
youWon=False
print("Welcome to text-based guess who you have 20 chances to guess who our special someone is before you lose.\ngood luck!")
print (ourguy.name)
for i in range(0,20):
  print("The people it could be is")
  for x in people:
    print(x.name)
  question = input("Give me a hair color, age, gender, or accessory and if our person dosen't have it I will eliminate all who do have that feature ")
  for x in people:
    if question == x.age and x.age != ourguy.age:
      people.pop(people.index(x))
    elif question == x.gender and x.gender != ourguy.gender:
      people.pop(people.index(x))
    elif question == x.hair_color and x.hair_color != ourguy.hair_color:
      people.pop(people.index(x))
    elif question == x.accessory and x.accessory != ourguy.accessory:
      people.pop(people.index(x))
  question = input("would you like to guess a name y/n:\n caution entering the wrong name gives you one less chance to enter features\n  ")
  if question == "y":
    question = input("What is his name: ")
    if question == ourguy.name:
      print("YOU WON CONGRATS")
      break
    elif question != ourguy.name:
      print("Oof bud that ain't it")
      i+=1
    else:
      print("uuuuuhm how did this even happen")
  elif question == "n":
    question ="big sad"
  else:
    print("Hey >:(\n lowercase y or lowercase n are your only options")
if youWon==False:
  print("OOF too many attempts you lose :(")
