# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

films = []



#izveidoju bezgalīgu cilpu, lai sniegtu izvēli, līdz tiek izpildīts nosacījums, kas to izbeigs.
while True:
     print("1. pievienot filmu norādot nosaukumu un reitingu, atzīmēt filmu kā skatīto/neskatīto ") 
     print("2. dzēst filmu no saraksta")
     print("3. atspoguļot top 10 filmas pec reitinga")
     print("4. iztukšot sarakstu")
     print("5. meklēt filmu pēc nosaukuma daļas")
     print("6.atfiltrēt noskatītas/nenoskatītas filmas")
     print("7. import json")
     print("8. Exit")
     command = input("Choose command: ")

     if command == "1":
        dictionary_films = {}
        
        name = input('Enter the film name: ')
        if len(name) < 2:
            print("Error")
            continue
        if len(name) > 120:
            print("Error")
            continue
        dictionary_films["name"] = name

        rating = input('Enter the film rating: ')
        if not rating.isdigit():
            print("Error")
            continue
        if int(rating) < 1 or int(rating) > 10:
            print("Error")
            continue
        
        dictionary_films["rating"] = int(rating)

        reviewed_yes_or_no = input('Have you seen this movie?: ')
        dictionary_films["reviewed"] = reviewed_yes_or_no

        films.append(dictionary_films)
        print(films)

     if command == "2":
        number_delete = int(input("enter number of film: "))
        del films[number_delete]
        print(films)
        pass 

     if command == "3":
          def my_func(films):
            return films["rating"]
            
          films.sort(key = my_func, reverse = True)
          print(films[0:9])

     if command == "4":
            films.clear()
            print(films)
            pass

     if command == "5":
            name_film = input('Enter the film name: ')
            new_films = []
            # izvēlos katru vārdnīcu no saraksta 
            for film in films:
                if film['name'] == name_film:  #pārbaudu, vai filmas nosaukums vārdnīcā sakrīt ar lietotāja rakstīto nosaukumu
                    new_films.append(film)     #Ja tas atbilst, es to pievienoju new_films

            print(new_films)

     if command == "6":
            reviewed = input("yes or no: ")
            new_films = []
            # izvēlos katru vārdnīcu no saraksta  
            for film in films:
                if film['reviewed'] == reviewed: #pārbaudīt, vai filma ir skatīta vai nē (atkarībā no lietotāja izvēles)
                    new_films.append(film)
            print(new_films) 

     if command == "7":
          import json
          with open('films.json', 'w') as file:
            json.dump(films, file)

          with open('films.json', 'r') as file:
            films_data = json.load(file)
            print(films_data)

     if command == "8":
            print("Exiting...")
            break 
