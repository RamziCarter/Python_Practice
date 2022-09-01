#slicing is the process of extracting elements from another string
#you can index or slice to complete this
#3 attributes to slice [start:stop:step]

name = "Ramzi Carter"
first_Name = name[0:5]  # [:3] means beginning until 2nd character
last_Name = name[6:12]  # [6:] means 6th character until end
full_Name = name[:12:3] #  <-- means from begining to 11th character
                        # and print every third character


building = "church"
reversed_Building = building[::-1]
print(first_Name)
print(last_Name)
print(full_Name)
print(reversed_Building)


website = "https://www.youtube.com/"
#creating a resuable slice object
slice = slice(12,-5)

print("The website name from the URL is " + website[slice])
