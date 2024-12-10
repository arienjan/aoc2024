input = [list(l.strip()) for l in open('input.txt').readlines()]
    
unique_chars = set()
freqs = dict()
ylen, xlen = len(input), len(input[0])
for y in range(ylen):
    for x in range(xlen):
        freq = input[y][x]
        if (freq in freqs):
            freqs[freq].add((y, x))
        else:
            freqs[freq] = set()
            freqs[freq].add((y,x))
        
  
anodes = set()  
anodes2 = set()        
for key in freqs.keys():
    if (key == '.'):
        continue
    for val in freqs[key]:
        for val2 in freqs[key]:
            anodes2.add(val)
            if val == val2:
                continue
            
            ydiff = val[0] - val2[0]
            xdiff = val[1] - val2[1]
            y = val[0]  + (val[0] - val2[0])
            x = val[1]  + (val[1] - val2[1])
            if y >= 0 and y < ylen and x >=0 and x < xlen:
                anodes.add((y,x))
            
            y2 = y
            x2 = x
            while (True):
                y += ydiff
                x += xdiff
                
                if y < 0 or y >= ylen or x < 0 or x >= xlen:
                    break;
                
                anodes2.add((y,x))
                input[y][x] = '#'
            while (True):
                y2 -= ydiff
                x2 -= xdiff
                
                if y2 < 0 or y2 >= ylen or x2 < 0 or x2 >= xlen:
                    break;
                
                anodes2.add((y2,x2))
                input[y2][x2] = '#'
            
            
print(len(anodes))
print(len(anodes2))