

#Med bruk av float("inf") som er python sin constant for infinity
def find_min(nums: list[int]) -> int | float:
    new_min = float("inf")
    for n in nums:
        if n < new_min:
            new_min = n 
    
    return new_min

#Logikken funker men det er en test som sender en tom nums liste og forventer "inf" som return, noe som ikke denne funksjonen gjør
def find_min_feil(nums: list[int]) -> int | float:
    new_min = nums[0]
    for n in nums:
        if n < new_min:
            new_min = n
            
    return new_min
        