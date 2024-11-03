# -*- coding: utf-8 -*-

from odoo import models, fields, api

class city(models.Model):
     _name = 'megalopolis.city'
     _description = 'megalopolis.city'

     name = fields.Char(string='Nom', readonly=False, required=True, help='El nom de la city')
     description = fields.Text()
     level = fields.Integer()
     buildings = fields.One2many(string='Buildings',
                                 comodel_name='megalopolis.building',
                                 inverse_name='city') #, ondelete='set null', help='La classe on va')

     resources = fields.Many2many(comodel_name='megalopolis.resources',
                                 relation='city_resources',
                                 column1='city_id',
                                 column2='resource_id')

class building(models.Model):
     _name = 'megalopolis.building'
     _description = 'The buildings'

     name = fields.Char(string='Nom')
     description = fields.Text()
     price = fields.Integer()
     num_people = fields.Integer()
     type = fields.Text()

     city = fields.Many2one(comodel_name='megalopolis.city')

     resources = fields.Many2many(comodel_name='megalopolis.resources',
                             relation='building_resources',
                             column2='building_id',
                             column1='resources_id')

     crops = fields.Many2one(comodel_name='megalopolis.crop', help='Lugar de trabajo')


class crop(models.Model):
     _name = 'megalopolis.crop'
     _description = 'The Crops'

     name = fields.Char()
     description = fields.Text()
     price = fields.Integer()
     buildings = fields.One2many(comodel_name='megalopolis.building',
                                inverse_name='crops',
                                help='Building que trabaja este crop')
     resources = fields.Many2many(comodel_name='megalopolis.resources',
                                  relation='crop_resources',
                                  column1='crop_id',
                                  column2='resources_id',
                                  help='Ressources produced in this crop')

class resources(models.Model):
     _name = 'megalopolis.resources'
     _description = 'megalopolis.resources'

     name = fields.Char()
     description = fields.Text()
     resource = fields.Many2many(comodel_name='megalopolis.crop',
                                relation='crop_resources',
                                column2='crop_id',
                                column1='resources_id',
                                help='Crop produced in this field')
     # nat_resource = fields.Many2one(comodel_name='megalopolis.natural_resources',
     #                                help='Resource obtained')
     nat_resource = fields.One2many(comodel_name='megalopolis.naturalresources',
                                inverse_name='resource',
                                help='Natural resource generated')

class naturalresources(models.Model):
     _name = 'megalopolis.naturalresources'
     _description = 'megalopolis.naturalresources'

     name = fields.Char(string='Name', required=True,help='Natural resource name')
     description = fields.Text()
     resource = fields.Many2one(comodel_name='megalopolis.resources',
                                required=True,
                                help='Natural resource obtain by')
#     value2 = fields.Float(compute="_value_pc", store=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


