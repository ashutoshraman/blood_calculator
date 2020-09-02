food=["apples","bananas","cherries","donuts"]
amounts=[11,22,33,44]

for f,i in enumerate(food):
    print("{} - {}".format(amounts[f],i))

for amount, i in zip(amounts,food):  #iterate thru multiple lists of same size
    print("{}-{}".format(amount,i))


def fruit(i):
    print("your food is {}".format(food[i]))
    print("you have {} of them".format(amounts[i]))
fruit(1)

def getinv(newfruit):
    for foods, amount in zip(food,amounts):
        if foods == newfruit:
            answer= amount #found your answer so break out of previous structure, like loop
            break  # use break to bring down compute times, since you already have answer and dont wanna keep iterating
    print("found fruit")
    return answer
if __name__=="__main__":
    print(getinv("donuts"))