---
title: "eCalc xcopterCalc"
created: 2026-10-30
captured: 2026-10-30
ingested: 2026-10-30
type: article
url: "https://www.ecalc.ch/xcoptercalc.php"
source_url: https://www.ecalc.ch/xcoptercalc.php
source_title: "eCalc xcopterCalc"
author: "eCalc (Solution for All, Markus Müller)"
sha256: "fb7288d0cc9d726637048ac27d01c5852f4bb588216a564fd51bff81b596409d"
source_html_sha256: "1d6c08dee9120ce9af5e064a63c725c020e8bd03f283d247dffab4f44a81ee6d"
capture_method: "HTTP GET 1회(2026-10-30), HTML을 텍스트로 기계 변환(요약·번역 없음). 폼 요소는 [input]/[select]/<opt> 표기. 드롭다운 목록은 JS로 채워지므로 미포함."
tags: [drone-hw]
---
eCalc - xcopterCalc - the most reliable Multicopter Calculator on the Web

JavaScript is disabled in your Browser 
- therefore eCalc will not work!
Please enable JavaScript for 
your Browser as described here....

 574'135'681 calculated drives - the most used setup tool

 | 

 |   
 | 

 | 

 Restricted Demo 
 Version

 sign-up for full version for only $0.99

 | 

 [img alt='eCalc - the most reliable RC Calculatoron on the Web']
 | 

 [img alt='']   

 [img alt='']   

 sign-up for full version for only $0.99

 Login here...

 | Accuracy: 
 +/-15%
 | xcopterCalc 
 - Multicopter Calculator
 | 
 News | 
 Toolbox | 
 Easy View | 
 Help | 
 Tutorial |  

 Language: [select name=lang] 

 |   
 |  

 | 

 | General
 |  
 | Model Weight:

 [input name=inGWeight type=text value='850'] g  
 [select name=inGWeightCalc]
 <opt 'AUW'>incl. Drive
 <opt 'BAT'>less Battery
 <opt 'SUM'>without Drive

 [input name=inGWeightOz type=text value='30'] oz

 |  
 | # of Rotors:

 [input name=inGRotors type=text value='4']

 [select name=inGConfig]
 <opt 'flat'>flat
 <opt 'coax'>coax

 |  
 | Frame Size:

 [input name=inGFrame type=text value='400'] mm

 [input name=inGFrameInch type=text value='15.75'] inch
 |  
 | FCU Tilt limit:

 [select name=inGTilt]
 <opt '90'>no limit
 <opt '10'>10°
 <opt '20'>20°
 <opt '25'>25°
 <opt '30'>30°
 <opt '35'>35°
 <opt '40'>40°
 <opt '45'>45°
 <opt '50'>50°
 <opt '55'>55°
 <opt '60'>60°
 <opt '65'>65°
 <opt '70'>70°
 <opt '75'>75°
 <opt '80'>80°

 |  
 |  
 |  
 | Field Elevation:

 [input name=inGElevation type=text value='500'] m 
 ASL

 [input name=inGElevationFt type=text value='1640'] ft 
 ASL

 |  
 | Air Temperature:

 [input name=inGTemp type=text value='25'] °C

 [input name=inGTempF type=text value='77'] °F
 |  
 | Pressure (QNH):

 [input name=inGPressure type=text value='1013'] hPa

 [input name=inGPressureInHg type=text value='29.91'] inHg 

 | Battery Cell
 |  
 | Type (Cont. / max. C) - 
 charge state:

 [select name=inBCell] 
 <opt '0'>Custom

 -
 [select name=inBChargeState] 
 <opt '6'>full
 <opt '0'>normal
 <opt '-6'>low

 |  
 | Configuration:

 [input name=inBS type=text value='3'] S   
 [input name=inBP type=text value='1'] P
 |  
 | Cell Capacity:

 [input name=inBCellCap type=text value=''] mAh

 [input name=inBCap type=text value=''] mAh total

 |  
 | max. discharge:

 [select name=inBDisc]
 <opt '0.10'>10%
 <opt '0.15'>15%
 <opt '0.20'>20%
 <opt '0.25'>25%
 <opt '0.30'>30%
 <opt '0.35'>35%
 <opt '0.40'>40%
 <opt '0.45'>45%
 <opt '0.50'>50%
 <opt '0.55'>55%
 <opt '0.60'>60%
 <opt '0.65'>65%
 <opt '0.70'>70%
 <opt '0.75'>75%
 <opt '0.80'>80%
 <opt '0.85'>85%
 <opt '0.90'>90%
 <opt '0.95'>95%
 <opt '1.00'>100%

 |  
 | Resistance:

 [input name=inBRi type=text value=''] Ohm
 |  
 | Voltage:

 [input name=inBVcell type=text value=''] V
 |  
 | C-Rate:

 [input name=inBCcont type=text value=''] C 
 cont.

 [input name=inBCmax type=text value=''] C 
 max.
 |  
 | Weight:

 [input name=inBWeight type=text value=''] g

 [input name=inBWeightOz type=text value=''] oz

 | Controller
 |  
 | Type:

 [select name=inEType] 
 <opt '0'>Custom

 |  
 | Current:

 [input name=inEContCurrent type=text value=''] A cont.

 [input name=inEMaxCurrent type=text value=''] A max.
 |  
 | Resistance:

 [input name=inERi type=text value=''] Ohm
 |  
 | Weight:

 [input name=inEWeight type=text value=''] g

 [input name=inEWeightOz type=text value=''] oz
 |  
 |  
 |  
 | Accessories
 |  
 | Current drain:

 [input name=inACurrent type=text value='0'] A
 |  
 | Weight:

 [input name=inAWeight type=text value='0'] g

 [input name=inAWeightOz type=text value='0'] oz

 | 
 Motor
 |  
 | Manufacturer - Type (Kv) - Cooling:  (² = discontinued)

 | 
 [select name=inMManufacturer] 
 <opt '-1'>select...

 | 
  - [select name=inMType] 
 <opt '0'>custom

 | 
 [select name=inGMotorCooling]
 <opt 'excellent'>excellent
 <opt 'good'>good
 <opt 'medium'>medium
 <opt 'poor'>poor
 <opt 'verypoor'>very poor

 | 

 |  
 | Kv (w/o torque):

 [input name=inMKv type=text value=''] rpm/V

 |  
 | no-load current:

 [input name=inMIo type=text value=''] A @
 [input name=inMVIo type=text value='']V
 |  
 | Limit (up to 15s):

 [input name=inMLimit type=text value=''] 
 [select name=inMLimitType]<opt 'A'>
 A
 <opt 'W'>W
 |  
 | Resistance:

 [input name=inMRi type=text value=''] Ohm
 |  
 | Case length:

 [input name=inMLength type=text value=''] mm

 [input name=inMLengthInch type=text value=''] inch
 |  
 | # mag. Poles:

 [input name=inMPoles type=text value='']
 |  
 | Weight:

 [input name=inMWeight type=text value=''] g

 [input name=inMWeightOz type=text value=''] oz

 | Propeller
 |  
 | Type - yoke twist:

 [select name=inPType] 
 <opt '0'>Custom

 - 
 [select name=inPTwist]
 <opt '7'>+7.0°
 <opt '6'>+6.0°
 <opt '5'>+5.0°
 <opt '4'>+4.0°
 <opt '3.5'>+3.5°
 <opt '3'>+3.0°
 <opt '2.5'>+2.5°
 <opt '2'>+2.0°
 <opt '0'>0°
 <opt '-2.5'>-2.5°
 <opt '-5'>-5.0°
 <opt '-7'>-7.0°

 |  
 | Diameter:

 [input name=inPDiameter type=text value='10'] inch

 [input name=inPDiameterMm type=text value='254'] mm

 |  
 | Pitch:

 [input name=inPPitch type=text value='4.7'] inch

 [input name=inPPitchMm type=text value='119'] mm 

 |  
 | # Blades:

 [input name=inPBlades type=text value='2']
 |  
 | PConst/TConst:

 [input name=inPConst type=text value='1.2'] /
 [input name=inTConst type=text value='1.0']
 |  
 | Gear Ratio:

 [input name=inPGearRatio type=text value='1'] : 
 1
 |  
 |  
 |  
 |  

 [input name=btnCalculate type=button value='btnCalculate']

