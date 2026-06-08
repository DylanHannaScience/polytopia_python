# Windows HP templates route: C:\Users\HP\PycharmProjects\polytopia_python\consoleApp\templates
# Windows truncated templates route: C:\PycharmProjects\polytopia_python\consoleApp\templates
# relative templates route: polytopia_python\consoleApp\templates
from flask import Flask, render_template

# Create a Flask consoleApp
consoleApp = Flask(__name__)

# add Index page, Privacy, Dashboard, About, Settings, HallOfFame and ThroneRoom routes! I have the content for them, you just make the routes and the navigation!

# Route for the homepage
@consoleApp.route("/")
def home():
    return (
        """
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
{% extends "base.html" %}

{% block content %}
<h1>The Battle of Polytopia</h1><p>The server is running at 127.0.0.1:5000</p>"
<p>This is the Index page. Explore other sections using the navigation above.</p>
{% endblock %}
@{
	ViewData["Title"] = "Home Page";
}
<div class="images">
    <img src="static/images/polyhead_ancient.jpg" alt="polyhead" title="polyhead">
    <img src="static/images/polytopia-background.jpg" alt="polytopia-background.jpg" title="polytopia-background.jpg">
    <img src="static/images/polytopia-main-menu.webp" alt="polytopia-main-menu.webp" title="polytopia-main-menu.webp">
    <img src="static/images/soundfx-ico.png" alt="soundfx-ico.png" title="soundfx-ico.png">

    <img>
    <img>
    <img>
</div>
<div class="text-center">
	<h1 class="display-4">The Battle of Polytopia</h1>
	<form action="/game" method="post">
		<label for="my-games" class="toggle">
			<input type="submit" name="my-games" value="My games" />
			<span class="toggle-btn">

			</span>

		</label>
	</form>

</div>
<style>
	.toggle .toggle-btn {
		display: inline-block;
		width: 60px;
		text-align: center;
		padding: 5px 0;
		font-size: 14px;
		font-weight: bold;
		color: white;
		background-color: lightblue;
		border-radius: 5px;
		user-select: none;
		transition: all 0.3s ease;
	}

	.toggle .toggle-btn:hover {
		background-color: white;
		color: black;
		border: 1px solid black;
	}
</style>
</body>
</html>
    """
            )

@consoleApp.route("/game")
def game():
    return ""
# Route for the Privacy page
# TODO Fix error Template file 'polytopia_python' not found
@consoleApp.route("/privacy")
def privacy():
    return
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% extends "base.html" %}

{% block content %}
<h1>Privacy Policy</h1>
<p>This is the Privacy page content.</p>
{% endblock %}

</body>
</html>
"""

# Route for the Dashboard page
# TODO Fix error Template file 'dashboard. html' not found
@consoleApp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Route for the About page
@consoleApp.route("/about")
def about():
    return render_template("about.html")

# Route for the Settings page
@consoleApp.route("/settings")
def settings():
    return render_template("settings.html")

# Route for the Hall of Fame page
@consoleApp.route("/hall-of-fame")
def hall_of_fame():
    return render_template("hall_of_fame.html")

# Route for the Throne Room page
@consoleApp.route("/throne-room")
def throne_room():
    return render_template("throne_room.html")

if __name__ == "__main__":
    consoleApp.run(debug=True, host="127.0.0.1", port=5000)
