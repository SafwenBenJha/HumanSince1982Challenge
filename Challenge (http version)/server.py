from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

humans = [{'name' : 'ls -l'}, {'name' : 'ifconfig'}, {'name' : 'Jahjouh'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/since1982', methods=['GET'])
def returnAll():
    return jsonify({'humans' : humans})

@app.route('/since1982/', methods=['GET'])
def returnOne(name):
    hums = [human for human in humans if human['name'] == name]
    return jsonify({'human' : hums[0]})

if __name__ == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode
