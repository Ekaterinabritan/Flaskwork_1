from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/clothes/')
def clothes():  # put application's code here
    return render_template('clothes.html')

@app.route('/shoes/')
def shoes():  # put application's code here
    return render_template('shoes.html')

@app.route('/jacket/')
def jacket():  # put application's code here
    return render_template('jacket.html')




@app.route('/shop/')
def shop():
    _shop = [
        {
            "clothes": "ZARA",
            "shoes": "BATI",
            "jacket": "ZARINA",

        },
        {
            "clothes": "OSTIN",
            "shoes": "CORSO COMO",
            "jacket": "TOP TOP",
        },
    ]
    context = {'shop': _shop}
    return render_template('shop.html', **context)



if __name__ == '__main__':
    app.run()