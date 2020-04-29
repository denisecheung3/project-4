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
    - [Populating our Database] 
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
### Populating our database 

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


#### Adding ingredient to shopping list 
- The models for this feature 
- I learnt a lot about the importance of models and how they directly impact the functionality you can achieve. This is my journey: 
    - Once I had my backend set up for this feature, I turned my attention to the frontend. I had no problem adding an ingredient to the shopping list but had to make a decision when it came to viewing my shopping list.
    - Imagine the scenario. The user has two ingredients in their shopping list for the Chicken Crunch recipe. He went to the shop, bought the chicken and checked the chicken off the list. However, the shop run out of butter, so the shopping list page will look like this: 
         - <img src="https://i.imgur.com/T8evZpG.png" width="350"/>
    
    - If the user refreshes, the page will look like this:
         - <img src="https://i.imgur.com/heyQlDR.png" width="350"/>
         - the strikethrough will disappear and it's as if the user still needs to buy chicken, which is not the case. (Note that these screenshots were taken when the shopping list page was only displaying ingredients and I have not yet written the code to make a request to the backend when user crosses an ingredient out) 
    - So I have a decision to make between two options: 
         - option 1: 
             - if the user refreshes the page, chicken will remain crossed out, but butter will not. This will remind the user that he has already bought chicken, but still need to buy butter.
         - option 2: 
            - if the user refreshes the page, the only thing left on will be butter, to remind the user that they onlt have butter left to buy to be able to cook the Chicken Crunch recipe. 
    - Thinking about my options:
        - if I went with option 1, I would need to store the information about whether an ingredient is purchased. This is so that when the shopping list page is rendered, it knows which ingredient to render with a strikethrough. In this case, I would need to redo my models to have a new model 'ingredient_to_buy' that is related to 'recipe_to_buy_for'. The ingredient_to_buy model will likely have the fields: ingredient (as a string), ispurchased (boolean) and foreign key to recipe_to_buy_for.
        - If i went with option 2, my existing set up and models could support this. This is the option I decided on. 
    - This experience was invaluable. I am glad that my models were able to support my desired functionality. I was able to see first hand the importance of models and how I should always spend time to plan my models.


