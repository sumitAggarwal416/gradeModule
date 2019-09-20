'''
I, Sumit Aggarwal, student number:0007893607, certify that all code submitted is my own code, that I have not copied it
from any other source. I also certify that I have not allowed any one else to copy my code.
'''
lab_wt= int(input("Enter the weight of labs in the course: "))
labs= int(input("Enter the number of labs in your course: "))
assignment_wt= int(input("Enter the weight of assignments in your course: "))
assignments=int(input("Number of assignments in your course? "))
exam_wt= int(input("What is the weight of the exams in your course? "))
exams= int(input("Number of exams in your course? "))

#x is the number of grades entered by the user

def exam_avg():
    x=1
    total=0
    while x<=exams:
        grade=float(input("Enter your grade in exam {}/{} ".format(x,exams)))
        if grade==-1:
            x-=1
            break
        else:
            total+=grade
            #avg= total/x
            if exams==1:
                break
            elif exams>1:
                x+=1
            else:
                break       
    exam_wt_each= exam_wt/exams
    global exam_total
    exam_total= x*exam_wt_each
    global exam_earned
    exam_earned= total*exam_wt_each
    global your_score1
    your_score1= (total*exam_wt_each)/100
    global total_score3
    total_score3=x*exam_wt_each
    
    
    

def assignment_avg():
    x=1
    total=0
    while x<=assignments:
        grade=float(input("Enter your grade in assignment #{}/{} ".format(x,assignments)))
        if grade==-1:
            x-=1
            break
        else:
            total+=grade
            #avg= total/x
            if assignments==1:
                break
            elif assignments>1:
                x+=1
            else:
                break  
    assignment_wt_each= assignment_wt/assignments
    global assignment_total
    assignment_total= x*assignment_wt_each
    global assignment_earned
    assignment_earned= total*assignment_wt_each
    global your_score2
    your_score2= (total*assignment_wt_each)/100
    global total_score2
    total_score2=x*assignment_wt_each
    
    
    

def lab_avg():
    x=1
    total=0
    while x<=labs:
        grade=float(input("Enter your grade in lab {}/{} ".format(x,labs)))
        if grade==-1:
            x-=1
            break
        else:
            total+=grade
            #avg= total/x
            if labs==1:
                break
            elif labs>1:
                x+=1
            else:
                break  
    lab_wt_each= lab_wt/labs
    global lab_total
    lab_total= x*lab_wt_each
    global lab_earned
    lab_earned= total*lab_wt_each
    global your_score3
    your_score3=(total*lab_wt_each)/100
    global total_score1
    total_score1=x*lab_wt_each
    

lab_avg()
assignment_avg()
exam_avg()
total_score=round(your_score1+your_score2+your_score3,1)
score=round(total_score1+total_score2+total_score3,1)

average = round((lab_earned + assignment_earned + exam_earned)/(lab_total + assignment_total + exam_total),1)
#print(average)

if average>=90:
    message="Letter grade A"
elif average>=75 and average<90:
    message="Letter grade B"
elif average>=60 and average<75:
    message="Letter grade C"
elif average>=50 and average<60:
    message="Letter grade D"
else:
    message="Letter grade F"

print("You got "+ str(total_score) + " out of " + str(score) + " and your average is " + str(average) + " "  + message)


            
