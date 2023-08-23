# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 
# It should print a prompt that makes it clear what is being calculated. 
# After accepting input the calculator should perform an accurate calculation 
# and display the results in a clear and well formatted message. 
# Be sure to convert your numeric values to numbers before performing math operations!


# 5e stat calculation by roll 4d6 dropping the lowest
# Had to look up how to drop the lowest, found min(). Neat!
def stat_calc(first,second,third,fourth):
    rolls = first + second + third + fourth
    stat = rolls - min(first,second,third,fourth)
    final = f"Your stat is {stat}."
    return final

# Keep it DRY. Probably a way to have it do 1st, 2nd, 3rd automatically. I like the text though.
pt1 = "What is the result on the"
pt2 = "d6? "

print("Calculator: D&D stat.")
print("Roll 4d6.")
      
first = int(input(f"{pt1} first {pt2}"))
second = int(input(f"{pt1} second {pt2}"))
third = int(input(f"{pt1} third {pt2}"))
fourth = int(input(f"{pt1} fourth {pt2}"))

result = stat_calc(first,second,third,fourth)
print(result)
