##############################################################################
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'test13e',
    'version': '13.0e.0.0.0',
    'category': 'Tools',
    'summary': "Test for v13 EE",
    'author': "jeo Software",
    'website': 'http://github.com/jobiols/module-repo',
    'license': 'AGPL-3',
    'depends': [
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-test', 'branch': '13.0'},

        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '13.0'},

        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools',
         'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting',
         'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'sale', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'product', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '13.0'},
        {'usr': 'ingadhoc', 'repo': 'account-invoicing', 'branch': '13.0'},

        {'usr': 'oca', 'repo': 'partner-contact', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'web', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'server-tools', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'social', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'server-ux', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'server-brand', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'manufacture', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'manufacture-reporting', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'management-system', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'sale-workflow', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '13.0'},
        {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '13.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '13.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '10.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
    ]
}
