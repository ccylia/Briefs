from flask import Flask, render_template, url_for, redirect,request
import pandas as pd
import numpy as np
from fonction import loadData, new_user, get_recommendations
from lightfm import LightFM
from scipy.sparse import csr_matrix


#init
app = Flask(__name__)


artist_name, ratings ,ap = loadData()




#chemin de la page
@app.route('/')
def index2():

    return render_template('index2.html',artist_name=artist_name)



@app.route("/page2", methods = ['POST'])
def page2():
    selected_Artist = request.form.get('selectedArtist')
    print(selected_Artist)
        # Build a user-artist rating matrix 
    ratings_df = ap.pivot(index='userID', columns='artistID', values='playCountScaled')

    #Rempli les valeurs NA / NaN à l'aide de la méthode spécifiée.
    ratings = ratings_df.fillna(0).values
    new_u = new_user(ap, selected_Artist, ratings)
    ratings = np.vstack((ratings, new_u))
    X = csr_matrix(ratings)
    model = LightFM(loss='warp',learning_schedule= 'adadelta', learning_rate= 0.08)
    model.fit(X, epochs=10, num_threads=2)
    userID=ratings.shape[0]-1
    reco= get_recommendations(model,userID,ratings_df,artist_name)
    reco=reco[:20]


    return render_template("page_suivante.html", liste_Artistes = selected_Artist,reco=reco)


 
