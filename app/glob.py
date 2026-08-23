# -*- coding: utf-8 -*-
# @Author: Jeremiah.Marks
# @Date:   2026-08-18 13:18:10
# @Last Modified by:   Jeremiah.Marks
# @Last Modified time: 2026-08-23 10:35:51
#
#
# Look, I know I can just download the project or 
# copy/paste the files to a file and claim that I 
# did it, but I am not.  I am copy/pasting, making
# sure that I understand the code, and changing 
# names when the old ones don't make sense.  This
# is not a blog, but I don't know what it is, so 
# it is GLOB.

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db

bp = Blueprint('glob', __name__)

@bp.route('/')
@login_required
def index():
    db = get_db()
    posts = db.execute(
        'SELECT id, source, body, created'
        ' FROM post'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('glob/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        source = request.form['source'].strip() or 'web'
        body = request.form['body'].strip()
        error = None

        if not body:
            error = "Body Content required"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (source, body)'
                ' VALUES (?, ?)',
                (source, body)
            )
            db.commit()
            return redirect(url_for('glob.index'))

    return render_template('glob/create.html')