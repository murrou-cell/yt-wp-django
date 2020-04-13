# yt-wp-django
A Python script that is used to automate Wordpress site for Youtube content using **XML-RPC**, **Django** and **pytube**.
<p><h1>HOW TO USE</h1></p> 
In <b>AutoWpPost</b> folder there are 2 python files, <b>execute.py</b> and <b>main.py</b>.
The file <b>execute.py</b> is there only for example using the script with "cron".

The file <b>main.py</b> is the base script that contains information for connecting with the Wordpress site.

You should modify the 8th row of the file with your credentials to be functional.


The 45-th row in the main.py is where you should modify the "downloadlink" variable with your Django server IP.


In the django-app folder are the <b>urls.py</b> and <b>views.py</b> that you should use for your django server.

<p><h1>HOW IT WORKS</h1></p>

 
Basicly execute.py executes functions from main.py that takes information from youtube like embed url videoID and process it automaticly to your site in readable format also uses django webserver with pytube to redirect the user to music-video direct mp4 stream with download button.
