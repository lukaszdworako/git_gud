def git_gud():
    didGudIn = ""
    while ((not didGudIn.isalpha()) or (didGudIn.lower() not in ["yes", "no"])):
        didGudIn = input("Did you do gud? (yes/ no): ")
    
    if (didGudIn.lower() == "yes"):
        print("DW brah, you good fam, you good")
    else:
        numericBad = ""
        while(not numericBad.isdecimal()):
            numericBad = input("Bruh, why you not good, how bad are you numerically: ")
        numericBad = int(numericBad)
        for i in range(numericBad):
            print("Bruh, you need to git gud")
    

if __name__ == "__main__":
    git_gud()
