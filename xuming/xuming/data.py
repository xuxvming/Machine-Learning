from faker import Faker
import random
import csv
from datetime import date
from datetime import timedelta
from datetime import datetime
from dateutil.parser import parse

fake = Faker()

ITERATIONS = 1000000

def rules(ftime):
    mean = [3,3]
    covariance = [[2,0.9],
                  [0.9,3]]
    if ftime <5:
        goout = int(mean[0] + (ftime - mean[1])*covariance[0][0]/covariance[0][1])
    else:
        goout = random.randint(1,5)
    
    if goout <0:
        goout = abs(goout)
    return goout

Mjob = []
Fjob = []
for i in range(0,5):
    Mjob.append(fake.job())
    Fjob.append(fake.job())

with open('data.csv', 'w',newline='') as csvfile:
    fieldnames = ['course', 'school', 'sex', 'age','address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for i in range(1,ITERATIONS+1):
        print(str(i) + " out of " + str(ITERATIONS) +" records have been created!")
        course = random.choice(["engineering", "computer science", "business", "health science", "math", "physics", "psychology"])
        school = random.choice(["NCI", "TCD", "UCD", "DIT", "UCC", "DCU", "NUI-Galway"])
        gender = random.choice(["m","f"])

        age = random.randint(15,22)
        address = random.choice(["U", "R"])
        
        famsize = random.randint(3,10)
        Pstatus = random.choice(["T", "A"])

        Medu = random.choice([0,1,2,3,4])
        Fedu = random.choice([0,1,2,3,4])

        reason = random.choice(["home", "reputation", "course", "other"])

        Mjobw = random.choice(Mjob)
        Fjobw = random.choice(Fjob)
        guardian =random.choice( ["mother", "father", "other"])

        traveltime = random.randint(1,240)

        studytime = random.randint(1,120)
        failures =  0 if random.random() >= 0.32 else random.randint(1,15)
        schoolsup = "yes" if random.random() >= 0.3 else "no"
        famsup = "yes" if random.uniform(.75, .9) > random.random() else "no"
        paid = "yes" if random.uniform(.1, .2) > random.random() else "no"
        activities = "yes" if random.uniform(.4, .6) > random.random() else "no"

        higher = "yes" if random.uniform(.4, .6) > random.random() else "no"
        internet = "yes" if random.uniform(.9, .98) > random.random() else "no"
        romantic = "yes" if random.uniform(.4, .6) > random.random() else "no"
        famrel = random.randint(1,5)
        freetime = random.randint(1,5)
        goout = rules(freetime)
        Dalc = random.randint(1,5)
        Walc = random.randint(1,5)
        health = random.randint(1,5)

        absences = random.randint(0, 20) if 0.6 > random.random() else random.randint(0, 100)

        G1 = random.randint(40, 100) if 0.7 > random.random() else random.randint(0, 39)
        G2 = random.randint(40, 100) if 0.6 > random.random() else random.randint(0, 39)
        G3 = random.randint(40, 100) if 0.6 > random.random() else random.randint(0, 39)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerow({'course':course, 'school':school, 'sex':gender, 'age':age, 'address':address,'famsize': famsize, 'Pstatus': Pstatus, 'Medu': Medu, 'Fedu': Fedu, 'Mjob': Mjobw, 'Fjob': Fjobw, 'reason': reason, 'guardian': guardian, 'traveltime': traveltime, 'studytime': studytime, 'failures': failures, 'schoolsup': schoolsup, 'famsup': famsup, 'paid': paid, 'activities':activities, 'higher':higher, 'internet':internet, 'romantic':romantic, 'famrel': famrel, 'freetime':freetime, 'goout':goout, 'Dalc':Dalc, 'Walc':Walc, 'health':health, 'absences':absences, 'G1':G1, 'G2':G2, 'G3':G3})