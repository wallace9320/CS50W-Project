# CS50W-Project
# Final Project of Online Course CS50W Web Programming in Python and JavaScript by Harvard, edX

### Video link of Screen Recording demonstrating the website:
https://youtu.be/qd0kD69FR04

### Distinctiveness and Complexity:

This project is distinct from all projects done before. In Project 4, other users can interact with the posts only through likes, and in Project 2, input from other users are only through bids and comments, which will not receive feedback, but in this project, other users can answer quizzes and gain feedback on their responses. Also, in Project 4, a following system is used for navigating posts, but in this project, the user can easily find the quizzes they created or answered by pressing relevant buttons, or find quizzes by manual search with the exact username of the quiz creator or part of the quiz title. This is also distinct from the search function in Project 1 as JavaScript is utilized. A new type of input, radio, is also introduced in this project.

Complexity is displayed in many places in the project. Firstly, users can create quizzes with 3 to 5 questions depending on their preferences by pressing ‘add question’ and ‘remove question’, meaning that I have to account for different number of questions for different quizzes, and also use JavaScript to dynamically change the number of questions when the buttons are pressed (this can be easily scaled to even more questions by simply adjusting the numbers in create.js, but is kept at this range for easier demonstration of this function). Secondly, the users can view not only their scores after completion, but also their responses to each question, and whether they got each question correct. The user can view their own results any time and for however many times after they completed the quiz. To facilitate this, an extra model ‘Option’ is created to facilitate storage of relevant data (i.e. which user chose which option). Last but not least, all users, including the quiz creator, can view the scores of all users who attempted the quiz, and the scores are arranged in descending order. The current user’s score is highlighted by italic font to make it easier for the user to distinguish.

Aesthetic-wise, various features are used to make the website look nicer. For example, different Bootstrap buttons are used for different categories of buttons. In addition, shadow is added to the boxes containing each item to make the boxes look more realistic and 3D.

### Description of what is contained in each file:

Quiz is the app I created in Django, and the quiz folder contains all the normal python files one would expect to find. In models.py, 5 models have been created: 
1.	User for storing user information
2.	Quiz for storing the owner, title, time created as well as list of users who answered the quiz
3.	Question for the question (3-5 per quiz)
4.	Option for option, whether the option is correct, and list of users who answered this option (4 per question)
5.	Score for storing the scores of each user for each quiz so that they can be easily accessed when displaying scores

In views.py, functions display and search are APIs for JavaScript JSON fetching. Most other functions render html documents with the same name, and they are briefly described below.

Inside templates, attempt.html contains the template for when a user attempts the quiz (the creator cannot attempt the quiz, and each user can attempt the quiz only once; as such, they will be denied from attempting the quiz if they try to do so by directly entering relevant url). In create.html, a form initially containing a title and three questions is provided for the user to fill in the question, options and the correct option. Using the ‘add question’ and ‘remove question’ buttons the user can adjust the number of questions between 3 and 5. The functions of the button are stored in create.js. In index.html, quizzes are displayed in reverse chronological order, and users can click to attempt the quiz if they have not completed it and if they are not the quiz creator (attempt.html), view their results if they have completed it (result.html), or view the results of attempts by all users (otherresult.html). The user can switch between ‘All Quizzes’, ‘Quizzes Created’ or ‘Quizzes Completed’, and can also filter quizzes by username or title. The behaviors of the buttons and the search bars are controlled by functions in quiz.js. All users must be logged in to view the quizzes, and if they are not logged in, they are redirected to login.html. In result.html, the users can view their performances in past attempts, including the score, the correct response to each question, their response and whether they got the answer right or wrong (as displayed by checkmark in green or cross in red)(similar to attempt.html, the user will be denied access through direct url entry if they created the quiz or if they have not answered the quiz yet). In otherresult.html, the results of all users who attempted the quiz are displayed in a table. All css elements are stored in styles.css.

In layout.html, the general framework of the website is defined, and is basically same as that found in Project 2 and 4. login.html and register.html allows the user to login and register respectively, and is also basically same as that found in previous projects. 

### How to run the application:

To run the application, the user can run the application like how one would run a Django application, i.e. by python manage.py runserver. Afterwards, the user should create an account and can then proceed to use the application.
