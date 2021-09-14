#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sep 2021
# This program calculates the cost of pizza

import constant


def main():
    # this function calculates the cost of pizza

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would like (inch): ")
    )

    # process
    sub_total = (
        constant.LABOR + constant.RENT + (diameter * constant.COST_PER_INCH)
    )
    total = sub_total + (sub_total * constant.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
