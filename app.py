from flask import Flask, render_template ,redirect,request, url_for
from collections import Counter
from product_data import product_responses

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_skin_type', methods= ['POST'])
def get_skin_type():
   responses = list(request.form.values())
   count = Counter(responses)

   if count:
        skin_type = count.most_common(1)[0][0]  # e.g., 'Oily', 'Dry', etc.
        return redirect(url_for('routine', skin_type=skin_type))
   else:
        return redirect(url_for('home'))
    

@app.route('/routine/<skin_type>')
def routine(skin_type):
    return render_template('routine.html', skin_type=skin_type)

@app.route('/products-ai', methods=['GET', 'POST'])
def product_ai():
    question = None
    response = None

    if request.method == 'POST':
        question = request.form['question'].lower()

        # Default response
        response = " Sorry, no recommendation available for that query. Try asking about toner, sunscreen, or moisturizer for a specific skin type."

        # Search for matching keywords
        for item in product_responses:
            if all(word in question for word in item["keywords"]):
                response = item["recommendation"]
                break

    return render_template('product_ai.html', question=question, response=response)













if __name__ == '__main__':
    app.run(debug=True)



    
