# -*- coding: utf-8 -*-
# from odoo import http


# class Megalopolis(http.Controller):
#     @http.route('/megalopolis/megalopolis', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/megalopolis/megalopolis/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('megalopolis.listing', {
#             'root': '/megalopolis/megalopolis',
#             'objects': http.request.env['megalopolis.megalopolis'].search([]),
#         })

#     @http.route('/megalopolis/megalopolis/objects/<model("megalopolis.megalopolis"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('megalopolis.object', {
#             'object': obj
#         })

