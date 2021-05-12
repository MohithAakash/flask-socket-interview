from flask import Flask, render_template, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

no_of_interviewers = 2
score_list = []
avg_dict = { 'type' : 'Average Scores', 'avg1' : 0, 'avg2' : 0, 'avg3' : 0, 'avg4' : 0}


@app.route('/')
def session():
    return render_template('index.html')


@socketio.on('my event')
def handle_my_custom_event(scores, methods=['GET', 'POST']):
    # print('received my event: ' + str(json))
    score_list.append(scores)
    print(score_list)

    if len(score_list) == no_of_interviewers:
        calculate_average(score_list)
        socketio.emit('my response', score_list)


def calculate_average(scores):
    for score in scores:
        for avg_key, score_key in zip(avg_dict.keys(), score.keys()):
            if(type(avg_dict[avg_key]) == int):
                avg_dict[avg_key] += int(score[score_key])

    for avg_key in avg_dict.keys():
        if(type(avg_dict[avg_key]) == int):
            avg_dict[avg_key]/=len(scores)
    
    score_list.append(avg_dict)


if __name__ == '__main__':
    socketio.run(app, debug=True)
