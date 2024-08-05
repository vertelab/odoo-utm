# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2024- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'UTM: Campaign AI Business Proposal', 
    'version': '14.0.0.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'summary': 'Create an individual business proposal for companines in a campaign',
    'category': 'Administration',
    'description': """
Create an individual business proposal using AI
===============================================

With information about the company and the website and special instructions on the
campaign, a business proposal are created for inspiration to the sales team.

example:

instruction: 
            	Crawl the website and extract relevant information, who should we contact selling Odoo for them. What is their business description. 
            What is the benefits with Odoo in their partical business? How can they sell more, how can they save money and streamline business processes?
            

result: 
{'Affärsförslag':'vad skall jag föreslå för lösning',
'Nyttor med Odoo för företaget': 'Vad i Odoo kan företaget använda?',
'Budget': 'Vad är företagets budget för ERP' ,
'Företagets mål': '',
'Kontakt': ''
}

needs crawl4ai  sudo pip3 install "crawl4ai @ git+https://github.com/unclecode/crawl4ai.git"

https://googlechromelabs.github.io/chrome-for-testing/
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver



""",
    #'sequence': '1',
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-utm/utm_campaign_business_proposal',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-utm',
    'depends': ['utm'],
    'data': [
        'views/utm_campaign_views.xml',
        'views/res_config_settings_views.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
