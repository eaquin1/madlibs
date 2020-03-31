from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import choices

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecret"

debug = DebugToolbarExtension(app)

@app.route('/')
def render_story_choices():
    """Render story choices"""
    return render_template("choices.html", choices = choices.values())

@app.route('/forms')
def render_forms():
    """Render madlib forms for user to choose words"""
    print(request.args)
    story_id = request.args["story_id"]
    story = choices[story_id]

    prompts = story.prompts
    return render_template("stories.html", story_id = story_id, title=story.title, prompts=prompts)

@app.route("/stories")
def render_result():
    """Render the completed Madlib with the user's response"""
    story_id = request.args["story_id"]
    story = choices[story_id]

    text = story.generate(request.args)
    return render_template("results.html", title=story.title, text=text)