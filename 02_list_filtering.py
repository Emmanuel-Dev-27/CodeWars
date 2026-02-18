def filter_list(l):
  new_list = []
  for item in l:
    if type(item) != str:
      new_list.append(item)
  return new_list