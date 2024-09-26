# Copyright 2024 ASAid Group Investment - Fatchul Bari Hikmawan
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, http

class WebsitePage(models.Model):
    _inherit = 'website.page'

    show_modal = fields.Boolean(string="Show Modal", default=False)

    @staticmethod
    def _get_current_page_id():
        # Get the current URL path
        path = http.request.httprequest.path
        # Search for the website.page record with the matching URL
        page = http.request.env['website.page'].sudo().search([('url', '=', path)], limit=1)
        return page.id if page else None