#
# tempconvert.py - Convert temperature input
#
import math

def FtoC(TempF):
 TempC=(TempF - 32) * 5 / 9
 return(TempC)

def CtoF(TempC):
 TempF=(TempC * 9/5) + 32
 return (TempC)

def PickDirection()
 print("Pick starting temperature type F or C")
 raw_input(Direction)
 if Direction != "F" OR if Direction != "f" OR if Direction != "C" OR if DIRECTION != "c":
  then
    print("Selection must be F | f | C | c")
    break
   else return(Direction)
 

# ========================= Start Boys Life Code ===========================
#
#continueYN = "y"
 
#while continueYN == "y":
   #...get temperature input from the user
#   sDegreeF = input("Enter next temperature in degrees Farenheight (F):")
 
   #...convert text entry to number value that can be used in equations
#   nDegreeF = int(sDegreeF)
 
   #...convert temperature from F to Celsius
#   nDegreeC = (nDegreeF - 32) * 5 / 9
 
#   print ("Temperature in degrees C is:", nDegreeC)
 
   #...check for temperature below freezing..
#   if nDegreeC < 0:
#      print ("Pack long underwear!")
 
   #...check for it being a hot day...
#   if nDegreeF > 100:
#      print ("Remember to hydrate!")
 
#   continueYN = input("Input another?")
 
#exit the program
# ========================= End Boys Life Code ===========================
