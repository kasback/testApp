from odoo import models, fields

class Region(models.Model):
    _name = "cardiologieb.region"
    _rec_name = "nom"

    nom = fields.Char()

class Ville(models.Model):
    _name = "cardiologieb.ville"
    _rec_name = "nom"

    nom = fields.Char()
    region = fields.Many2one('cardiologieb.region')