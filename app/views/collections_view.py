end = 0

from flask import render_template, url_for, redirect
from flask import flash
from flask import Markup

from flask_classful import route

from flask_login import login_required
from flask_login import current_user

from .view import View

from app.models import Collection

from app.forms.collections import NewCollectionForm

class CollectionsView(View):
    @route("/new", methods=["GET", "POST"])
    @login_required
    def new(self):
        new_collection_form = NewCollectionForm()

        if new_collection_form.validate_on_submit():
            try:
                new_collection = Collection.new(new_collection_form.title.data)

                flash(Markup(f"Collection <b>{new_collection.title}</b> was created successfully"))

                return redirect(url_for("ItemsView:index"))
            except Exception as e:
                flash(e.error_message, category="error")

                return redirect(url_for("CollectionsView:new"))
            end
        end

        return render_template("collections/new.html", form=new_collection_form)
    end
end
