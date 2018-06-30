def Run_list_o_matic():
    listt=["cat","dog","cat"]

    while listt:
        if not listt:
            return print("Goodbye!")
        else:
            print("\nlook at all the animals ",listt)
            inputData=input("enter the name of an animal: ")
            if inputData == "quit":
                return print("Goodbye!")
                break
            else:
                list_o_matic(inputData,listt)


def list_o_matic(inputData,listt):

    if not inputData:
        x=listt.pop()
        return print(x + " popped from list")
        if not listt:
            return print("Goodbye!")

    else:
        if inputData in listt:
            listt.remove(inputData)
            return print("1 instance of "+inputData+" removed from list")
        else:
            listt.append(inputData)
            return print("1 instance of "+inputData+" appended to list")




Run_list_o_matic()
