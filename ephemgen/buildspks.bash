#!/bin/bash

pushd ephemeris

for i in *.setup
do
	mkspk -setup $i -input $(basename $i .setup).data -output $(basename $i .setup).spk
done
