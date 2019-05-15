import datetime
from copy import deepcopy

f = open("input.txt", "r")
rows = int(f.readline())
no_of_walls=int(f.readline())

Wallpositions = []
for i in range(no_of_walls):
    help=f.readline()
    x = help.split(",")

    dict={
        "row": int(x[0]),
        "col": int(x[1])
        }
    Wallpositions.append(dict)


terminal_states=int(f.readline())


terminalpositions = []
for i in range(terminal_states):
    help=f.readline()
    x = help.split(",")
    dict={
        "row": int(x[0]),
        "col": int(x[1]),
        "reward": float(x[2])
        }
    terminalpositions.append(dict)

# print terminalpositions

probability=float(f.readline())
# print probability
rewards=float(f.readline())
# print rewards
Discount=float(f.readline())









f.close()


term=[]
gridder=[]
for i in range(rows):
    helper = []
    termhelp=[]
    for j in range(rows):
        termhelp.append("H")
        helper.append(0)
    term.append(termhelp)
    gridder.append(helper)


for j in range(len(Wallpositions)):
    gridder[Wallpositions[j].get("row")-1][Wallpositions[j].get("col")-1]=float("-inf")
# print terminalpositions
for j in range(len(terminalpositions)):
    rowss=terminalpositions[j].get("row") - 1
    colss=terminalpositions[j].get("col")-1
    rew=terminalpositions[j].get("reward")
    gridder[rowss][colss]=rew

    term[rowss][colss]= "E"
    # print term[terminalpositions[j].get("row")-1][terminalpositions[j].get("col")-1]

#
# print gridder
# print term
a=datetime.datetime.now()



def solution(gridder,rows,term,Discount,probability,rewards):

    ans = []
    f = open("output2.txt", "w")
    newgridder = []
    for i in range(rows):
        helper1 = []
        termhelp1 = []
        for j in range(rows):
            termhelp1.append('')
            helper1.append(0.0)
        ans.append(termhelp1)
        newgridder.append(helper1)

    while(newgridder!=gridder):
        b = datetime.datetime.now()
        delta = b - a
        if int(delta.total_seconds()) > 26:
            return ans
        help=0.0
        newgridder=deepcopy(gridder)
        for i in range(len(gridder)):
            for j in range(len(gridder)):
                best=float("-inf")

                if gridder[i][j]==float("-inf"):
                    ans[i][j]='N'
                    continue
                if term[i][j]=='E':
                    ans[i][j]='E'

                    continue

                # walk up


                if i-1>=0:
                    u1 = 0.0
                    u2 = 0.0
                    main=0.0
                    if j-1>=0 and i-1>=0:
                        if gridder[i-1][j-1]!=float('-inf'):
                            u1=0.5*(1-probability)*newgridder[i-1][j-1]
                        else:
                            u1=0.5*(1-probability)*newgridder[i][j]
                    else:
                        u1=0.5*(1-probability)*newgridder[i][j]
                    if j+1<len(gridder) and i-1>=0:
                        if gridder[i-1][j+1]!=float('-inf'):
                            u2=0.5*(1-probability)*newgridder[i-1][j+1]
                        else:
                            u2=0.5*(1-probability)*newgridder[i][j]
                    else:
                        u2 = 0.5 * (1 - probability)*newgridder[i][j]
                    if gridder[i-1][j]!=float('-inf'):
                        main=probability*newgridder[i-1][j]
                    else:
                        main = probability * newgridder[i][j]

                else:
                    u1=0.5*(1-probability)*newgridder[i][j]
                    u2=0.5*(1-probability)*newgridder[i][j]
                    main = probability * newgridder[i][j]
                util=u1+u2+main
                # print "up"
                # print i
                #
                # print j
                # print u1
                # print u2
                # print main

                # f.write("up")
                # f.write(str(i))
                # f.write(str(j))
                # f.write(str(u1))
                # f.write(str(u2))
                # f.write(str(main))
                # f.write("\n")



                util=rewards+ (Discount*util)
                if util > best:
                    best = util
                    ans[i][j] = "U"

                    # walk down

                if i + 1 < len(gridder)  :
                    u1 = 0.0
                    u2 = 0.0

                    if j - 1 >= 0:
                        if gridder[i + 1][j - 1] != float('-inf'):
                            u1 = 0.5 * (1 - probability) * newgridder[i + 1][j - 1]
                        else:
                            u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    else:
                        u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    if j + 1 < len(gridder):
                        if gridder[i + 1][j + 1] != float('-inf'):
                            u2 = 0.5 * (1 - probability) * newgridder[i + 1][j + 1]
                        else:
                            u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    else:
                        u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    if gridder[i + 1][j] != float('-inf'):
                        util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i + 1][j])))
                    else:
                        util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j])))


                else:
                    u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j])))
                if util > best:
                    best = util
                    ans[i][j] = "D"

                # walk right

                if j+ 1 < len(gridder)  :
                    u1 = 0.0
                    u2 = 0.0
                    if i - 1 >= 0:
                        if gridder[i - 1][j + 1] != float('-inf'):
                            u1 = 0.5 * (1 - probability) * newgridder[i -1][j + 1]
                        else:
                            u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    else:
                        u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    if i + 1 < len(gridder):
                        if gridder[i + 1][j + 1] != float('-inf'):
                            u2 = 0.5 * (1 - probability) * newgridder[i + 1][j + 1]
                        else:
                            u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    else:
                        u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    if gridder[i][j+1] != float('-inf'):
                        util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j+1])))
                    else:
                        util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j])))


                else:
                    u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j])))
                if util > best:
                    best = util
                    ans[i][j] = "R"

                # walk left

                if j - 1 >= 0 :
                    u1 = 0.0
                    u2 = 0.0
                    if i - 1 >= 0:
                        if gridder[i - 1][j - 1] != float('-inf'):
                            u1 = 0.5 * (1 - probability) * newgridder[i - 1][j - 1]
                        else:
                            u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    else:
                        u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    if i + 1 < len(gridder):
                        if gridder[i + 1][j - 1] != float('-inf'):
                            u2 = 0.5 * (1 - probability) * newgridder[i + 1][j - 1]
                        else:
                            u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    else:
                        u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    if gridder[i][j - 1] != float('-inf'):
                        util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j - 1])))
                    else:
                        util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j])))

                else:
                    u1 = 0.5 * (1 - probability) * newgridder[i][j]
                    u2 = 0.5 * (1 - probability) * newgridder[i][j]
                    util = rewards + (Discount * (u1 + u2 + (probability * newgridder[i][j])))
                if util > best:
                    best = util
                    ans[i][j] = "L"
                gridder[i][j] = best
                if abs(gridder[i][j]-newgridder[i][j])>help:
                    help=abs(gridder[i][j]-newgridder[i][j])

        if help<0.0001*(1-Discount)/Discount:
             break

    return ans


answer=solution(gridder,rows,term,Discount,probability,rewards)



f = open("output.txt", "w")
for i in range(len(answer)):
    for j in range(len(answer)):
        f.write(answer[i][j])
        if j==len(answer)-1:
            continue
        f.write(",")

    f.write("\n")




