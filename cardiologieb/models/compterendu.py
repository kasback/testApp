from odoo import fields,models,api


class CompteRendu(models.Model):
    _name = "cardiologieb.compterendu"
    _rec_name = 'titre'

    titre = fields.Char()
    fdr_c_vx = fields.Char(string="Facteurs de risques cardio-vasculaires")
    antecedents = fields.Char(string="Antécédents")
    histoire = fields.Html(string="Histoire")
    examin_general = fields.Html(string="Examin Clinique")
    examin_cv = fields.Html(string="Examin Cardiovasculaire")
    examin_pp = fields.Html(string="Examin Pleuro-pulmonaire")
    examin_abdo = fields.Html(string="Examin abdominal")
    examin_loge = fields.Html(string="Examin de la loge thyroidienne")
    conclusion = fields.Html(string="Conclusion")
    ecg = fields.Html(string="ECG")
    biologie = fields.One2many('cardiologieb.biologie_note', 'compte_rendu', string="Biologie")
    malade = fields.Many2one('cardiologieb.malade')
    create_uid = fields.Many2one('res.users')
    create_date = fields.Datetime('Date')
    prescriptions = fields.Many2many('cardiologieb.prescription')
    attachement = fields.Many2many('ir.attachment', string="Pièce jointe")
    etat = fields.Selection([
        ('draft', 'Brouillon'),
        ('validation', 'Validation'),
        ('valide', 'Validé'),
    ], default='draft')

    @api.one
    def draft_progressbar(self):
        self.write({
            'etat': 'draft',
        })

    # This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def validation_progressbar(self):
        self.write({
            'etat': 'validation'
        })

    # This function is triggered when the user clicks on the button 'In progress'
    @api.one
    def valide_progressbar(self):
        self.write({
            'etat': 'valide'
        })


class Biologie(models.Model):
    _name = "cardiologieb.biologie"
    _rec_name = 'nom'

    nom = fields.Char(string="Nom")


class BiologieNote(models.Model):
    _name = "cardiologieb.biologie_note"

    biologie = fields.Many2one('cardiologieb.biologie')
    valeur = fields.Integer(0)
    compte_rendu = fields.Many2one('cardiologieb.compterendu')


class Prescription(models.Model):
    _name = "cardiologieb.prescription"
    _rec_name = 'nom'

    nom = fields.Char()
    code_cis = fields.Char()
    forme_pharmaceutique = fields.Char()
    voies_dadministration = fields.Char()
    titulaires = fields.Char()
    compte_rendu = fields.Many2many('cardiologieb.compterendu')


