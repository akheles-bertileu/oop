class LowPopulationError(Exception):
    pass

try:
    cities = []
    while True:
        city = input("Enter city name (or 'q' to quit): ")
        if city.lower() == 'q':
            break
        population_input = input("Enter city population: ")
        try:
            population = int(population_input)
            if population < 50000:
                raise LowPopulationError("Population too low! City is too small.")
        except ValueError:
            print("Please enter a valid number for population.")
            continue
        except LowPopulationError as e:
            print("Custom Exception:", e)
            continue

        cities.append((city, population))
        print(f"Record added: {city} — {population}\n")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("All cities entered successfully.")
finally:
    print("Program completed.\n")

if cities:
    print("All entered cities:")
    for name, pop in cities:
        print(f"{name} — {pop}")
    average = sum(pop for _, pop in cities) / len(cities)
    print("Average population:", average)
else:
    print("No valid data entered.")

