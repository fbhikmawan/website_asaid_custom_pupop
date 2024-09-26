# -*- coding: utf-8 -*-
# Copyright 2024 ASAid Group Investment - Fatchul Bari Hikmawan
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': "ASAid Custom Popup",

    'summary': "Display custom Popup as modal in desired website pages",

    'description': """
Display custom Popup as modal in various website pages, including the blog post, product item, event and others.
Modal appearance will be toggled by Website Builder options.
    """,

    'author': "ASAid Group Investment",
    'website': "https://www.asaidgroup.com",
    "license": "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '17.0.2.2.0',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/modal_template.xml',
    ],

    # Inclulde assets to website
    'assets': {
        'web.assets_frontend': [
            'website_asaid_custom_popup/static/src/js/websiteAds.js',
            'website_asaid_custom_popup/static/src/scss/websiteAds.scss',
        ],
    },
}

