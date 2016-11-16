#!/usr/bin/env python

import numpy as np
import krpc

import ephem_templates

import os

real_planet_names=["MERCURY","VENUS","EARTH","MARS","JUPITER","SATURN","URANUS","NEPTUNE","PLUTO"]
real_planet_NAIF_codes=[199,299,399,499,599,699,799,899,999]

base_output_dir="./ephemeris"

from collections import defaultdict


conn = krpc.connect(address="192.168.0.101",name="ephemeris")


ksp_bodies = conn.space_center.bodies

ksp_sun = ksp_bodies['Sun']

#get all the planets, both into a dictionary and a sorted list
ksp_planets = dict([i for i in ksp_bodies.iteritems() if i[1].orbit != None and i[1].orbit.body.name == "Sun"])
ksp_planet_list = list(ksp_planets.itervalues())
ksp_planet_list.sort(key=lambda x:x.orbit.semi_major_axis)

#Get all the moons, and put them into dictionaries by planet.
ksp_moons = dict([i for i in ksp_bodies.iteritems() if i[1].orbit != None and i[1].orbit.body.name != "Sun"])
ksp_moons_by_planet = defaultdict(list)
for one_moon in ksp_moons.itervalues():
	ksp_moons_by_planet[one_moon.orbit.body.name].append(one_moon)

#sort the moon lists
for one_list_of_moons in ksp_moons_by_planet.itervalues():
	one_list_of_moons.sort(key=lambda x:x.orbit.semi_major_axis)




ten_to_min_nine=0.000000001
solar_gm=1172332800.0

#generate the templates
for i in range(len(ksp_planet_list)):
	one_planet = ksp_planet_list[i]
	its_orbit = one_planet.orbit

	setup_file_string = ephem_templates.setup_template.format(object_id=real_planet_NAIF_codes[i],
			object_name=real_planet_names[i],
			center_id=0,
			center_gm=solar_gm)
	ephemeris_data = ephem_templates.ephemeris_template.format(object_id=real_planet_NAIF_codes[i],
			center_id=0,
			center_gm=solar_gm,
			rad_periapsis_km=its_orbit.periapsis*0.001,
			eccentricity=its_orbit.eccentricity,
			inclination=np.rad2deg(its_orbit.inclination),
			longitude_of_ascending_node=np.rad2deg(its_orbit.longitude_of_ascending_node),
			argument_of_periapsis=np.rad2deg(its_orbit.argument_of_periapsis),
			mean_anomaly_at_epoch=np.rad2deg(its_orbit.mean_anomaly_at_epoch)
			)

	ephem_data = ""
	ephem_data += ephem_templates.ephemeris_template_header.format(object_id=real_planet_NAIF_codes[i],
			center_id=0,
			center_gm=solar_gm)
	for j in range(20):
		ephem_data += ephem_templates.ephemeris_data_line.format(time_in_seconds=j*its_orbit.period,
			rad_periapsis_km=its_orbit.periapsis*0.001,
			eccentricity=its_orbit.eccentricity,
			inclination=np.rad2deg(its_orbit.inclination),
			longitude_of_ascending_node=np.rad2deg(its_orbit.longitude_of_ascending_node),
			argument_of_periapsis=np.rad2deg(its_orbit.argument_of_periapsis),
			mean_anomaly_at_epoch=np.rad2deg(its_orbit.mean_anomaly_at_epoch)
			)





	with open(os.path.join(base_output_dir,"{}_{}.setup".format(i+1,one_planet.name)),"w") as setupfile:
		setupfile.write(setup_file_string)
	with open(os.path.join(base_output_dir,"{}_{}.data".format(i+1,one_planet.name)),"w") as datafile:
		datafile.write(ephem_data)
	
	
#conn.close()
