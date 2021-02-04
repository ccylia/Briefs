from flask import Flask, render_template, url_for, redirect,request
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from lightfm import LightFM

#chargement des données
def loadData():
    plays = pd.read_csv('/home/cecilia/Documents/brief/brief_reco_lastfm/user_artists.dat', sep='\t')
    artists = pd.read_csv('/home/cecilia/Documents/brief/brief_reco_lastfm/artists.dat', sep='\t', usecols=['id','name'])

    # Merge artist and user pref data (Fusionner les données de préférence de l'artiste et de l'utilisateur)
    ap = pd.merge(artists, plays, how="inner", left_on="id", right_on="artistID")
    ap = ap.rename(columns={"weight": "playCount"})

    # Group artist by name
    artist_rank = ap.groupby(['name']) \
    .agg({'userID' : 'count', 'playCount' : 'sum'}) \
    .rename(columns={"userID" : 'totalUsers', "playCount" : "totalPlays"}) 

    # Merge into ap matrix #join rajoute les colonnes de artist rank sur ap en correlant sur le nom des artiste (name)
    artist_rank['avgPlays'] = artist_rank['totalPlays'] / artist_rank['totalUsers']
    ap = ap.join(artist_rank, on="name", how="inner") \
    .sort_values(['name'], ascending=True)  

    # Preprocessing
    pc = ap.playCount
    play_count_scaled = (pc - pc.min()) / (pc.max() - pc.min())
    ap = ap.assign(playCountScaled=play_count_scaled)

    # Build a user-artist rating matrix 
    ratings_df = ap.pivot(index='userID', columns='artistID', values='playCountScaled')

    #Rempli les valeurs NA / NaN à l'aide de la méthode spécifiée.
    ratings = ratings_df.fillna(0).values

    # Show sparsity  #.nonzero Renvoie les indices des éléments non nuls.

    # Build a sparse matrix
    #X = csr_matrix(ratings)

    n_users, n_items = ratings_df.shape

    artist_name= ap.sort_values("artistID")["name"].unique()


    artist_name=ap['name'].unique()

    return artist_name,ratings, ap
    #return tuple(ap['name'].unique())



#création nouvel utilisateur
def new_user(ap,selectedArtist,ratings):
    new_u = np.zeros(ratings.shape[1])
    artist_name=ap['name'].unique()
    artist_index=0
    for artist in artist_name:
        if artist in selectedArtist:
            new_u[artist_index]=np.mean(ratings[:,artist_index])
        artist_index +=1

        
    return new_u

#reco
def get_recommendations(model,userID,ratings_df,artist_name):
    
    n_users, n_items = ratings_df.shape
    scores = model.predict(userID, np.arange(n_items))
    top_items = artist_name[np.argsort(-scores)]
    return top_items