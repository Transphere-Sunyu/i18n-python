# i18n-python


**i18n-python**  is a demo i18n website built with Flask and uses Flask-Babel to support internationalization.
Read our article to understand how internationalization was implemented.

### [Learn more at transphere.com &rarr;](https://www.transphere.com/)

# Requirements
1. Python 3.10.7
# Quick Start
     git clone https://github.com/Transphere-Sunyu/i18n-python.git

# Install Packages

     cd i18n-python && pip3 install -r requirements.txt

# Add path to your locales directory
    
     app.config["BABEL_TRANSLATION_DIRECTORIES"] = '/Path/To/Your/locales/directory'


# Run the web application
    
     flask run

Open the website in your browser at https://127.0.0.1:5000