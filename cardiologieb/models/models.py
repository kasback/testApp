# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cardiologieb(models.Model):
    _name = 'cardiologieb.cardiologieb'


class Resident(models.Model):
    _name = 'cardiologieb.resident'
    _rec_name = 'nom'

    nom = fields.Char()
    prenom = fields.Char()
    secteur = fields.Many2one('cardiologieb.secteur')
    chambre = fields.Many2one('cardiologieb.chambre')
    promotion = fields.Many2one('cardiologieb.promotion')
    email = fields.Char(string="Adresse email")
    sexe = fields.Selection([('H', 'Homme'), ('F', 'Femme')])
    telephone = fields.Char(string="Téléphone")
    gardes = fields.One2many('cardiologieb.garde', 'resident')
    note = fields.One2many('cardiologieb.note', 'resident')

    @api.onchange('secteur')
    def _secteur_onchange(self):
          res = {}
          res['domain'] = {'chambre': [('secteur_id', '=', self.secteur.id)]}
          return res

    @api.onchange('region')
    def _region_onchange(self):
        res = {}
        res['domain'] = {'ville': [('region', '=', self.region.id)]}
        return res


class Garde(models.Model):
    _name = 'cardiologieb.garde'

    date_garde = fields.Date()
    resident = fields.Many2one('cardiologieb.resident')


class Stat(models.Model):
    _name = 'cardiologieb.stat'
    _rec_name = 'nom'

    nom = fields.Char()


class Note(models.Model):
    _name = 'cardiologieb.note'

    stat = fields.Many2one('cardiologieb.stat')
    resident = fields.Many2one('cardiologieb.resident')
    note_resident = fields.Integer(0)


class Promotion(models.Model):
    _name = 'cardiologieb.promotion'
    _rec_name = 'nom'

    nom = fields.Char()



