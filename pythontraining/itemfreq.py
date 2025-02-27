def wordcount(input_str):
    worddic={}
    wordsplit=input_str.lower(). split()
    for i in wordsplit:
        if i in worddic:
            worddic[i]+=1
        else:
            worddic[i]=1
    return worddic

def main():
    input_str=input("Enter the string: ")
    worddict=wordcount(input_str)
    print(worddict)
if __name__ == "__main__":
    main()