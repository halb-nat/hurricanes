from  data import *

# 1
# Update Recorded Damages
def update_damages():
  conversion = {"M": 1000000,
                "B": 1000000000}
  return [val if val == 'Damages not recorded' else int(float(val[:-1])*conversion[val[-1]]) for val in damages]

update_list_damages = update_damages()   
print(update_list_damages)

# 2
# Create and view the hurricanes dictionary
def create_hurr_dict():
  dict_lists = [
   names,
   months,
   years,
   max_sustained_winds,
   areas_affected,
   update_list_damages,
   deaths]

  dict_keys = [
   "Name",
   "Month",
   "Year",
   "Max Sustained Wind",
   "Areas Affected",
   "Damage",
   "Death"]

  num_rec = len(names)
  num_keys = len(dict_keys)

  return {names[i] : {dict_keys[j] : dict_lists[j][i] for j in range(num_keys)} for i in range(num_rec)}

hurr_dict = create_hurr_dict()
print(hurr_dict)

# 3
# Organizing by Year
def org_by_year (hurr_dict):
   year_dict = {}

   for k1 in hurr_dict.keys():
     curr_year = hurr_dict[k1]["Year"]
     if curr_year not in year_dict.keys():
       year_dict[curr_year] = []

     year_dict[curr_year].append(hurr_dict[k1])
   return year_dict

# create a new dictionary of hurricanes with year and key
year_dict = org_by_year (hurr_dict)
print(year_dict)

# 4
# Counting Damaged Areas
def num_hurr_area (hurr_dict):
  areas_dict = {}

  for hurr in hurr_dict.values():
    for area in hurr["Areas Affected"]:
      if not(area in areas_dict):
        areas_dict[area] = 1
      else:
        areas_dict[area] += 1

  print(areas_dict)

# create dictionary of areas to store the number of hurricanes involved in
num_hurr_area (hurr_dict)

def max_value (hurr_dict, key_name):
    max_d = 0
    name_d = ''
    for hurr in hurr_dict.values():
        if (hurr[key_name] != "Damages not recorded" and max_d < hurr[key_name]):
           max_d = hurr[key_name]
           name_d = hurr["Name"]
    print("Hurricane {}: {} {}".format(name_d, key_name.lower(), max_d))

def hurr_rating(hurr_dict_, key_name, rating_scale, do_check = False, check_list = []):
  rating_dict = {}

  for k1 in hurr_dict_.keys():
    curr_rating = hurr_dict_[k1][key_name]
    if not do_check or  (do_check and not(curr_rating in check_list)):
      curr_rating = 5
      for key_rating in rating_scale:
        if (hurr_dict_[k1][key_name] <= rating_scale[key_rating]):
           curr_rating = key_rating
           break
    if not(curr_rating in rating_dict.keys()):
        rating_dict[curr_rating] = []

    rating_dict[curr_rating].append(hurr_dict_[k1])

  print("\n{} rating".format(key_name))
  print (rating_dict)


# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths
max_value(hurr_dict, "Death")

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

hurr_rating(hurr_dict, "Death", mortality_scale)

# 8
# Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
max_value(hurr_dict, "Damage")



# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
hurr_rating(hurr_dict, "Damage", damage_scale, True, ["Damages not recorded"])
