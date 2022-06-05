# 1. TASK: print "Hello World"
print( "Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "hello",name,"!" )	# with a comma
print("hello "+name+"!")	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print( "hello",name,"!" )	# with a comma
print( "hello"+name,"!" )	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( " I love to eat {} and {}".format(fave_food1, fave_food2) ) # with .format()
print(f" I love to eat {fave_food1} and {fave_food2}"  ) # with an f string

myname= "Asma"
print("hello ",myname,"!" )
print("hello "+ myname+ "!")

fav_num=6
print("hello",fav_num)
print("hello"+fav_num)

# resolve the above errors
name = 42
print( "hello",name,"!" )	
print( "hello "+str(name),"!" )

fav_num=6
print("hello",fav_num)
print("hello "+ str(fav_num))

# favorite food

fav_f1="rice"
fav_f2="chicken"
print(" I love to eat {} and {}".format(fav_f1, fav_f2))
print(f" I love to eat {fav_f1} and {fav_f2}"  )

# try more string methods

fname="Asma"
lname="ALamri"
print("My first name is %s and my last name is %s" %(fname,lname))



