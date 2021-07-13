# EXERCISE
# Create four route: user, admin, guest
# Admin page should return a string saying “I am the admin. My name is <the name you passed as
# parameter in user
# else
# Guest page should return a string saying “I am on the guest page. My name is <the name you
# passed as parameter in user
# Pass a parameter name to user. If name is admin got to admin page.
# Add another route called payment to accept a float variable called salary.
# If salary is less than 10500.50 redirect to fnb else redirect to sahomeloan website.

from flask import Flask, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

# user
@app.route('/user/<name>')
def user_page(name):
    # if user name is Mona, then that means mona is an admin
    # if user name is not Mona, they are a guest
    if name == "Mona":
        return redirect("/admin/" + name)
    else:
        return redirect("/guest/" + name)

# admin
@app.route('/admin/<name>')
def admin_page(name):
    return "<body><h1>Admin Page</h1>" \
           "<h2>Welcome, " + name + \
           "</h2></body> "

# payment
@app.route('/payment/<float:sal>')
def payment_page(sal):
    if sal > 10500.50:
        return redirect(url_for("https://www.sahomeloans.com/"))
    else:
        return redirect("https://www.fnb.co.za/")

# guest
@app.route('/guest/<name>')
def guest_page(name):
    return "<body><h1>Guest Page</h1>" \
           "<h2>Welcome, " + name + \
           "</h2></body> "

if __name__ == "__main__":
    app.debug = True
    app.run()