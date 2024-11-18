import pickle

dataFile = 'test.data'

name = 'river'

f = open(dataFile, 'wb')

pickle.dump(name, f)
f.close()

del name

f = open(dataFile, 'rb')
storedName = pickle.load(f)

print(storedName)