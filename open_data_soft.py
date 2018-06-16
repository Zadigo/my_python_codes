import requests
import urllib

BASE_URI = u'https://data.opendatasoft.com/api/records/1.0/search/?{query}'

class BaseOpenDataSoft:
    def __init__(self, dataset, **kwargs):
        params = {
            'dataset': '',
            'sort': 'uo_lib',
        }
        params.update({'dataset':dataset})
        if dataset == '':
            raise TypeError('There was no dataset to work with')
        else:
            if not isinstance(dataset, str):
                raise TypeError('Received %s instead of a string' %
                    dataset.__class__.__name__ 
                )
        if kwargs:
            for key, value in kwargs.items():
                params[key] = value
        request_url = BASE_URI.format(
            query=urllib.parse.urlencode(params)
        )
        try:
            response = requests.get(request_url)
        except ConnectionError as error:
            print('There was an error %s' % error.args)
        else:
            self.json_obj = response.json()['records'][0]['fields']

class OpenDataSoft(BaseOpenDataSoft):
    def _set(self):
        for key, value in self.json_obj.items():
            setattr(OpenDataSoft, key, value)
        return self

# class Data(OpenDataSoft):
#     def _get(self):
#         super()._set()


# class UniversityMixins:
#     def __init__(self, obj):
#         self.localite_acheminement_uai      = obj['localite_acheminement_uai']
#         self.uucr_id                        = obj['uucr_id']
#         self.aca_nom                        = obj['aca_nom']
#         self.identifiant_eter               = obj['identifiant_eter']
#         self.identifiant_isni               = obj['identifiant_isni']
#         self.type_d_etablissement           = obj['type_d_etablissement']
#         self.com_nom                        = obj['com_nom']
#         self.uo_lib                         = obj['uo_lib']
#         self.element_wikidata               = obj['element_wikidata']
#         self.inscrits_2010                  = obj['inscrits_2010']
#         self.inscrits_2011                  = obj['inscrits_2011']
#         self.inscrits_2012                  = obj['inscrits_2012']
#         self.inscrits_2013                  = obj['inscrits_2013']
#         self.inscrits_2014                  = obj['inscrits_2014']
#         self.inscrits_2015                  = obj['inscrits_2015']
#         self.code_postal_uai                = obj['code_postal_uai']
#         self.com_code                       = obj['com_code']
#         self.siren                          = obj['siren']
#         self.siret                          = obj['siret']
#         self.libelle_mission_chef_de_file   = obj['libelle_mission_chef_de_file']
#         self.coordonnees                    = obj['coordonnees']
#         self.wikipedia                      = obj['wikipedia']
#         self.compte_facebook                = obj['compte_facebook']
#         self.dep_nom                        = obj['dep_nom']
#         self.aca_id                         = obj['aca_id']
#         self.statut_juridique_court         = obj['statut_juridique_court']
#         self.statut_juridique_long          = obj['statut_juridique_long']
#         self.sigle                          = obj['sigle']
#         self.reg_nom_old                    = obj['reg_nom_old']
#         self.adresse_uai                    = obj['adresse_uai']
#         self.secteur_d_etablissement        = obj['secteur_d_etablissement']
#         self.url                            = obj['url']
#         self.pays_etranger_acheminement     = obj['pays_etranger_acheminement']
#         self.mooc                           = obj['mooc']