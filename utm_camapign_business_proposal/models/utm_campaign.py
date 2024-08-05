# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class UtmCampaign(models.Model):
    _name = 'utm.campaign'
    _inherit = ['utm.campaign','mail.thread', 'mail.activity.mixin',]

    bp_instruction = fields.Text(string='Instructions',help="""Give instructions and what your goals are""",)
                                # ~ placeholder="""e.g. Crawl the website and extract relevant information, who should we contact selling Odoo for them. What are their business description. 
                                                # ~ What is the benefits with Odoo in their partical business? How can they sell more, how can they save money and streamline business processes?""")
    bp_result = fields.Text(string='Result',help="Json-record that you want as result",)
                            # ~ placeholder="""e.g. {'Affärsförslag': '', 'Nyttor med Odoo': ''}""")
                            
