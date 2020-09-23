
# Leave Management System Using Django

    The Leave Management System is a wweb application which can be used to automate leave application and approval process. 
    
    In this project, i have implemented complete  authentication system with two roles employee and manager. Used CRUD operation to access SQLite database. 
    
    Front end work is done with HTML, CSS, Bootstrap and at backend Python's web Framework Django is used. It has built in support for SQLite database. 

# Overview

        In Leave Management System, User will have to register himself first. After successful completion of registration he can login to web application to access data.
        
        This was simple authentication of user. The screenshots of this process are as follows
        
                    # Home
                    ![alt text](ScreenShots/Screenshot (2).png)

                    # Register
                    ![alt text](ScreenShots/Screenshot (5).png)

                    # Login
                    ![alt text](ScreenShots/Screenshot (6).png)
        
        Once user logged in, he will be redirected to leave status page. leave status page is shown below
        
                    # Leave Status
                    ![alt text](ScreenShots/Screenshot (7).png)
        
        To apply for leave, user have to go to "Apply For Leave" tab in navbar. 
        
                    # Apply For Leave
                    ![alt text]('https://github.com/SheetalJade2019/LeaveMgmtSystem/blob/master/ScreenShots/Screenshot%20(8).png')
        
        Then Only Manager can Approve or Decline leave. Once leave is approves total number of available leaves are calculated at backend and displayed in leave status table 
        

# Steps to run project

1) Donwload and install 

       Python : https://www.howtogeek.com/197947/how-to-install-python-on-windows/
       Django : https://docs.djangoproject.com/en/1.8/howto/windows/
       Rest Framework : https://www.django-rest-framework.org/#installation

2) Download Leave Management System Project. 

       https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository 
       link to my project : https://github.com/SheetalJade2019/LeaveMgmtSystem.git

3) Open command prompt. Change directory to Leave Management System. Run command

       python manage.py runserver
    
       if you see following text then your web applications is started
       ![alt text](https://github.com/SheetalJade2019/LeaveMgmtSystem/blob/master/ScreenShots/runlms.png?raw=true)
       ![alt text](https://user-images.githubusercontent.com/61681150/94037695-3eb9f800-fde3-11ea-99f9-ae5e5be7b636.png)
       
       <img src="https://github.com/SheetalJade2019/LeaveMgmtSystem/blob/master/ScreenShots/runlms.png" alt=" " width="500" height="600">
    
# Prerequisites
Before executing this project, you must have 

    Django==3.0.8
    djangorestframework==3.11.1
    Python==3.7.2

# Built With

    Django - Python's Web Framework

# Author

    Sheetal Jade 
    [Github Profile](https://github.com/SheetalJade2019)
    [Linkedin Profile](http://www.linkedin.com/in/sheetal2019)
    
# Acknowledgments

    A very big thank you to those who helped, inspired and guided me directly and indirectly.
