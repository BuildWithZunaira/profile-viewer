from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    "James": {"name": "James Smith", "age": 30, "email": "James@example.com"},
    "Michael": {"name": "Michael Johnson", "age": 25, "email": "Michael@example.com"},
    "john": {"name": "john Brown", "age": 35, "email": "John@example.com"},
    "alice": {"name": "Alice Smith", "age": 21, "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "age": 28, "email": "bob@example.com"},
    "charlie": {"name": "Charlie Brown", "age": 40, "email": "charlie@example.com"}
}


@app.route('/user/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        if 'username' in request.form:
            selected_user = request.form['username']
            user_profile = users.get(selected_user)
            return render_template('profile.html', user=user_profile)

        elif 'max_age' in request.form:
            max_age = int(request.form['max_age'])
            matched_users = []
            for user_details in users.values():
                if user_details['age'] <= max_age:
                    matched_users.append(user_details)
                    matched_users.sort(key=lambda x: x['age'])
            return render_template('profile_age.html', users=matched_users, max_age=max_age)

    return render_template('index_combined.html', usernames=users.keys())


@app.route("/main/")
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()



