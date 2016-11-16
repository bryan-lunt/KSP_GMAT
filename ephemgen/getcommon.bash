#!/bin/bash

pushd common
wget https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/Gravity.tpc
wget http://naif.jpl.nasa.gov/pub/naif/pds/data/ody-m-spice-6-v1.0/odsp_1000/data/lsk/naif0007.tls

popd

