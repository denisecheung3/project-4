### ![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png) General Assembly, Software Engineering Immersive
# Recipedia 

by [Denise Cheung](https://github.com/denisecheung3) & [Emma Hobday](https://github.com/emmahobday).

The project is deployed [here](https://recipedia1.herokuapp.com/#/) on Heroku, please do feel free to check it out.

## Overview 
Recipedia, a full stack application, is my fourth and final project during the software engineering immersive course at General Assembly. It was completed over the course of one week in **pairs**.

---

## Table of contents
1. [Brief](#Brief)
2. [Technologies Used](#Technologies-Used)
3. [Approach](#Approach)
    - [Homepage](#Homepage)
        - [Recipe-of-the-day]
        - [Fridge recipe search feature](#Fridge-recipe-search-feature)
    - [Find Recipe Page]
        - [Basic search by dish name and/or ingredient] 
        - [Advance search by diet labels and/or health labels]
    - [Single Recipe Page]
        - [Rating a recipe] 
        - [Adding a recipe to your meal planner calendar]
        - [Add ingredient to shopping list]
    - [Your Five Starred Recipes]
    - [Personalised Suggested Recipes]
        - [The logic] 
    - [Viewing the Meal Plan Calendar]
    - [Others]

4. [Screenshots](#Screenshots)
5. [Potential Future Features](#Potential-future-features)
6. [Bugs](#Bugs)
7. [Lessons learnt](#Lessons-learnt)

## Brief 
* Choose to work solo or in a team
* **Build a full-stack application** by making your own backend and your own front-end
* **Use a Python Django API** using Django REST Framework to serve your data from a Postgres database
* **Consume your API with a separate front-end** built with React
* **Be a complete product** which most likely means multiple relationships and CRUD functionality for at least a couple of models
* **Have a visually impressive design** to kick your portfolio up a notch and have something to wow future clients & employers.
* **Be deployed online** so it’s publicly accessible.

## Technologies used 
- JavaScript (ES6)
- React.js
- Python 
- Django 
- PostgreSQL 
- SCSS
- HTML
- Webpack 
- React-scheduler
- Moment
- Heroku 
- Git and GitHub
- Bulma
- Google Fonts

## Approach

### Single Recipe Page 
#### Rating a Recipe 
- Frontend: Viewing the rating button
     - Minor logic on frontend so that
        - not logged in users will not see the rating button (rating feature not available) 
        - logged in users who have not rated the specific recipe will be able to rate 
        - logged in users who have rated the recipe will be able to view their rating 

- Frontend & Backend: When single recipe component mounts, makes a call to fetch single recipe details 
     - the fetch will attach token if user is logged in 
     - data returned includes a 'rating' field 
         - <img src="https://i.imgur.com/PA3lnkB.png" width="350"/>
         - Recall that there is no 'rating' field on the recipe field, so to have the data returned from the fetch to include a 'rating' fields required making some changes to the DetailedRecipeSerializer. 
              ```js
              class DetailedRecipeSerializer(serializers.ModelSerializer):
                    rating = serializers.SerializerMethodField()

                    class Meta:
                        model = Recipe
                        fields = (........, 'rating')

                    def get_rating(self, obj):
                        user = self.context["request"].user
                        print(user.is_authenticated)
                        if user.is_authenticated:  
                            user_rating = obj.ratings.filter(user=user).first()
                            print(user_rating)
                            if user_rating:  # if user logged in but never rated, rating field will be null
                                return user_rating.rating_num
                        return None  # if user isn't logged in rating field will be null
              
              ```
              -  here I used Django SerliazerMethodField and some logic to check if the user has logged in and if yes, has rated the recipe to get the rating

              - If the user is not logged in, or the user has not rated that specific recipe, rating will be null. If the user is logged in and has rated the recipe, the rating returned will be a number between 1 to 5, which is the rating the user gave.





