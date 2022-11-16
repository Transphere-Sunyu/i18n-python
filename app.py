from flask import Flask, render_template, request, session
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = {
    'en': 'English',
    'zh': 'Chinese(Simplified)',
    'ar': 'Arabic'
}
# TODO: Generate a secret your key
app.config['SECRET_KEY'] = 'your secret key'

# TODO: Add path to your locales or translation directory
app.config["BABEL_TRANSLATION_DIRECTORIES"] = '/Path/To/Your/locales'


# Make languages and current_languages variables
# accessible in all the templates
@app.context_processor
def inject_conf_var():
    return dict(languages=app.config['LANGUAGES'],
                current_language=session.get('lang',
                                             request.accept_languages.best_match(app.config['LANGUAGES'].keys())))


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')

    return session.get('lang', request.accept_languages.best_match(app.config['LANGUAGES'].keys()))


@app.route('/')
def index():
    get_locale()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
