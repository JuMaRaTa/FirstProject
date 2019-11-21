import flask
import random
import model

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/fakebook")
def fakebook():
    return flask.render_template("exercise_00100_my_fakebook.html")

@app.route("/secret-number-game")
def secret_number_game():
    return flask.render_template("secret_number_game.html", secret_number=random.randint(0,10))

@app.route("/blog")
def blog():

    receipe_1 = model.Receipe("Apfelstrudel","Cut Apple Bake Sweet", "Sweet")
    receipe_2 = model.Receipe("Hamburger", "Fry Meat And Eat", "Salty")
    receipe_3 = model.Receipe("Suppe", "Cut carotte Add Water", "Mild")


    return flask.render_template("Blog.html", receipes=[receipe_1, receipe_2, receipe_3])

if __name__=='__main__':
    app.run()

