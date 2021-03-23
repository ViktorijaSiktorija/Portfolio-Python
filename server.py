from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)  # Flask koristi jinja template jezik, daje dinamicnost
# sa {{}}, kao u html sa url_for bibliotekom (iz flask)
print(__name__)


@app.route('/')  # ('/<username>/<int:post_id>')
def my_home():  # (username=None, post_id=None):
    # zbog render_template stavljamo html u template folder
    # <body>
    # {{name}}
    # {{post_id}}
    return render_template('index.html')  # , name=username, post_id=post_id)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:  # mode append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        print(csv_writer)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # sta posaljemo pretvori u dict
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Nije sacuvano u bazi'
    else:
        return 'Nesto ne valja'
