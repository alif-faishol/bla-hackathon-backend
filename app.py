import os
from flask import Flask, request, jsonify, session
from flask_restless import APIManager
from database import session
from init_db import initDB
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
CORS(app,
     origins=os.getenv('FRONTEND_URI'),
     supports_credentials=True)

manager = APIManager(app, session=session)
from models import User, Usaha, Ulasan, ProposalModal, Order, Product
manager.create_api(User,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   results_per_page=20)
manager.create_api(Usaha,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   results_per_page=20)
manager.create_api(Ulasan,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   results_per_page=20)
manager.create_api(ProposalModal,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   results_per_page=20)
manager.create_api(Order,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   results_per_page=20)
manager.create_api(Product,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   results_per_page=20)
manager.create_api(ProposalModal,
                   methods=['GET', 'POST', 'PUT', 'DELETE'],
                   results_per_page=20)

@app.route('/api/login', methods=['POST'])
def handle():
    from database import session
    from models import User
    from werkzeug.security import check_password_hash

    email = request.json['email']
    password = request.json['password']
    user = session.query(User).filter(User.email == email).scalar()
    if user == None:
        return jsonify({ 'message': 'User not found.' })
    if check_password_hash(user.password, password):
        from flask import session
        session['id'] = user.id
        return jsonify({ 'status': 'success', 'user_id': user.id })

    return jsonify({ 'message': 'Wrong password.' })

@app.route('/api/current-user', methods=['GET'])
def currentUser():
    from flask import session, request
    if 'id' in session:
        return jsonify({ 'user_id': session['id'] })
    return jsonify({ 'message': 'Unauthorized.' })

@app.route('/api/ongoing-event/<page>', methods=['GET'])
def ongoingEvent(page):
    import requests
    r = requests.post('http://patrakomala.disbudpar.bandung.go.id:8080/api/v1/public/event/list-event',
                     json={ 'event': 'ongoing', 'page': page },
                     headers={ 'access-key': os.getenv('PATRAKOMALA_TOKEN') })
    return jsonify(r.json())

@app.route('/api/past-event/<page>', methods=['GET'])
def pastEvent(page):
    import requests
    r = requests.post('http://patrakomala.disbudpar.bandung.go.id:8080/api/v1/public/event/list-event',
                     json={ 'event': 'past', 'page': page },
                     headers={ 'access-key': os.getenv('PATRAKOMALA_TOKEN') })
    return jsonify(r.json())

@app.route('/api/upcoming-event/<page>', methods=['GET'])
def upcomingEvent(page):
    import requests
    r = requests.post('http://patrakomala.disbudpar.bandung.go.id:8080/api/v1/public/event/list-event',
                     json={ 'event': 'upcoming', 'page': page },
                     headers={ 'access-key': os.getenv('PATRAKOMALA_TOKEN') })
    return jsonify(r.json())

@app.route('/api/detail-event/<event_id>', methods=['GET'])
def detailEvent(event_id):
    import requests
    r = requests.get('http://patrakomala.disbudpar.bandung.go.id:8080/api/v1/public/event/detail-event?content_id={}'.format(event_id), headers={ 'access-key': os.getenv('PATRAKOMALA_TOKEN') })
    return jsonify(r.json())


initDB()

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
