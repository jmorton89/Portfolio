w=" bottle of beer"
x="\nTake one down and pass it around, "
y=" bottles of beer on the wall"
z=" bottles of beer."
for i in reversed(range(3,100,1)):print("{}{}, {}{}".format(i,y,i,z)+x+str(i-1)+y+".\n")
print("2"+y+", 2"+z+x+"1"+w+" on the wall.")
print("\n1"+w+" on the wall, 1"+w+"."+x+"no more"+y+".")
print("\nNo more"+y+", no more"+z+"\nGo to the store and buy some more, 99"+y+".\n")