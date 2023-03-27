import random


#class of a population 
class pop:
  def __init__(self, chromo, fitness):
    self.chromo = chromo
    self.fitness = fitness


  def set_fitness(self, x):
        self.fitness = x

  def set_chromo(self, x):
        self.chromo = x


  def get_fitness(self):
        return self.fitness
  
  def get_chromo(self):
        return self.chromo




def printPOP(pop):
  printRep(pop.chromo)
  print("Fitness:",pop.fitness)
  print()



def printRep(pop):
 
    rep=[[' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],]
    
    print(pop)

    for i in range(0,8):
     rep[8-pop[i]][i]="Q"


    for i in range(8):
     print(rep[i])
     

#helper for chromo() method
def randint():
 list1=[1,2,3,4,5,6,7,8]
 return random.choice(list1)  


#for random chromosome generation
def chromo():
  return [randint(),randint(),randint(),randint(),randint(),randint(),randint(),randint()]



 
    

    
#calculating fitness of a population by finding number of non attacking pairs
def fitness(pop):
  fitness=0
  for i in range(8):
    popVal=pop[i]
    popUp=pop[i]
    popLow=pop[i]

    for j in range(i+1,8):
      popUp+=1
      popLow-=1
      if pop[j]!=popVal and pop[j]!=popUp and pop[j]!=popLow:
        fitness+=1


  return fitness


#this function chooses 2 parents using roulette wheel method
def rouletteWheel(pop1,pop2,pop3,pop4):

  totalFit=pop1.fitness+pop2.fitness+pop3.fitness+pop4.fitness

  #calculating probabilities of every population
  prob1=pop1.fitness/totalFit
  prob2=pop2.fitness/totalFit
  prob3=pop3.fitness/totalFit
  prob4=pop4.fitness/totalFit
  
  #calculating cumulative probability to imitate roulette wheel
  cumProb1=prob1
  cumProb2=prob1+prob2
  cumProb3=prob1+prob2+prob3
  cumProb4=prob1+prob2+prob3+prob4
  
  
  #spinning the roulette wheel for parent1
  randNum=random.uniform(0, 1)
  
  if randNum<cumProb1:
    parent1=pop1

  elif   randNum>cumProb1 and randNum<=cumProb2:
    parent1=pop2 

  elif   randNum>cumProb2 and randNum<=cumProb3:
    parent1=pop3 

  elif   randNum>cumProb3 and randNum<=cumProb4:
    parent1=pop4 

  #spinning the roulette wheel for parent2
  randNum=random.uniform(0, 1)
  
  if randNum<cumProb1:
    parent2=pop1

  elif   randNum>cumProb1 and randNum<=cumProb2:
    parent2=pop2 

  elif   randNum>cumProb2 and randNum<=cumProb3:
    parent2=pop3 

  elif   randNum>cumProb3 and randNum<=cumProb4:
    parent2=pop4 

      

  return parent1,parent2


#this function mutates a specific population
def mutation(childChromo1):
  list1=[0,1,2,3,4,5,6,7]
  list2=[1,2,3,4,5,6,7,8]
  mutIndex=random.choice(list1)

  mutIndexVal=childChromo1[mutIndex]
  list2.remove(mutIndexVal)

  mutVal=random.choice(list2)
  
  childChromo1[mutIndex]=mutVal

  return childChromo1
   

#this method is used to apply crossover and mutation
def crossOver( parent1, parent2):
  
  #crossover
  list1=[1,2,3,4,5,6,7]

  crossPoint=random.choice(list1)  #for choosing random crossover point

  child1=pop(0,0)
  child2=pop(0,0)
  
  chromo1=parent1.get_chromo()
  chromo2=parent2.get_chromo()
  
  #the first child after crossover
  childChromo1=chromo1[:crossPoint]
  childChromo1.extend(chromo2[crossPoint:])
  

  #the second child after crossover
  childChromo2=chromo2[:crossPoint]
  childChromo2.extend(chromo1[crossPoint:])


  
  


  #mutation for child1
  childChromo1=mutation(childChromo1)  #for choosing random mutation

  #mutation for child2
  childChromo2=mutation(childChromo2)  #for choosing random mutation
  


  #calculating child fitness
  child1.set_chromo(childChromo1)
  child2.set_chromo(childChromo2)
  
  child1.set_fitness(fitness(childChromo1))
  child2.set_fitness(fitness(childChromo2))

  return parent1,parent2,child1,child2









def main():
  #defining 4 random populations
  pop1=pop(chromo(),0)
  pop1.set_fitness(fitness(pop1.chromo))

  pop2=pop(chromo(),0)
  pop2.set_fitness(fitness(pop2.chromo))

  pop3=pop(chromo(),0)
  pop3.set_fitness(fitness(pop3.chromo))

  pop4=pop(chromo(),0)
  pop4.set_fitness(fitness(pop4.chromo))

  print("The Initial population is:")
  printPOP(pop1)
      
  printPOP(pop2)
        
  printPOP(pop3)
        
  printPOP(pop4)

  iteration=0
  while(1):
    
    
    

    
    #print("The parents are:")
    parent1,parent2=rouletteWheel(pop1,pop2,pop3,pop4)

    #printPOP(parent1)
    #printPOP(parent2)

    
    pop1,pop2,pop3,pop4=crossOver(parent1,parent2)

    if pop1.get_fitness()==28:
       print("Best population generation:",iteration)
       printPOP(pop1)
       break
    
    elif pop2.get_fitness()==28:
       print("Best population generation:",iteration)
       printPOP(pop2)
       break
    
    elif pop3.get_fitness()==28:
       print("Best population generation:",iteration)
       printPOP(pop3)
       break
    
    elif pop4.get_fitness()==28:
       print("Best population generation:",iteration)
       printPOP(pop4)

       break
    
    iteration+=1
    

    

main()
