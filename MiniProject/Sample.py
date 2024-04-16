base = 'P0999'
num_str = int(base[1:])
term = base[:-len(str(num_str+1))] + str(num_str+1)
print(term)