import random

# Function definition to simulate two die roll's.
# Returns sum of die roll's & a double roll flag (1 = double rool)
def die_roll ():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)

    if die_1 == die_2:
        double_flag = 1
    else:
        double_flag = 0

    return(die_1+die_2,double_flag);


# Initial definations of Monopoly elements.
# Property names in the board sequence.
Property_Names = ["Go", "Old Kent Road", "Community Chest #1", "Whitechapel", "Income Tax",
                  "Kings Cross", "The Angel Islington", "Chance #1", "Euston Road", "Pentonville Road",
                  "Jail", "Pall Mall", "Electric Company", "Whitehall", "Northumberland Avenue",
                  "Marylebone Station", "Bow Street", "Community Chest #2", "Marlborough Street", "Vine Street",
                  "Free Parking", "Strand", "Chance #2", "Fleet Street", "Trafalgar Square",
                  "Fenchurch St Station", "Lecicester Square", "Coventry Street", "Water Works", "Piccadilly",
                  "Go To Jail", "Regent Street", "Oxford Street", "Community Chest #3", "Bond Street",
                  "Liverpool Station", "Chance #3", "Park Lane", "Super Tax", "Mayfair"]

# Chance cards. Only the cards relevant to affecting positoin are listed here.
C_Cards = ["Advance to 'Go'","Go to jail","Advance to Pall Mall",
           "Take a trip to Marylebone Station","Advance to Trafalgar Square","Advance to Mayfair",
           "Go back three spaces"]
# Community Chest cards. Only the cards relevant to affecting positoin are listed here.
CC_Cards = ["Advance to 'Go'","Go back to Old Kent Road","Go to jail"]


# Property Count - Counts the number of times the player has landed on this square.
# All squares set to zero except GO.
Prop_Count = [1,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0,
           0,0,0,0,0]

# Setting initial conditions for the game
random.shuffle(C_Cards)
random.shuffle(CC_Cards)
P_Pos = 0
C_Cards_Pos = 0
CC_Cards_Pos = 0


# Run the code for x number of rolls
for i in range(1000000):
    roll, double_flag = die_roll()
    P_Pos += roll

    # Check if the player has passed GO based on die roll, and initiate reset if required
    if P_Pos >39:
        P_Pos = P_Pos-40

    # Update the respective property counter by 1
    Prop_Count[P_Pos] +=1

    #Check if the player position is Chance or Community Chest and initiate workflow

    #Workflow if the player position is a Community Chest
    if Property_Names[P_Pos] == "Community Chest #1" or Property_Names[P_Pos] == "Community Chest #2" or Property_Names[P_Pos] == "Community Chest #3":
        if CC_Cards[CC_Cards_Pos] == "Advance to 'Go'":
            P_Pos = 0
        elif CC_Cards[CC_Cards_Pos] == "Go back to Old Kent Road":
            P_Pos = 1
        elif CC_Cards[CC_Cards_Pos] == "Go to jail":
            P_Pos = 10

        # Statements for testing
        #print(CC_Cards[CC_Cards_Pos],Property_Names[P_Pos])

        # Updating Community Chest card counter, and performing a counter reset + card deck shuffle if in case the counter has exceeded the number of Community Chest cards
        CC_Cards_Pos += 1
        if CC_Cards_Pos >= len(CC_Cards):
            CC_Cards_Pos = 0
            random.shuffle(CC_Cards)

            #Statements for testing
            #print("Community Chest shuffled")
            #print(CC_Cards)

        Prop_Count[P_Pos] += 1

    # Workflow if the player position is a Chance
    elif Property_Names[P_Pos] == "Chance #1" or Property_Names[P_Pos] == "Chance #2" or Property_Names[P_Pos] == "Chance #3":
        if C_Cards[C_Cards_Pos] == "Advance to 'Go'":
            P_Pos = 0
        elif C_Cards[C_Cards_Pos] == "Go to jail":
            P_Pos = 10
        elif C_Cards[C_Cards_Pos] == "Advance to Pall Mall":
            P_Pos = 11
        elif C_Cards[C_Cards_Pos] == "Take a trip to Marylebone Station":
            P_Pos = 15
        elif C_Cards[C_Cards_Pos] == "Advance to Trafalgar Square":
            P_Pos = 24
        elif C_Cards[C_Cards_Pos] == "Advance to Mayfair":
            P_Pos = 39
        elif C_Cards[C_Cards_Pos] == "Go back three spaces":
            P_Pos -= 3
            # Not worrying about negative player positions as Change square positions are always > 3.

        # Statements for testing
        #print(C_Cards[C_Cards_Pos], Property_Names[P_Pos])

        #Updating Chance card counter, and performing a counter reset _ card deck shuffle if in case the counter has exceeded the number of Chance cards
        C_Cards_Pos += 1
        if C_Cards_Pos >= len(C_Cards):
            C_Cards_Pos = 0
            random.shuffle(C_Cards)

            # Statement for testing
            #print("Chance cards shuffled")
            #print(C_Cards)

        Prop_Count[P_Pos] += 1

Prop_Probability = [x / sum(Prop_Count) for x in Prop_Count]

print (Prop_Probability)

import csv

output_path = "/media/sriharinarayanan/New Volume/CodeBase/Python/02 Monopoly/Monopoly_Data.csv"

with open(output_path, "w") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(Prop_Probability)


