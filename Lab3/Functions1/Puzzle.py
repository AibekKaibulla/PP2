def solve(numheads, numlegs):
    rabbits=(numlegs-numheads*2)/2
    chicken=heads-rabbits    
    print(int(chicken), int(rabbits))
    
heads=35
legs=94
solve(heads, legs)