from bottle import Bottle, run, route, request

app = Bottle()

@app.route('/listener')
def my_listener():
    data = request.query.your_data
    #do_something_with_data(data)
    print(data)
    return data

run(app, host='18.228.34.10', port=80)