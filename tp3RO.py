from operator import truediv
import matplotlib.pyplot as plt
data_item=[]
data_weight=[]
data_value=[]
n=int(input("Entrer le nombre d'objets:"))
for i in range(n):
    data_item.append('x'+str(i))
    p=int(input("Entrer p"+str(i)+":"))
    data_weight.append(p)
    c=int(input("Entrer u"+str(i)+":"))
    data_value.append(c)
max_weight=int(input("Entrer le poid maximum:"))
data_eff = list(map(truediv, data_value, data_weight))
order = [i[0] for i in sorted(enumerate(data_eff), key=lambda x:x[1], reverse=True)]
#trier les données en fonction de leur efficacité, c'est-à-dire valeur / poids
data_eff = [data_eff[i] for i in order]
data_weight = [data_weight[i] for i in order]
data_value = [data_value[i] for i in order]
data_item = [data_item[i] for i in order]

class State(object):
    def __init__(self, level, benefit, weight, token):
        #jeton = marquage de liste si une tâche est un jeton.
        #disponible = liste marquant toutes les tâches disponibles
        self.level = level
        self.benefit = benefit
        self.weight = weight
        self.token = token
        self.available = self.token[:self.level]+[1]*(len(data_value)-level)
        self.ub = self.evaluation()


    def evaluation(self): #définir la limite supérieure à l'aide d'un sac à dos fractionnaire
        evaluation = 0 #limite supérieure initiale
        weight_accumulate = 0 #poids accumulé utilisé pour arrêter la sommation de la limite supérieure
        for i in range(len(data_weight)):
            if data_weight[i] * self.available[i] <= max_weight - weight_accumulate:
                weight_accumulate += data_weight[i] * self.available[i]
                evaluation += data_value[i] * self.available[i]
            else:
                evaluation += data_value[i] * (max_weight - weight_accumulate) / data_weight[i] * self.available[i]
                break
        return evaluation

    def separation(self):
        level = self.level + 1
        if self.weight + data_weight[self.level] <= max_weight: #s'il n'est pas en surpoids, donnez à l'enfant de gauche
            left_weight = self.weight + data_weight[self.level]
            left_benefit = self.benefit + data_value[self.level]
            left_token = self.token[:self.level]+[1]+self.token[self.level+1:]
            left_child = State(level, left_benefit, left_weight, left_token)
        else: left_child = None
        #de toute façon, donne le bon enfant
        right_child = State(level, self.benefit, self.weight, self.token)
        if left_child != None: 
            return [left_child, right_child]
        else: return [right_child]

Root = State(0, 0, 0, [0]*len(data_value)) #commencer avec rien
waiting_States = [] #liste des états en attente d'être explorés
current_state = Root
while current_state.level < len(data_value):
    waiting_States.extend(current_state.separation())
    waiting_States.sort(key=lambda x: x.ub) #trier la liste d'attente en fonction de leur rang supérieur
    current_state = waiting_States.pop() #explore celui avec le plus grand supérieur
best_solution = current_state
best_item = []
for i in range(len(best_solution.token)):
    if (best_solution.token[i] == 1):
        best_item.append(data_item[i])

print ("Poid total: ", best_solution.weight)
print ("Utilité total: ", best_solution.benefit)
print ("Objets:", best_item)
