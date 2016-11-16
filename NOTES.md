#What's next?

Generate PCK data for planets. (rotation of the planets.)
ftp://naif.jpl.nasa.gov/pub/naif/misc/toolkit_docs_N0061/Tutorials/pdf/individual_docs/20_pck.pdf
https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/pck.html
http://naif.jpl.nasa.gov/pub/naif/utilities/PC_Linux_32bit/msopck.ug



#general NAIF tutorials
http://naif.jpl.nasa.gov/naif/tutorials.html



##Automatically switched patched-conics in GMAT.
	GMAT is meant to do realistic N-Body simulations, it can and does to patched conics, but that is acheived by creating multiple propagators and having your script switch between them at the appropriate time. Would it be possible to create a plugin that would provide an automatically switching patched-conics propagator?

	http://gmatplugins.sourceforge.net/blog/wp-content/uploads/2011/09/PluginDevelopment.pdf

	It looks like it won't be so bad. Check out the code from the included plugin "EphemPropagatorPlugin". It may be as simple as altering that code.
	While conic sections are more efficient, it might be good enough just to do a regular force-model but assign the force only to the one object whose sphere of influence we are in, orbital mechanics/calculus will take care of the rest.


