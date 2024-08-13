from odoo import models, fields, api, _
from datetime import date
import logging
from odoo.exceptions import ValidationError, UserError
from crawl4ai import WebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy

_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_crm_business_proposal(self):
        try:
            crawler = WebCrawler()
            crawler.warmup()
        except Exception as e:
            self.message_post(
                body=f'Business Proposal: Unexpected error {e}  (warmup)',
            )
            _logger.warning(f'Business Proposal: Unexpected error {e} (warmup)')  

        for crm in self:
            _logger.warning(f'crm_business_proposal {crm.name=}')
            _logger.warning(f"""
                                Instruktioner: {crm.campaign_id.bp_instruction}
                                One extracted model JSON format should look like this: {crm.campaign_id.bp_result}
                                Skriv texterna på svenska
                            """)
            if not crm.website:
                raise UserError("No website assigned to this crm lead")

            try:
                result = crawler.run(
                    url=crm.website,
                    word_count_threshold=1,
                    extraction_strategy=LLMExtractionStrategy(
                        provider=self.env['ir.config_parameter'].sudo().get_param('massmail_business_proposal.bp_provider'),
                        api_token=self.env['ir.config_parameter'].sudo().get_param(
                            'massmail_business_proposal.bp_api_token'),
                        instruction=f"""
                                    Instruktioner: {crm.campaign_id.bp_instruction}
                                    One extracted model JSON format should look like this: {crm.campaign_id.bp_result}
                                    Skriv texterna på svenska
                                """
                    ),
                    bypass_cache=True,
                ).dict()
                _logger.warning(f" {result=}")

                _logger.warning('\n'.join([f"<p><b>{key}</b> {val}</p>" for key, val in result.items()]))

                crm.message_post(
                    body='\n'.join([f"<p><b>{key}</b> {val}</p>" for key, val in result.items()]),
                )
            except Exception as e:
                crm.message_post(
                    body=f'Business Proposal: Unexpected error {e}',
                )
                _logger.warning(f'Business Proposal: Unexpected error {e}')  
