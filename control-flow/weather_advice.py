weather_condition =input("hat's the weather like today? (sunny/rainy/cold): ")


# If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
# If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
# If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.


if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print(("Sorry, I don't have recommendations for this weather."))