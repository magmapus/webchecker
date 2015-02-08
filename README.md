# webchecker
A small python script to send pushbullet notifications when there's a change to websites.

Make sure to install the dependancies:

`pip install requests`

then pull submodules (for pushbullet support)

`git submodule pull`

Now make a pushbullet config file:

` ~/.config/pushbullet`

with the text
`API_KEY=your api key for pushbullet`

You can get your API key [here](https://www.pushbullet.com/account)

Edit `websites.conf`. The first column is the URL to the website, the second is the name that's pushed. Note the tab separation!

Run runme.py with python2, and enjoy!


