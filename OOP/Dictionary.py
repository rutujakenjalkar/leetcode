#empty dictionary
dict1={}

#key of same name but different capitalisztion are different form each other 
#keys have to be unique but the values can be the same 

#creating dictionary with filled values
dict1={1:"abcd",2:"erutu",3:"kejenfr"}
#Accessing values 
print(dict1[3])
#if try to access keys which are not existing then key error is obtained
#to add entry 
dict1[4]="ahello"
print(dict1)
#entry is always added at the back
dict1[2]="modifef"
print(dict1)

#to delete an item del dictionary name and key
del dict1[4]
print(dict1)

#delete all entries
dict1.clear()
print(dict1)

dict1[5]="eruihurt"
#takes the key and return the values which is deleted
print("the removed item:",dict1.pop(5))

#key has to be of immutable type
dict1[34,5,2]="were"
print(dict1)
#even if add a mutable type it will get converted to immtuabtble type list ket then ==> tuple

#use of sort function
print(sorted(dict1.keys()))

dict2={"name":"sdgfsk", "age":12
}

#for string keys the sorting is as follows
print(sorted(dict2.keys()))
#['age', 'name']
