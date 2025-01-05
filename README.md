# Journal App

## Distinctiveness and Complexity
The **Journal** web application is designed to provide a secure and interactive platform for users to document their thoughts and experiences through journaling. A key feature of the app is the flexibility to keep journal entries private or share them with others, giving users full control over their content. This allows for a personalized journaling experience, where users can choose how they want to engage with their entries. Unlike the social media or e-commerce platforms, this app focuses on journaling and the core feature of being able to make entries public or private.

Initially the project was created with simply the journal entry functionality. Essentially the only notable feature was being able to set your entry as public or private. After pondering for a bit I was able to come up with more features to implement into the project such as a search bar for various entry titles, markdown functionality for more stylish journal entries from users alongside a dark mode button to toggle on and off darkmode for users who want that experience.

Distinctively, this project utilizes Django for the back-end to manage user authentication and journal entries, while incorporating JavaScript to provide a dynamic and responsive front-end experience. The app's complexity lies in the implementation of key features such as a fully functional search bar, a light and dark mode toggle, and Markdown compatibility for rich-text editing. Additionally, the responsive design ensures that the app adapts seamlessly to different screen sizes, offering a smooth user experience on both mobile and desktop devices. The project also includes additional features like the ability for users to edit, delete, and view their journal entries. Allowing users to change or remove their entries as they please.

This project satisfies the complexity requirements by integrating front-end JavaScript (e.g., for the light and dark mode functionality/edit popup) alongside the impelmentation of a search bar and compatability with markdown. Setting it apart from other course projects.

Future enhancements for the application may include features inspired by Instagram Stories, enabling users to share their journal entries privately with specific friends or contacts within their network. This functionality would require implementing a friend system with access control for selective sharing. Additionally, plans are in place to integrate an improved file upload feature, allowing users to easily attach images directly into the journal entry text area. This would involve expanding the existing file handling capabilities to support seamless image uploads while maintaining data integrity and user privacy.



## Files Overview
The project includes the following key files and directories:

journalcapstone/urls.py: URL routing for the application. Defines endpoints for user registration, login, journal entry views, etc.

journalcapstone/models.py: Contains Django models representing the application's core data (e.g., User, JournalEntry, publicity, etc).

journalcapstone/views.py: Handles the logic for processing requests and rendering the appropriate templates for views such as the journal dashboard, entry detail page, etc.

journalcapstone/static/: Contains static files like CSS and JavaScript. The JavaScript here powers the editing functionality alongside the light and dark mode toggling.



## How to Run the Application
1. Clone the repository:
To get started, clone the project repository to your local machine using Git:

git clone https://github.com/CassiusMercellus/Harvard-Capstone

2. Install dependencies:
Install the necessary Python packages from requirements.txt:


pip install -r requirements.txt

3. Apply migrations:
Create the database schema by running the following command:

python manage.py migrate


4. Run the development server:
Start the Django development server:

python manage.py runserver

5. Access the application:
Open your browser and go to http://127.0.0.1:8000/ to view the application.


## Additional Information

Responsive Design: The web application is fully responsive, ensuring that users have a smooth experience on devices ranging from smartphones to large desktop monitors.

Markdown Support: Journal entries support Markdown formatting for enhanced content creation and formatting.

## Dependencies

The following Python packages are required to run this application:

Django
djangorestframework
markdown
