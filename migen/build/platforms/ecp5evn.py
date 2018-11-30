# This file is Copyright (c) 2018 Jens Andersen <jens.andersen@gmail.com
# License: BSD

from migen.build.generic_platform import *
from migen.build.lattice import LatticePlatform
from migen.build.lattice.programmer import LatticeProgrammer


_io = [
    ("clk12", 0, Pins("A10"), IOStandard("LVCMOS33")),
    ("clk200", 0, Pins("Y19"), IOStandard("LVDS")),

    # 50Mhz clock is optional and must be soldered
    ("clk50", 0, Pins(""), IOStandard("LVCMOS33")),
    ("clk50en", 0, Pins(""), IOStandard("LVCMOS33")),

    ("user_led", 0, Pins("B17"), IOStandard("LVCMOS25")),
    ("user_led", 1, Pins("A17"), IOStandard("LVCMOS25")),
    ("user_led", 2, Pins("C17"), IOStandard("LVCMOS25")),
    ("user_led", 3, Pins("B18"), IOStandard("LVCMOS25")),
    ("user_led", 4, Pins("A18"), IOStandard("LVCMOS25")),
    ("user_led", 5, Pins("B19"), IOStandard("LVCMOS25")),
    ("user_led", 6, Pins("A12"), IOStandard("LVCMOS25")),
    ("user_led", 7, Pins("A13"), IOStandard("LVCMOS25")),

    ("user_dip_btn", 0, Pins("J1"), IOStandard("LVCMOS33")),
    ("user_dip_btn", 1, Pins("H1"), IOStandard("LVCMOS33")),
    ("user_dip_btn", 2, Pins("K1"), IOStandard("LVCMOS33")),
    ("user_dip_btn", 3, Pins("E15"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 4, Pins("D16"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 5, Pins("B16"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 6, Pins("C16"), IOStandard("LVCMOS25")),
    ("user_dip_btn", 7, Pins("A16"), IOStandard("LVCMOS25")),

    ("user_btn", 0, Pins("P4"), IOStandard("LVCMOS33")),

    ("spiflash", 0,
        Subsignal("cs_n", Pins("R2"), IOStandard("LVCMOS33")),
        Subsignal("clk", Pins("U3"), IOStandard("LVCMOS33")),
        Subsignal("mosi", Pins("W2"), IOStandard("LVCMOS33")),
        Subsignal("miso", Pins("V2"), IOStandard("LVCMOS33"))
    ),

    ("spiflash4x", 0,
        Subsignal("cs_n", Pins("R2"), IOStandard("LVCMOS33")),
        Subsignal("clk", Pins("U3"), IOStandard("LVCMOS33")),
        Subsignal("dq", Pins("W2 V2 Y2 W1"), IOStandard("LVCMOS33"))
    ),
]

_connectors = [
   ("J39",
        "None",  # (no pin 0)
        "None",  #  1 GND
        "None",  #  2 N/C
        "None",  #  3 +2V5
        "D15",   #  4
        "B15",   #  5
        "C15",   #  6
        "B13",   #  7
        "B20",   #  8
        "D11",   #  9
        "E11",   # 10
        "B12",   # 11
        "C12",   # 12
        "D12",   # 13
        "E12",   # 14
        "C13",   # 15
        "D13",   # 16
        "E13",   # 17
        "A14",   # 18
        "A9",    # 19
        "B10",   # 20
        "None",  # 21 +5V IN
        "None",  # 22 GND
        "None",  # 23 +2V5
        "None",  # 24 GND
        "None",  # 25 +3V3
        "None",  # 26 GND
        "None",  # 27 +3V3
        "None",  # 28 GND
        "E7",    # 29
        "None",  # 30 GND
        "A11",   # 31
        "None",  # 32 GND
        "A19",   # 33
        "None",  # 34 GND
        "None",  # 35 +3V3
        "None",  # 36 GND
        "None",  # 37 +3V3
        "None",  # 38 GND
        "None",  # 39 +3V3
        "None",  # 40 GND
    ),
   ("J40",
        "None",  # (no pin 0)
        "K2",    #  1
        "None",  #  2 GND
        "A15",   #  3
        "F1",    #  4
        "H2",    #  5
        "G1",    #  6
        "J4",    #  7
        "J5",    #  8
        "J3",    #  9
        "K3",    # 10
        "L4",    # 11
        "L5",    # 12
        "M4",    # 13
        "N5",    # 14
        "N4",    # 15
        "P5",    # 16
        "N3",    # 17
        "M3",    # 18
        "None",  # 19 GND
        "None",  # 20 +3V3
        "K5",    # 21
        "None",  # 22 GND
        "M5",    # 23
        "None",  # 24 GND
        "L3",    # 25
        "None",  # 26 GND
        "N2",    # 27
        "M1",    # 28
        "L2",    # 29
        "None",  # 30 GND
        "L1",    # 31
        "N1",    # 32
        "C14",   # 33
        "None",  # 34 GND
        "P1",    # 35
        "E14",   # 36
        "D14",   # 37
        "None",  # 38 CARDSEL#
        "K4",    # 39
        "None",  # 40 GND
    ),
]

# Serial needs R34, R35 and R21 soldered to route to FTDI
_serial = [
    ("serial", 0,
        Subsignal("tx", Pins("P3"), IOStandard("LVCMOS33")),
        Subsignal("rx", Pins("P2"), IOStandard("LVCMOS33")),
    ),
]


class Platform(LatticePlatform):
    default_clk_name = "clk12"
    default_clk_period = 83.333

    def __init__(self, **kwargs):
        LatticePlatform.__init__(self, "LFE5UM5G-85F-8BG381C", _io, _connectors, **kwargs)

    def do_finalize(self, fragment):
        LatticePlatform.do_finalize(self, fragment)

    def create_programmer(self):
        _xcf_template = """
<?xml version='1.0' encoding='utf-8' ?>
<!DOCTYPE        ispXCF    SYSTEM    "IspXCF.dtd" >
<ispXCF version="3.4.1">
    <Comment></Comment>
    <Chain>
        <Comm>JTAG</Comm>
        <Device>
            <SelectedProg value="TRUE"/>
            <Pos>1</Pos>
            <Vendor>Lattice</Vendor>
            <Family>ECP5UM5G</Family>
            <Name>LFE5UM5G-85F</Name>
            <IDCode>0x81112043</IDCode>
            <File>{{bitstream_file}}</File>
            <Operation>Fast Program</Operation>
        </Device>
    </Chain>
    <ProjectOptions>
        <Program>SEQUENTIAL</Program>
        <Process>ENTIRED CHAIN</Process>
        <OperationOverride>No Override</OperationOverride>
        <StartTAP>TLR</StartTAP>
        <EndTAP>TLR</EndTAP>
        <VerifyUsercode value="FALSE"/>
    </ProjectOptions>
    <CableOptions>
        <CableName>USB2</CableName>
        <PortAdd>FTUSB-0</PortAdd>
        <USBID>Lattice ECP5 Evaluation Board</USBID>
    </CableOptions>
</ispXCF>
"""
        return LatticeProgrammer(_xcf_template)
