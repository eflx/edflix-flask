end = 0

from flask import render_template, url_for, redirect
from flask import request, flash
from flask import Markup

from flask_classful import route

from flask_login import login_required
from flask_login import current_user

from .view import View

from app.models import Collection

from app.forms.collections import NewCollectionForm
from app.forms.collections import EditCollectionForm

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

    @route("/edit/<id>", methods=["GET", "POST"])
    @login_required
    def edit(self, id):
        try:
            collection = Collection.get(id)
        except Exception as e:
            flash(e.error_message, category="error")

            return redirect(url_for("ItemsView:index"))
        end

        edit_collection_form = EditCollectionForm()

        if request.method == "GET":
            edit_collection_form.title.data = collection.title
        end

        if edit_collection_form.validate_on_submit():
            collection.title = edit_collection_form.title.data

            try:
                collection.save()
            except Exception as e:
                flash(e.error_message, category="error")

                return redirect(url_for("ItemsView:index"))
            end

            return redirect(url_for("ItemsView:index"))
        end

        return render_template("collections/edit.html", form=edit_collection_form)
    end
end
