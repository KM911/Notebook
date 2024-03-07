


# avoid index raise error 
# Raises ValueError if the value is not present.

def Find(list : list , key : str):
  try :
    return list.index(key)
  except:
    return -1
