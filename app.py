from flask import Flask, render_template, request, redirect, url_for
import db_tools_project3


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
                           artists=db_tools_project3.get_artists())


@app.route('/artist/<int:pk>')
def artist_detail(pk):
    artist, albums = db_tools_project3.get_artist(pk=pk)
    return render_template('artist_detail.html',
                           artist=artist, albums=albums)


@app.route('/genre/<int:pk>')
def genre_detail(pk):
    genre, artists = db_tools_project3.get_genre(pk=pk)
    return render_template('genre_detail.html', genre=genre, artists=artists)


@app.route('/add/album', methods=['POST'])
def add_album():
    artist_id = request.form.get('artist_id')
    name = request.form.get('name')
    year = request.form.get('year')
    charts = request.form.get('charts')
    print(artist_id, name, year, charts)
    db_tools_project3.insert_album(name=name, artist_id=artist_id,
                                   year=year, charts=charts)
    return redirect(url_for('artist_detail', pk=artist_id))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
    
