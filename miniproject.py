import os
import time
import conn
class Main():
    def __init__(self):
        self.teacher=['Nayan','1234']
        self.student={}
        self.assignment=[]
        self.submissions=[]
        self.peergraded={}
    def maincontent(self):
        while True:
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|\t---------  PEER GRADE SYSTEM  ---------\t\t|")
            print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|\t\t1. Teacher Login\t\t\t|\n\t\t\t\t|\t\t2. Student Login\t\t\t|\n\t\t\t\t|\t\t3. Student Register\t\t\t|\n\t\t\t\t|\t\t4. Exit\t\t\t\t\t|")
            print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t\t\tEnter your choice : - ",end="")
            choice=input()
            try:
                choice=int(choice)
            except:
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t|\t\tINVALID INPUT!!!!!!!!!!\t\t      |")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                time.sleep(1)
                continue
            if(choice==1):
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t|\t---------------  LOGIN  ---------------\t\t|")
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t\tEnter username : - ",end="")
                name=input()
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t\tEnter password : - ",end="")
                password=input()
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t|\t\tPLEASE WAIT ........\t\t\t|")
                print("\t\t\t\t---------------------------------------------------------")
                time.sleep(1)
                if(name==self.teacher[0] and password==self.teacher[1]):
                    print("\t\t\t\t|\t\tLogin Successfull!!!\t\t\t|")
                    print("\t\t\t\t---------------------------------------------------------")
                    time.sleep(1)
                    while True:
                        os.system("CLS")
                        print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t|\t---------  OPTIONS FOR TEACHER  ---------\t|")
                        print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t|\t\t1. Create assignment\t\t\t|\n\t\t\t\t|\t\t2. Show assignments\t\t\t|\n\t\t\t\t|\t\t3. Show submissions\t\t\t|\n\t\t\t\t|\t\t4. Mark assignment\t\t\t|\n\t\t\t\t|\t\t5. Logout\t\t\t\t|")
                        print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t\t\tEnter your choice : - ",end="")
                        choi=input()
                        try:
                            choi=int(choi)
                        except:
                            os.system("CLS")
                            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                            print("\t\t\t\t|\t\t\t\t\t\t      |")
                            print("\t\t\t\t*******************************************************")
                            print("\t\t\t\t-------------------------------------------------------")
                            print("\t\t\t\t|\t\tINVALID INPUT!!!!!!!!!!\t\t      |")
                            print("\t\t\t\t-------------------------------------------------------")
                            print("\t\t\t\t*******************************************************")
                            print("\t\t\t\t|\t\t\t\t\t\t      |")
                            print("\t\t\t\t*******************************************************")
                            time.sleep(1)
                            continue
                        if(choi==1):
                            os.system("CLS")
                            self.createassignment()
                        elif(choi==2):
                            os.system("CLS")
                            self.showassignment()
                        elif(choi==3):
                            os.system("CLS")
                            self.showsubmissions()
                        elif(choi==4):
                            os.system("CLS")
                            self.markings()
                        elif(choi==5):
                            os.system("CLS")
                            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                            print("\t\t\t\t|\t\t\t\t\t\t      |")
                            print("\t\t\t\t*******************************************************")
                            print("\t\t\t\t-------------------------------------------------------")
                            print("\t\t\t\t|\t\tLOGOUT SUCCESSFULL!!!!\t\t      |")
                            print("\t\t\t\t-------------------------------------------------------")
                            print("\t\t\t\t*******************************************************")
                            print("\t\t\t\t|\t\t\t\t\t\t      |")
                            print("\t\t\t\t*******************************************************")
                            time.sleep(1)
                            break
                        else:
                            os.system("CLS")
                            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                            print("\t\t\t\t|\t\t\t\t\t\t      |")
                            print("\t\t\t\t*******************************************************")
                            print("\t\t\t\t-------------------------------------------------------")
                            print("\t\t\t\t|\t   PLEASE ENTER A VALID NUMBER!!!\t      |")
                            print("\t\t\t\t-------------------------------------------------------")
                            print("\t\t\t\t*******************************************************")
                            print("\t\t\t\t|\t\t\t\t\t\t      |")
                            print("\t\t\t\t*******************************************************")
                            time.sleep(1)
                            continue
                else:
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|\t\tINVALID CREDENTIALS!!!!\t\t      |")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    time.sleep(1)
            elif(choice==2):
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t|\t---------------  LOGIN  ---------------\t\t|")
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t      Enter roll number : - ",end="")
                name=input()
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t\tEnter password : - ",end="")
                password=input()
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t\tPLEASE WAIT ........")
                print("\t\t\t\t---------------------------------------------------------")
                time.sleep(1)
                self.student=conn.give_results()
                if(name in self.student.keys()):
                    if(self.student[name]==password):
                        print("\t\t\t\t\t\tLogin Successfull!!!")
                        print("\t\t\t\t---------------------------------------------------------")
                        time.sleep(1)
                        while True:
                            os.system("CLS")
                            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t|\t---------  OPTIONS FOR STUDENTS  ---------\t|")
                            print("\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t|\t\t1. Submit assignment\t\t\t|\n\t\t\t\t|\t\t2. Grade peers\t\t\t\t|\n\t\t\t\t|\t\t3. View marks\t\t\t\t|\n\t\t\t\t|\t\t4. Logout\t\t\t\t|")
                            print("\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t\t\tEnter your choice : - ",end="")
                            ch=input()
                            try:
                                ch=int(ch)
                            except:
                                os.system("CLS")
                                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                                print("\t\t\t\t|\t\t\t\t\t\t      |")
                                print("\t\t\t\t*******************************************************")
                                print("\t\t\t\t-------------------------------------------------------")
                                print("\t\t\t\t|\t\tINVALID INPUT!!!!!!!!!!\t\t      |")
                                print("\t\t\t\t-------------------------------------------------------")
                                print("\t\t\t\t*******************************************************")
                                print("\t\t\t\t|\t\t\t\t\t\t      |")
                                print("\t\t\t\t*******************************************************")
                                time.sleep(1)
                                continue
                            if(ch==1):
                                os.system("CLS")
                                self.submitassignment(name)
                            elif(ch==2):
                                os.system("CLS")
                                self.givemarks(name)
                            elif(ch==3):
                                os.system("CLS")
                                self.showmarks(name)
                            elif(ch==4):
                                os.system("CLS")
                                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                                print("\t\t\t\t|\t\t\t\t\t\t      |")
                                print("\t\t\t\t*******************************************************")
                                print("\t\t\t\t-------------------------------------------------------")
                                print("\t\t\t\t|\t\tLOGOUT SUCCESSFULL!!!!\t\t      |")
                                print("\t\t\t\t-------------------------------------------------------")
                                print("\t\t\t\t*******************************************************")
                                print("\t\t\t\t|\t\t\t\t\t\t      |")
                                print("\t\t\t\t*******************************************************")
                                time.sleep(1)
                                break
                            else:
                                os.system("CLS")
                                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                                print("\t\t\t\t|\t\t\t\t\t\t      |")
                                print("\t\t\t\t*******************************************************")
                                print("\t\t\t\t-------------------------------------------------------")
                                print("\t\t\t\t|\t   PLEASE ENTER A VALID NUMBER!!!\t      |")
                                print("\t\t\t\t-------------------------------------------------------")
                                print("\t\t\t\t*******************************************************")
                                print("\t\t\t\t|\t\t\t\t\t\t      |")
                                print("\t\t\t\t*******************************************************")
                                time.sleep(1)
                                continue
                    else:
                        os.system("CLS")
                        print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                        print("\t\t\t\t|\t\t\t\t\t\t      |")
                        print("\t\t\t\t*******************************************************")
                        print("\t\t\t\t-------------------------------------------------------")
                        print("\t\t\t\t|\t\tINVALID PASSWORD!!!!\t\t      |")
                        print("\t\t\t\t-------------------------------------------------------")
                        print("\t\t\t\t*******************************************************")
                        print("\t\t\t\t|\t\t\t\t\t\t      |")
                        print("\t\t\t\t*******************************************************")
                        time.sleep(1)
                else:
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|\t\tINVALID CREDENTIALS!!!!\t\t      |")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    time.sleep(1)
            elif(choice==3): 
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t|\t--------------- REGISTER --------------\t\t|")
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t      Enter roll number : - ",end="")
                name=input()
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t\tEnter password : - ",end="")
                password=input()
                print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\t\tPLEASE WAIT ......")
                print("\t\t\t\t---------------------------------------------------------")
                time.sleep(1)
                self.student=conn.give_results()
                if(name in self.student.keys()):
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|\t     ROLL NUMBER ALREADY EXISTS!!!!\t      |")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    time.sleep(1)
                else:
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|\t       REGISTERED SUCCESSFULLY!!!!\t      |")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    time.sleep(1)
                    # self.student[name]=password
                    conn.insert(name,password)
            elif(choice==4):
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t|\t   THANK YOU FOR USING PORTAL!!!\t      |")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                time.sleep(1)
                break
            else:
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t|\t\tINVALID INPUT!!!!!!!!!!\t\t      |")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                time.sleep(1)
    def createassignment(self):
        os.system("CLS")
        print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
        print("\t\t\t\t|\t--------- ASSIGNMENT CREATION --------\t\t|")
        print("\t\t\t\t---------------------------------------------------------")
        print("\t\t\t\t\t      Enter assignment name : - ",end="")
        aname=input()
        print("\t\t\t\t---------------------------------------------------------")
        print("\t\t\t\t\t\tEnter maximum marks : - ",end="")
        marks=input()
        print("\t\t\t\t---------------------------------------------------------")
        print("\t\t\t\t|\t\tPLEASE WAIT ......\t\t\t|")
        print("\t\t\t\t---------------------------------------------------------")
        print("\t\t\t\t|           ASSIGNMENT CREATED SUCCESSFULLY!!!\t\t|")
        print("\t\t\t\t---------------------------------------------------------")
        time.sleep(1)
        temp=[aname,marks]
        self.assignment.append(temp)
    def showassignment(self):
        if(len(self.assignment)!=0):
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|\t--------- ASSIGNMENTS CREATED --------\t\t|")
            print("\t\t\t\t---------------------------------------------------------")
            for i in self.assignment:
                print("\t\t\t\t\t\tSubject : - ",i[0])
                print("\t\t\t\t\t\tMaximum marks : - ",i[1])
                print("\t\t\t\t---------------------------------------------------------")
            input("\t\t\t\t\t\tPress Enter to continue...")
        else:
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t|\t   NO ASSIGNMENTS CREATED YET!!!!\t      |")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            time.sleep(1)
    def submitassignment(self,name):
        if(len(self.assignment)!=0):
            flag=1
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|      --------------SUBMIT ASSIGNMENT---------------\t|")
            print("\t\t\t\t---------------------------------------------------------")
            for i in range(len(self.assignment)):
                print("\t\t\t\t\t\t",(i+1),". ",self.assignment[i][0],"\n\t\t\t\t\t\tMaximum marks : ",self.assignment[i][1])
                print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t\tWhich assignment do you want to submit : - ",end="")
            sub=int(input())
            print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t\t\tPLEASE WAIT ......")
            print("\t\t\t\t---------------------------------------------------------")
            os.system("CLS")
            if((sub-1)<len(self.assignment)):
                for i in self.submissions:
                    if(i[0]==name and i[1]==self.assignment[sub-1][0] and len(i[2])>0):
                        os.system("CLS")
                        print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t|      --------------Already Submitted---------------\t|")
                        print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t\t\tAssignment name : - ",self.assignment[sub-1][0])
                        print("\t\t\t\t\t\tMaximum marks : - ",self.assignment[sub-1][1])
                        print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t\tYour submission : - ",i[2])
                        print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\tYou have already submitted this assignment do you want to")
                        print("\t\t\t\t\t\treplace (1. Yes 2. No) : - ",end=" ")
                        flag=int(input())
                        print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t\t\tPLEASE WAIT ......")
                        print("\t\t\t\t---------------------------------------------------------")
                        time.sleep(1)
                        if(flag==1):
                            self.submissions.remove(i)
                            break
                if(flag==1):
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                    print("\t\t\t\t|      --------------SUBMIT ASSIGNMENT---------------\t|")
                    print("\t\t\t\t---------------------------------------------------------")
                    print("\t\t\t\t\t\tAssignment name : - ",self.assignment[sub-1][0])
                    print("\t\t\t\t\t\tMaximum marks : - ",self.assignment[sub-1][1])
                    print("\t\t\t\t---------------------------------------------------------")
                    print("\t\t\t\t\tEnter all the content : - ",end=" ")        
                    content=input()
                    print("\t\t\t\t---------------------------------------------------------")
                    tempsub=[name,self.assignment[sub-1][0],content,0,0,0," "," "]
                    self.submissions.append(tempsub)
                    print("\t\t\t\t\t\tPLEASE WAIT ......")
                    print("\t\t\t\t---------------------------------------------------------")
                    print("\t\t\t\t|         ASSIGNMENT SUBMITTED SUCCESSFULLY!!!\t\t|")
                    print("\t\t\t\t---------------------------------------------------------")
                    time.sleep(1)
            else:
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t|\t   PLEASE ENTER A VALID NUMBER!!!\t      |")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                time.sleep(1)
        else:
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t|\t   NO ASSIGNMENTS CREATED YET!!!!\t      |")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            time.sleep(1)
    def showsubmissions(self):
        if(len(self.submissions)!=0):
            count=0
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|\t------------- SUBMISSIONS ------------\t\t|")
            print("\t\t\t\t---------------------------------------------------------")
            for i in range(len(self.assignment)):
                print("\t\t\t\t\t\t",(i+1),". ",self.assignment[i][0],"\n\t\t\t\t\t\tMaximum marks : ",self.assignment[i][1])
                print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\tWhich assignments submission do you want to see : - ",end="")
            sub=int(input())
            print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t\t\tPLEASE WAIT ......")
            print("\t\t\t\t---------------------------------------------------------")
            if((sub-1)<len(self.assignment)):
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t|      ------------SUBMITTED ASSIGNMENTS-------------\t|")
                print("\t\t\t\t---------------------------------------------------------")
                for i in self.submissions:
                    if(i[1]==self.assignment[sub-1][0]):
                        count=count+1
                        print("\t\t\t\t\t\tRoll number : - ",i[0])
                        print("\t\t\t\t\t\tAssignment name : - ",self.assignment[sub-1][0])
                        print("\t\t\t\t\t\tMaximum marks : - ",self.assignment[sub-1][1])
                        print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t\tAssignment submitted : - ",i[2])
                        print("\t\t\t\t---------------------------------------------------------")
                        if(i[3]==0 and i[4]==0):
                            print("\t\t\t\t\tMarks given by students : - NA  , NA")
                            print("\t\t\t\t---------------------------------------------------------")
                        elif(i[3]!=0 and i[4]==0):
                            print("\t\t\t\t\tMarks given by students : - ",i[3]," ,  NA")
                            print("\t\t\t\t\tMarks given by (Roll No) : - ",i[6]," ,  NA")
                            print("\t\t\t\t---------------------------------------------------------")
                        else:
                            print("\t\t\t\t\tMarks given by students : - ",i[3]," ,  ",i[4])
                            print("\t\t\t\t\tMarks given by (Roll No) : - ",i[6]," ,  ",i[7])
                            print("\t\t\t\t---------------------------------------------------------")
                        if(i[5]==0):
                            print("\t\t\t\t\tMarks given by you : Not given")
                            print("\t\t\t\t---------------------------------------------------------")
                        else:
                            print("\t\t\t\t\tMarks given by you : - ",i[5])
                            if(i[3]!=0 and i[4]!=0 and i[5]!=0):
                                print("\t\t\t\t\tTotal marks obtained : - ",float((i[3]+i[4]+i[5]))/3)
                            print("\t\t\t\t---------------------------------------------------------")
                        print("\t\t\t\t---------------------------------------------------------")
                print("\t\t\t\t\tTotal number of submission till now = ",count)
                print("\t\t\t\t---------------------------------------------------------")
                input("\t\t\t\t\t\tPress Enter to continue...")
            else:
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t|\t   PLEASE ENTER A VALID NUMBER!!!\t      |")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                time.sleep(1)
        else:
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t|\t   NO ASSIGNMENTS SUBMITTED YET!!\t      |")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            time.sleep(1)
    def markings(self):
        if(len(self.submissions)!=0):
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|\t--------------- MARKINGS -------------\t\t|")
            print("\t\t\t\t---------------------------------------------------------")
            for i in range(len(self.assignment)):
                print("\t\t\t\t\t\t",(i+1),". ",self.assignment[i][0],"\n\t\t\t\t\t\tMaximum marks : ",self.assignment[i][1])
                print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\tFor which assignment do you want to give marks : -  ",end="")
            sub=int(input())
            print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t\t\tPLEASE WAIT ......")
            print("\t\t\t\t---------------------------------------------------------")
            if((sub-1)<len(self.assignment)):
                os.system("CLS")
                flag=0
                flag1=0
                for i in self.submissions:
                        if(i[1]==self.assignment[sub-1][0]):
                            if(i[5]==0):
                                flag1=1
                                break
                if(flag1==1):
                    for i in self.submissions:
                        if(i[1]==self.assignment[sub-1][0]):
                            if(i[5]==0):
                                os.system("CLS")
                                print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                                print("\t\t\t\t|      ------------SUBMITTED ASSIGNMENTS-------------\t|")
                                print("\t\t\t\t---------------------------------------------------------")
                                print("\t\t\t\t\t\tRoll number : - ",i[0])
                                print("\t\t\t\t\t\tAssignment name : - ",self.assignment[sub-1][0])
                                print("\t\t\t\t\t\tMaximum marks : - ",self.assignment[sub-1][1])
                                print("\t\t\t\t---------------------------------------------------------")
                                print("\t\t\t\t\tAssignment submitted : - ",i[2])
                                print("\t\t\t\t---------------------------------------------------------")
                                if(i[3]==0 and i[4]==0):
                                    print("\t\t\t\t\tMarks given by students : - NA  , NA")
                                    print("\t\t\t\t---------------------------------------------------------")
                                elif(i[3]!=0 and i[4]==0):
                                    print("\t\t\t\t\tMarks given by students : - ",i[3]," ,  NA")
                                    print("\t\t\t\t\tMarks given by (Roll No) : - ",i[6]," ,  NA")
                                    print("\t\t\t\t---------------------------------------------------------")
                                else:
                                    print("\t\t\t\t\tMarks given by students : - ",i[3]," ,  ",i[4])
                                    print("\t\t\t\t\tMarks given by (Roll No) : - ",i[6]," ,  ",i[7])
                                    print("\t\t\t\t---------------------------------------------------------")
                                while(True):
                                    print("\t\t\t\t\tEnter marks or -1(exit) : - ",end=" ")
                                    marks=float(input())
                                    if(marks<=float(self.assignment[sub-1][1])):
                                        if(marks==float(-1)):
                                            flag=1
                                            break
                                        else:
                                            i[5]=marks
                                            print("\t\t\t\t---------------------------------------------------------")
                                            print("\t\t\t\t\t\tMarks given successfully!!!!!")
                                            print("\t\t\t\t---------------------------------------------------------")
                                            input("\t\t\t\t\t\tPress Enter to continue...")
                                            break
                                    else:
                                        print("\t\t\t\t---------------------------------------------------------")
                                        print("\t\t\t\t\tMarks entered are greater than maximum marks!!")
                                        print("\t\t\t\t---------------------------------------------------------")
                            if(flag==1):
                                break        
                else:
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|\t   NOTHING LEFT TO GRADE!!!!!!!\t\t      |")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    time.sleep(1)
            else:
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t|\t   PLEASE ENTER A VALID NUMBER!!!\t      |")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                time.sleep(1)
        else:
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t|\t   NO ASSIGNMENTS SUBMITTED YET!!\t      |")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            time.sleep(1)
    def showmarks(self,name):
        if(len(self.assignment)!=0):
            flag=0
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|      -----------------SHOW MARKS----------------   \t|")
            print("\t\t\t\t---------------------------------------------------------")
            for i in range(len(self.assignment)):
                print("\t\t\t\t\t\t",(i+1),". ",self.assignment[i][0],"\n\t\t\t\t\t\tMaximum marks : ",self.assignment[i][1])
                print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\tFor which assignment do you want to see marks : - ",end=" ")
            sub=int(input())
            print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t\t\tPLEASE WAIT ......")
            print("\t\t\t\t---------------------------------------------------------")
            time.sleep(1)
            os.system("CLS")
            if((sub-1)<len(self.assignment)):
                os.system("CLS")
                for i in self.submissions:
                    if(i[0]==name and i[1]==self.assignment[sub-1][0]):
                        if(i[3]==0 or i[4]==0 or i[5]==0):
                            flag=1
                            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t|      ----------------MARKS OBTAINED----------------\t|")
                            print("\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t\t\tAssignment name : - ",self.assignment[sub-1][0])
                            print("\t\t\t\t\t\tMaximum marks : - ",self.assignment[sub-1][1])
                            print("\t\t\t\t\t\tYour submission : - ",i[2])
                            print("\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t\tMarks given by your peers : - NA     NA")
                            print("\t\t\t\t\t\tMarks given by teacher : - NA")
                            print("\t\t\t\t---------------------------------------------------------")
                            input("\t\t\t\t\t\tPress Enter to continue...")
                        else:
                            flag=1
                            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t|      ----------------MARKS OBTAINED----------------\t|")
                            print("\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t\t\tAssignment name : - ",self.assignment[sub-1][0])
                            print("\t\t\t\t\t\tMaximum marks : - ",self.assignment[sub-1][1])
                            print("\t\t\t\t\t\tYour submission : - ",i[2])
                            print("\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t\tMarks given by your peers : - ",i[3]," ,  ",i[4])
                            print("\t\t\t\t\t\tMarks given by teacher : - ",i[5])
                            print("\t\t\t\t---------------------------------------------------------")
                            print("\t\t\t\t\t\tTotal marks obtained : -  ",float((i[3]+i[4]+i[5]))/3)
                            print("\t\t\t\t---------------------------------------------------------")
                            input("\t\t\t\t\t\tPress Enter to continue...")
                if(flag==0):
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|\t   NO ASSIGNMENTS SUBMITTED!!!!!!\t      |")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    time.sleep(1)
            else:
                os.system("CLS")
                print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t|\t   PLEASE ENTER A VALID NUMBER!!!\t      |")
                print("\t\t\t\t-------------------------------------------------------")
                print("\t\t\t\t*******************************************************")
                print("\t\t\t\t|\t\t\t\t\t\t      |")
                print("\t\t\t\t*******************************************************")
                time.sleep(1)
        else:
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t|\t   NO ASSIGNMENTS CREATED YET!!!!\t      |")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            time.sleep(1)
    def givemarks(self,name):
        if(len(self.submissions)!=0):
            count=0
            t=0
            flagtemp=0
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t|\t--------------- MARKINGS -------------\t\t|")
            print("\t\t\t\t---------------------------------------------------------")
            for i in range(len(self.assignment)):
                print("\t\t\t\t\t\t",(i+1),". ",self.assignment[i][0],"\n\t\t\t\t\t\tMaximum marks : ",self.assignment[i][1])
                print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\tFor which assignment do you want to give marks : - ",end=" ")
            sub=int(input())
            print("\t\t\t\t---------------------------------------------------------")
            print("\t\t\t\t\t\tPLEASE WAIT ......")
            print("\t\t\t\t---------------------------------------------------------")
            time.sleep(1)
            os.system("CLS")
            if((sub-1)<len(self.assignment)):
                for i in self.submissions:
                    if(i[1]==self.assignment[sub-1][0] and i[0]==name):
                        flagtemp=1
                    if(i[1]==self.assignment[sub-1][0] and i[0]!=name):
                        t=t+1
                if(flagtemp==1):
                    if(t>=2):
                        for i in self.submissions:
                            if(i[1]==self.assignment[sub-1][0] and i[0]!=name and count!=2 and i[6]!=name and i[7]!=name):
                                    if(i[3]==0 or i[4]==0):
                                        os.system("CLS")
                                        print("\n\n\n\n\n\n\t\t\t\t---------------------------------------------------------")
                                        print("\t\t\t\t|      ------------SUBMITTED ASSIGNMENTS-------------\t|")
                                        print("\t\t\t\t---------------------------------------------------------")
                                        print("\t\t\t\t\t\tAssignment name : - ",self.assignment[sub-1][0])
                                        print("\t\t\t\t---------------------------------------------------------")
                                        print("\t\t\t\t\t\tMaximum marks : - ",self.assignment[sub-1][1])
                                        print("\t\t\t\t---------------------------------------------------------")
                                        print("\t\t\t\t\tAssignment submitted : - ",i[2])
                                        print("\t\t\t\t---------------------------------------------------------")
                                        if(i[3]==0):
                                            while(True):
                                                print("\t\t\t\t\t\tEnter marks : - ",end=" ")
                                                marks=float(input())
                                                if(marks<=float(self.assignment[sub-1][1])):
                                                    i[3]=marks
                                                    count=count+1
                                                    i[6]=name
                                                    print("\t\t\t\t---------------------------------------------------------")
                                                    print("\t\t\t\t\t\tMarks given successfully!!!!!")
                                                    print("\t\t\t\t---------------------------------------------------------")
                                                    input("\t\t\t\t\t\tPress Enter to continue...")
                                                    break
                                                else:
                                                    print("\t\t\t\t---------------------------------------------------------")
                                                    print("\t\t\t\t\tMarks entered are greater than maximum marks!!")
                                                    print("\t\t\t\t---------------------------------------------------------")
                                        elif(i[4]==0):
                                            while True:
                                                print("\t\t\t\t\t\tEnter marks : - ",end=" ")
                                                marks=float(input())
                                                if(marks<=float(self.assignment[sub-1][1])):
                                                    i[4]=marks
                                                    count=count+1
                                                    if(i[6]==" "):
                                                        i[6]=name
                                                    else:
                                                        i[7]=name
                                                    print("\t\t\t\t---------------------------------------------------------")
                                                    print("\t\t\t\t\t\tMarks given successfully!!!!!")
                                                    print("\t\t\t\t---------------------------------------------------------")
                                                    input("\t\t\t\t\t\tPress Enter to continue...")
                                                    break
                                                else:
                                                    print("\t\t\t\t---------------------------------------------------------")
                                                    print("\t\t\t\t\tMarks entered are greater than maximum marks!!")
                                                    print("\t\t\t\t---------------------------------------------------------")
                    else:
                        os.system("CLS")
                        print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                        print("\t\t\t\t|\t\t\t\t\t\t      |")
                        print("\t\t\t\t*******************************************************")
                        print("\t\t\t\t-------------------------------------------------------")
                        print("\t\t\t\t|\tFEW SUBMISSIONS ARE STILL LEFT!!!\t      |")
                        print("\t\t\t\t-------------------------------------------------------")
                        print("\t\t\t\t*******************************************************")
                        print("\t\t\t\t|\t\t\t\t\t\t      |")
                        print("\t\t\t\t*******************************************************")
                        time.sleep(1)
                else:
                    os.system("CLS")
                    print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|\t YOU HAVE NOT SUBMITTED YOUR ASSIGNMENT!! |")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t|GRADING AVAILABALE AFTER YOU SUBMIT YOUR ASSIGNMENT!!|")
                    print("\t\t\t\t-------------------------------------------------------")
                    print("\t\t\t\t*******************************************************")
                    print("\t\t\t\t|\t\t\t\t\t\t      |")
                    print("\t\t\t\t*******************************************************")
                    time.sleep(1)
        else:
            os.system("CLS")
            print("\n\n\n\n\n\n\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t|\t   NO ASSIGNMENTS SUBMITTED YET!!\t      |")
            print("\t\t\t\t-------------------------------------------------------")
            print("\t\t\t\t*******************************************************")
            print("\t\t\t\t|\t\t\t\t\t\t      |")
            print("\t\t\t\t*******************************************************")
            time.sleep(1)
obj=Main()
obj.maincontent()

