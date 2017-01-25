##f = open('test_input.txt')
##food = []
##separators = [' ', ',']
##
##for line in f:
##    print(line)
##    content = line.replace('\n','').split(',')
##    food += content
##    
##    
##
##print(food)

##f_write = open('test_output.txt', 'w')
##
##f_write.write('First line of my file\n')
##f_write.write('Second line of my file!')
##
##f_write.close()

with open('test_output.txt', 'w') as f:
    f.write('Shortcut test')

# Throws an error!
f.write('Some other line')

