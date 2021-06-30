#!/usr/bin/env python3

import math
import sys
import argparse

# Derived units.
kgf = 9.807  # N
mm = 1e-3  # m
cm = 1e-2  # m
g = 1e-3  # kg

# Constants.
density = 7.9 * g / cm ** 3 # Of stainless steel.


def frequency(tension, length, gauge):
    return math.sqrt(tension / (density * math.pi * (gauge / 2) ** 2)) / (2 * length)


def tension(frequency, length, gauge):
    return (frequency * 2 * length) ** 2 * (density * math.pi * (gauge / 2) ** 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument(
        "-T", "--tension", metavar="N", type=float, help="The tension in N."
    )
    parser.add_argument(
        "-k", "--tension-kgf", metavar="kgf", type=float, help="The tension in kgf."
    )
    parser.add_argument(
        "-f", "--frequency", metavar="Hz", type=float, help="The frequency in Hz."
    )
    parser.add_argument(
        "-L",
        "--length",
        metavar="mm",
        type=float,
        help="The spoke length in mm (from cross to nipple).",
    )
    parser.add_argument(
        "-G",
        "--gauge",
        metavar="mm",
        type=float,
        help="The spoke gauge in mm. Default: %(default)s.",
        default=1.8,
    )
    args = parser.parse_args(sys.argv[1:])

    length = args.length * mm
    gauge = args.gauge * mm

    if args.frequency:
        f = args.frequency
        T = tension(f, length, gauge)
        print(f"f = {f:.3g} Hz")
        print(f"T = {T:.3g} N ({T / kgf:.3g} kgf)")

    if args.tension:
        T = args.tension
        f = frequency(T, length, gauge)
        print(f"T = {T:.3g} N ({T / kgf:.3g} kgf)")
        print(f"f = {f:.3g} Hz")

    if args.tension_kgf:
        T = args.tension_kgf * kgf
        f = frequency(T, length, gauge)
        print(f"T = {T / kgf:.3g} kgf ({T:.3g} N)")
        print(f"f = {f:.3g} Hz")
