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


def main():
  # 1: Finding the Airport Variables
  world_cup_country = 'South Africa'
  country = 'Guatemala'
  
  country_last_letter = 'i'
  
  # 1: Finding the Airport
  print(airport_code(population(country, host_year(world_cup_country))))

  # 2: Locker Number (part 1)
  print(country_code(country_last_letter))
  
if __name__== "__main__":
  main()
