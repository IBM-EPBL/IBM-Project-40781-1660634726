import http.client
conn=http.client.HTTPSConnection("spoonacular-recipe-food-nutrition-v1.p.rapidapi.com")
headers = {
'X-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.prapidapi.com"
'X-rapidapi-key': "93706bmsh70946cd35d92e9bp1ea575jsn75fb7b705b36"
}
conn.request("GET", "/recipes/guessNutrition?title=cereal", headers)

res = conn.getresponse{} data=res.read{} 
print[data.decode{"utf-8"}]