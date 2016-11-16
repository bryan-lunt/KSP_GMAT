#!/usr/bin/env python

import numpy as np
import krpc

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
	
	real_planet_name = real_planet_names[i]
	first_cap_name = real_planet_name[:1].upper() + real_planet_name[1:].lower()
	eq_radius_in_km = one_planet.equatorial_radius*1.0e-3
	mu_in_km_cubed_over_sec_squared = one_planet.gravitational_parameter*1.0e-9

	print "GMAT {planet_name}.EquatorialRadius = {eq_radius_in_km};".format(planet_name=first_cap_name, eq_radius_in_km=eq_radius_in_km)
	print "GMAT {planet_name}.Mu = {mu_in_km_cubed_over_sec_squared};".format(planet_name=first_cap_name, mu_in_km_cubed_over_sec_squared=mu_in_km_cubed_over_sec_squared)



#Sphere of influence radii
print "Create Array SOIradii[10,1];"
for i in range(len(ksp_planet_list)):
	one_planet = ksp_planet_list[i]
	soi_in_km = one_planet.sphere_of_influence*1.0e-3
	print "GMAT SOIradii({}, 1) = {};".format(i+1,soi_in_km)


conn.close()
