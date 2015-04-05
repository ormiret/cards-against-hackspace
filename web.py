from flask import Flask, render_template, jsonify, request, json, redirect
app = Flask(__name__)

import cah

@app.route("/cah")
def cah_filled():
    return render_template("message.html", message=cah.fill_statement())

@app.route("/cah.json/<topic>")
def cah_topic(topic):
    topic = topic.lower()
    for i in xrange(1000):
        statement = cah.fill_statement()  
        if topic in statement.lower():
            break
    else:
        statement = "Nothing wise found about %s. Have some random wisdom instead: %s"%(
            topic, cah.fill_statement())
    return jsonify({"wisdom": statement})

@app.route("/cah.json")
def cah_json():
    return jsonify({"wisdom":cah.fill_statement()})
