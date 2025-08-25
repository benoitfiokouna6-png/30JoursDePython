from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

# Importons le ballon à partir du flacon d'importation FLASK, RENDER_TEMPLAT, DEM AND, REDIRECT, URL_FOR IMPORT OS # Importation du module du système d'exploit ation

App = Flask ( _name_) @ app.Route ('/') # Ce décorateur crée la route à la maison def home (): Techs = ['html', 'css', 'flask', 'python'] name = '30 jours de Python Programming ' = ' home') @ app.Route ('/ About') def about (): name = '30 Days of Python Programming 'return render_template (' about.html ', name = name, title =' à propos de nous ') @ app.Route (' / pos t ') def post ():) render_template ('post.html', nom = nom, titre = name)
if __name__ == '_main_': # pour le déploiement # Pour le faire fonctionner pour la p roduction et le développement du port = int (os.environ.get ("port", 5000)) app.run (deb ug = true, host = '0.0.0.0', port = port)

