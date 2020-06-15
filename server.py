from flask import Flask,  render_template, url_for, request, redirect
import csv
app = Flask(__name__)
#app.run(debug=True)
print(__name__)

# @app.route('/')
# def hello_world():
#    return 'Hello, Stylianos!'


@app.route('/')
def my_home():
	# print(url_for('static', filename='mohico.ico'))
	return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
   	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
 		email = data["email"]
 		subject = data["subject"]
 		message = data["message"]
 		file = database.write(f'\n{email}, {subject}, {message}')



def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
 		email = data["email"]
 		subject = data["subject"]
 		message = data["message"]
 		csv_writer = csv.writer(database2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
 		csv_writer.writerow([email,subject,message])
 		


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	# return 'form submitted successfully'
	if request.method == 'POST':
		try:
            data = request.form.to_dict()
            write_to_csv(data)
            write_to_file(data)		
            # print(data)
            # return 'form_submitted'
            return redirect('/thankyou.html')
	except:
		return 'Did not save to database'
	else:
		return "Something went wrong, please try again"



    	# return render_template('login.html', error=error)

    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)




# @app.route('/<username>/<int:post_id>')
# def hello_world_username(username=None, post_id=None):
	
# 	return render_template('index.html', name=username, post_id=post_id)

# @app.route('/components.html')
# def components():
#    return render_template('components.html')


# @app.route('/favicon.ico')
# def favicon():
#    return render_template('mohico.ico')

 # @app.route('/index.html')
 # def index():
 #    return render_template('index.html')
# @app.route('/index.html')
# def my_home2():
# 	# print(url_for('static', filename='mohico.ico'))

# 	return render_template('index.html')

# @app.route('/work.html')
# def work():
#    return render_template('work.html')

# @app.route('/contact.html')
# def contact():
#    return render_template('contact.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/blog/2020/dogs')
# def blog2020dogs():
#    return 'These are my thoughts on dogs'

# @app.route('/blog')
# def blog2():
#    return 'These are my thoughts on blogs2'


#
