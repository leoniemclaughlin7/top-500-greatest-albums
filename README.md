# Flowchart

<img src="assets/readme-images/flowchart-top-albums.png">

# Testing

Testing of the functionality of this python terminal based application can be seen in the following tables. All testing was carried out in the deployed version of this application. 

### Menu

|Feature  | Expect  | Action | Result | 
|--|--|--|--|
| Option 1 | When option 1 is selected the user will be redirected to a list of all albums |Chose option 1 | pass
|Option 2 | When option 2 is selected the user will be redirected to a list of the top 100 albums  |Chose option 2 | pass
|Option 3 |When option 3 is selected the user is redirected to the owned list if this list is empty the user will be informed of this |Chose option 3| pass
|Option 4|When option 4 is selected the user is directed to a search menu |Chose option 4 | pass
| Input incorrect selection (integer) |An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4" |Chose 5 as a selection | pass
|Input incorrect selection (string)|An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4"|Chose "cat" as a selection | pass
|Input incorrect selection (empty)|An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4"|Enter empty input | pass

### Owned menu 

|Feature  | Expect  | Action | Result | 
|--|--|--|--|
| Option 1 | When option 1 is selected the user will be asked to input the ranking of the album they would like to add to the owned list |Chose option 1 | pass
| Input value out of range for option 1 | An error message will appear in red "Invalid input: Please enter a number between 1 and 500" |Input 501 | pass
| Input string for option 1 | An error message will appear in red "Invalid input: Please enter a number between 1 and 500" |Input "cat" | pass
| Input empty value for option 1 | An error message will appear in red "Invalid input: Please enter a number between 1 and 500" |Input empty value | pass
| Input value already in list for option 1 | An error message will appear in red "Album already in list!" |Input value already present in list | pass
|Option 2 | When option 2 is selected the user will be asked to chose the ranking of the album they would like to remove |Chose option 2 | pass
| Input value out of range for option 2 | An error message will appear in red "Invalid input: Please enter a number between 1 and 500" |Input 501 | pass
| Input string for option 2 | An error message will appear in red "Invalid input: Please enter a number between 1 and 500" |Input "cat" | pass
| Input empty value for option 2 | An error message will appear in red "Invalid input: Please enter a number between 1 and 500" |Input empty value | pass
| Input value not in list for option 2 | An error message will appear in red "Album not in owned list!" |Input value not in list | pass
|Option 3 |When option 3 is selected the user is redirected back to the main menu |Chose option 3| pass
|Option 4|When option 4 is selected the user is directed to the opening title including the main menu |Select option 4 | pass
| Input incorrect selection (integer) |An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4" |Chose 5 as a selection | pass
|Input incorrect selection (string)|An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4"|Chose "cat" as a selection | pass
|Input incorrect selection (empty)|An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4"|Enter empty input | pass

### Search menu

|Feature  | Expect  | Action | Result | 
|--|--|--|--|
| Option 1 | When option 1 is selected the user will be asked to input a search query according to the album title |Chose option 1 | pass
| Input string that is not a valid query for option 1 | An error message will appear in red "No albums found, please try again!" |Input "poxa" | pass
| Input empty value for option 1 | An error message will appear in red "Invalid input: Input cannot be empty" |Input empty value | pass
|Option 2 | When option 2 is selected the user will be asked to "Please input a year from 1955 to 2011"|Chose option 2 | pass
| Input value out of range for option 2 | An error message will appear in red "Invalid input: Please try again!" |Input 2012 | pass
| Input string for option 2 | An error message will appear in red "Invalid input: Please try again!" |Input "cat" | pass
| Input empty value for option 2 | An error message will appear in red "Invalid input: Please try again!" |Input empty value | pass
|Option 3 | When option 1 is selected the user will be asked to input a search query according to the album artist |Chose option 3| pass
| Input string that is not a valid query for option 3 | An error message will appear in red "No albums found, please try again!" |Input "poxa" | pass
| Input empty value for option 3 | An error message will appear in red "Invalid input: Input cannot be empty" |Input empty value | pass
|Option 4|When option 4 is selected the user is asked to input a search query relating to genre |Select option 4 | pass
| Input string that is not a valid query for option 4 | An error message will appear in red "No albums found, please try again!" |Input "cat" | pass
| Input empty value for option 4 | An error message will appear in red "Invalid input: Input cannot be empty" |Input empty value | pass
| Input incorrect selection (integer) |An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4" |Chose 5 as a selection | pass
|Input incorrect selection (string)|An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4"|Chose "cat" as a selection | pass
|Input incorrect selection (empty)|An error message in red is displayed to the user "Invalid input: Please choose a number between 1 and 4"|Enter empty input | pass

## Validator Testing

###  CI Python Linter
The Three python files run.py, search.py and owned.py where passed through the official [CI Python Linter](https://pep8ci.herokuapp.com/#)

There where Two warnings relating to trailing whitespace on lines 179 and 182 in run.py, in which the ASCII art is defined, these whitespaces were not removed as it would change the look of the ASCII art. 

<img src="assets/readme-images/run.py.png">

There where no errors present in owned.py.

<img src="assets/readme-images/owned.py.png">

There where no errors present in search.py.

<img src="assets/readme-images/search.py.png">

# Deployment 

1. Create a list of requirements that the project needs to run.  Heroku must install the dependencies used in the project. To do this type the command ```pip3 freeze > requirements.txt``` in the terminal to update the requirements.txt file.
2. Navigate to heroku.com and either log in or sign up using the form provided. 
3. Click create app from your Heroku dashboard.
4. Give the app a unique name.
5. Navigate to the settings tab.
6. Add a Config Var with a key of ```PORT``` and value of ```8000```.
7. Add Buildpacks first python and then node.js.
8. Navigate to the deploy tab.
9. Select GitHub as the deployment method.
10. Search for GitHub repository, click connect to link up the GitHub repository to our Heroku app.
11. You can choose to either automatic deploy or manually deploy the app.
12. Automatic deploy will build the app each time it is pushed to GitHub. To enable this choose the branch you would like to deploy and click ```Enable Automatic Deploys```. 
13. To manually deploy the app click ```Deploy Branch```.
14. To view the deployed app click ```Open app``` at the top of the page.