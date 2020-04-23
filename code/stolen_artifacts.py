import csv

def host_year(country):
  file = 'code/world_cup.csv'
  with open(file) as csv_file:
    world_cup = csv.DictReader(csv_file, delimiter=',')
    for row in world_cup:
      if row['host'] == country:
        return row['year']
      
def population(country, year):
  file = 'code/world_population.csv'
  with open(file, encoding="utf-8-sig") as csv_file:
    world_population = csv.DictReader(csv_file, delimiter=',')
    for row in world_population:
      if row['Country Name'] == country:
        return row[year]
  
def airport_code(population):
  latitude = float(population) / 100000
  file = 'code/airport_codes.csv'
  with open(file) as csv_file:
    airport_code = csv.DictReader(csv_file, delimiter=',')
    for row in airport_code:
      if row['latitude'] == str(latitude):
        return row['iata_code']

def country_code(letter):
  file = 'code/world_population.csv'
  # old code file needs: (file, encoding="utf-8-sig")
  with open(file) as csv_file:
    world_population = csv.DictReader(csv_file, delimiter=',')
    for row in world_population:
      if row['Country Name'][-1] == letter:
        return row['Country Code']
      
def population_count(year):
  file = 'code/world_population.csv'
  with open(file) as csv_file:
    world_population = csv.DictReader(csv_file, delimiter=',')
    country_count = 0
    for row in world_population:
      if int(row[year]) > 2000000:
        country_count += 1
    return country_count
  
def country_index(country):
  file = 'code/world_population.csv'
  with open(file) as csv_file:
    world_population = csv.DictReader(csv_file, delimiter=',')
    country_list = []
    for row in world_population:
      country_list.append(row['Country Name'])
    country_list.sort()
    for item in country_list:
      if item == country:
        return country_list.index(country)

def population_decrease_count(year1, year2):
  file = 'code/world_population.csv'
  with open(file) as csv_file:
    world_population = csv.DictReader(csv_file, delimiter=',')
    country_count = 0
    for row in world_population:
      if int(row[year1]) < int(row[year2]):
        country_count += 1
    return country_count

def world_cup_winner(year):
  file = 'code/world_cup.csv'
  with open(file) as csv_file:
    world_cup = csv.DictReader(csv_file, delimiter=',')
    for row in world_cup:
      if row['year'] == year:
        return row['winner_code']

def airport_type_count(airport_type, country_code):
  file = 'code/airport_codes.csv'
  with open(file) as csv_file:
    airport_codes = csv.DictReader(csv_file, delimiter=',')
    airport_count = 0
    for row in airport_codes:
      if row['type'] == airport_type and row['iso_country'] == country_code:
        airport_count += 1
    return airport_count

  
  
  
def main():
  # 1: Finding the Airport Variables
  world_cup_country = 'England' # 1: South Africa 2: England
  country = 'Uzbekistan' # 1: Guatemala 2: Uzbekistan
  
  # 2: Locker Number (part 1) Variables
  country_last_letter = 'd' # 1: i 2: d
  
  # 3: Locker Number (part 2) Variables
  country_populations_year = '1975' # 1: 2000 2: 1975
  
  # 4: Lock Code (part 1) Variables
  country_name = 'Austria' # 1: Azerbaijan 2: Austria
  
  # 5: Lock Code (part 2) Variables
  population_year = '1991' # 1: 2010 2: 1991
  population_year_2 = '1968' # 1: 2000 2: 1968
  
  # 6: Lock Code (part 3) Variables
  world_cup_year = '1978' # 1: 2010 2: 1978
  airport_type = 'heliport' # 1 & 2: heliport
  
  # 1: Finding the Airport
  print(airport_code(population(country, host_year(world_cup_country))))

  # 2: Locker Number (part 1) and 3: Locker Number (part 2)
  print(f"{country_code(country_last_letter)}{population_count(country_populations_year)}")
  
  # 4: Lock Code (part 1) and 5: Lock Code (part 2) and 6: Lock Code (part 3)
  print(f"{country_index(country_name)} {population_decrease_count(population_year, population_year_2)} {airport_type_count(airport_type, world_cup_winner(world_cup_year))}")
  
  
if __name__== "__main__":
  main()
