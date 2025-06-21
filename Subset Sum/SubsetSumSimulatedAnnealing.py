import random
import numpy as np
import decimal
def subsetsumAnnealing(set, target):


    e = 2.718
    temperature = 100

    random.shuffle(set)

    subSet = []

    for i in range(len(set)):

        currentError = absoluteErrorCalculate(subSet,target)

        if set[i] <= currentError:
            subSet.append(set[i])



    random.shuffle(set)

    done = False

    currentError = absoluteErrorCalculate(subSet, target)


    while done == False:

        neighbourSubset = subSet.copy()
        removedVal = random.choice(neighbourSubset)
        neighbourSubset.remove(removedVal)

        random.shuffle(set)

        for i in range(len(set)):

            if set[i] not in neighbourSubset:
                neighbourError = absoluteErrorCalculate(neighbourSubset, target)

                if set[i] <= neighbourError:
                    neighbourSubset.append(set[i])

        neighbourError = absoluteErrorCalculate(neighbourSubset, target)

        if neighbourError <= currentError:

            currentError = neighbourError
            subSet = neighbourSubset

        else:
            probability = e ** ((currentError - neighbourError) / temperature)
            probCheck = random.uniform(0, 1)
            if probCheck <= probability:
                subSet = neighbourSubset
                currentError = neighbourError


        temperature = temperature - (0.0005 * temperature/50)


        if currentError == 0:
            done = True
        elif temperature <= 1:
            done = True

    return currentError



def absoluteErrorCalculate(set, target):

    for i in set:
        target = target - i

    return target









