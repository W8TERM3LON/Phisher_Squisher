# <div align="center"> 🚫Phish🚫

## Phishing sites getting on your nerves? Feed them fake data! Lots of it!

# <div align="center"> About

**🚫Phish🚫** is a easy to use program written in Python used to combat phishing scams by feeding them massive amounts of fake logins, thus rendering their valid logins that they phished up near impossible to find nor use, at the same time forcing them to either temporarily close the site or abandon it completely due to the massive amounts of unusable data.

# <div align="center"> Features
- Allows you to feed massive amounts of fake usernames and passwords to phishing sites.
- Uses randomly generated first names, last names, order, numbers and variable length passwords.
- Picks between 9 different email providers to maximize legitimacy. (more can be added)
- Other parameters can also be included such as screen size and window resolution to further confuse up the scammers.
- Proxies can be used to prevent being IP blocked or to prevent IP leakage.
- Works on sites with HTTPS.
- Blocks redirects.

# <div align="center"> Usage

# Python

**Python 3.5.3 or higher is recommended**

Navigate to line 19, and replace "REPLACE WITH URL" with URL to the login query.

```Python
    url = 'REPLACE WITH URL'
```
Navigate to lines 89-92 and replace "login_email" and "login_password" with the parameters specified in the POST request.

```Python
    s.post(url, allow_redirects=False, verify=False, data={
		'login_email': username,
		'login_password': password,
	})
 ```
If proxies need to be used, uncomment line 13 (deleting the #) and add proxies as needed lines 5-8.
```Python
#s.proxies = proxies
```

# Jupyter Notebook, Google Colaboratory, Kaggle, AWS Sagemaker, etc

**Ready to use Colaboratory version [here](https://colab.research.google.com/drive/1MidYKosEovRzeUNP8iMIo2NG9vgI-La_).**

**Note: Google Colaboratory has a maximum time limit of 12 hours per session. Usually less if you're not using GPU or TPU.**

Navigate to line 19 on cell 2, and replace "REPLACE WITH URL" with URL to the login query.

```Python
    url = 'REPLACE WITH URL'
```
Navigate to lines 89-92 on cell 2 and replace "login_email" and "login_password" with the parameters specified in the POST request.

```Python
    s.post(url, allow_redirects=False, verify=False, data={
		'login_email': username,
		'login_password': password,
	})
 ```
If proxies need to be used, uncomment line 13 on cell 2 (deleting the #) and add proxies as needed lines 5-8.
```Python
#s.proxies = proxies
```
# <div align="center"> Tips
- You must have the names library installed. Either install it in virtualenv or install it on your system by using pip install names (in terminal)

# <div align="center"> Inspirations
- Took inspiration from Engineer man's video on [spamming a scammer](https://www.youtube.com/watch?v=UtNYzv8gLbs). 

- Take a look at his repo [here](https://github.com/engineer-man/youtube/tree/master/033).

- Watch his video if you need help on getting the URL and form data. Start watching [here](https://youtu.be/UtNYzv8gLbs?t=40).

# <div align="center"> PLEASE DO NOT USE THIS FOR MALICIOUS PURPOSES.
