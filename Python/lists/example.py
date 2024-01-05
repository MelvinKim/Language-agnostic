acronyms = ['LOL', 'IDK', 'SMH']

# append
acronyms.append('BFN')
acronyms.append('IMHO')

print(acronyms)

# remove
acronyms.remove('BFN')
del acronyms[3]

print(acronyms)

# check if it exists
# example 1
if 1 in [1,2,3,4,5]:
    print("print something")
# example 2
word = 'LOL'
if word in acronyms:
    print(word + ' is in the list')
else:
    print(word + ' is NOT in the list')
    
# for loops
for acronym in acronyms:
    print(acronym)


