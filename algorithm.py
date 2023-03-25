import pandas as pd
import random
import numpy as np
from tabulate import tabulate
NUM_OF_QUESTIONS = 20

def algorithm():   
    # Importing 
    df = pd.read_csv("Pitt Nemesis Pact (Responses) - Form Responses 1.csv", sep=",")
    del df["Timestamp"]
    del df["Email Address"]
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    
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
    print()
    print("2D Array Containing Total Differences Between People")
    counter = 0
    for row in difference:
        print(row, " ", names[counter])
        counter += 1
    print()
    print("2D Array Containing Amount of Questions People Differed On")
    counter = 0
    for row in questionDifferenceCount:
        print(row, " ", names[counter])
        counter += 1
    

    


    for row in difference:
        maxnum = max(row)
        indices = [index for index, item in enumerate(row) if item == maxnum]
        print(maxnum, " ", indices)
    
    

def main():
    algorithm()

if __name__ == "__main__":
    main()