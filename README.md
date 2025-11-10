# xrp-huskylens
This repository provides support for using a HuskyLens with the XRP robot.
This is an unofficial project and is not maintained by the HuskyLens or XRP developers.

**Installation**

Place all files in this repository into your lib folder exactly as provided.

This implementation is configured to use QWIIC port 0 by default.
To use a different port, modify the value in qwiic_huskylens.py (line 118).

**Pin References**

Refer to the labels printed on your XRP board or the official SparkFun pinout documentation:

https://docs.sparkfun.com/SparkFun_XRP_Controller/hardware_overview/#expansion-headers

![XRP Pinout](images/XRP-Controller-Expansion-Pinout-Table.jpg)

**Contributions**

Feedback and improvements are welcome!
The current fix works but is still a bit rough around the edges, and I'd love to see cleaner or alternative solutions from the community.


Please note:

The original code is subject to the license specified in the SparkFun repository.
This repository does not claim ownership of the original code.
For official usage, distribution, or modification rights, refer to the license in the original repository.

https://github.com/sparkfun/Qwiic_I2C_Py/tree/master
https://github.com/sparkfun/qwiic_huskylens_py/tree/master
