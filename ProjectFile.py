import time
import random
import pandas as pd
import csv
import numpy as np
import string
import matplotlib.pyplot as plt

class present_data:
    
        def __init__(self,user_name,user_id,dict,dict2):
            self.name = user_name
            self.userid = str(user_id)
            self.accuracy = str(dict["accuracy"])     # a list as data member
            self.wpm = str(dict["wpm"])               # a list as data member
            self.avg_accuracy = str(dict2["accuracy"][0])
            self.avg_wpm = str(dict2["wpm"][0])
            self.final_wpm = str(dict2["efs"][0])

def MaintainRank(dict,user_id,user_name):

    ## contaions the present data which has to be checked from each file containing the top three scores
    ## The files has to be updated on the basis of final_wpm

    dict2 = dict_to_dict(dict,user_id,user_name)

    class present_data:
    
        def __init__(self,user_name,user_id,dict,dict2):
            self.name = user_name
            self.userid = str(user_id)
            self.accuracy = str(dict["accuracy"])     # a list as data member
            self.wpm = str(dict["wpm"])               # a list as data member
            self.avg_accuracy = str(dict2["accuracy"][0])
            self.avg_wpm = str(dict2["wpm"][0])
            self.final_wpm = str(dict2["efs"][0])

    obj = present_data(user_name,user_id,dict,dict2)

    file1 = open('first.txt','r')
    file2 = open('second.txt','r')
    file3 = open('third.txt','r')

    content1 = file1.readlines()
    content2 = file2.readlines()
    content3 = file2.readlines()
    
    file1.close()
    file2.close()
    file3.close()

    
 
    if len(content1)==0:
        file1 = open('first.txt','w')
        file1.write(obj.name + "\n")
        file1.write(obj.userid + "\n")
        file1.write(obj.accuracy + "\n")
        file1.write(obj.wpm + "\n")
        file1.write(obj.avg_accuracy + "\n")
        file1.write(obj.avg_wpm + "\n")
        file1.write(obj.final_wpm)
        file1.close()

    elif len(content2)==0:
        if float(obj.final_wpm)>float(content1[6]):
            file1 = open('first.txt','w')
            file1.write(obj.name + "\n")
            file1.write(obj.userid + "\n")
            file1.write(obj.accuracy + "\n")
            file1.write(obj.wpm + "\n")
            file1.write(obj.avg_accuracy + "\n")
            file1.write(obj.avg_wpm + "\n")
            file1.write(obj.final_wpm)
            file1.close()
            ## with the help of content1 update second.txt and third.txt with content2.
        
            file2 = open('second.txt','w')

            for x in content1:
                file2.write(x)

            file2.close()

        else:
            file2 = open('second.txt','w')
            file2.write(obj.name + "\n")
            file2.write(obj.userid + "\n")
            file2.write(obj.accuracy + "\n")
            file2.write(obj.wpm + "\n")
            file2.write(obj.avg_accuracy + "\n")
            file2.write(obj.avg_wpm + "\n")
            file2.write(obj.final_wpm)
            file2.close()


    elif len(content3)==0:
        if float(obj.final_wpm)>float(content1[6]):
            file1 = open('first.txt','w')
            file1.write(obj.name + "\n")
            file1.write(obj.userid + "\n")
            file1.write(obj.accuracy + "\n")
            file1.write(obj.wpm + "\n")
            file1.write(obj.avg_accuracy + "\n")
            file1.write(obj.avg_wpm + "\n")
            file1.write(obj.final_wpm)
            file1.close()
        ## with the help of content1 update second.txt and third.txt with content2.
        
            file2 = open('second.txt','w')

            for x in content1:
                file2.write(x)

            file2.close()

            file3 = open('third.txt','w')

            for x in content2:
                file3.write(x)

            file3.close()   

        elif float(obj.final_wpm)>float(content2[6]):
            file2 = open('second.txt','w')
            file2.write(obj.name + "\n")
            file2.write(obj.userid + "\n")
            file2.write(obj.accuracy + "\n")
            file2.write(obj.wpm + "\n")
            file2.write(obj.avg_accuracy + "\n")
            file2.write(obj.avg_wpm + "\n")
            file2.write(obj.final_wpm)

            file2.close()
            ## with the help of content2 update third.txt

            file3 = open('third.txt','w')

            for x in content2:
                file3.write(x)

            file3.close()

        else:
            file3 = open('third.txt','w')
            file3.write(obj.name + "\n")
            file3.write(obj.userid + "\n")
            file3.write(obj.accuracy + "\n")
            file3.write(obj.wpm + "\n")
            file3.write(obj.avg_accuracy + "\n")
            file3.write(obj.avg_wpm + "\n")
            file3.write(obj.final_wpm)

            file3.close()
                                


    elif float(obj.final_wpm)>float(content1[6]):
        file1 = open('first.txt','w')
        file1.write(obj.name + "\n")
        file1.write(obj.userid + "\n")
        file1.write(obj.accuracy + "\n")
        file1.write(obj.wpm + "\n")
        file1.write(obj.avg_accuracy + "\n")
        file1.write(obj.avg_wpm + "\n")
        file1.write(obj.final_wpm)
        file1.close()
        ## with the help of content1 update second.txt and third.txt with content2.
        
        file2 = open('second.txt','w')

        for x in content1:
            file2.write(x)

        file2.close()

        file3 = open('third.txt','w')

        for x in content2:
            file3.write(x)

        file3.close()   

    elif float(obj.final_wpm)>float(content2[6]):
        file2 = open('second.txt','w')
        file2.write(obj.name + "\n")
        file2.write(obj.userid + "\n")
        file2.write(obj.accuracy + "\n")
        file2.write(obj.wpm + "\n")
        file2.write(obj.avg_accuracy + "\n")
        file2.write(obj.avg_wpm + "\n")
        file2.write(obj.final_wpm)

        file2.close()
        ## with the help of content2 update third.txt

        file3 = open('third.txt','w')

        for x in content2:
            file3.write(x)

        file3.close()

    elif float(obj.final_wpm)>float(content3[6]):
        file3 = open('third.txt','w')
        file3.write(obj.name + "\n")
        file3.write(obj.userid + "\n")
        file3.write(obj.accuracy + "\n")
        file3.write(obj.wpm + "\n")
        file3.write(obj.avg_accuracy + "\n")
        file3.write(obj.avg_wpm + "\n")
        file3.write(obj.final_wpm)

        file3.close()
                    
