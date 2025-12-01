# spoke-tuner

A really simple script to aid with the tensioning of spokes during wheelbuilding.

It calculates spoke tension from the resonant frequency excited by plucking the spoke, with a couple of inputs:

* Spoke gauge (diameter)
* Spoke length (from cross to nipple)

Just pluck the spoke between the nipple and the first cross (where it touches another spoke) and measure the frequency with a tuning app on your phone. [DaTuner](https://play.google.com/store/apps/details?id=com.bork.dsp.datuna) works well for Android.

## Common gauges

Non-round spokes can be approximated as having an oval cross-section, from which the diameter of a
circle of equal cross-sectional area can be dervied:

* Sapim CX-Ray: 1.41 mm
