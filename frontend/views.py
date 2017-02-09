from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from frontend.models import Issue

issues = Blueprint('issues', __name__, template_folder='templates')


class ListView(MethodView):
    def get(self):
        issues = Issue.objects.all()
        return render_template('issues/list.html', issues=issues)


class DetailView(MethodView):
    def get(self, slug):
        issue = Issue.objects.get_or_404(slug=slug)
        return render_template('issues/detail.html', issue=issue)


# Register the urls
issues.add_url_rule('/', view_func=ListView.as_view('list'))
issues.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
