hurricanehackers.com
====================

Problem:
========
Live updates are being made to the google docs:
*https://bit.ly/hh-index
*https://bit.ly/hh-linklist
*https://bit.ly/hh-projects
*https://bit.ly/hh-timeline
*Add your new collaborative page here: (did I miss any?)

But this excellent collaboration is not being reflected on the website which is a shame! Booo!

Solution:
=========
*Conenct our live google docs via the google python API: https://code.google.com/p/gdata-python-client/
*django - throw in a little django magic
*refer to a previous project which uses django + google docs collaboration in some way to create a solution which is quick to implement:
*https://github.com/sukey/sukey-website-build/blob/master/build-website.py note this is GPLv3'd code :)

Description:
============
Builds the website from django templates.
Uses the django template system to create static files for the website. This
allows easy inclusion of common content, but removes the need for (e.g.) PHP
includes that don't really do anything dynamic.


Build Requirements:
===================
-Python 2.6 (or above): http://www.python.org/getit/
-Django: http://www.djangoproject.com/download/
-Apache (or another http server): http://www.apache.org/dyn/closer.cgi

Build Instructions:
===================
You can build the website for all languages, by doing:
$ python build-website.py

Development
===========
Without push access to repository:
*fork from https://github.com/HurricaneHackers/hurricanehackers.com/
*submit a pull request
*try not to edit code on the server directly, it is better to git clone https://github.com/HurricaneHackers/hurricanehackers.com/ to a local directory and then push back up to github before doing a git pull from github --> server (iniated by git pull command on the server).

With push access to repository:
PM @samthetechie on irc or DM/@ on twitter.

Deployment
==========
1st time:
$ ssh username@yourserver.com
$ cd /var/www
$ sudo su (needed for writing to the apache directory depending on your configuration)
$ git clone https://github.com/HurricaneHackers/hurricanehackers.com/
$ python build-website.py

updating:
$ ssh username@yourserver.com
$ cd /var/www
$ sudo su (needed for writing to the apache directory depending on your configuration)
$ git pull https://github.com/HurricaneHackers/hurricanehackers.com/
$ python build-website.py

.djt Template Code Examples
===========================
for loop demo
-------------
strings:
{# note: not iteritems(); django does this automatically #}

{% for k, v in strings.iteritems %}
{{k}} = {{v}}
{% endfor %}

accessing "deep" variables directly
-----------------------------------
{{strings.key1}}
{% endblock %}

Known Bugs:
-----------------------------------
jQuery bug stops the FAQ box from expanding
Horrible inline style in certain divs. Any css tweaks welcome :)

