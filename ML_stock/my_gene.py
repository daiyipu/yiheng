#-*- coding: UTF-8 -*-
class TargetString(object):
    '''
    a class saving target string, providing method to give judgement to a guess
    '''
    def __init__(self,str):
        self.str=str
        self.len=len(str)
        self.times=0
    def check(self,str):
        '''
        check whether given str is consist with self.str, and return the number of correct chars.
        '''
        self.times+=1
        #print "%d time(s) guess"%self.times
        #check length,length incorrect, return False
        counter=0
        if len(str)!=self.len:
            print 'TargetString.check-warning: length even wrong'
            return 0, False
            #check equality, if equal, return True 
        if self.str==str:
            return self.len, True
        else:
            for each in zip(self.str,str):
                if each[0]==each[1]:
                    counter+=1
            return counter,False


import random
import numpy as np
from scipy.special import comb
import pprint
import time

class Guessor(object):
    def __init__(self,target_string,init_candidates_number=10000,mutating_rate=0.005,cross_over_rate=0.0005,cross_over_window_size=0.3,char_set=None):
        '''
        parameters
        
        mutating_rate: [0.0-1.0] eg. 0.0005=0.05% the possibility for each character to mutate 
        
        cross_over_rate:[0.0-1.0] eg.0.0005=0.05% percent of whole possible combination(pairs) to apply cross over
        
        cross_over_window_size:[0.0-1.0] to limit the width of fragment to cross_over. It is a percent to length of string.
        eg. cross_over_window_size=0.5 means the width should not excceed half length of string
        
        char_set: char list. customized char set
        
        note
        1. a re-generation function after elimination is neccesarriy to be used, because other wise the population will drop sharply, leaving no candidates to continue iteration.
        2. large mutating_rate will lower the efficiency dramatically. Seems like that high-rating mutation is messing up good candidates selected by previous iteration. 
        3. narrowing the width of fragments to be crossed over will prove performance, especially during the later iterations
        4. more cross_over plus narrow window for cross_over seem like a good combination.
        5. 当迭代到natural_selection函数会保留大多数candidates的时候，应该适当调低变异率，同时适当调高交换率并调小交换窗口
        '''
        self.target_string=target_string
        self.target_len=target_string.len
        self.init_candidates_number=init_candidates_number
        self.mutating_rate=mutating_rate
        self.cross_over_rate=cross_over_rate
        self.cross_over_window_size=cross_over_window_size
        if char_set is None:
                self.char_set=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        else:
            self.char_set=char_set
        self.condidates=[]#contents candidates strings
        self.fitnesses=[]#contents candidates fitness(have same order with self.candidates)
        self.guess_result=''#saving final result(right guess, should equal to self.target_string)
        self.iteration_times=0
        self.report_init_state()
        
        self.mutated=[]#save numbers of mutations done during each mutation process(func: mutation)
        self.crossed_over=[]#save number of pairs which are crossed over
        self.kept=[]#save numbers of condidates kept by each selection process(func: natural_selection)
        self.populations=[]#save populations data during each iteration
        self.regenerated=[]#save number of candidates regenerated each time
        

    def report_init_state(self):
        '''
        print object state(import variables of the object)
        '''
        pprint.pprint({'target_string':'keep screte!','target_len':self.target_len,'init_candidates_number':self.init_candidates_number,'mutating_rate':self.mutating_rate,'cross_over_rate':self.cross_over_rate,'cross_over_window_size':self.cross_over_window_size,'char_set':self.char_set})


    def random_pop(self):
        '''
        return a char randomly(uniform distribution) from self.char_set
        '''
        #import random
        return self.char_set[random.randint(0,len(self.char_set)-1)]

    def generator(self,length,number):
        print 'generator: ready to generate initial generation...(population[%d])'%number
        self.candidates=[]
        new_candidate=''
        for i in range(number):
            for i in range(self.target_len):
                new_candidate+=self.random_pop()
            self.candidates.append(new_candidate)
            new_candidate=''
        print 'generater: [%d] candidates created'%number
        print 'generater: done!'
		

    def guess(self):
        '''
        main function of class Guessor. It uses genetic algorithm to solve 
        the problem. It will call other functions.
        '''
        #generate initial candidates
        self.generator(self.target_len,self.init_candidates_number)
        self.iteration_times=0
        while True:
            print self.candidates
            #statistic
            self.populations.append(len(self.candidates))
            
            print 'gene_guess: current candidates:[%d], iter:[%d]'%(len(self.candidates),self.iteration_times)
            
            self.iteration_times+=1
            #mutation
            self.mutation(self.mutating_rate)
            #cross_over
            self.cross_over(self.cross_over_rate,self.cross_over_window_size)
            #calculate fitness
            if self.cal_fitness()==True:
                print 'gene_guess:guess succeed, quit!'
                return {'answer':self.guess_result,'iteration':self.iteration_times}
            #natural selection
            if self.natural_select()==False:
                print 'gene_guess:guess failed, quit!'
                return {'answer':'','iteration':self.iteration_times}
            #re generate new population based on selected ones
            self.breed(self.init_candidates_number-len(self.candidates))
            time.sleep(1)


    def mutation(self,possibility=0.005):
        #import random
        print "mutation: mutating with possiblity [%f%%]..."%(possibility*100)
        counter=0
        for i in range(len(self.candidates)):
            mutated_candidate=''
            #print self.candidates[i]
            for j in range(len(self.candidates[i])):

                if random.random()<=possibility:#draw possibility, if fall within (0,possibility),randomly mutate
                    mutated_candidate+=self.random_pop()
                    counter+=1
                else:
                    mutated_candidate+=self.candidates[i][j]
                
            self.candidates[i]=mutated_candidate
                #print self.candidates[i]
                #time.sleep(1)
                
            #statistic
        self.mutated.append(counter)
        print "mutation: [%d] chars mutated"%counter
        print "mutation: done!"

    def cross_over(self,possibility=0.0005,window_size=0.3):
        #randomly select two candidates for cross_over operation
        print 'cross_over: randomly selecting pairs for crossing over([%f%%] of all possibility)...'%(possibility*100)
        cross_over_pairs=[]#to save pairs of candidates to be crossed over
        for i in range(int(comb(len(self.candidates),2)*possibility)):#number of pairs to be selected shall be decided by possiblity
            first=random.randint(0,len(self.candidates)-1)
            second=random.randint(0,len(self.candidates)-1)
            if first==second:
                continue
            #if (first,second) not in cross_over_pairs:
            cross_over_pairs.append((first,second))#get one pair, save in

        #statistic
        self.crossed_over.append(len(cross_over_pairs))

        print "cross_over: crossing over [%d] pairs(with max window size[%f])... "%(len(cross_over_pairs),window_size)
        #time.sleep(1)
        #do cross_over
        for i in range(len(cross_over_pairs)):
			#randomly decide the section(start and end positions) to be crossed over
            start_pos=random.randint(0,self.target_len-1)
            if start_pos+self.target_len*window_size>=self.target_len-1:#limit window size of cross over
                end_pos=random.randint(start_pos,self.target_len-1)
            else:
                end_pos=random.randint(start_pos,start_pos+int(self.target_len*window_size))

            #print self.candidates[cross_over_pairs[i][0]]+' <===>'
            #print self.candidates[cross_over_pairs[i][1]] +' cross over........'
            #print 'from [%d] to [%d]'%(start_pos,end_pos)
            #take sections out
            if start_pos==end_pos:
                piece0=self.candidates[cross_over_pairs[i][0]][start_pos]
                piece1=self.candidates[cross_over_pairs[i][1]][start_pos]
            else:
                if end_pos==self.target_len-1:
                    piece0=self.candidates[cross_over_pairs[i][0]][start_pos:]
                    piece1=self.candidates[cross_over_pairs[i][1]][start_pos:]
                else:
                    piece0=self.candidates[cross_over_pairs[i][0]][start_pos:end_pos+1]
                    piece1=self.candidates[cross_over_pairs[i][1]][start_pos:end_pos+1]
                #print 'piece0: '+ piece0
                #print 'piece1: '+ piece1
                #swap sections
            if end_pos==self.target_len-1:
                #self.candidates.append(self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1)
                #self.candidates.append(self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece0)
                self.candidates[cross_over_pairs[i][0]]=self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1
                self.candidates[cross_over_pairs[i][1]]=self.candidates[cross_over_pairs[i][1]][0:start_pos]+piece0
            else:
                #self.candidates.append(self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1\
                #+self.candidates[cross_over_pairs[i][0]][end_pos+1:])
                #self.candidates.append(self.candidates[cross_over_pairs[i][1]][0:start_pos]+piece0\
                #+self.candidates[cross_over_pairs[i][1]][end_pos+1:])
                self.candidates[cross_over_pairs[i][0]]=self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1+self.candidates[cross_over_pairs[i][0]][end_pos+1:]
                self.candidates[cross_over_pairs[i][1]]=self.candidates[cross_over_pairs[i][1]][0:start_pos]+piece0+self.candidates[cross_over_pairs[i][1]][end_pos+1:]				

                #print self.candidates[cross_over_pairs[i][0]]+' <===>'
                #print self.candidates[cross_over_pairs[i][1]] +'  cross overed.......'
                #print 'sections swapped'
                #time.sleep(1)
                
        print 'cross_over: done!'



    def cal_fitness(self):
        print 'cal_fitness: calculating fitnesses...'
        self.fitnesses=[]
        for i in range(len(self.candidates)):
            counter, confirmed=self.target_string.check(self.candidates[i])
            self.fitnesses.append(counter)
            #guess right, save result and return
            if confirmed:
                self.guess_result=self.candidates[i]
                print 'cal_fitness: guess succeed! right answer: '+self.candidates[i]
                return True
        print 'cal_fitness: done!'
        return False

    def natural_select(self):
        print 'natural_select: selecting and eliminating...'
        total_fitness=sum(self.fitnesses)

        #no candidate get even one char right, continue iteration(mutation and cross_over)
        if total_fitness==0:
            print 'nature_selection: all candidates fitness are zero, no elimination, continue interation...'
            return True
		
        #decide randomly(but by a certain possiblity) which candidates shall be keep(others eliminated)
        to_be_kept=[]
        for i in range(len(self.candidates)):
            if random.random()<=(self.fitnesses[i]*1.0/self.target_len):
                to_be_kept.append(i)

        #statistic
        self.kept.append(len(to_be_kept))

        print 'natural_select: [%d] eliminated out of [%d] population ([[%d]] kept)'%(len(self.candidates)-len(to_be_kept),len(self.candidates),len(to_be_kept))
		
        #print to_be_kept
        #print 'total_fitness: %d'%total_fitness
        #time.sleep(1)
        #elimination
        #all keept(hardly possible)
        if len(to_be_kept)==len(self.candidates):
            print 'nature_selection: randomly no selectioin is done!(none of candidiate is eliminated),continue iteration...'
            return True

        new_candidates=[]
        for each in to_be_kept:
            new_candidates.append(self.candidates[each])
        self.candidates=new_candidates

        if len(self.candidates)==0:
            print 'nature_selection: candidates extinct, no more candidates to run further selection'
            return False
        else:
            return True

    def breed(self,amount):
        print 'breed: selecting pairs for mate...'
        #randomly select two candidates for cross_over operation
        cross_over_pairs=[]#to save pairs of candidates to be crossed over and generater
        for i in range(amount/2):#number of candidates to be breed
            first=random.randint(0,len(self.candidates)-1)
            second=random.randint(0,len(self.candidates)-1)
            if first==second:
                continue
            #if (first,second) not in cross_over_pairs:
            cross_over_pairs.append((first,second))#get one pair, save in
        #print cross_over_pairs
        print "breed: [%d] pairs start mating... "%len(cross_over_pairs)
        time.sleep(5)
        #do cross_over and generate new condidates
        counter=0
        for i in range(len(cross_over_pairs)):
            #randomly decide the section(start and end positions) to be crossed over
            start_pos=random.randint(0,self.target_len-1)
            if start_pos+self.target_len/3>=self.target_len-1:#limit window size of cross over
                end_pos=random.randint(start_pos,self.target_len-1)
            else:
                end_pos=random.randint(start_pos,start_pos+self.target_len/3)
            #print self.candidates[cross_over_pairs[i][0]]+' <===>'
            #print self.candidates[cross_over_pairs[i][1]] +' cross over........'
            #print 'from [%d] to [%d]'%(start_pos,end_pos)
            #take sections out
            if start_pos==end_pos:
                piece0=self.candidates[cross_over_pairs[i][0]][start_pos]
                piece1=self.candidates[cross_over_pairs[i][1]][start_pos]
            else:
                if end_pos==self.target_len-1:
                    piece0=self.candidates[cross_over_pairs[i][0]][start_pos:]
                    piece1=self.candidates[cross_over_pairs[i][1]][start_pos:]
                else:
                    piece0=self.candidates[cross_over_pairs[i][0]][start_pos:end_pos+1]
                    piece1=self.candidates[cross_over_pairs[i][1]][start_pos:end_pos+1]
			#print 'piece0: '+ piece0
			#print 'piece1: '+ piece1
			#swap sections
            if end_pos==self.target_len-1:
                self.candidates.append(self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1)
                self.candidates.append(self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece0)
                #self.candidates[cross_over_pairs[i][0]]\
                #=self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1
                #self.candidates[cross_over_pairs[i][1]]\
                #=self.candidates[cross_over_pairs[i][1]][0:start_pos]+piece0
            else:
                self.candidates.append(self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1\
                +self.candidates[cross_over_pairs[i][0]][end_pos+1:])
                self.candidates.append(self.candidates[cross_over_pairs[i][1]][0:start_pos]+piece0\
                +self.candidates[cross_over_pairs[i][1]][end_pos+1:])

                #self.candidates[cross_over_pairs[i][0]]\
                #=self.candidates[cross_over_pairs[i][0]][0:start_pos]+piece1\
                #+self.candidates[cross_over_pairs[i][0]][end_pos+1:]
                #self.candidates[cross_over_pairs[i][1]]\
                #=self.candidates[cross_over_pairs[i][1]][0:start_pos]+piece0\
                #+self.candidates[cross_over_pairs[i][1]][end_pos+1:]				
            counter+=2
            #print self.candidates[cross_over_pairs[i][0]]+' <===>'
            #print self.candidates[cross_over_pairs[i][1]] +'  cross overed.......'

            #print 'sections swapped'
            #time.sleep(1)
        #statistic
        self.regenerated.append(counter)
        print 'bread: [%d] new candidates generated,current total candidates: [%d]'%(counter,len(self.candidates))

        print 'bread: done!'
        #time.sleep(1)


    def save_stats(self,dir='/Users/zhuyu/Documents/',plot=False):
        import pandas as pd
        
        df=pd.DataFrame({'population':self.populations,'mutation':self.mutated,'cross_over':self.crossed_over,'kept':self.kept,'regenerate':self.regenerated})
        
        #df.name=self.target_string.string
        #file_name='str-'+self.target_string.string+'-'
        #df.to_csv('dir+')

    def plot_stats(self):
        import matplotlib.pyplot as plt
        import pandas as pd
        fig=plt.figure()
        ax1=fig.add_subplot(1,1,1)
        #ax1=fig.add_subplot(2,1,1)
        #ax2=fig.add_subplot(2,1,2)

        ax1.plot(np.arange(len(self.populations)),pd.Series(self.populations),c='k',linewidth=3,label='populaltion')
        ax1.plot(np.arange(len(self.mutated)),pd.Series(self.mutated)/self.target_len,c='g',label='mutation/..')
        ax1.plot(np.arange(len(self.crossed_over)),pd.Series(self.crossed_over)/self.init_candidates_number,c='y',label='cross_over/..')
        ax1.plot(np.arange(len(self.kept)),pd.Series(self.kept),c='r',linewidth=2,label='kept')
        ax1.bar(np.arange(len(self.regenerated)),pd.Series(self.regenerated),label='regenerate')
        ax1.legend(loc='best')
        plt.title('gene method process')
        plt.show()

if __name__=="__main__":
    t=TargetString('hello world zhu')
    g=Guessor(t,20000)
    g.guess()
    g.plot_stats()
    












