### QUESTION 3

#initial concentrations were assigned to variables
X = 10
Y = 10
Time = 0
Tx = 0
Ty = 0
change_cons = 0.001
while Time  < 1000: # for maximum of 1000 iterations was desired
#Equations prepared with the information given
    new_X = X + 0.41*X-(X-0.01*Ty*X) 
#The bacterium X can produce 0.5 moles of Toxin X in an hour, but the question states that 1 mole of Toxin X kills 0.5% of bacterium Y, so 0.5 moles of Toxin X kill 0.25% of bacterium Y.
    new_Y = Y + 0.55*Y-(Y-0.025*Tx*Y) 
    new_Tx = Tx + 0.5*X 
    new_Ty = (Ty + 1*Y) - (0.05*Ty) 
#If X or Y is equal 0, the change concentration cannot be calculated by the equation and should be considered 0
    if X != 0:
        changeX = abs((new_X - X) / X)
    else:
        changeX = 0
    if Y != 0:
        changeY = abs((new_Y - Y) / Y)
    else:
        changeY = 0
        
    if changeX < change_cons or changeY < change_cons: #If the concentration change of X or Y is less than 0.001, the process stops.
        print("Steady state conditions reached.")
        break
    Time += 1
    X = new_X
    Y = new_Y
    Tx = new_Tx
    Ty = new_Ty
    print(f"Hour: {Time}, {new_X} moles of Bacteria X,{new_Y} moles of Bacteria Y,{new_Tx} moles of Toxin X,{new_Ty} moles of Toxin Y")
if Time == 1000:
    print("1000 iterations are done")
