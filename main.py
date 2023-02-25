#app renamed to main

from flask import Flask, render_template, request
import pickle
import pandas as pd

model = pickle.load(open('iplpipe.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def man():
  return render_template('home.html')


@app.route('/back', methods=['GET'])
def back():
  return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
  BattingTeam = request.form['bat']
  BowlingTeam = request.form['bowl']
  selected_city = request.form['city']
  target = request.form['target']
  score = request.form['score']
  overs = request.form['overs']
  wickets = request.form['wickets']

  runs_left = int(target) - int(score)
  balls_left = 120 - (int(overs) * 6)
  wickets = 10 - int(wickets)
  crr = int(score) / int(overs)
  rrr = (runs_left * 6) / balls_left

  input_df = pd.DataFrame({
    'BattingTeam': [BattingTeam],
    'BowlingTeam': [BowlingTeam],
    'City': [selected_city],
    'runs_left': [runs_left],
    'balls_left': [balls_left],
    'wickets': [wickets],
    'total_run_x': [int(target)],
    'current_run_rate': [crr],
    'required_run_rate': [rrr]
  })

  result = model.predict_proba(input_df)
  loss = round(result[0][0] * 100)
  win = round(result[0][1] * 100)

  return render_template('res.html',
                         datal=loss,
                         dataw=win,
                         databat=BattingTeam,
                         databowl=BowlingTeam)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
