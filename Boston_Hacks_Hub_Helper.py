#BostonHacksHubHelper
from itertools import combinations
from itertools import permutations
import itertools



#list_types=[philosophical, aesthetic, historical, science1, science/social2,individual, global_citizenship, writing_intensive, critical_thinking]
philosophical=["cs111","cs112","cs131","cs132","wr120"]
aesthetic=["ly111", "ly112","ly211", "ly212"]
historical=["wr120", "wr150", "wr151", "wr152"]

list_types=[philosophical, aesthetic, historical]



#function for making 2 lists type combinations
def create_2_hub_combo(a_list): #Will be List_types
    combos=[]

    for i in range(len(a_list)):
         for course in a_list[i]:
             
             for j in range(i +1, len(a_list)):
                 [combos.append((course, coursepairmatch)) for coursepairmatch in a_list[j]] #ALl pairs of 2 from diff hubs
        
    return combos
    
#Make lists of 2 units, adds in classes
def create_2_combo(a_list):#my_list is list_types

    master2list=[]

    permutations={}
    

    for i in range(len(a_list)):         
        for j in range(i +1, len(a_list)):
            permutations['combos'+str(i)+"_"+str(j)] = [set(a_list[i])& set(a_list[j])]

            #If there are no combos, don't add to list
            if permutations['combos'+str(i)+"_"+str(j)]!={}:
                master2list=master2list+ [permutations['combos'+str(i)+"_"+str(j)]] #MAKE INTO DICTIONARY

    return master2list


#function for making 3 lists type combinations
def create_3_hub_combo(a_list):#Will be list_types
    """"input is list_types"""
    combos=[]
    for i in range(len(list_types)):
        for course in list_types[i]:
             
            for j in range(i +1, len(list_types)):
                for k in range(j+1, len(list_types)):
                    [ [combos.append((course, course2, course3))for course3 in list_types[k]] for course2 in list_types[j]]
   
    return combos


#Make lists of three units,adds in classes
def create_3_combo_(a_list): #Will be list_types
    """adds common classes in 3 types of hub units to a masterlist of 3 unit courses"""

    combos=create_3_hub_combo(a_list)

    master3list=[]
    permutations={}
    for x in combos:

       permutations['combos'+x] = [set(combos[x[0]])& set(combos[x[1]]) & set(combos[x[2]])]

        #If there are no combos, don't add to list
       if permutations['combos'+x]!={}:
            master3list=master3list+ [permutations['combos'+x]]


       
    return master3list




