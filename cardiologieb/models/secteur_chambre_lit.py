from odoo import models, fields
from odoo.fields import Date


class Secteur(models.Model):
    _name = 'cardiologieb.secteur'
    _rec_name = 'nom'

    nom = fields.Char()
    chambres = fields.One2many('cardiologieb.chambre', 'secteur_id')
    dms = fields.Float(string="Durée moyenne de séjour", compute='_calcul_dms', store=False)
    tmo = fields.Float(string="Taux Moyen d'occupation", compute='_calcul_tmo', store=False)

    def _calcul_tmo(self):
        for secteur in self:
            chambreTmo = 0
            for chambre in secteur.chambres:
                occupes = 0
                for lit in chambre.lits:
                    if lit.occupe:
                        occupes += 1
                chambreTmo += (occupes / len(chambre.lits)) * 100
            secteur.tmo = chambreTmo / len(secteur.chambres)

    def _calcul_dms(self):
        for secteur in self:
            chambreDms = 0
            for chambre in secteur.chambres:
                hospitalisations = self.env['cardiologieb.hospitalisation'].search([['chambre', '=', chambre.id]])
                totalDs = 0
                for hospitalisation in hospitalisations:
                    if hospitalisation.lit.id is not False:
                        today = Date.from_string(Date.today())
                        date_entree = Date.from_string(str(hospitalisation.date_entree))
                        result = today - date_entree
                        totalDs += result.days
                chambreDms += totalDs / len(chambre.lits)
                secteur.dms = chambreDms / len(secteur.chambres)



class Chambre(models.Model):
    _name = 'cardiologieb.chambre'
    _rec_name = 'nom'

    nom = fields.Char()
    secteur_id = fields.Many2one('cardiologieb.secteur')
    responsable_id = fields.Many2many('cardiologieb.resident')
    lits = fields.One2many('cardiologieb.lit', 'chambre')
    dms = fields.Float(string="Durée moyenne de séjour", compute='_calcul_dms', store=False)
    tmo = fields.Float(string="Taux Moyen d'occupation", compute='_calcul_tmo', store=False)

    def _calcul_tmo(self):
        for chambre in self:
            occupes = 0
            for lit in chambre.lits:
                if lit.occupe:
                    occupes += 1
            chambre.tmo = (occupes / len(chambre.lits)) * 100

    def _calcul_dms(self):
        for chambre in self:
            hospitalisations = self.env['cardiologieb.hospitalisation'].search([['chambre', '=', chambre.id]])
            totalDs = 0
            for hospitalisation in hospitalisations:
                if hospitalisation.lit.id is not False:
                    today = Date.from_string(Date.today())
                    date_entree = Date.from_string(str(hospitalisation.date_entree))
                    result = today - date_entree
                    totalDs += result.days
                    # print('Chambre ' + chambre.nom + ' Lit ' +
                    #     hospitalisation.lit.nom + ' a une ds de : ' + str(result.days) + ' Jours')
            chambre.dms = totalDs / len(chambre.lits)


class Lit(models.Model):
    _name = 'cardiologieb.lit'
    _rec_name = 'nom'

    nom = fields.Char()
    chambre = fields.Many2one('cardiologieb.chambre')
    occupe = fields.Boolean(string="Occupe")
