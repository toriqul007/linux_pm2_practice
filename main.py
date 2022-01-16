from flask import Flask, template_rendered,request,redirect
from flask.templating import render_template


app=Flask(__name__, static_folder='static', static_url_path="")

title='This is title'
text='This is a text'

kittens=[

    {
        'name':'Tyson',
        'age': 7,
        'color': 'Grey'
    },
        
    {
        'name':'Cocos',
        'age': 12,
        'color': 'Orange'
    },
    {
        'name':'MrBigg',
        'age': 19,
        'color': 'Purple'
    }
]


cool=True

@app.get('/')
def index():
    return render_template('index.html',
     title=title,
     text=text,
     kittens=kittens,
     cool=cool
     )
#@app.route('/add-kitten', methods=['POST'])
@app.post('/add-kitten')
def add_kitten():
    #default is form data an immutable dict
    form=request.form

    kitten={
        'name' : form['name'],
        'age' : form['age'],
        'color' : form['color']
    }

    kittens.append(kitten)

    return redirect('/')

@app.get('/remove/<id>')
def remove_kitten(id):
    for kitten in kittens:
        if kitten['index']==id:
            kittens.remove(kitten)

    return redirect('/')

#only start server when executing this python script
if __name__=='__main__':
    app.run(debug=True)









