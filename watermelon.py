w=int(input("enter weight of the wm:"))
if(w%2!=0 or w==2):
    print("no it is odd")   
else:
    x=w/2
    if(w%2==0):
        print("yes,brother1 get ",x,"brother2 get ",x)
    else:
        print("yes,brother1 get",x-1,"brother2 get ",x+1)
