def merge_dictionaries(dict1, dict2):
  merged_dict = dict1.copy()
  return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")

merged = merge_dictionaries(dict1, dict2)
print(f"Merged Dictionary: {merged}")
