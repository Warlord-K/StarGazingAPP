#gaia
from astroquery.gaia import Gaia 
import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

tables = Gaia.load_tables()
gaiadr2_table = Gaia.load_table('gaiadr2.gaia_source')
for column in gaiadr2_table.columns:
    print(column.name)


coord = SkyCoord(ra=280, dec=-60, unit=(u.degree, u.degree), frame='icrs')
radius = u.Quantity(1.0, u.deg)
j = Gaia.cone_search_async(coord, radius)
r = j.get_results()


from astroquery.ipac.ned import Ned
result_table = Ned.query_object("Sirius")


#simbad
from astroquery.simbad import Simbad
from astropy.constants import sigma_sb
Simbad.add_votable_fields('fe_h', 'diameter')
result_table2 = Simbad.query_object('sirius')
print(result_table2)

Simbad.list_votable_fields()
Simbad.get_field_description('diameter')

luminosity = sigma_sb * 
luminosity 