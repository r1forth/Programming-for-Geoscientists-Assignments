names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
masses_10_24kg = [0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102]
perihelions_10_6km = [46.0, 107.5, 147.1, 206.7, 740.6, 1357.6, 2732.7, 4471.1]
aphelions_10_6km = [69.8, 108.9, 152.1, 249.3, 816.4, 1506.5, 3001.4, 4558.9]
Gravitational_constant = 6.674e-11

# a = (G*M)/(r ** 2) formula here for mental reference of the calculation.

while True:

    user_input_planet = input("\nPlease enter the name of the planet (or enter 'stop')").strip()

    if user_input_planet == "stop":
        print("\nThank you.")
        break
# I placed the stop at the start as it is clean and functional.
    if user_input_planet in names:
        planet_index_number = names.index(user_input_planet)
        print(f"\nThe planet {user_input_planet}, has a positional number of {planet_index_number+1}")

        detected_planets = []
# detected planets is an open list and we use .append to numbers to its tally.
        user_input_planet_aphelion = (aphelions_10_6km[planet_index_number] * 1e9)
        user_input_planet_perihelion = (perihelions_10_6km[planet_index_number] * 1e9)
        outer_planet = planet_index_number
        inner_planet = planet_index_number
# I had to do 1e9 as I needed to ensure distance was converted to metres.
        while outer_planet < 7:
# This while loop ensures outer_planet runs through entire names list of planets.
            outer_planet = outer_planet + 1
# Needed to do +1 as it ensures we are running up the list namee variuables.
            maximum_radius = user_input_planet_aphelion + (aphelions_10_6km[outer_planet] * 1e9)
            minimum_radius = (perihelions_10_6km[outer_planet] * 1e9) - user_input_planet_aphelion
            maximum_acceleration = ((Gravitational_constant) * masses_10_24kg[outer_planet] * 1e24)/((minimum_radius) ** 2)
            minimum_acceleration = ((Gravitational_constant) * masses_10_24kg[outer_planet] * 1e24)/((maximum_radius) ** 2)
# Kind of messed up by making calculations so long on a single line, but its hard now to redo it again and split it up easily.
            Gravitational_effect = maximum_acceleration - minimum_acceleration

            if Gravitational_effect > 5.5e-8:
                detected_planets.append(names[outer_planet])
                print(f"\nDetected outer planet: {names[outer_planet]}")
                print(f"Maximum distance between {user_input_planet} and {names[outer_planet]}, is {maximum_radius}m")
                print(f"Minimum distance between {user_input_planet} and {names[outer_planet]}, is {minimum_radius}m")
                print(f"Gravitational effect for this pairing is {Gravitational_effect}ms^-2")
        while inner_planet > 0:
            inner_planet = inner_planet - 1
            maximum_radius = user_input_planet_aphelion + (aphelions_10_6km[inner_planet] * 1e9)
            minimum_radius = user_input_planet_perihelion - (aphelions_10_6km[inner_planet] * 1e9)
# Nearly fell for this trap, as the aphelion is usally largest but if its for an inner planet it will always be smaller than the outer planets perihelion.
            maximum_acceleration = ((Gravitational_constant) * masses_10_24kg[inner_planet] * 1e24)/((minimum_radius) ** 2)
            minimum_acceleration = ((Gravitational_constant) * masses_10_24kg[inner_planet] * 1e24)/((maximum_radius) ** 2)
            Gravitational_effect = maximum_acceleration - minimum_acceleration

            if Gravitational_effect > 5.5e-8:
                detected_planets.append(names[inner_planet])
                print(f"\nDetected inner planet: {names[inner_planet]}")
                print(f"Maximum distance between {user_input_planet} and {names[inner_planet]}, is {maximum_radius}m")
                print(f"Minimum distance between {user_input_planet} and {names[inner_planet]}, is {minimum_radius}m")
                print(f"Gravitational effect for this pairing is {Gravitational_effect}ms^-2")

        if detected_planets:
            print(f"\nSummary of planets detectable to {user_input_planet}: {detected_planets}")
# I am not very good at using elif prompts idk if they could have been used here, but I feel like this could have been done in a more optimal way.
        else:
            print(f"\nNo planets have a detectable gravitational effect on {user_input_planet}.")
# I made sure to go back to the assignment and print all things like distances and gravitational effects to verify the program worked in all cases.
    else:
        print(f"Error! [{user_input_planet}] is not a valid planet name, Please try again.")

