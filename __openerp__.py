# -*- coding: utf-8 -*-
{
    'name': 'Super Admin',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
    """,
    'author': 'Ruchir Shukla',
    'website': 'www.bizzappdev.com',
    'depends': ["mail"],
    'init_xml': [],
    'update_xml': [
        "base_view.xml",
        "mail_data.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
        "static/src/xml/base.xml",
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
