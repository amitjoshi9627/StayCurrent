# StayCurrent
StayCurrent is a python program which scrapes latest news headlines and your local weather and can also deliver it right it into your mail inbox.

**To start the program just run `python staycurrent.py`**.

## Dependencies

Requires Python 3.4+ and pip3 for installing and running.

It relies on Firefox headless mode, so make sure you have Firefox version > 56.0 installed, also **geckodriver** is needed, you can follow [Install geckodriver for firefox](https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu) to see how to download and configure it.

## Before you send an email

If you try to run the script with your credentials, you’ll probably get an error like this one.

**smtplib.SMTPAuthenticationError: Please log in via your web browser and then try again. Learn more [here](https://support.google.com/mail/answer/78754)**

So what does this error mean?

Don’t worry. There is actually nothing wrong with the code.

Gmail by default tries to make your email secure by preventing this type of third-party access. You can manage your gmail security settings by going to [this link](https://myaccount.google.com/lesssecureapps) and allowing less secure apps. It’s turned off by default so you have to turn it on.
