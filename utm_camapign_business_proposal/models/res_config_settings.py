from odoo import models, fields, api, _
from datetime import date, datetime
import logging
from GoogleNews import GoogleNews
import base64
import requests


from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
        
    bp_provider = fields.Char(string='Provider', default='openai/gpt-40', config_parameter='massmail_business_proposal.bp_provider')
    bp_api_token = fields.Char(string='API-token', default='1d', config_parameter='massmail_business_proposal.bp_api_token')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()

