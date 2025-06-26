import matplotlib.pyplot as plt
import ast
import csv

file = open("tmdb_5000_movies (1).csv","r")
genre={}
with open("tmdb_5000_movies (1).csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        genres=ast.literal_eval(row[1])
        for el in genres:
            if el["name"] not in genre.keys():
                genre[el["name"]]=1
            else:
                genre[el["name"]]+=1

keys = list(genre.keys())
values = list(genre.values())
plt.bar(keys, values)
plt.xlabel('Genres')
plt.ylabel('Number of Movies')
plt.title('Number of Movies for Each genre')

plt.show()
