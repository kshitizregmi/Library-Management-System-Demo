from flask import Flask,render_template,request

app = Flask(__name__, template_folder="templates")

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('naav.htm')



@app.route('/loginandsign.htm', methods=['GET', 'POST'])
def login():
    return render_template('loginandsign.htm')    



@app.route('/home.htm', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        uname = request.form['username']
        password = request.form['password']
        print(uname)
        if uname=='kr' and password=='kr':
            return render_template('home.htm',name=uname)
        else:
            return render_template('loginandsign.htm')   
    # else:
    #     return render_template('home.htm')


# def parse_data():
#     import pandas as pd
#     df = pd.read_csv('C:\Users\User\Downloads\Programs\books.csv')
#     print(df.head())

if __name__ == '__main__':
    app.run(debug=True)