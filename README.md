**DJANGO ONLINE VOTING SYSTEM**
A basic online voting system built wiht Django (Python) for backend and HTML + CSS for frontend.
This is a learning project aimed at exploring functions, logic building and the problem statement of voting manipulation through technology.
⚠️ **Note:** This project is incomplete and currently serves as a prototype/playground for experimenting with features

📌**Current Features**
1. Poll participation: Users can vote on polls ONLY ONCE.
2. Basic UI: No frontend frameworks, just raw HTML and CSS for simplicity
3. Database Logic: Poll data and votes are stored and checked via Django models

🔧**Current Limitations**
1. Polls must be created via the Python shell as there is no admin UI yet.
2. @login_required is missing on the homepage, so that edge case needs fixing.
3. No adming panel customization yet.
4. Minimal UI and no responsive design.

🛠️**Planned Features**

For Admins:
1. Create polls directly from the web interface
2. Add candidates, due, dates and poll catgories:
   a) Upcoming Polls -> "Starts in X days"
   b) Ending Soon -> "Ends in X hours"
3. Manage participants and results dynamically

For Users:
1. Participate Section: Users can submit entries for upcoming polls (e.g., Who wants to be CR?)
2. Thir names will appear in a dropdown when admins create polls.
3. User Profile page with past participation and voting history.

🚀**Future Goals**
1. Transition into a fully dynamic voting platform after learning Full Stack Dev
2. Possibly rebuild using Node.js/Express.js/React for a richer and interactive UX
3. Implement real-time updates and modern UI enhancements

⚙️**Tech Stack**
1. Backend: Django (Python)
2. Frontend: HTML, CSS
3. Database: SQLite (default for dev)
4. Authentication: Django's built-in user model

📁**How to Use**
1. Clone the repo
   git clone https://github.com/Aarushi-1604/Online-Voting-System.git
   cd Online-Voting-System
2. Install dependencies
3. Run migrations
   python manage.py makemigrations
   python manage.py migrate
4. Create a superuser
   python manage.py createsuperuser
5. Run the server
   python manage.py runserver
6. Create polls via shell
   python manage.py shell

📌**Note for Developers**
No sensitive data (.env or dbsqlite3) is committed, hence, safe to clone
This project is a _learning exercise_ so code may not follow production-level best practices yet. 
