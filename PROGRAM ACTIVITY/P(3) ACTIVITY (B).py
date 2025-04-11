def merged_dictionaries(dict1, dict2):
  merged_dict = dict1.copy()
  for key, value in dict2.items():
    if key in merged_dict:
      merged_dict[key] += value
    else:
      merged_dict[key] = value
  return merged_dict

dict1 = {"a": 1, "b": 2, "c": 5}
dict2 = {"c": 3, "d": 4, "a": 7}
print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")

merged_dict = merged_dictionaries(dict1, dict2)
print(f"Merged Dictionary: {merged_dict}")
