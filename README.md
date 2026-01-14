# Pokémon Performance Analysis Using SQL and Power BI
This project builds an automated pipeline that scrapes Pokémon data from PokémonDB, stores it in a self-hosted SQL database, and analyzes the data using Power BI. The analysis focuses on identifying high-performing and statistically strong Pokémon based on key performance metrics, whether that is speed, defense or overall total stats. 
## How to Navigate this Project
-   'Screenshots' is home to images of my dashboards and some of its functions
-   'Datascraper.py' is the main webscraping and data collecting script.
-   'Database_Schema.sql' is my sql code for creating the actual Schema

## Things I learned ✅
-   Basic usage of Bs4 library for Webscrabing and digging through a sites html code
-   Using Pandas for simple Transform and Datacleaning.Some Data cleaning is also done when webscraping.
-   MYSQL and a of DAX function in PowerBi, embedding image, custom DAX function and Measures to show current item/pokemon vs the Average Performace and many others
-   PowerBI visualization: filters, graphs and overall creating a visually aesthetic dashboard

## Things I would do different/improve if I had more time
-   Create more pages on the PowerBI dashboard/report, perhaps charts showing any trends with certain stats like, scatterplot showing relationship between speed/defense, or health/attack
  Overall going more in-depth on certain aspects instead of a brief overview of which pokemon performs the best. Going more indepth on why? does a pokemon perform better, what stats are significant?
-   If this was for more larger scale datasets, perhaps switching pandas to Apache spark, investing more time into a better transform/data cleaning process.
-   Although this project was done on pokemon, future projects could focus on products and sales. Perhaps instead of highest performing Pokemon, it could be certain top performing products/sales, their profit%
  and how that specific product sales and performance compares to the overall average %, similar to what I had in this project with Pokemon.

Thank you for viewing!
