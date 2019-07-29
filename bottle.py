from bottle import Bottle, run, route, request

app = Bottle()

@app.route('/listener')
def my_listener():
    data = request.query.your_data
    #do_something_with_data(data)
    return data

run(app, host="0.0.0.0", port=8080)