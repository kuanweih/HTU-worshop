import numpy as np
import sqlutilpy

RADIUS = 1

labels = "ra,dec,type,psfmag_u,psfmag_g,psfmag_r,psfmag_i,psfmag_z,modelmag_u,modelmag_g,modelmag_r,modelmag_i,modelmag_z"

sql_str = """
          SELECT {}
          FROM sdssdr9.phototag
          WHERE q3c_radial_query(ra, dec, {}, {}, {})
                and mode=1
                and psfmag_u > 0 and modelmag_u > 0
                and psfmag_g > 0 and modelmag_g > 0
                and psfmag_r > 0 and modelmag_r > 0
                and psfmag_i > 0 and modelmag_i > 0
                and psfmag_z > 0 and modelmag_z > 0
          """.format(labels, 150, 0, RADIUS)

sql_query = sqlutilpy.get(sql_str,
                          host='xxx',
                          user='xxx',
                          password='xxx')

np.savetxt("sdss_phototag_{}.csv".format(RADIUS),
           np.array(sql_query).T,
           delimiter=",",
           header=labels,
           comments="")

print('%d objects' %len(sql_query[0]))