def plot1(wpm,accuracy):
    length=len(wpm)
    X = []
    for x in range(length):
      X.append(x+1)

    y1_coordinates = accuracy
    y2_coordinates = wpm

    plt.plot(X, y1_coordinates,label = "Accuracy",marker = 'o')
    plt.plot(X, y2_coordinates,label = "WPM",marker = 'o')

    plt.xlabel("No. of Trials")
    plt.ylabel("Accuracy or Word/Min")
    plt.title("Individual score in terms of Accuracy and Word/Min in different trials")
    plt.legend()
    plt.show()

def plot2(userid,username,wpm,accuracy,performance):
    name = userid
    index = performance

    plt.plot(name, index, color='red', marker='o')
    plt.title('Performance Comparison', fontsize=14)
    plt.xlabel('Contestent ID', fontsize=14)
    plt.ylabel('Performance Index', fontsize=14)
    plt.grid(True)
    plt.show()

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def function1(dict1):
    df=pd.DataFrame(dict1)
    df.to_csv('individual.csv')

def function2():
    df = pd.read_csv("individual.csv")
    df.to_dict("individual.csv")
    return df    

def function3(maindata):
    l=len(maindata)
    with open("database.csv", "a",newline='') as file:
       writer=csv.writer(file)
       for i in range(l):
           writer.writerow(maindata[i])    

def function4():
    df=pd.read_csv("database.csv")
    df.to_dict(orient='dict')  
    return df         
    
def dict_to_dict(dict,user_id,user_name):
    new_dict={}
    name = [user_name]
    userid = [user_id]
    sum_accuracy=0 
    for i in dict["accuracy"]:
        sum_accuracy = sum_accuracy + i

    length_accuracy = len(dict["accuracy"])
    avg_accuracy = sum_accuracy/length_accuracy
    accuracy = [avg_accuracy]
    sum_wpm=0
    for k in dict["wpm"]:
        sum_wpm = sum_wpm + k

    length_wpm = len(dict["wpm"])
    avg_wpm = sum_wpm/length_wpm
    wpm = [avg_wpm]

    fwpm = accuracy[0]*wpm[0]   ### fwpm -> an integer variable to store final_wpm

    final_wpm = [fwpm]

    new_dict["name"] = name
    new_dict["user_id"] = userid
    new_dict["accuracy"] = accuracy
    new_dict["wpm"] = wpm
    new_dict["efs"] = final_wpm

    return new_dict  

def calculate(dict,user_id):
    uid=np.array(dict["user_id"])
    fwp=np.array(dict["efs"])
    acc=np.array(dict["accuracy"])
    n=len(uid)
    rank=n
    for i in range(n-1):
      for j in range(n-1):
        if(fwp[j]<fwp[j+1]):
          t1=fwp[j]
          fwp[j]=fwp[j+1]
          fwp[j+1]=t1
          t2=uid[j]
          uid[j]=uid[j+1]
          uid[j+1]=t2
    #print(list(uid))      
    for k in range (n):
      if(uid[k]==user_id):
        rank=k+1
    percentile=[]  
    if(n>1):  
        percentile.append(((n-rank)/(n-1))*100)
    else:
        percentile.append(100)
    uid=np.array(dict["user_id"])
    for i in range(n-1):
      for j in range(n-1):
        if(acc[j]<acc[j+1]):
          t1=acc[j]
          acc[j]=acc[j+1]
          acc[j+1]=t1
          t2=uid[j]
          uid[j]=uid[j+1]
          uid[j+1]=t2
    for k in range (n):
      if(uid[k]==user_id):
        rank=k+1
    if(n>1):    
        percentile.append(((n-rank)/(n-1))*100)
    else:
        percentile.append(100)
    return percentile        # list returned, index 0 for final_wpm percentile and 1 for accuracy percentile    


