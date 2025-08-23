
from organising_data import *
from linkedlist import LinkedList
from node import Node


age_ratings = []
for movie in movie_data:
    if movie[2] not in age_ratings:
        age_ratings.append(movie[2])

## Removing nan as an option
age_ratings.pop(5)

## Select IMDB rating
rating_input = str(input('\nWhat IMDB rating would you like?\nEnter A for 0-8, B for 8-8.5, C for 8.5-9, D for 9-10 \n').lower())

movies_with_chosen_rating = []
for movie in movie_data:
    if rating_input == 'a':
        if 0 <= movie[4] < 8:
            movies_with_chosen_rating.append(movie)
    elif rating_input == 'b':
        if 8 <= movie[4] < 8.5:
            movies_with_chosen_rating.append(movie)
    elif rating_input == 'c':    
        if 8.5 <= movie[4] < 9:
            movies_with_chosen_rating.append(movie)
    elif rating_input == 'd':    
        if 9 <= movie[4] < 10:
            movies_with_chosen_rating.append(movie)


print(movies_with_chosen_rating)
## Putting our age ratings into a LinkedList
def insert_age_ratings():
    age_ratings_list = LinkedList()
    for rating in age_ratings:
        age_ratings_list.insert_beginning(rating)

    return age_ratings_list

## initialising our data as a LinkedList
def insert_movie_data():
    movie_data_list = LinkedList()

    for rating in age_ratings:
        movie_sublist = LinkedList()
        for movie in movies_with_chosen_rating:
            if movie[2] == rating:
                movie_sublist.insert_beginning(movie)

        movie_data_list.insert_beginning(movie_sublist)

    return movie_data_list

my_rating_list = insert_age_ratings()
my_movie_list = insert_movie_data()

selected_movie_rating = ""

while len(selected_movie_rating) == 0:
    print(age_ratings)
    selected_movie_rating = str(input('\nWhat movie age rating would you like?\n'))

    print("Selected Movie Rating: " + selected_movie_rating)
    movie_list_head = my_movie_list.get_head_node()
    while movie_list_head.get_next_node() is not None:
        sublist_head = movie_list_head.get_value().get_head_node()
        if sublist_head.get_value() is None:
            print('No movies meet criteria, try again')
            break
        if sublist_head.get_value()[2] == selected_movie_rating:
            while sublist_head.get_next_node() is not None:
                print("--------------------------")
                print("Name: " + sublist_head.get_value()[1])
                print("Release Year: " + sublist_head.get_value()[2])
                print("Rating: " + sublist_head.get_value()[3])
                print("Runtime Minutes: " + str(sublist_head.get_value()[4]))
                print("IMDB Rating: " + str(sublist_head.get_value()[4]))
                print("--------------------------\n")
                sublist_head = sublist_head.get_next_node()
        movie_list_head = movie_list_head.get_next_node()