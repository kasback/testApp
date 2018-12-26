from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo.fields import Date


class Malade(models.Model):

    _name = "cardiologieb.malade"
    _rec_name = 'nom'

    nom = fields.Char()
    prenom = fields.Char()
    telephone = fields.Char()
    numEntree = fields.Char()
    pec = fields.Selection([('ramed', 'RAMED'), ('cnss', 'CNSS')])
    region = fields.Many2one('cardiologieb.region')
    ville = fields.Many2one('cardiologieb.ville')
    date_naissance = fields.Date()
    age = fields.Char(compute='_calcul_age', default="0", store=True)
    diagnostic = fields.Many2many('cardiologieb.diagnostic')
    compte_rendus = fields.One2many('cardiologieb.compterendu', 'malade')

    def _check_lit(self):
        for malade in self:
            if malade.lit is None:
                self.with_lit = 'Sans lit'

    @api.onchange('region')
    def _region_change(self):
        res = {}
        res['domain'] = {'ville': [('region', '=', self.region.id)]}
        return res

    @api.constrains('date_naissance')
    def _date_naissance_constrain(self):
        if self.date_naissance > Date.today():
            raise ValidationError('La date de naissance ne peut pas être suppérieure à la date d\'aujourdhui')

    @api.depends('date_naissance')
    def _calcul_age(self):
        for malade in self.filtered('date_naissance'):
            today = Date.from_string(Date.today())
            pickedDay = Date.from_string(str(malade.date_naissance))
            result = (today.year - pickedDay.year)
            malade.age = str(result) + ' Ans'


class Diagnostic(models.Model):
    _name = "cardiologieb.diagnostic"
    _rec_name = 'nom'

    nom = fields.Char()
    malade = fields.Many2many('cardiologieb.malade')

