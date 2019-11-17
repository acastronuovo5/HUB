#BostonHacksHubHelper
from itertools import combinations


#list_types=[philosophical, aesthetic, historical, science1, science/social2,individual, global_citizenship, writing_intensive, critical_thinking]
#philosophical=["cs111","cs112","cs131","cs132"]
#aesthetic=["ly111", "ly112","ly211", "ly212"]
#historical=["wr120", "wr150", "wr151", "wr152"]
#list_types=[philosophical, aesthetic, historical]



#function for making 2 lists type combinations
def create_2_hub_combo(a_list): #Will be List_types
    combos=()
    
    for combo in combinations(a_list, 2):  # 2 for pairs, 3 for triplets, etc
        
        combos=combos+combo
        
    return combos
    
#Make lists of 2 units, adds in classes
def create_2_combo(a_list):#my_list is list_types
    combos=create_2_hub_combo(a_list)

    master2list=[]

    permutations={}
    
    for x in combos:

       permutations['combos'+x] = [set(combos[x[0]])& set(combos[x[1]])]

        #If there are no combos, don't add to list
       if permutations['combos'+x]!={}:
            master2list=master2list+ [permutations['combos'+x]]
        
    return master2list


#function for making 3 lists type combinations
def create_3_hub_combo(a_list):#Will be list_types
    """"input is lis_types"""
    combos=()
    for combo in combinations(a_list,3):  # 2 for pairs, 3 for triplets, etc
        combos=combos+combo
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




