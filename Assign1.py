# Initiate an empty list to store the entries
favorites = []

# Prompt user for their favorite sport and team
sport = input("Enter your favorite sport:")
team = input(f"Enter your favorite team in {sport}:")
favorites.append(["sport, {team}"])
print("\nCurrent Favorites List: ")
for entry in favorites:
    print(f"Sport:
          {entry[0], team:
           entry[1]}")
# # f-string with curly braces properly closed
    
# # # Add the sport and the team as a list to the favorites list
# favorites.append([sport, team])

# # # Display the added favorite sport and team
# # print("\nCurrent favorites List:")
# for entry in favorites:
#     print(f"sport:
#           {entry[0]}, team:
#            {entry[1]}")

    # # Ask if the user wants to add another entry
    # another = input("would you like to add another favorite? (yes/no):").strip().lower()
    # if another !='yes':
    #     break

    # # Display all favorites added by the user
    # print("\nYour Favorite Sports and Teams:")
    # for entry in favorites:
    #     print(f"Sport:
    #           {entry[sport]}, Team:
    #           {entry[team]}")