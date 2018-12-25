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
    ecg = fields.Html(string="ECG")
    biologie = fields.One2many('cardiologieb.biologie_note', 'compte_rendu', string="Biologie")


class Biologie(models.Model):
    _name = "cardiologieb.biologie"
    _rec_name = 'nom'

    nom = fields.Char(string="Nom")


class BiologieNote(models.Model):
    _name = "cardiologieb.biologie_note"

    biologie = fields.Many2one('cardiologieb.biologie')
    note = fields.Integer(0)
    compte_rendu = fields.Many2one('cardiologieb.compterendu')


class Prescription(models.Model):
    _name = "cardiologieb.prescription"
    _rec_name = 'nom'

    nom = fields.Char()
    code_cis = fields.Char()
    forme_pharmaceutique = fields.Char()
    voies_dadministration = fields.Char()
    titulaires = fields.Char()