[input name=user type=None value='']

 | 
Load 
 | 
Hover Time 
 | 
Maximum 
 | 
Temperatur 
 | 
Thrust-Weight-Ratio 
 | 
spec. Thrust 
 | 
Configuration 

 | Remarks:
 |  
 |  

 | Battery

 | Load:
 | 
 -
 | C

 | Voltage:
 | 
 -
 | V

 | Rated Voltage:
 | 
 -
 | V

 | Energy:
 | 
 -
 | Wh

 | Capacity:
 | 
 -
 | mAh

 | Capacity used:
 | 
 -
 | mAh

 | min. Flight Time:
 | 
 -
 | min

 | Mixed Flight 
 Time:
 | 
 -
 | min

 | Hover Flight 
 Time:
 | 
 -
 | min

 | Weight:
 | 
 -
 | g

 |  
 | 
 -
 | oz

 |  
 | Motor @ Optimum 
 Efficiency

 | Current:
 | 
 -
 | A

 | Voltage:
 | 
 -
 | V

 | Revolutions:
 | 
 -
 | rpm

 | electric Power:
 | 
 -
 | W

 | mech. Power:
 | 
 -
 | W

 | Efficiency
 | 
 -
 | %

 Wattmeter & Logger readings

 | Current:
 | 
 -
 | A

 | Voltage:
 | 
 -
 | V

 | Power:
 | 
 -
 | W

 |  
 | Motor @ Maximum

 | Current:
 | 
 -
 | A

 | Voltage:
 | 
 -
 | V

 | Revolutions:
 | 
 -
 | rpm

 | electric Power:
 | 
 -
 | W

 | mech. Power:
 | 
 -
 | W

 | Power-Weight:
 | 
 -
 | W/kg

 |  
 | 
 -
 | W/oz

 | Efficiency
 | 
 -
 | %

 | est. Temperatur
 | 
 -
 | °C

 |  
 | 
 -
 | °F

 | Rm:
 | -
 | mΩ

 | Controller:
 | -
 | epm

 |  
 | Motor @ Hover

 | Current:
 | 
 -
 | A

 | Voltage:
 | 
 -
 | V

 | Revolutions:
 | 
 -
 | rpm

 | Throttle 
 (log):
 | 
 -
 | %

 | Throttle 
 (linear):
 | 
 -
 | %

 | electric Power:
 | 
 -
 | W

 | mech. Power:
 | 
 -
 | W

 | Power-Weight:
 | 
 -
 | W/kg

 |  
 | 
 -
 | W/oz

 | Efficiency
 | 
 -
 | %

 | est. Temperatur
 | 
 -
 | °C

 |  
 | 
 -
 | °F

 | specific Thrust
 | 
 -
 | g/W

 |  
 | 
 -
 | oz/W

 |  
 | Total Drive

 | Drive Weight:
 | 
 -
 | g

 |  
 | 
 -
 | oz

 | Thrust-Weight:
 | 
 -
 | :1

 | Current @ hover:
 | 
 -
 | A

 | P(in) @ Hover:
 | 
 -
 | W

 | P(out) @ Hover:
 | 
 -
 | W

 | Efficiency 
 @ Hover:
 | 
 -
 | %

 | Current @ max:
 | 
 -
 | A

 | P(in) @ max:
 | 
 -
 | W

 | P(out) @ max:
 | 
 -
 | W

 | Efficiency @ 
 max:
 | 
 -
 | %

 |  
 | Multicopter

 | All Up Weight:
 | 
 -
 | g

 |  
 | 
 -
 | oz

 | add Payload:
 | 
 -
 | g

 |  
 | 
 -
 | oz

 | max. Tilt:
 | 
 -
 | °

 | max. Speed:
 | 
 -
 | km/h

 |  
 | 
 -
 | mph

 | est. Range
 | -
 | m

 |  
 | -
 | mi

 | max. rate of climb:
 | 
 -
 | m/s

 |  
 | 
 -
 | ft/min

 | Total Disc Area:
 | 
 -
 | dm²

 | 
 | 
 -
 | in²

 | Engine failure:
 | 
 -
 | 

 Range Estimator

 Speed (km/h)

 Motor Characteristics

 Ampere

 | NoteLeft
 | NoteRight

Version: X / Data: 
with 
Motors

 | 

 Here Comes the Message

    Ok   

 Here Comes the Message

    Ok   
 Cancel
