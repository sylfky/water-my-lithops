#
#
#
#   when in doubt...
no_water = "\nDon\'t water your Lithops.\n"
#
#
arrow_txt ="\n\n-----------> "
bad_ans = "\nPlease enter a valid answer.\n"
#
# intro text
def intro():
    print("\nShould I water my Lithops?\n")
    start = input("Press enter to find out:\n\n")
#
#   Lithops shouldn't be watered after flowering
def flower_check():
    choices1 = "[yes, no, idk]"
    print("Has it flowered?  " + choices1)
    flower = input(arrow_txt)
    while flower != "yes" and flower !="no" and flower !="idk":
        flower = input(bad_ans + choices1 + arrow_txt)
    if flower =="yes":
        print(no_water)
    else:
        print("\nMaybe?")
    return flower
#
#   Lithops shouldn't be watered during or after new leaf growth
#   if new leaves are coming in, then the Lithops (if mature) has already flowered
def leaf_status():
    choices2 = "[shed, growing, neither]"
    print("Is your Lithops growing new leaves? Or has it already shed its old leaves?\n" + choices2)
    new_leaves = input(arrow_txt)
    while new_leaves != "shed" and new_leaves !="growing" and new_leaves !="neither":
        new_leaves = input(bad_ans + choices2 + arrow_txt)
    if new_leaves == ("shed" or "growing"):
        print(no_water)
    else:
        print("\nPerhaps?")
    return new_leaves
#
#   here we go...
intro()
flower_answer = flower_check()
#check to make sure return flower worked
#print(flower_answer)
if flower_answer == "yes":
    quit()
else:
    print("Let's continue.\n")
leaf_answer = leaf_status()
#checking returned answers
#print(flower_answer," ",leaf_answer)
if leaf_answer == ("shed" or "growing"):
    quit()
else:
    print("Just a few more questions.\n")
