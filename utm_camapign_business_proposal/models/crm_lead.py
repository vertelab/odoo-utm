from odoo import models, fields, api, _
from datetime import date
import logging
from odoo.exceptions import ValidationError
from crawl4ai import WebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy

_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    def action_crm_business_proposal(self):
        crawler = WebCrawler()
        crawler.warmup()

        for crm in self:
            _logger.warning(f'crm_business_proposal {crm.name=}')
            _logger.warning(f"""
                                Instruktioner: {crm.campaign_id.bp_instruction}
                                One extracted model JSON format should look like this: {crm.campaign_id.bp_result}
                                Skriv texterna på svenska
                            """)
            result = crawler.run(
                        url=crm.website,
                        word_count_threshold=1,
                        extraction_strategy= LLMExtractionStrategy(
                            provider=self.env['ir.config_parameter'].sudo().get_param('massmail_business_proposal.bp_provider'), 
                            api_token = self.env['ir.config_parameter'].sudo().get_param('massmail_business_proposal.bp_api_token'),
                            instruction=f"""
                                Instruktioner: {crm.campaign_id.bp_instruction}
                                One extracted model JSON format should look like this: {crm.campaign_id.bp_result}
                                Skriv texterna på svenska
                            """),            
                    bypass_cache=True,
            )
            _logger.warning(f" {result=}")
            _logger.warning('\n'.join([f"<p><b>{key}</b> {result['key']}</p>" for key in result.keys()]))

            crm.message_post(body='\n'.join([f"<p><b>{key}</b> {result['key']}</p>" 
                                    for key in result.keys()]),
                            )
                             
                                                        