strings=["Nothing is more peaceful than sitting in a valley under Himalayas",
"when I realised that the person sitting beside me was none other than Sherlock himself",
"The origin of different cosmic radiation recieved so far is still not clear",
"National heritage of India is rich with diverse cultures",
"Microsoft overtakes Apple becoming the company with highest net worth",
"who could have thought that an apple will decide the path of science today",
"mount Vinson Massif is the highest peak of Antarctica",
"laws and regulations regarding virtual privacy has become a serious issue to ponder upon",
"movie industries in any country plays a vital role in introducing a new culture in the society",
"different computer languages are used for different purposes according to different features it provides",
"work from home during COVID has become the new normal",
"Da Vinci code is a novel written by Dan Brown",
"You only live once and if you do it right once is enough", 
"Many of life's failures are people who did not realize how close they were to success when they gave up",
"Never let the fear of striking out keep you from playing the game",
"In order to write about life first you must live it",
"You never really learn much from hearing yourself speak",
"Life is ten percent what happens to you and ninety percent how you respond to it"]

print("\n\t\t\t\t\tWelcome this a platform to test your typing speed \n\nYou can attempt this test in following 3 precisions, the more you type the more precise will be your results: ")
while(True):
    print("\n1. Low precision (Type 4 sentences)")
    print("2. Moderate precision (Type 7 sentences)")
    print("3. High precision (Type 10 sentences)")
    print("4. Will try next time (Quit)")

    res=input("\nPlease enter you choice 1, 2, 3 or 4: ")

    if(res=="1"):
        number_of_sentences=4
    elif(res=="2"):
        number_of_sentences=7
    elif(res=="3"):
        number_of_sentences=10    
    elif(res=="4"):
        exit()
    else:
        print("\nWrong input!!")
        input("Press Enter to continue ")
        continue
    indData={"wpm": [], "accuracy": [] } 
    name = input("Please input your name: ") 
    print("\nCrack your fingers and get ready to type !!")    
    iter=number_of_sentences
    while(iter>0):
        idx=random.randrange(0,18)
        input("\nPress enter for the sentence and enter the string that follows as fast as you can and press Enter after finish typing ")
        t0=time.time()
        inputText=str(input("\n'%s'\n"%strings[idx]))
        t1=time.time()
        word_count=len(strings[idx].split())
        accu=len( set(inputText.split()) & set( strings[idx].split() ) )
        accu=accu/word_count
        timeTaken=t1-t0   #in_seconds
        timeTaken=timeTaken/60    #in_minutes
        wordPM=(word_count/timeTaken)
        indData["wpm"].append(wordPM)
        indData["accuracy"].append(accu)
        iter-=1

    forId=random.randrange(3,9)
    userID=get_random_string(forId)

    #Updating top rankers as per the need
    MaintainRank(indData, userID, name)

    #storing individual data in individual.csv    
    function1(indData)

    #dictionary for appending in database.csv    
    forDB=dict_to_dict(indData, userID, name)

    #converted list from dictionary for appending in databse using Arya's function
    list=[[ forDB["user_id"][0], forDB["name"][0], forDB["wpm"][0], forDB["accuracy"][0], forDB["efs"][0] ]]
    function3(list)

    #dictionary having final average values after calculating from the database.csv
    forCalc=function4()

    #list having accuracy and wpm percentile of individual candidate 
    results=calculate(forCalc, userID)

    # Results
    print("Following is the analysis of your performance: ")
    print("Name: " +  name + "\t\t Your ID: " + userID)
    print("Remember you user ID for checking your position in graph")
    print("For individual sentences: ")
    for z in range(0,len(indData["accuracy"]) ):
        a=str(indData["accuracy"][z])
        w=str(indData["wpm"][z])
        print("Sentence " + str(z+1) + "---> accuracy: " + a + "; Words per minute: " + w)

        
        
    print("Your overall performance is as follows:")
    a=str(forDB["accuracy"][0])
    w=str(forDB["wpm"][0])
    print("Average accuracy: " + a + " and average typing  speed is " + w + " words per minute")
    a=str(results[1])
    w=str(results[0])
    print("Your percentile among all candidates is---> accuracy: " + a + "; Words per minute: " + w)
    for i in range(len(indData["accuracy"])):
        indData["accuracy"][i] *= 100 
    print("Following is the graph of your individual attempts:")
    plot1(indData["wpm"], indData["accuracy"])
    print("And this is the final graph of all participants: ")
    plot2(forCalc["user_id"], forCalc["name"], forCalc["wpm"], forCalc["accuracy"], forCalc["efs"])
       



   

