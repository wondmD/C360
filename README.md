# University Resource Web App


This repository contains a Django-based web application designed to provide digital resources and course information to students at my university. 
The web app aims to streamline the process of accessing and managing educational materials, making it easier for students to find and utilize the resources they need.
## Features- **User Authentication**: 
Students can create accounts and log in to access personalized features.- 
<br>
**Course Catalog**: 
The app provides a comprehensive catalog of courses offered at the university. Students can search for courses.- 
<br>
**Resource Repository**: 
The web app offers a centralized repository for digital resources related to each course. Staffs can upload lecture slides, assignments, and other relevant materials, which students can then access and download.- 
<br>
**Discussion Forum**: The app includes a discussion forum where students can engage in academic discussions, ask questions, and seek help from their peers or instructors.- 
<br>
**Personalized Dashboard**: Each student has a personalized dashboard that displays their enrolled coursesand.- 
<br>
**Responsive Design**: The web app is designed to be responsive, ensuring optimal user experience across different devices and screen sizes.
<br>
## Getting StartedTo get a local copy of the project up and running on your machine, 
<br>follow these steps:1. <br>
**Prerequisites**: Make sure you have Python and Django installed on your system. You can download Python from the [official Python website](https://www.python.org/), and install Django using pip:
<br> ```pip install django   ```<br>
2. **Clone the Repository**: Clone this repository to your local machine using Git:   <br>
```git clone https://github.com/wondmD/C360.git   ``` <br>
3. **Set Up the Environment**: Navigate to the project directory and create a virtual environment: <br>
```cd C360   python -m venv env   ``` <br>
4. **Activate the Virtual Environment**: Activate the virtual environment using the appropriate command for your operating system:<br>
-**Windows**:     ```env\Scripts\activate     ```   <br>- **Unix or Linux**:     ```source env/bin/activate     ``` <br>
5. **Install Dependencies**: Install the project dependencies using pip:   ```pip install -r requirements.txt   ``` <br>
6. **Database Migration**: Apply the database migrations to set up the initial database schema:  <br> ```python manage.py migrate   ```<br>
7. **Create Superuser**: Create a superuser account to access the admin interface:   <br>```python manage.py createsuperuser   ```<br>
8. **Start the Development Server**: Start the development server using the following command:   <br>```python manage.py runserver   ``` <br>
The web app will be accessible at `http://localhost:8000` in your browser.
## Contributions to this project are welcome! 
If you find any issues or have suggestions for improvements, please submit an issue or create a pull request. Make sure to follow the existing code style and provide detailed information about your changes.
## Acknowledgments- 
Thanks to the Django community for providing a robust web framework.- Special thanks to all the contributors who helped shape this project.
## ContactFor any inquiries or feedback, 
please contact [wondmenehdereje@gmail.com](mailto:wondmenehdereje@gmail.com).Happy learning!
