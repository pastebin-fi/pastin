from flask import abort, flash, Flask, redirect, render_template, Response, \
        request, send_from_directory
import random
import string
from sqlalchemy import desc, or_
import werkzeug.exceptions as ex

from main import app, db, document_manager, hcaptcha, md, migrate
from paste import Paste, PasteForm

@app.context_processor
def document_injector():
    return dict(documents=document_manager.documents.values())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    latest_pastes = Paste.query.order_by(desc(Paste.timestamp)).limit(5).all()
    for paste in latest_pastes:
        paste.defaults()
    # TODO: Show latest pastes on all pages
    return render_template("index.html", paste_form=PasteForm(), \
        latest_pastes=latest_pastes)

@app.route('/new/', methods=["POST"])
def new_paste():
    form = PasteForm()
    if not hcaptcha.verify():
        # TODO: Localize error messages
        flash('hCaptchan verifiointi epäonnistui.', 'negative')
        # TODO: Complain about other errors even when there is an hCaptcha error
        return redirect('/'), 400
    if form.validate():
        letters = string.ascii_letters + string.digits
        paste_id = ''.join(random.choice(letters) for i in range(12))
        paste = Paste(id=paste_id, contents=form.contents.data, \
            name=form.name.data, private=form.private.data)
        db.session.add(paste)
        db.session.commit()
        return redirect('/p/' + paste_id + '/')
    for field, errors in form.errors.items():
        if field == 'csrf_token':
            errors[0] = 'Tapahtui CSRF-virhe. Yritä uudelleen.'
        for error in errors:
            flash(error, 'negative')
    return redirect('/')

# TODO: Merge get_paste and get_raw_paste into a single function

@app.route('/p/<paste_id>/')
def get_paste(paste_id):
    paste = Paste.query.filter_by(id=paste_id).first()
    if paste:
        paste.defaults()
        return render_template("paste.html", paste=paste, path=request.path)
    # TODO: Use the actual 404 handler with a custom 404 message
    return render_template("404-paste.html"), 404

@app.route('/r/<paste_id>/')
def get_raw_paste(paste_id):
    paste = Paste.query.filter_by(id=paste_id).first()
    if paste:
        paste.defaults()
        return Response(paste.contents, mimetype="text/plain")
    return Response("Ei löytynyt - 404", mimetype="text/plain"), 404

@app.route('/search/')
def search_paste():
    query = request.args.get("q")
    search = "%{}%".format(query)
    pastes = Paste.query.filter(or_(Paste.name.like(search), Paste.contents \
        .like(search))).filter(Paste.private == False).limit(10).all()
    for paste in pastes:
        paste.defaults()
    return render_template("search.html", pastes=pastes, query=query)


if __name__ == "__main__":
    app.run(host=app.config["ADDR"], port=app.config["PORT"], \
            extra_files=["app.py", "paste.py", "document.py", "main.py", \
            "config.py"])
