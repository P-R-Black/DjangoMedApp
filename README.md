
# A Simple Meditation Application

#### Video Demo URL: https://youtu.be/IVx3p5eXFsc
The mediation application allows a user to start meditating in less than a few clicks. The application tracks a users pre-meditation mood, and it also provides several soundscapes for anyone who prefers to have background noise while they mediate. By picking a mood (up to five allowed), background music, and a length of time to meditate, the user can start meditating.

For users who just want to get in a quick meditation session. By clicking the "Meditation" link, a mood - "Content" - a background noise, and a length of time to meditate have already been preloaded and only requires the user to hit the "Start Timer" button.


## How to Use Melete
#### Register:
To use Melete, first register by providing a user name, email address, date of birth, and password.

#### Login:
After registering, the user will login by providing they username and password they provided during registration.

#### Quick Meditation:
Once logged in, the user can go into a brief meditation session by clicking on the "Meditate" link in the navigation bar.

#### Customized Meditation:
Once logged in, the user can customize their meditation by selecting how they are feeling, choosing background noise to meditate too, and by choosing the amount of time they would like to meditate. Towards the bottom of the page, in the meditation box, once the usr clicks the "Start Timer" button, the background music and the countdown timer will begin. Once the timer reaches 0:00, the music will stop, and a bell will notify the user that the meditation is over.

#### History
By clicking on the "History" link in the navigation bar, the user can view their meditation history. The history will provide the date of their medidtations, along with their pre-medition mood/moods, the background music they selected to meditate to, and the amount of time they meditated.

#### Logout
By clicking on the "Logout" link in the navigation bar, the user will be logged out.

## Project Details
Django was the framework used for this project. 

"meditation" is the project application folder. Within the meditation app folder the admin.py, apps.py, decorators.py, forms.py, models.py, tests.py, urls.py and views.py files can be found.

#### admin.py

The admin.py file is responsible for the layout of the administration page. The administration page, is where the app creator can add moods, soundscapes, and view the number of users.

#### apps.py

The apps.py file is created when a Django project is created, and didn't require adjusting for this project.

#### decorators.py

The decorators.py file holds the code for the decorator that is used to restrict access to certain pages of the site to users who aren't registered and logged-in.

#### forms.py

The forms.py file is used to create the form needed for user registration.

#### models.py

The models.py file is used to create the databases needed for the application. For Melete, users, the background music, the music used to notifiy the user that the end of the meditatin session has ended, and the user's meditation history have their own database within the Melete app.

#### test.py

The test.py file is used to create function and class test for the applicaton. No test were written for this application.

#### urls.py
The urls.py file is used to create the paths to the web pages needed for the Melete application.

#### views.py
The views.py file is used to create the views needed for each website page. The view created for each page is used in the url.py file.

### meditation/static

#### app.js

In the app.js file, the code required to make the applicaton functional for th user is located. Within app.js, the code needed to create the mobile navigation menu can be found. Also, the **setGreeting** function greets the login user with a different message depending on the time of day. The **selectSound** function, allows user to select a sound and have that sound loaded to play once the meditation timer starts. the **playAudio** function, allows the song to be played and paused. The **selectMood** function, allows a user to select up to five moods, to express how they're are feeling before their meditation session. The **removeLi** function allows the user to edit their selected mood. The **theSelectedTime** function allows the user to change the length of time they want to meditate. The **timerCountdown** function displays the countdown timer to the user. 

The **moodSummary** function collects the moods the user selected after the mediation is completed. The **finalBackdropSummary** secures the sound choice of the meditation, and **finalTimeSummary** secures the amount of time the user mediated for. The **getCookie** function along with the **sendPost** function, takes the values of **moodSummary**, **finalBackdropSummary**, **finalTimeSummary**, and saves them to the database that keeps track of the user's history.

#### styles.css

The styles.css file is used for styling the website.

### meditation/templates

#### attributes. html
Provides recognition to the sound used for the project. The links to the right's owner's YouTube page is listed with the name of the YouTube page.

#### history.html
Provides a table displaying the user's meditation history.

#### index.html
Is the home page for the project, and it's the page the user is shown upon logging in.

#### layout.html
The layout.html file is a template page that has the navigation bar and footer that's is displayed in the other html files. The layout.html page also holds the metadata and script tags needed for Melete to function.

#### login.html
The login.html file is the page users view when they are ready to log in.

#### logout.html
The logout.html file is the page users will view when they have logged out of the applicaton.


#### mediate.html
The mediate.html file provies a mediation box pre-filled with a mood, background music, and a 5 minute timer. Users can use this if they want to get get right into meditating.

#### register.html
The register html file provides the page needed for users to register to use the Melete site.



## Acknowledgements

 - [The Easiest Way to Create a README For Github](https://youtu.be/QcZKsbgsLa4)
 - [Background Music Used]
 - [Campfire, Wind, and River](https://www.youtube.com/watch?v=xx_w4RFwUuw)
 - [Crashing Waves](https://www.youtube.com/watch?v=59vAvqo8Et0)
 - [Koto Zen Garden](https://www.youtube.com/watch?v=FpqivQ6P0s4)
 - [Meditative LoFi](https://www.youtube.com/watch?v=nhZyPQzx7JI)
 - [Mountian Wind and an Open Fire](https://www.youtube.com/watch?v=EqqpcFj8G-s)
 - [Relaxing River](https://www.youtube.com/watch?v=ScLySiULmvA)
 - [Tibeetan Bowls (Indoors)](https://www.youtube.com/watch?v=kSaOxSLEHfg)
 - [Tibetan Bowls Outdoors](https://youtu.be/VvO_7ejeKVc)
 - [App Idea Inspired By]
 - [developedbyed](https://www.youtube.com/watch?v=oMBXdZzYqEk)



## Authors

- [@P-R-Black](https://www.github.com/p-r-black)


## FAQ

#### Why create a meditation app?

The popular meditation apps of the day have a lot of features that I don't need. Also, many of the features found in meditation apps are behind a paywall. I just wanted an app that I could use to track when I meditate while providing a timer and background music.



## Features

- Responsive Design
- History of meditation times and mood at time of meditation
- Fullscreen mode


## Demo

Insert gif or link to demo

https://youtu.be/IVx3p5eXFsc
## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?

1. Why Ajax and jQuery are important. One of the issues I ran into was clicking on a mood, having that mood load into mediation box, and then sending the mood along with other information to the Django database without refresing the page when the meditation timer started. While solving this problem I learned why Ajax is so important.

2. When thinking about JavaScript functionality, before writing the code, think about functionality with the beginning, the middle, and the end in mind. On several occassions I wrote a function that did the first thing I needed it to do, but would have to rewrite it later on. For instance, to get the music to play was pretty simple, but the initial code didn't allow for the music to pause and pause the timer and restart the music without resetting the timer. In another case, the function that moved the selected mood to the meditation box, had to be redone in order to prevent adding one mood twice and to allow for the mood to be removed by the user from the meditation box. 
## Screenshots

Melete Registration Page
![Melete Registration Page](https://res.cloudinary.com/prblack/image/upload/v1672179736/Mediation/Mediation%20App/Melete%20Registration%20Page.png)
Melete Login Page
![Melete Login Page](https://res.cloudinary.com/prblack/image/upload/v1672179736/Mediation/Mediation%20App/Melete%20Login.png)
Melete Home Page
![Melete Home Page](https://res.cloudinary.com/prblack/image/upload/v1672179731/Mediation/Mediation%20App/The%20Melete%20Home%20Page.png)
Melete Meditation Box
![Melete Meditation Box](https://res.cloudinary.com/prblack/image/upload/v1672180114/Mediation/Mediation%20App/The%20Melete%20Meditation%20Box.png)
Melete Quick Meditation Page
![Melete Quick Meditation Page](https://res.cloudinary.com/prblack/image/upload/v1672179731/Mediation/Mediation%20App/The%20Meditation%20Page.png)
Melete Logout
![Melete Logout](https://res.cloudinary.com/prblack/image/upload/v1672179736/Mediation/Mediation%20App/The%20Melete%20Logout%20Page.png)
Melete Home Page Mobile 1
![Melete Home Page Mobile 1](https://res.cloudinary.com/prblack/image/upload/v1672180659/Mediation/Mediation%20App/Melete%20Home%20Page%20Mobile%201.png)
Melete Home Page Mobile 2
![Melete Home Page Mobile 2](https://res.cloudinary.com/prblack/image/upload/v1672180661/Mediation/Mediation%20App/Melete%20Home%20Page%20Mobile%202.png)


## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Django


## Support

For support, email ramoneblack@me.com
