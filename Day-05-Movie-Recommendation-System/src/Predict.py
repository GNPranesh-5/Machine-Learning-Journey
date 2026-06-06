import pandas as pd 
df=pd.read_csv("../data/movies.csv")
movie=input("Enter the movie name: ")
result=df[df["Movie"].str.lower()==movie.lower()]
if result.empty:
    print("Movie not found")
else:
    genre=result.iloc[0]["Genre"]
    recommendations=df[(df["Genre"]==genre)&(df["Movie"]!=result.iloc[0]["Movie"])]
    print("\nRecommended Movies:\n")
    for movie in recommendations["Movie"]:
        print(movie)