# -*- coding: utf-8 -*-
# from odoo import http


# class DemoCrm(http.Controller):
#     @http.route('/demo_crm/demo_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_crm/demo_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_crm.listing', {
#             'root': '/demo_crm/demo_crm',
#             'objects': http.request.env['demo_crm.demo_crm'].search([]),
#         })

#     @http.route('/demo_crm/demo_crm/objects/<model("demo_crm.demo_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_crm.object', {
#             'object': obj
#         })
