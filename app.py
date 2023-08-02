from flask import Flask, render_template
import pandas as pd


data = pd.read_csv(r'C:\Users\mcedd\Box\Dashboard\flask\dashboard_clinic\sample_data\Contacts+Diagnostics.csv', sep=',', encoding='latin-1')

# Calculate counts of admissions and visits by type (department/service)
admission_count_by_type = data[data['TYPE'] == 'admission']['TYPE'].value_counts().reset_index()
admission_count_by_type.columns = ['TYPE', 'admission_count']

visit_count_by_type = data[data['TYPE'] == 'visit']['TYPE'].value_counts().reset_index()
visit_count_by_type.columns = ['TYPE', 'visit_count']


app = Flask(__name__, template_folder='templates')  # Specify the template folder

@app.route("/")
def render_index():
    return render_template('index.html', admission_counts=admission_count_by_type.to_dict(orient='records'),
                           visit_counts=visit_count_by_type.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
