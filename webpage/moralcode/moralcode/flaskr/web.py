import functools
import csv

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

import jinja2

bp = Blueprint('web', __name__, url_prefix='/web')

search_list = {}
f = open('flaskr/data/sample_data.csv', 'r')
for line in f:
    line = line.split(", ")
    search_list[line[0].lower()] = line[1:]
    
    
    
    
@bp.route('/home', methods=('GET', 'POST'))
def home():
    search_input = None
    results = []
    if request.method == 'POST':
        
        search = request.form['search']
        db = get_db()
        error = None

        if not search:
            error = 'Search bar cannot be empty.'
            
        if error is None:
            search_input = str(search).lower()
            results = []
            for i in search_list:
                if search_input in i:
                    results.append(i)
            
            #try:
            #    db.execute(
            #        "INSERT INTO user (username, password) VALUES (?, ?)",
            #        (username, generate_password_hash(password)),
            #    )
            #    db.commit()
            #except db.IntegrityError:
            #    error = f"User {username} is already registered."
            #else:
                #return redirect(url_for("auth.login"))
        
        flash(error)
        flash(results)

    return render_template('web/web1.html',
                            search_input = search_input,
                            results = results,
                            search_list = search_list)
    
    
    
    
    
    
    
    
    
    
    
    