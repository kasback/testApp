# -*- coding: utf-8 -*-

from odoo import models, fields


class Cardiologieb(models.Model):
    _name = 'cardiologieb.cardiologieb'


class Resident(models.Model):
    _name = 'cardiologieb.resident'
    _rec_name = 'nom'

    nom = fields.Char()
    prenom = fields.Char()
    secteur = fields.Many2one('cardiologieb.secteur')
    chambre = fields.Many2one('cardiologieb.chambre')
    gardes = fields.One2many('cardiologieb.garde','resident')
    note = fields.One2many('cardiologieb.note','resident')
    promotion = fields.Many2one('cardiologieb.promotion')

    def _secteur_onchange(self):
          res = {}
          res['domain'] = {'chambre': [('secteur_id', '=', self.secteur.id)]}
          return res


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



