def run():
    listt=["cat","dog","cat"]

    while listt:
        print("Look at the animal ",listt)
        if "" in listt:
            print("Goodbuy!")
        else:
            inputData=input("enter the name of an animal:")
            if inputData == "Quit":
                print("Goodbuy!")
                break
            else:
                list_o_matic(inputData,listt)


def list_o_matic(inputData,listt):
    if not inputData:
        x=listt.pop()
        print(x + " popped from list")
        if not listt:
            print("Goodbuy!")

    else:
        if inputData in listt:
            listt.remove(inputData)
            print("1 instance of "+inputData+" removed from list")
            if inputData == "Quit":
                print("Goodbuy!")
        else:
            listt.append(inputData)
            print("1 instance of "+inputData+" appended to the list")
            if inputData == "Quit":
                print("Goodbuy!")




if __name__ == '__main__':
    run()
