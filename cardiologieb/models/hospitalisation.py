from odoo import fields, models, api
from odoo.fields import Date

class Hospitalisation(models.Model):
    _name = 'cardiologieb.hospitalisation'
    _rec_name = 'malade'

    malade = fields.Many2one('cardiologieb.malade')
    secteur = fields.Many2one('cardiologieb.secteur')
    chambre = fields.Many2one('cardiologieb.chambre')
    ds = fields.Char(compute='_calcul_ds', store=False)
    date_entree = fields.Date()
    date_sortie = fields.Date()
    lit = fields.Many2one('cardiologieb.lit')

    @api.onchange('secteur')
    def _secteur_onchange(self):
        res = {}
        res['domain'] = {'chambre': [('secteur_id', '=', self.secteur.id)]}
        return res

    @api.onchange('chambre')
    def _chambre_onchange(self):
        res = {}
        res['domain'] = {'lit': ['&', ('chambre', '=', self.chambre.id), ('occupe', '=', False)]}
        return res

    # Create method override
    @api.model
    def create(self, values):
        record = super(Hospitalisation, self).create(values)
        self.env['cardiologieb.lit'].browse(record['lit'].id).occupe = True
        self.env['cardiologieb.malade'].browse(record['malade'].id).lit = record['lit'].id
        return record

    # Update method override
    @api.one
    def update(self, values):
        self.env['cardiologieb.lit'].browse(self.lit.id).occupe = False
        record = super(Hospitalisation, self).write(values)
        self.env['cardiologieb.lit'].browse(values['lit']).occupe = True
        return record

    # Delete method override
    @api.one
    def unlink(self):
        self.env['cardiologieb.lit'].browse(self.lit.id).occupe = False
        record = super(Hospitalisation, self).unlink()


    @api.one
    def sortir_malade(self):
        self.env['cardiologieb.lit'].browse(self.lit.id).occupe = False

        # Calcul de la ds lors de la sortie du malade

        today = Date.from_string(Date.today())

        print(today)
        self.write({'date_sortie': str(today)})
        self.write({'lit': None})

    # Mise à jour de la DS au chargement de la page

    def _calcul_ds(self):
        for hospitalisation in self:
            if hospitalisation.lit.id is not False:
                today = Date.from_string(Date.today())
                pickedDay = Date.from_string(str(hospitalisation.date_entree))
                result = today - pickedDay
                hospitalisation.ds = str(result.days) + ' Jours'
            else:
                date_entree = Date.from_string(str(hospitalisation.date_entree))
                date_sortie = Date.from_string(str(hospitalisation.date_sortie))
                result = date_sortie - date_entree
                hospitalisation.ds = 'Sortit avec une DS de ' + str(result.days) + ' Jours'
