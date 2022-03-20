# CoPY, the C struct to Python compiler

It can seems awkward to use a compiler to translate low level to high level code but due to massive usage of Python for fast prototyping and mapping of binary structures in embedded development, it can be usual to use Python tools.

To process binary data generated by hardware, this project aims to automatically translates C structures to their Python ctypes equivalent.

This can be pretty useful for development of Python exploit, data decoding for instance.
A quick example is provided based on a FAT32 structure look alike.