# -*- coding: utf-8 -*-
import datetime
from flask import url_for
from frontend import db


class Issue(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    issue_date = db.DateTimeField(default=datetime.datetime.now, required=True)
    issue_type = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    comment = db.StringField(required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.issue_type

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }
