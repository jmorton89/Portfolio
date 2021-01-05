days = {
    1: "First",
    2: "Second",
    3: "Third",
    4: "Fourth",
    5: "Fifth",
    6: "Sixth",
    7: "Seventh",
    8: "Eighth",
    9: "Ninth",
    10: "Tenth",
    11: "Eleventh",
    12: "Twelfth"
}
words = [
    "A Partridge in a Pear Tree.",
    "Two Turtle Doves, and",
    "Three French Hens,",
    "Four Calling Birds,",
    "Five Gold Rings,",
    "Six Geese-a-Laying,",
    "Seven Swans-a-Swimming,",
    "Eight Maids-a-Milking,",
    "Nine Ladies Dancing,",
    "Ten Lords-a-Leaping,",
    "Eleven Pipers Piping,",
    "Twelve Drummers Drumming,"
]
for i in range(12):    
    x= days.get(i+1)
    y= words[i]
    print("\nOn the {} day of Christmas\nMy true love sent to me\n{}".format(x,y))
    z=reversed(range(0,i))
    for i in z:
        print(words[i])