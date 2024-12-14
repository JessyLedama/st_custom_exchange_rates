{
    'name': 'Exchange Rate Management. Manage Exchange Rates in Sales, Customer Invoice, Vendor Bills, Journal Entries',
    'version': '17.0.1.0.0',
    'summary': 'Manage exchange rates from Sales, Invoices, Bills and journal entries. The resulting journal entries use this custom exchange rate.',
    'description': 'Manage exchange rates from Sales, Invoices, Bills and Journal Entries. The resulting journal entries use this custom exchange rate for debits and credits.',
    'author': 'SIMI Technologies',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'images': ['static/description/images/invil.png'],
}
