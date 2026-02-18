def in_array(array1, array2):
  result = []
  for word in array1:
    for string in array2:
      if word in string and word not in result:
        result.append(word)
  return sorted(result)