
def get_population():
  keys = ["Col", "Bol"]
  values = [300, 200]
  return keys, values 

A = "Hola"

def population_by_country(data, country):
  result = list(filter(lambda item: item["Country"] == country,data))
  return result 