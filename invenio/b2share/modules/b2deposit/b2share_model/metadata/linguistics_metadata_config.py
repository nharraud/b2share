from invenio.ext.sqlalchemy import db
from linguistics_lang_codes import lang_codes

domain = "Linguistics"
table_name = 'CLARIN'
image = 'domain-clarin.png'
domaindesc = 'Linguistic data.'

fields = [
    {
        'name': 'language_code',
        'display_text': 'Language Code',
        'col_type': db.String(128),
        'required': True,
        'value': 'eng',
        'description': 'This element can be used to add an ISO language code from '
                       'ISO-639-3 to uniquely identify the language a document '
                       'is written in',
        'data_provide': 'select',
        'data_source': [(c, u'{c} [{n}]'.format(c=c, n=n.decode('utf-8'))) for c, n in lang_codes]
    },
    {
        'name': 'region',
        'display_text': 'Country/Region',
        'col_type': db.String(256),
        'description': 'This element allows users to specify a country and/or '
                       'a region to allow depositors to specify where the language '
                       'the document is in is spoken'
    },
    {
        'name': 'ling_resource_type',
        'display_text': 'Resource Type',
        'col_type': db.String(256),
        'required': True,
        'data_provide': 'select',
        'cardinality': 'n',
        'data_source': ['Text', 'Image', 'Video', 'Audio', 'Time-Series', 'Other'],
        'description': 'This element allows the depositor to specify the type '
                       'of the resource (Text, Audio, Video, Time-Series, Photo, etc.)'
    },
    {
        'name': 'project_name',
        'display_text': 'Project Name',
        'col_type': db.String(256),
        'description': 'This element allows the depositor to specify the projects '
                       'which were at the source of the creation of the resource'
    },
    {
        'name': 'quality',
        'display_text': 'Quality',
        'col_type': db.String(256),
        'description': 'This element allows depositors to indicate the quality of '
                       'the resource allowing potential users to immediately see '
                       'whether the resource is of use for them.'
    }
]
