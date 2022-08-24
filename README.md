<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/72341453/134747028-7e2d90cc-a92f-4f66-815e-54a0d50cca54.PNG">

# StudyBuddy
</div>

This project is forked from [StudyBud](https://github.com/divanov11/StudyBud) to improve the original functionality.

## Improvements

* Implemented asynchronously updating Rooms with WebSockets, Django Channels and Redis
* Added Like/Unlike Functionality for Room Messages
* Implemented Online/Offline status for Users
* Further minor changes

### Cloning the repository

--> Install Redis, if not already installed :
```bash
brew install redis
brew services start redis

```


--> Clone the repository using the command below :
```bash
git clone https://github.com/RonnieBlade/StudyBud-with-DjangoChannels.git

```

--> Move into the directory where we have the project files : 
```bash
cd StudyBud

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="100%">      
&nbsp; 
<br>
<p align="center">
  Room with Likes
</p>
<img src="likes_screenshot.png">
</table>
