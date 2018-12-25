from odoo import models, fields, api


class Secteur(models.Model):
    _name = 'cardiologieb.secteur'
    _rec_name = 'nom'

    nom = fields.Char()
    chambres = fields.One2many('cardiologieb.chambre', 'secteur_id')


class Chambre(models.Model):
    _name = 'cardiologieb.chambre'
    _rec_name = 'nom'

    nom = fields.Char()
    secteur_id = fields.Many2one('cardiologieb.secteur')
    responsable_id = fields.One2many('cardiologieb.resident', 'chambre')
    lits = fields.One2many('cardiologieb.lit', 'chambre')

class Lit(models.Model):
    _name = 'cardiologieb.lit'
    _rec_name = 'nom'

    nom = fields.Char()
    chambre = fields.Many2one('cardiologieb.chambre')
