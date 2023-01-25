gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('The Sorting Hat')


print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

pregunta = int(input('Enter answer (1-2): '))

if pregunta == 1:
  gryffindor += 1
  ravenclaw += 1
elif pregunta == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')



print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

pregunta = int(input('Enter your answer (1-4): '))

if pregunta == 1:
  hufflepuff += 1
elif pregunta == 2:
  slytherin +=1
elif pregunta == 3:
  ravenclaw +=1
elif pregunta == 4:
  gryffindor +=1
else:
  print('Wrong input.')



print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

pregunta = int(input('Enter your answer (1-4): '))

if pregunta == 1:
  slytherin +=1
elif pregunta == 2:
  hufflepuff +=1
elif pregunta == 3:
  ravenclaw +=1
elif pregunta == 4:
  gryffindor +=1
else:
  print('Wrong input.')
  
print(gryffindor)
print(ravenclaw)
print(hufflepuff)
print(slytherin)

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')