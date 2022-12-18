from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint

app = Flask(__name__)
app.config["SECRET_KEY"] = "add_random_string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'

db=SQLAlchemy(app)

class login(db.Model):
    loginUser=db.Column(db.String[100],primary_key=True)
    loginPassword= db.Column(db.String[100])


@app.route('/',methods=['POST','GET'])

def index():
    content ={
        "data":"keyword_search",
        "flashit":"hahaha"
    }
    flash("Please enter all..",'error')
    return render_template('index.html',context = content)

#def index():
    #return render_template('index.html')
@app.route('/create')
def create():
    db.create_first()
    return 'All tables created'

if __name__ == "__main__":
    
    app.run(debug=True)

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)