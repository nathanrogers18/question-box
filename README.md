#Question-box
Stack-Overflow clone using Python, Django, Django REST, HTML, CSS, JavaScript, jQuery, and AJAX -- deployed to Heroku.


#Objectives
This assignment is meant to test our whole knowledge of Python and JavaScript as tools to build web applications.


#Collaborators
In addition, it is a test of working in a team. On this team:
- Jon Alligood: https://github.com/jonalligood
- Maggie Correll: https://github.com/maggiecorrell
- Tara Davis: https://github.com/tarakdavis
- Nathan Rogers: https://github.com/nathanrogers18


#Important files in this app
requirements.txt - pip install requirements by entering 'pip install -r requirements.txt' in your command line
runtime.txt - Python version necessary to run this app


#Requirements
No PEP8 or Pyflakes warnings or errors.
No JSHint warnings or errors.

Create a GitHub organization for your team to use.
  - Plan your models together.
  - Plan for incremental feature build-out.
  - Plan for the division of work among your team-members.
  - Create models, views, and templates for each feature in feature branches, and merge them into master as features are completed.
  - Create a dynamic user interface that works with your backend web app and API.
  - Deploy to Heroku and test often - don't put this off to the last minute!

Build a complete app (back-end Django app, back-end REST API, and front-end UI) to ask questions and accept good answers. The functionality of this is inspired by one of your most used sites the last two months, Stack Overflow.


#Features
###Ask questions
- Answer questions
- Vote on answers positively or negatively
- Questions need to have:
  - A title
  - The question text
  - Any number of tags (tags being short phrases that show the topics of the question)
###Any number of answers
Answers need to have:
- The answer text
- A score based on the sum of all votes

###Users can also have:
- A profile page that shows their score and other info.
- A score.
  - The score starts at 0, and increases in the following ways:
  - When a user asks a question, +5 points.
  - When a user's answer is upvoted, +10 points per positive vote.
  - When a user's answer is downvoted, -5 points per negative vote.
  - When a user downvotes an answer, -1 point (yes, it costs from your score to vote something down).
- Track all events that change a user's points and show them on the user's profile page.

###Questions can also have:
- An accepted answer. The question's author can accept one and only one answer given. The author of the answer gets +100 points.
- Votes and comments.
### Answers can also have:
- Any number of comments about the answer.
- Questions and answers can be edited or deleted by their owners until:
  - 10 minutes have passed.
  - In the case of a question, it cannot be edited or deleted after it has one or more answers.
  - In the case of an answer, it cannot be edited or deleted after it has one or more votes or comments.
