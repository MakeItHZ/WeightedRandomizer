import random
import string

#Define Outcomes
ExampleBank1 = ["Example 1", "Example 2", "Example 3", "Example 4", "Example 5"] #Add as many options here as you would like
ExampleBank2 = ["Example 1a", "Example 2b", "Example 3c", "Example 4f", "Example 5g"] #

#Define Weights 
BalancedWeight = (20, 20, 20, 20, 20) #Even Odds across 5 Choices, written as %
Guaranteed3Plus = (0, 0, 90, 9, 1)#Weighted odds across 5 choices, with a 0% Chance of getting > 3

ChooseFrom5 = (random.choices(ExampleBank2, weights=(BalancedWeight), k=1))# Choose randomly from 1 of 5 Examples provided
ThreeOrBetter = (random.choices(ExampleBank1, weights=(Guaranteed3Plus), k=1)) #Used to calculate a rarity, or omit strings from selections. We have omitted Example 1 & 2.

print(ChooseFrom5)
print(ThreeOrBetter)
