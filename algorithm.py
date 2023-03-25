import pandas as pd
import random
import numpy as np
from tabulate import tabulate
import itertools
import time

NUM_OF_QUESTIONS = 20
NAME_OF_FILE = "Pitt Nemesis Pact (Responses) - Form Responses 1.csv"
L_OR_H = -998 #positive 988 for good matches. make sure to change to min(row)
L_OR_H2 = -999 #positive 999 for good matches.
def algorithm():   
    # Importing 
    df = pd.read_csv(NAME_OF_FILE, sep=",")
    del df["Timestamp"]
    del df["Email Address"]
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    df = df.sample(frac = 1)
    names = df["What is your full name?"].values
    #Names contains all the names
    #look at first person's questions. Compare person 1's question 1 to everyone elses question 1. 
    #updating counter of difference between the first person and everyone else. find the max. if multiple maxes, choose at random.
    #somehow keep running total of who's got worst match
    #at the end find the pair
    #name.pop(pair of people)
    #continue with person 2

    people = df.to_dict(orient = 'records')

    # for i in range(len(people)):
    #     for j in range(NUM_OF_QUESTIONS):
    #         people["What is your full name?"]
    difference = np.zeros((len(people),len(people)))
    questionDifferenceCount = np.zeros((len(people),len(people)))
    for i, person in enumerate(people):
        #print(person[question], end=" ")
        for k, person2 in enumerate(people):
            totDiff = 0
            diffQuestions = 0
            for j, question in enumerate(person):
                if(type(person[question]) == int):
                    totDiff += abs(person[question] - person2[question])

                    if(person[question] != person2[question]):
                        diffQuestions += 1
                    #print("comparing", person[question], "to", person2[question], " The difference so far is: ", totDiff)
            difference[i][k] = totDiff
            questionDifferenceCount[i][k] = diffQuestions
                    

        #print()
        #print(f'{i}: {person["What is your full name?"]}')
    print("\n"*15)
    # print("2D Array Containing Total Differences Between People")
    # counter = 0
    # for row in difference:
    #     print(row, " ", names[counter])
    #     counter += 1
    # print()
    # print("2D Array Containing Amount of Questions People Differed On")
    # counter = 0
    # for row in questionDifferenceCount:
    #     print(row, " ", names[counter])
    #     counter += 1
    
    # for row in difference:
    #     maxnum = max(row)
    #     indices = [index for index, item in enumerate(row) if item == maxnum]
    #     print(maxnum, " ", indices)
    # print()
  
    return difference, questionDifferenceCount, names
    

def match(difference, questionDifferenceCount, names):
    for i in range(len(difference)):
        difference[i][i] = L_OR_H
    
    currentPerson = 0 
    for row in difference:
        time.sleep(0.1)
        
        if(row[currentPerson] != L_OR_H2): #tests if person we are looking at is already marked.
            maxnum = max(row)
            #maxnum = min(row)
            indices = [index for index, item in enumerate(row) if item == maxnum] #finds the indices of the max people
            matchNum = random.choice(indices)  #chooses one of the max people if there is tie
            print(names[currentPerson].upper(), "matches to", names[matchNum].upper())
            print("Difference value:", maxnum) #prints out match
            print("Number of questions answered differently:", questionDifferenceCount[matchNum][currentPerson])
            print()
            for i in range(len(names)): #marks matched people
                difference[i][currentPerson] = L_OR_H2
                difference[i][matchNum] = L_OR_H2
        #print(difference)
        #print(names)
        currentPerson += 1
    print("done!")

def complexMatch(difference,questionDifference,names):
    temp = itertools.combinations(names,2)
    combinations = np.array(list(temp))
    populations = matchHelper(combinations)
            
    # names1 = names.copy(order='C')
    # names2 = names.copy(order='C')
    # np.cross(names1, names2, axisa=-1, axisb=-1, axisc=-1, axis=None)
    # want to change algorithm to make it so that it considers the entire population and every single population matchup chart.
    # adds up all the differences and finds the population with the max difference.

def matchHelper(combinations):
    #use recursion to find all combinations of the population.
    #because the population is dynamic, need to use recursion.
    return None

def main():
    difference, questionDifferenceCount, names = algorithm()
    match(difference, questionDifferenceCount, names)

if __name__ == "__main__":
    main()