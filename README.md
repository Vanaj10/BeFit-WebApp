# Project Title: BeFit
#### Video Demo:  https://youtu.be/seIdxyQp7Bc
#### Description:
I am Vanaj Kamboj and this is my final project for CS50x 2021
I have build a web application using Flask framework which is called BeFit.

The purpose of this website is to let users easily calculate their:
> Basal Metabolic Rate(BMR)

Basal Metabolic Rate is the number of calories your body needs to accomplish its most basic (basal) life-sustaining functions.
So with the help of BMR you can plan your nutrition according to your goal.

> Body Mass Index(BMI)

BMI (Body Mass Index) is a measurement of body fat based on height and weight that applies to both men and women between the
ages of 18 and 65 years. BMI can be used to indicate if you are overweight, obese, underweight or normal. A healthy BMI score
is between 20 and 25

> Body Fat Percentage

The body fat percentage is the total mass of fat divided by total body mass, multiplied by 100 body fat includes essential
body fat and storage body fat. Body fat percentage is a measure of fitness level
> Ideal Weight

The two primary parameters that impact your health – your height and weight are co-related using height and weight charts.
It sets the standards for you to determine if your height and weight are in harmony, mirroring the state of your health.


I have created 10 templates for this project which includes the 2 pages for each of the above
calculators (GET and POST scenarios) along with the main homepage and layout.

In styles.css I have considered colorful design choice for logos and sub headings because I feel people looking
for answers to their body goals need to look at their results in a cheerful way which the colors
reflect :)
All the design and navbar links are there in the template layout.html that is used throughout the project

The template bmr.html is run using the method GET and takes in takes input of four values from the user which are height, weight, age and gender
and runs a formula in application.py using POST method which is different for males and females to calculate BMR
and then renders template bmirtable.html
> for males BMR = (10*weight) + (6.25*height) - (5*age) + 5
> for females BMR = (10*weight) + (6.25*height) - (5*age) + 161
B


The template bmi.html takes in takes input of four values from the user which are height and weight
and runs a formula in application.py using POST method and then renders template bmitable.html
> BMI = (weight/(height * height))*10000

The template fat.html takes in input as height, weight and age and renders template fattable.html
formula used
> For males fat = (1.2*bmi) + (0.23*age) - 16.2
> For females fat = (1.2*bmi) + (0.23*age) - 5.4

The template weight.html takes in height and gender from the user and displays Ideal weight for the user
by rendering template weighttable.html

Lastly there is the python application file which contains all of the calculations and data that is
dynamically processed to give the final result

Thank You
