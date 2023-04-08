# insecam_scraper
# What is it ?
http://insecam.org Is one of biggest online cameras directorie

# What this python script is use for ?
This python script is used for downloading all urls from insecam with just the country code...

# At your turn !
To use it.
Step 1: you need to install some python modules.
  
  BeautifulSoup
  requests
  yarl
  geoip2
  csv

Step 2: Download "GeoLite2-City.mmdb" file from https://www.maxmind.com (you need to create an account at : https://www.maxmind.com/en/geolite2/signup) and place it inside the same directorie were "pays.py" is.

Step 3: Open "pays.py" with a text editor, and replace the "pays_code" variable to the country of your choice (by default is FR).

Step 4: Run it (by typing "python3 pays.py" or "py pays.py") and when the execution is finished, open "urls_(and the country code).csv" and voilà !
