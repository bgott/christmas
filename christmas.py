import sys
import random
import hashlib
import random as r
import time
import string

names = []
phrase = ' BUYS FOR '
matching_store = {}
frequency_store = {}
type_speed = 500
fast_speed = 1000

def my_shuffle(array):
    copy = array[:]
    random.shuffle(copy)
    return array

def match():
    randomized = names[:]
    random.shuffle(randomized)
    buyers = ''
    for index, name in enumerate(names):
        proposed = randomized[index]
        if (name == proposed):
            return 'conflict'
        else:
            match = name + phrase + proposed
            if (index < (len(names) - 1) ):
                match += '\n'
            buyers += match
    return buyers

def create_matching():
    list = match()
    while (list == 'conflict'):
        list = match()
    return list

def log_matching_results(matchings):
    hash_object = hashlib.md5(matchings.encode())
    hash = hash_object.hexdigest()
    #store frequency of each matching
    if hash in frequency_store:
        frequency_store[hash] += 1
    else:
        frequency_store[hash] = 1
    #store each matching
    if not hash in matching_store:
        matching_store[hash] = matchings

def run_matchings(keep_iterating):
    while(keep_iterating):
        log_matching_results(create_matching())
        keep_iterating -= 1

def print_tree():
    #get input
    n = 25
    #make the top of the tree
    #print(n*' '+'/\\')
    slow_type(n*' '+'/\\',fast_speed)
    #this loop draws the entire tree's body--
    #--------------------------------
    for i in range(1,n):
        #s is stored as a string of length i*2 with * and ~ in random positions, this is used for the body of the tree
        s = ''.join(r.choice(['*','~',r.choice(['o','+','*','~'])]) for i in range(i*2))
        #string sl and sr holds the random string for the left and right side boundary of the tree's body
        sl = r.choice(['/','+'])
        sr = r.choice(['\\','o'])
        #print all of 'em at last
        slow_type((n-i)*' '+sl+s+sr, fast_speed)
    #print the trunk
    slow_type((n-1)*' ' + '\'||\'', fast_speed)
    slow_type((n-1)*' ' + '\'||\'', fast_speed)
    slow_type((n-1)*' ' + '\'||\'' + '\n', fast_speed)
    #print the ground
    #print(' '+n*2*'-')

def display_matching_results():
    sorted_frequency_store = sorted(frequency_store, key=frequency_store.get, reverse=True)
    winner = sorted_frequency_store[0]
    slow_type(matching_store, type_speed)
    slow_type(frequency_store, type_speed)
    print '\n*\n*\n*\n*\n*\n*-*-*-*-*-*-*-*-*-*-*-RESULTS-*-*-*-*-*-*-*-*-*-*-*\n'
    print_tree()
    slow_type(matching_store[winner], type_speed)
    print '\n\n*-*-*-*-*-*-*-*-*-*-END RESULTS-*-*-*-*-*-*-*-*-*-*\n'

def slow_type(obj,speed):
    for x in obj:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(r.random()*10.0/speed)
    print ''


names = raw_input('List all your christmas gift participants (separated by commas) ').split(",")
iterations = input('How many time would you like to shuffle the names up? (we will choose the most frequent matching) ')
run_matchings(iterations)
display_matching_results()
