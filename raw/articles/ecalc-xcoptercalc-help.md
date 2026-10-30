---
title: "eCalc xcopterCalc Help"
created: 2026-10-30
captured: 2026-10-30
ingested: 2026-10-30
type: article
url: "https://www.ecalc.ch/calcinclude/help/xcoptercalchelp.htm"
source_url: https://www.ecalc.ch/calcinclude/help/xcoptercalchelp.htm
source_title: "eCalc xcopterCalc Help"
author: "eCalc (Solution for All, Markus Müller)"
sha256: "8a652ebb31c951d98bf0d35c77cff79c4d2628890f1a9f738dbe93d4ec27f95d"
source_html_sha256: "0364b4fd1f75aa6b9e9bf0f9fba2c265833902f0710111d250d3dd0960f66f33"
capture_method: "HTTP GET 1회(2026-10-30), 원본 인코딩 cp1252 HTML을 UTF-8 텍스트로 기계 변환(요약·번역 없음). 영문·독문 병기 원문 그대로."
tags: [drone-hw]
---
eCalc - the most reliable RC Calculators on the Web for electric Motors

 | 

[img alt='eCalc - e Motoren Calculator']

 |   - the most reliable RC Calculator on the Web

 | 

 | 

xcopterCalc:  Help - Hilfe

 | 

 | 

 | | Results |
 Long Wiring | Vortex Ring State 
 | Efficiency |
 |  
 | | Resultate |
 Kabelverlängerung | Wirbelring 
 | Effizienz |

 |   
 |  
 |  

 | 
How to use this
 Calculator

Problems - eCalc does not work? Find a Trouble 
 Shooting Guide here... 

For explanatory videos and tutorials visit and subscribe our 
 growing 

 YouTube Channel.
This Multicoper Calculator supports you in choosing an adequate motor setup for your electric
 RC Multicopter with fixed pitch Propellers. it is suitable 
 for flat and coax configurations.
Always define the frame 
 size first - then the propulsion with eCalc and use the largest 
 possible propeller diameter.
Calculation
 with available components:

Enter the all up weight (incl. Camera), number of rotors and  
 the configuration - read the hints regarding flat 
 vs. coax...

Enter the environmental numbers (Field Elevation, Air Temperatur
 & Air Pressure (QNH)).

Choose the Battery from the drop  down list and adjust
 the numbers of cells in serial and parallel.

Choose the ESC from the drop down list.

To find the required KV range use the Prop-KW-Wizard and 
 Search function. Choose the motor manufacturer and type from the drop down list..

Choose the type of propeller with Diameter and Pitch. Use 
 always the largest possible Diameter for your frame for best 
 efficieny. If you
 are using a folding prop enter the effective diameter including
 the (twisted) yoke.

Enter your Gear Ratio ( = Propeller Pinion Teeth : Motor Pinion
 Teeth).

Press the Button [calculate].

Aim for a Hover Throttle (linear) of less than
- 70% for camera 
 platforms
- 60% for aerial photygraphy
- 50% for FPV 
 aerial explorer
- 45% for FPV Race Copters

Find a more in depth

 tutorial here... (by Michael Kelly)

# of rotors: 
Total number of Rotors and 
 there arrangement respectively configuration: 
  - flat: one 
 rotor on each arm 
  - coaxial: two 
 identical counter-rotating motors using same 
 prop on 
    each arm

Frame Size: 
The size of the frame is defined by the distance of the two 
 opposite motors (X) or double the arm length from center to motor (Y). 
 eCalc does a plausability check for the Propeller Tip Clearance 
 between the Propellers (but not to the center hub!) provided the frame 
 is full symetric.

Model Weight (incl. Drive / less Battery / without Drive):

 You can chose whether your entry is the 
 - All Up Weight 
 (incl. Drive)
 - the empty weight (without Battery) - the battery 
 weight will be added to 
    your entry
 - the basic weight  
 (without Drive) - then the chosen Components 
    (Battery, ESC, Motor) weight will be added
 to your entry. 

 Example for a Quad: «without Drive» adds to your weight entry
 1xBattery, 4xESC, 4xMotor, +10% (e.g. for Prop).

Accessories:
you may define the weight of 
 additional accessories (e.g. camera, gimbal, light,...) and the 
 corresponding current consumption if supplied by flight battery. Use 
 current drain=0A for accessories supplied by own battery.
If you 
 use solar panels to prolonge flight time insert the current delivery 
 from solar panel as negative value e.g. -4A
FCU Tilt limit:

 Most FCU (Flight Control Units) or flight modes do limit the maximum 
 tilt for a better controlability. You can choose the tilt limit of 
 your FCU for a more accurate result of the max. horizontal Speed.

Battery Charge State:

 as the battery voltage does decrease over its discharge cycle you
 can choose the state of your battery at measurement for better
 comparison:

 - full: battery is fully charged and has low charging cycles (use 
 only to evaluate short term motor peak values).

 - normal: average battery discharge voltage. All resultas are average values 
 over a discharge cycle.

 - low: battery voltage with about 25% remaining capacity (use only 
 to evaluate the motor end of
 flight values).
Battery max. discharge:
This 
 defines the maximum percentage of the total capacity be used for a 
 flight (=used capacity). This is the base for all flight time related 
 calculations.
Remark: Never ever deep discharge a LiPo Battery 
 - aim for at least 10% remaining capacity after flight.

 Battery performance in cold weather:
The internal 
 Resistance of a LiPo battery variies with it's chmerstry temperature. 
 If cold outside temperature leading to chemerstry temperature below 
 20°C you must expect  degraded performance during operation. 
 Pre-heating the cells to 20...30°C may help to improve the performance 
 in cold weather operation.
Currently eCalc does not consider the 
 adverse affect of cold chemestry.

 Choice of ESC:
Remember the ESC is able handle the 
 max. rated current only under these circumstances:
  - with 
 efficient cooling airflow
  - at full throttle (no pulse width 
 modulation active)
We suggest to plan for additional headroom of

 - 20% for inefficient cooling airflow
  - 40% for convective 
 cooling
  - 20% if used in partial load
Remark: These 
 are rules of thumb and must be confirmed by temperature measurements.

 Motor Cooling Guideline:
The motor cooling gets 
 efficient with a steady air stream along the motor case. The higher 
 the volume of air the better the motor gets rid of the heat. Here some 
 guidelines to the cooling options:
- Excellent: 
 very high air flow along the motor
   (e.g. due open 
 mounting, forced ventilation (edf), redirected air flow to motor)
-
 Good: normal air flow along motor

 (e.g. vent holes or additional fan)
- Medium: low 
 air flow
   (e.g. in lee of large spinner)
- 
 Poor: convective air flow in wide fuselage
- Very 
 poor: convective air flow in narrow fuselage

 (e.g. hotliner with no venting)
However, in real live your motor 
 case should never ever exceed 80°C/180°F otherwise 
 you run into risk of overheat and even burning the motor.
Prop-KV-Wizard:

 The Prop-KV-Wizard is a helpfull and powerfull tool to
- find the 
 largest propeller for your frame size - the bigger the prop the more

 efficient is the hover performance.
- evaluate the recommended 
 motor KV range as starting point for your
  calculations

 For full symetric frames the wizard does assure the propeller tip clearance between 
 props but NOT the center hub clearance as this depends on 
 the frame make.
the right propeller:
the 
 bigger the total disc area (propeller diameter) the more efficient 
 does your copter hover, but the slower gets the control responce.

 Propeller with a Pitch to Diameter ratio greater than 0.667 tends to 
 stall with increasing load. A stalling propeller blade might lead to 
 loss of control.
Therefore aim for a Pitch to Diameter ratio of 
 less than 2/3. 
Be carefull with a high ratio on your race copter. 
 Even a setup works on one (lighter) copter it might end up in loss of 
 control on another (heavier) copter!

 Folding Propeller:

 If you are using a yoke wider than standard (see below) just add the
 difference to the standard yoke to the diameter. Always use the effective propeller
 diameter (Tip to Tip). Standard Yoke for

 - Aeronaut Blades is 42mm/1.65"
- GM Blades is 32mm/1.26"
- Graupner Blades is 42mm/1.65"

 - Leomotion Blades is 32mm/1.26"

 - RFM Blades is 42mm/1.65"

 - eflight Blades is 36mm/1.42"

 Generic Propeller
By selecting a Generic (thin, 
 notmal, wide) Propeller from the list. eCalc dynamically calculates 
 the propeller constanst PConst to match best a unknown or not listed 
 prop.
Calculation with custom components:

 You can use any Battery, ESC, Motor or Propeller as long as the
 technical data are available. Choose «custom» in the respective drop
 down list and enter all the required data in fields right
 of it. (Important: the parameter for the 
 Battery are required for a single cell)
When using Custom Components only use manufacturer 
 data or own measurements. Do never ever assume parameters or derive 
 parameters from similar motors as inaccurate parameters will lead to 
 inaccurate results.
Evaluate Motor Resistance: Using an ohm meter 
 is a bad idea, as you also will measure the contact resistance! For 
 better results use the Kelvin 4-wire method.
Evaluate no-load current and Kv: run your motor 
 without any prop at full throttle on a 3s or 2s battery (Voltage must 
 be below max allowed Voltage of the manufacturer) and measure the 
 resulting no-load current, voltage and rpm. Calculate 
 now Kv = rpm / Voltage.
Warning: 
 Do run your motor under no-load condition only for a very limited time 
 (<10s) as waste power is high and a motor may overheat!Logger 
 and Watt Meter:
Logger and Watt Meter values du correspond 
 to
Voltage = eCalc Battery Voltage Result
Current = eCalc Motor 
 @ Maximum Current
Wattage = not desplayed in eCalc (multyply the 
 above two values) 
Note: 
 Before using logging device - especially when integrated into the ESC - 
 make a reference measurement with a quality multimeter to calibrate your 
 logger. In some cases we have experienced deviation of 25% or 
 even more to the reality.
Battery Custom data:

 As a reminder these input data are for a single cell of your battery 
 pack.
Export Data 
 (for members only when logged in):
The calculated results may be 
 exported to any spreadsheet application (e.g. Excel) that may read CSV 
 files (comma separated).
[Add >>] adds the actually displayed data 
 to the export file.
[Download .csv (x)] downloads the CSV file to 
 your computer. (x) indicates the number of setups in the file.
[<< 
 Clear] deletes all the data in the prepared export file.

 Share or Save your Setups (for members only):
If you would like to share or save a 
 designated setup use the [share] button.
eCalc reloads the 
 prarametrized link (url, page) with your settings preselected. You may 
 re-calculate, save the link in your Browser favorites/bookmarks or 
 copy/past the link for sharing your setup.
By calling this link 
 eCalc will preselect your components for calculation.
Print:

 Best results for printing eCalc results on paper are acheved with 
 these printer settings:
FireFox & Safari: Portait
Chrome & 
 Explorer: Landscape
 |  
 | 
Wie setzten Sie
 den Calculator ein?

Probleme - eCalc funtioniert nicht? Hier finden 
 Sie Problemlösungen....

Für erklärende Videos und Anleitungen besuchen und abonnieren Sie 
 unseren 
 stetig wachsenden

 eCalc YouTube Kanal.

Dieser Multicopter Calculator unterstützt Sie bei der Wahl eines 
 elektrischen Antriebs für ihren Multicopter/Drohnen mit
 Starr-Propeller. Damit können  Konfigurationen mit einem 
 Propeller  (flache) oder zwei Propeller (coacial) pro Arm 
 berechnet werden.

Definieren Sie erst die Rahmengrösse - dann erst den 
 Antrieb mit eCalc mit dem grösst möglichen Propeller-Durchmesser.

Berechnung mit vorhandenen Komponenten:

Geben Sie das totale Fluggewicht (inkl. Kamera) und Anzahl Rotoren 
 und deren Anordnung Ihres
 Multicopters ein - lesen Sie mehr zum Thema 
 coaxial vs. flacher Konfiguration...

Geben Sie die Rahmenbedingungen (Flugplatzhöhe, Temperatur) ein.

Wählen Sie Ihren Akku aus und geben die entsprechende
 Konfiguration des Akkus ein (Anzahl Zellen seriell bzw.
 parallel).

Wählen Sie Ihren Regler bzw. Steller.

Um das optimale KV Intervall zu finden benutzen Sie den 
 Prop-KV-Wizard sund die Such-Funktion. Wählen Sie Ihren Motor aus der Hersteller- und Typenliste
 aus.

Wählen Sie Ihren Propellertyp aus und geben den Durchmesser und die
 Steigung/Pitch ein. Nutzen See entsprechend Ihrer Rahmengrösse 
 stehtst den grösst möglichen Durchmesser für besten Wirkungsgrad. Falls Sie einen Klapp-Propeller verwenden
 geben sie den effektiven Durchmesser inkl. (verschränktem)
 Mittelstück ein.

Geben Sie Ihr Untersetzungsverhältnis ein ( = Anzahl Propritzelzähne : Anzahl Motorritzelzähne) 

Drücken Sie den Knopf [berechnen]

Wir empfehlen eine Regleröffnung von weniger als
- 70% 
 für Kamera Plattformen
- 60% für dynamische Luftaufnahmen

 - 50% für FPV Luftaufnahmen
- 45% für FPV Race Kopter

Ein

 bebilderte Anleitung finden Sie hier.... (englisch, von Michael 
 Kelly)

Anz. Rotoren: 
Totale Anzahl der Rotoren und 
 deren Anordnung: 
  - flach: ein Rotor pro Arm 
  - koaxial: zwei identische, gegenläufig drehende Motoren 

    (mit gleicher Luftschraube) pro Arm 

Rahmengrösse: 
Die Rahmengrösse ist definiert durch die Distanz zwischen den 
 gegenüberliegenden Motoren (X) oder die doppelte Armlänge vom 
 Zentrum zum Motor. eCalc überprüft die Propellerfreiheit zwischen 
 den Propellern (aber nicht zur zentralen Plattform!) für 
 voll-symetrische Rahmen.
Modellgewicht (mit Antrieb / ohne Akku / ohne Antrieb):

 Sie können Wählen ob ihre Gewichtsangabe dem totalen Abfluggewicht
 (inkl. Antrieb) enspreicht oder das Abfluggewicht aus Ihrem
 eingegebenen Leergewicht (ohne Akku) bzw. Rohbaugewicht (ohne 
 Antrieb) und den gewählten Komponenten errechnet
 werden soll.

Zubehör:
Gewichtsangaben des Zubehörs (z.B. 
 Kamera, Gimbal, Licht,....) und dessen Stromverbrauch - falls vom 
 Flugakku versorgt - können definiert werden.
Geben Sie Stromverbrauch=0A 
 ein, wenn das Zubehör über eine separate Stromversorgung verfügt.

 Sollten Sie die Flugzeit mit Solarpanelen verlängern, gben Sie die 
 Stromzufur der Panelen als negativen Wert ein, z.B. 
 -4A
max. FCU Neigung:

 Viele Flug Controler (FCU) oder Flug Modi limitieren die maximale 
 Nick-Neigung für eine bessere Stabilität. Da diese einen direkten 
 Einfluss auf die erreichbare max. Gewindigkeit im horitontalflug 
 hat, kann sie nun entsprechend der FCU Limitationen limitiert 
 werden.
Some FCU (Flight Control Units) or flight modes do limit 
 the maximum tilt for a better controlability. You can choose the tilt 
 limit of your FCU inorder for a more accurate result of the max. 
 Speed.

Akku Ladezustand:

 Da die von der Batterie abgegebene Spannung über einen
 Entladezyklus sukzessive abnimmt, wird sie auch je nach Ladezustand
 einen unterschiedlichen Messungwert liefern. Wählen Sie den
 ensprechenden Ladezustand um einen Vergleich mit Ihren Messungen zu
 machen:

 - voll: Der Akku ist voll geladen und weist wenige Ladezyklen
 auf 

   (damit lassen sich kurzzeitige Motoren-Spitzenwerte ermitteln).

 - normal: mittlere Akkuspannung. Alle Resultate entsprechen dem Mittelwert 
 über einen Entladezyklus.

 - tief: Akkuspannung bei rund 25% Restkapazität (damit lassen sich 
 die Motoren-Werte am ende eines Fluger ermitteln).

Batterie max. Entladung:
Definition wieviel 
 Prozent der gematen Kapazität wärend dem Flug verbraucht wird (= 
 genutzte Kapazität). Alle Flugzeiten basienren auf dier prozentualen 
 Entladung.
Anmerkung: LiPo Akkus sollten nie tiefentladen 
 werden - nach dem Flug sollte mindestens 10% der Kapazität im Akku 
 verbleiben.
Batterie Leistung bei kaltem Wetter:

 Der Zellen-Widerstand nimmt bei niedrigen Zell-Chemie-Temperaturen 
 massiv zu. Dies kann bei kalten Aussentemperaturen zu merklichem 
 Leistungseinbruch führen, wenn die Zell-Chemie nicht auf 
 "Betriebstemperatur" gebracht wird. Ein Vorwärmen der Zellen auf 
 20...30°C vor Gebrauch verbessert die Zellenleistung bei kaltem 
 Wetter.
eCalc berücksichtigt den Effekt kalter Zell-Chemie aktuell 
 nicht.
Regler-Wahl:
Maximale 
 Strom-Angaben auf Reglern sind oft nur unter folgenden Bedingungen 
 zulässig:
  - bei effizientem kühlenden Luftstrom
  - 
 voll durchgeschaltet (keine Puls-Weiten-Modulation aktiv)
Folgende 
 Reserven sind empfehlennswert:
  - 20% bei schlechtem 
 Kühlluftstrom
  - 40% bei konvektiver Kühlung
  - 20% 
 für Teillastbetrieb
Anmerkungen: Dies sind Faustregeln und 
 müssen mit einer Temperatur-Messung verifiziert werden.

 Motorkühlung - Empfehlung:
Mi einem konstanten 
 Luftstrom wir eine effiziente Kühlung dess Motors sichergestellt. Je 
 höher das Luftvolumen desto einfacher kann die Abwärme abgeführt 
 werden. Hier unsere Empfehlung bzgl. Kühlungsoptionen des Motors:
-
 sehr gut: hoher Luftstrom entlang des Motos.

 (z.B. auuserhalb des Rumpfes. Zwangslüftung in Impeller oder 

 durch Leitbelche)
- gut: normaler Luftstrom 
 entlang des Motors
   (z.B. durch Lüftungslöcher oder 
 zusätzlichem Lüfter)
- mittel: geringer Luftstrom 
 entlang des Motors.
   (z.B. im Windschatten von grossen 
 Spinnern)
- gering: konvektiver Luftstrom in 
 weitem Rumpf
- sehr schlecht: konvektiver 
 Luftstrom in engem Rumpf
   (z.B. im Hotliner-Rumpf ohne 
 jegliche Lüftung)
Prop-KV-Wizard: (ab Version 6.60, ende Mai)

 Der Prop-KV-Wizard ein hilfreiches Werkzeug um
- um die grösste 
 Luftschraube für Ihre Rahmengrösse zu finden - je grösser

 die Luftschraube um so besser ist ihre Schwebe-Leistung.
- ein 
 Motor-KV-Intervall als optimalen Ausgangspunkt für weitere 

 Berechnungen zu ermitteln.
Für voll-symetrische Rahmen stellt
 der Wizard die 
 gegenseitige Propellerfreiheit sicher nicht aber die Freiheit zur 
 zentralen Aufnahme, da diese vom Rahmenfabrikat abhängt.

 der richtige Propeller:
Je grösser die 
 Propellerfläche (Propellerdurchmesser) desto effizenter ist das 
 Schweben, desto träger wird jedoch die Regelung
Bei Propellern mit 
 einem Pitch-Durchmesserverhältnis über 0.667 kann der Lufstrom am 
 Propellerblatt abreissen und zu einem Kontrollverlust führen.
Wir 
 empfehlen ein Pitch-Durchmesserverhältnis von unter 2/3.
Vorsicht 
 ist geboten bei Renn-Koptern mit einem höheren 
 Pitch-Durchmesserverhältnis: Ein gut funktionierendes Setup von einem 
 (leichten) Renn-Kopter kann bei einem anderen (schwereren) Kopter zum 
 Kontrollverlust führen!
Klapp-Proppeller:

 Sollten Sie ein Mittelstück einsetzten, welches von der
 Standartbreite abweicht, muss dies durch Anrechnung der Different
 zum Standart-Propeller-Durchmesser berücksichtigt werden. Verwenden Sie
 stehts den effektiven Propeller-Durchmesser (Spitze zu Spitze in
 Zoll). Das Standart-Mittelstück für

 - Aeronaut Blätter ist 42mm/1.65"
- GM Blades ist 32mm/1.26"
- Graupner Blätter ist 42mm/1.65"

 - Leomotion Blades ist 32mm/1.26"

 - RFM Blätter ist 42mm/1.65"

 - eflight Blätter ist 36mm/1.42"

Generic Propeller
Wenn Sie einen Gemeric 
 (Thin, normal, wide) Propeller aus der Liste wählen, werden die 
 Propeller-Eckdaten Pconst dynamisch berechnet, damit sie eine 
 möglichst gute Annäherung für einen unbekannten oder nicht 
 gelisteten Propeller erhalten.
Berechnung mit nicht vorgegebenen Komponenten:

 Wenn Sie in Besitz der techn. Angaben sind, können Sie mit jedem
 beliebigen Akku, Steller oder Motor eine Berechnung durchführen.
 Wählen Sie dafür in der entsprechenden Liste «andere»  aus
 und geben die nötigen Daten in den rechts davon liegenden Feldern
 ein.  (Witchtig: Die Battery Daten müssen pro 
 Einzelzelle erfasst werden)
Bei der Verwendung eigener Komponenten sollten Sie 
 ausschliesslich Herstellerdaten oder eigene Messungen verwenden. 
 Gehen Sie nie von Annahmen aus oder leiten Sie die Daten nicht von 
 ähnlichen Komponenten ab, da ungenaue Parameter zu ungenauen 
 Resultaten führt.
Bestimmung des Innenwiderstandes des Motors: Bei Verwendung 
 eines Ohm-Meters werden die oft sehr kleinen Widerstandswerte durch 
 den Übergangswiderstand verfälscht. Nutzen Sie

 diese Methode.
Bestimmung des Leerlaufstroms und Kv: Betreiben 
 Sie Ihren Motor ohne Propeller mit Vollgas an einer 3s oder 2s 
 Batterie (bitte respektieren Sie die max. Motorspannung des 
 Herstellers). Nun messen Sie den Leerlaufstrom, die 
 Spannung und die Drehzahl. Nun können Sie Kv = 
 Drehzhl / Spannung berechnen.
Achtung: Betreiben 
 Sie Ihren Motor nur kurz im Leerlauf (<10s), da die Verlustleistung 
 (ohne Prop) sehr hoch sein kann und der Motor zur Überhitzung neigt.
Akku-Zellen Eingabedaten:

 Die Eingabedaten für den Akku beziehen sich auf eine einzelne Zelle 
 Ihres Akku-Packs.
Logger und Watt-Meter:

 Logger und Watt-Meter Werte entsprechen den folgenden Resultaten:

 Spannung = eCalc Batterie Spannung
Strom = eCalc Motor @ Maximum 
 Strom
Leistung = nicht angezeigt (entspricht der multiplikation der 
 beiden Werte oben)
Anmerkung: Wenn sie einen Daten-Logger verwenden - 
 insbesondere im Regler integrierte - machen sie eine Referenzmessung 
 mit einem Multimeter um den Logger zu kalibieren. Unsere 
 Erfahrung zeigt, dass Logger über 25% von einer realen Messung 
 abweichen können.
Daten Exportieren 
 (nur für angemeldete Mitglieder):
Die berechneten Daten können mit 
 Hilfe dieser Funktion in ein beliebiges Programm exportiert werden, 
 welche CSV Dateien (Komma separiert) lesen kann (z.B. Excel).

 [hinzufügen 
 >>] fügt die aktuell angezeigten Daten zur Export Datei hinzu.

 [.csv herunterladen(x)] Die Export Datei wird runtergeladen. (x) zeigt die 
 Anzahl gespeicherten Antriebe in der Export Datei an.
[<< 
 löschen] 
 löscht alle in der Export Datei befindlichen Daten.
Teilen 
 oder Speichern von Antrieben 
 (nur für angemeldete Mitglieder):
Sie können ein Antrieb teilen 
 oder speichern 
 mit Hilfe des Knopf [Teilen]. 
eCalc läd die Seite neu mit einem 
 parametrierten Link. Ihre Einstellungen werden damit automatisch 
 übernommen. Sie können nun den gewählten Antrieb erneut berechnen, den 
 Link in den Favoriten speichern oder copieren um mit jemandem ihre 
 auslegung zu teilen.
Mit Hilfe dieses Links werden die 
 Komponenten später automatisch zur erneuten Berechnung abfüllen.
Drucken:

 Zum Drucken Iher eCalc Ergebisse empfehlen wir folgende 
 Druck-Einstellungen in ihrem Browser:
FireFox & Safari: Hochformat

 Chrome & Explorer: Querformat

 | 

 | 

 | 
Interpret the Results 

All results are based on indicated All-Up-Weight.

Quick Check Gauges:
Some parameters are additional shown as 
 gauges for a quick overview of the setup.

Load: discharge rate of battery
- green: 
 range of continuous C-rate
- yellow: range to peak C-rate
- 
 red: over limit

Hover Flight Time: ranges according 
 experience

est. Temperature: estimated maximum 
 temperature
- green: normal range 0…70°C
- yellow: critical 
 range 70…90°C
- red: over limit, risk of overheat

Electric Power / Current: maximum values in 
 relation to specified motor limit (max. 15s) either in wattage or 
 amps.
- green: range below 70% of limitation 
- yellow: 
 critical range up to limitation
- red: over limit, risk for 
 permanent damage

Thrust-Weight Ratio: indication for flight 
 performance (the higher the more agile your copter gets) and 
 (indirectly) throttle for hovering
- green: 1.8 and more 
 resulting in ~ 60% throttle or lower 
- yellow: 1.2 to 1.8 
 resulting in 60 to 80% throttle – limited maneuverability
- 
 red: hovering is not possible

Specific Thrust: specific thrust of the 
 propeller is an indication of overall hover efficiency
- green: 
 6g/W and more considered as good efficiency 
- yellow: 4…6g/W 
 is poor
- red: below 4g/W is ineffective

Remark:

 The Calculator checks various parameters (e.g. max current, power)
 and will generate  an adequate message. These are NOT 
 errors but advices where you may run into a problem. Blue 
 remarks are advisory, red critical.
The max. physical RPM
 are not monitored. 
Always respect the limits of the manufacturer!

All results are based on the calculated All-up Weight:

Battery:

Load: the actual discharge rate in relation to the
 capacity.

 Voltage: Battery-Voltage under expected max. Current.

 Rated Voltage: You find on your Pack.
Energy: 
 of the battery.
Total Capacity: of the Battery

 Used Capacity: for the flight used capacity 
 according to the selected max. discharge percentage of the battery. This 
 is the base for any flight time related calculations!

 min. Flight Time: expected min Flight Time is based on  
 maximum Throttle (based on max. discharge % of Battery) and is 
 independent of the weight.

 mixed Flight Time: Expected Flight Time based on all-up 
 weight  when moving based on max. discharge % of Battery, base is 
 geometric mean value of current difference from hover to max.)

 hover Flight Time: Expected Flight Time based on all-up 
 weight  when hovering only (based on max. discharge % of 
 Battery)

 Weight: of Battery-Pack

Motor @ Optimal Efficiency  (for each motor!):

Current: current for maximum motor efficiency with 
 varying torque (dyno test).

 other data same as  below.

Motor @ Maximum (for each motor!):

max Current: maximum Amp draw.

 Voltage: Voltage at the motor

 Revolutions: maximum revolutions.

 el. Power: electric input power.

 mech. Power: mechanical output ower or shaft power.

 Power-Weight: Power Weight Ratio for the 
 maximum current case.

 Efficiency: Efficiency at max. Amp. Draw

 est. Temperature: Estimated Temperature of the 
 Motor Case - subject to the motor cooling. Temperatures over 80°C and higher might damage your 
 motor. Temperature over 100°C are very critical.
Rm: 
 dynamic resistance of the drive.

 Controller: number of pulses fired by the controller to 
 achive the motors revolution (epm = events per minute) and is 
 equal to the magnetic RPM. 
 Controllers are limited in the maximum number of pulses per 
 minute. eCalc does not monitor this limit. It is often in the 
 range of 200'000 to 500'000 epm. 

Wattmeter redaings:

Values for current, voltage and wattage 
 as you will read out with a classic wattmeter or logger device doing a 
 static benchtest. Remeber to use the battery charge state «full» for 
 comparison on full recharged batteries.

Motor @ Hover (for each motor!):

Hover Calculation might become inaccurate with a 
 Diameter-Pitch-Ratio of more than 0.667 (stalling props). Extreme 
 Ratios lead to unavailable figures for hover.
However, 
 for Race Copters high pitch props will be accepted (if 
 Diameter less than 6.5"). Be aware the reduced hover accuracy will 
 be a trade to the wish of the Race Copter community using high 
 pitch props for calculation....

Current: estimated current for hovering. the hover 
 current shuld be be close to the optimal current (see abouve) or 
 sligtly below.

 Voltage: motor voltage for hovering.

 Revolutions: Propeller revolutions to hover.
Throttle (log): 
 Some ESC aims  for a (pseudo) power or thrust linearity. This Trottle 
 position for hovering represents the stick position to hover in 
 manual mode assuming a logarithmic PWM (Puls Width Modulation) 
 transformation by a power or thrust linear ESC. 
Remark: As this logarithmic 
 curve may differ between brands this is a empirical value.

 Throttle (linear): Concentional ESC aims for (preudo) RPM 
 linearity. The Trottle position for hovering represents 
 the stick position to hover in manual mode with a linear PWM (Puls 
 Width Modulation) by RPM linear ESCs. That means 60% Throttle represent the PWM 
 controles the FET 60% on / 40% off resulting in a linear voltage/rpm 
 at the motor.
Remark: Do not mistake 
 this value with the PVM Time in μsec shown on some flight control 
 logs.

 el. Power: electric input power.

 mech. Power: mechanical output power or shaft power.

 Power-Weight: Power Weight Ratio for the 
 hover case. 150W/kg is a rule of thumb, very efficient setups 
 bring that down to approx. 80W/kg.
Efficiency: motor efficiency at hovering.
est. 
 Temperature: predicted motor temperature - subject to the 
 motor cooling.

 specific Thrust: How many Gramm of Thrust will be
 produced with one Watt of electric Input Power at the propeller. 

Total Drive:

Drive Weight: weight of all components (with 10% margin, 
 e.g. for propeller weight compensation) 

 Thrust-Weight: Thrust Weight Ratio - flying below 1.2 
 is almost impossible.

 Current @ Hover: sum of all motors when hovering.
el. Power 
 @ Hover: electric input power at battery when hovering.

 mech. Power @ Hover: mechanical output power or shaft power 
 when hovering.

 Efficiency @ Hover: Total Efficiency when hovering.

 Current @ max: sum of all motors at full thrust.
el. Power 
 @ max: electric input power at battery at full thrust.

 mech. Power @ max: mechanical output power or shaft power 
 at full thrust.

 Efficiency @ max: Total Efficiency at full thrust.

Multicopter:

All-up Weight: calculated actual Flying Weight 
 (Basic Weight + Drive Weight, add. Payload is NOT considered). All 
 calculated values are based on this All-Up-Weight.

 add. Payload: maximum additional payload possible to hover with 80%
 Throttle to garantee maneuverability. (we recommend below 50% 
 throttle for 
 arobatics and below 80% throttle for Photography). 

 max. Tilt: Theoretically max. possible Tilt of 
 the copter to maintain level flight (neglecting down force due 
 tilt).
max Speed: Theoretically max. attainable forward speed 
 in flight at max. tilt and max throttle (neglecting copter aerodynamic drag and down force 
 due tilt). With restricted tilt that my result in a climb.

 est. Range: represents the max Range considering 
 standard drag. Real values may differ depending on the real drag.

 est. rate of climb: estimated maximum 
 achievable rate of climb (neglecting copter aerodynamic drag).

 Total Disc Area: The total disc area is the area 
 covered y rotors when looking from the top to the copter. The 
 higher the disc area the more efficient the copter gets.
with Rotor fail: Prediction of the 
 resulting controlability of your multicopter in case of a 
 rotor/engine failure (r = number 
 of rotors):

 [img alt='resistant']Resistant 
 to single Rotor Failure: your configuration has 6 rotors or more 
 and hovering is possible with less than 80% throttle assuming the 
 opposite engine is not required   for lift (equal to two 
 engine failures on opposit engines, r-2). 
Or, your configuration 
 has 5 rotors and hovering is possible with less than 66% throttle 
 on remaining motors (r-1).

 [img alt='conrtolable']Single 
 Rotor Failure is most probable controlable for a 
 immediate emergency landing. However if the asymetry is to big due 
 weight  distribution or wind the copter might still get uncontrolable. Your 
 configuration has 5 rotors or more and hovering 
 is possibible with 66% to 80% throttle on remaining motors (r-1).

 [img alt='uncontrolable']A 
 single 
 Rotor Failure is uncontrolable and will lead to 
 a flip-over. your configuration has 4 or less rotors  or 
 hovering 
 needs more than 80% throttle on remaining motors (r-1).

 Remark: We remind you this is a prediction only - 
 to be sure regarding resistancy you have do disable one motor and 
 try to safely take off to hover.
It is in the nature of any Quad- or Tre-Copter that a 
 rotor failure will lead to a flip-over. 

Range Estimator:
The Range Estimator 
 gives you a relative value of the expected range in still air 
 on a level flight of a copter as so far the 
 translational lift is not yet considered. You may typically expect a 
 range (green) between the two graphs of «No Drag Range» (theoretical 
 maximum without drag) and «Std Drag Range» (Range using a average drag 
 assumption wid Cd=1.3) or even more when flying in the sweet spot of 
 translational lift. As this is a rought basic assumption, the range may also 
 be lower than the Standard Drag Range at higher Speed. The far end of the range graph 
 is equal to the max. speed in level flight.
Average Drag Assumption (blue): 
 the center hub is as big as the biggest possible prop will fit to the 
 defined symetric frame size. The arms are 2.5cm/1inch wide and the 
 copter is 10cm/4inch high. If your copter is bigger the real range / 
 top speed (red vertical marker) will be less.

 [img alt='']

 stadard drag = blue area
Motor Characteristics:

 The Diagram shows the full thrust parameters with increasing current 
 (Dyno Test) with marked maximum values. The
 estimated Motor Case Temperature will turn red as soon as it goes
 over 80°C. Higher Motor Case Temperature can result permanent Damage. 

 |  
 | 
Der Umgang mit
 den Resultaten

Alle Resultate basieren auf dem angezeigten 
 Abfluggewicht.

Kurzanalyse:
Einige Parameter werden zusätzlich als 
 Messuhr angezeigt um einen schnellen überblick der Berechnung zu 
 erlangen.

Entladerate: Entladerate der Batterie
- 
 grün: Dauer-Entladerate
- gelb: Bereich bis max. Entladerate

 - rot: ausserhalb der Limite

Flugzeit Schweben: Erfahrungswerte

Temperatur (ca.): erwartete 
 Maximal-Temperatur
- grün: normaler Bereich 0…70°C
- gelb: 
 Kritischer Bereich 70…90°C
- rot: ausserhalb der Limite, 
 Überhitzungsrisiko

el. Leistung / Strom: Maximal-Wert in 
 Relation zur spezifizierten Motorenlimite (max 15s) in Watt oder 
 Ampere.
- grün: bis 70% der Limite
- gelb: Kritischer 
 Bereich 70% bis zur Limite
- rot: ausserhalb der Limite, Risiko 
 für Beschädigungen

Schub-Gewicht (-Verhältnis): Indikator für 
 Flugverhalten (je höher desto agiler)
- grün: 1.8 und höher 
 (Gasstellung < 60%)
- gelb: Schweben 1.2 bis 1.8 (Gasstellung 
 60…80%) – Eingeschränkte Wendigkeit
- rot: Schweben mit 1.2 und 
 tiefer ist kaum möglich

Spez. Schub: Der spezifische Schub am 
 Propeller ist ein Indikator für die Schwebe-Effizienz
- grün: 
 6g/W und mehr sind gute Werte
- gelb: 4…6g/W sind bescheidene 
 Werte
- rot: unter 4g/W sind unbrauchbar

Anmerkung:

 Der Calculator überwacht die max. zulässigen Ströme bzw. Leistung der Komponenten und gibt bei entsprechender Überschreitung eine Warnung an
 sie. Dies sind KEINE Fehlermeldungen, sondern 
 Warnungen, wo allenfalls Probleme zu erwarten sind. Blau Warnungen 
 sind informativ, rote sind kritisch.
Die max. physikalische Drehzahl wird nicht
 überwacht. 
Bitte beachten Sie immer die Herstellerangaben.

Alle Resultate basieren auf dem errechneten Abfluggewicht:

Batterie:

Belastung: Aktuell Akkubelastung im Verhältnis zu
 seiner Kapazität.

 Spannung: Spannung am Akku  bei errechneter Volllast.

 Nennspannung: gemäss Akkubeschriftung
Energie: 
 Gesamtenergie der Batterie
Gesamtkapazität: 
 der Batterie
genutzte Kapazität: die für den 
 Flug nutzbare Kapazität gemäss der gewählten max. Entladung des 
 Akkus. Alle Flugzeiten basieren auf diser entladenen Kapazität.

 Flugzeit Vollast: erwartete Flugzeit mit der gewählten x% 
 Entladung beim Fliegen mit Vollgas und unabhängig vom 
 Abfluggewicht.

 Ø Flugzeit: erwartete Flugzeit mit der gewählten x% 
 Entladung bei 
 Rundflügen basierend auf dem Abfluggewicht.
Flugzeit Schweben: 
 erwartete Flugzeit mit der gewählten x% Entladung nur durch Schweben 
 basierend auf dem Abfluggewicht (Basis ist der geometrische 
 Mittelwert des Stroms).

 Gewicht: des gesamten Akkus

Motor @ Optimaler Wirkungsgrad (Angaben pro Motor!):

Strom: Strom beim maximalen Wirkungsgrad (Dyno Test mit 
 zunehmender Last).

 (restliche Angaben analog unten)

Motor @ Maximum (Angaben pro Motor!):

max Strom: maximal zu erwartender Strom.

 Spannung: Spannung am Motor.

 Drehzahl: Drehzal des Motors unter Last.

 el. Leistung: elektrische Eingangsleistung.

 mech. Leistung: mechanische Ausgangsleistung oder
 Wellenleistung
Leistungs-Gewicht: Verhältnis von Leistung zu Gewicht 
 bei Vollgas.

 Wirkungsgrad: Wirkungsgrad des Motors bei max. Belastung
Temperatur (ca.): geschätzte 
 Gehäusetemperatur  - abhängig von der Motorkühlung. Ab 80°C Gehäusetemperatur läuft der Motor an 
 der Leistungslimite. Temperaturen über 100°C sind kritisch und 
 können zu permanenten Schäden führen.
Rm: 
 Dynamischer Widerstand des Anbtriebs.
Regler: 
 Anzahl der Impulse, die vom Regler abgegeben werden, um die 
 Motordrehzhl zu erreichen (epm = Impulse pro Minute) und 
 entspreicht der magnetischen Drehzahl. Regler sind 
 limitiert in der maximalen Anzahl Impulse pro Minute. eCalc 
 überwacht diese Limit nicht. Sie liegt oft im bereich von 200'000 
 bis 500'000 epm. 

Wattmeter-Messung:

Ausgabe der Strom-, Spammungs- und 
 Leistungswerte, wie sie an einem Wattmeter oder Logger erscheinen bei 
 einer Standmessung. Für eine optimale Vergleichbarkeit mit frisch 
 geladenen Akkus, wählen Sue unbeding den Batterie Ladezustand «voll».

Motor @ Schweben (Angaben pro Motor!):

 Die Schwebe-Berechnung wird mit einem 
 Durchmesser-Steigungs-Verhältnis von über 0.667 ungenauer. Daher 
 wird bei extremen Auslegungen die Berechnung nicht angezeigt.

 Für Race Kopter mit Propeller unter 6.5" wird auf 
 grossen Wunsch in jedem Fall ein Resultat angezeigt. Sind Sie sich 
 Bewusst, dass die Genauigkeit in diesemFall aber reduziert ist

Strom: erwarteter Strom zum Schweben. Für eine effiziente 
 Auslegung solle dieser möglichst beim optimalen Strom (vgl. oben) 
 oder leicht darunter liegen.

 Spannung: Spannung am Motor
Drehzahl: 
 Propeller Drehzahl zum schweben.

 Regleröffnung(log): Einige Regler zielen auf eine lineare 
 Leistungs- bzw. Schubentfaltung. Diese Regleröffnung zum Schweben - ist 
 äquivalent zur Schwebe-Gas-Position in Manual Mode mit einer 
 logarithmischen PWM Kurve des Reglers mit Leistungs-/Schublinearität.
Anmerkung: Da die 
 logarithmischen Kurven ja nach Hersteller abweichen können, ist dies 
 ein Erfahrungswert. 

 Regleröffnung(linear): Konventionelle Regler zielen auf eine 
 lineare Drehzahlentfaltung. Diese Regleröffnung zum Schweben - ist 
 äquivalent zur Schwebe-Gas-Position in Manual Mode mit einer 
 linearen PWM Kurve des Reglers mit Drehzahllinearität. Somit beteutet 60% Regleröffnung, 
 dass die PWM den FET zeitlich 60% ein- bzw 40% ausgeschaltet lässt 
 und damit linear zur anliegenden Motorspannung ist.

 Anmerkung: Verwechseln Sie diesen Wert nicht mit der PWM Zeit welche 
 in einigen Flight Control Logs in μsec ausgewiesen wird.
el. Leistung: elektrische Eingangsleistung.

 mech. Leistung: mechanische Ausgangsleistung oder
 Wellenleistung.
Leistungs-Gewicht: Verhältnis von Leistung zu Gewicht 
 beim Schweben. Fausregel: ~150W/kg, sehr effiziente auslegungen 
 bringen diesen Wert bis ca. 80W/kg runter.

 Wirkungsgrad: Wirkungsgrad des Motors beim Schweben.

 Temperatur (ca.): Vorhersage der Motorentemperatur 
 - abhängig von der Motorkühlung.

 spezifischer Schub: Wie viel Gramm Auftrieb kann der Propeller pro Watt
 Eingangsleistung erzeugen. 

Gesamter Antrieb:

Komponenten: Gewicht aller komponenten mit 10% Zuschlag 
 (z.B. für Luftschraube).

 Schub-Gewicht: Verhältnis von Schub zu Gewicht 
 - fliegen mit weniger als 1.2 ist beinahe unmöglich.

 max. Zuladung: maximal 
 mögliche Zuladung um mit 80% liearer
 Regleröffnung mit Reserve zum Manöverieren zu schweben (Empfehlung 
 für  Akro <50%, für Foto <80%).
Gesamtstrom @ 
 Schweben: Gesamtstrom aller Motoren beim Schweben

 P(in) @ Schweben: elektrische Eingangsleistung  beim 
 Schweben

 P(out) @ Schweben: mechanische Ausgangsleistung  beim 
 Schweben

 Wirkungsgrad @ Schweben: Gesamtwirkungsgrad des Antriebs  
 beim Schweben.
Gesamtstrom @ max: Gesamtstrom aller Motoren 
 bei Vollgas

 P(in) @ max: elektrische Eingangsleistung bei Vollgas

 P(out) @ max: mechanische Ausgangsleistung bei Vollgas

 Wirkungsgrad @ max: Gesamtwirkungsgrad des Antriebs bei 
 Vollgas.

Multikopter:

Abfluggewicht: berechnetes aktuelles Fluggewicht (inklusive Komponenten, die 
 max. Zuladung wird NICHT berücksichtigt). Alle Berechnungen 
 basieren auf diesem Abfluggewicht.
max. Zuladung: maximal 
 mögliche Zuladung um mit 80% liearer
 Regleröffnung mit Reserve zum Manöverieren zu schweben (empfohlene 
 maximale (!) Regleröffnung 
 für  Akro <50%, für Foto <80%).
max. 
 Neigung: maximale Neigung des Kopters um noch horizontal 
 zu fliegen (nicht berücksichtigt ist Abtrieb durch die Neigung).

 max. Geschwindigkeit: Theoretisch erreichbare 
 Horizontal-Geschwindigkeit bei max. Neigung und Voll-Gas (nicht berücksichtig sind 
 aerodynamischer Widerstand und Abtrieb durch die Neigung). Mit 
 eingeschänkter Neigung führt die zum Steigen.
gesch. 
 Reichweite: entspricht der max. Reichweite unter 
 Berücksichtigung des Standard-Luftwiderstand. Die effektiv 
 errreichbare Reichweite hängt vom realen Luftwiderstand des 
 Kopters ab.
gesch. Steigleistung: 
 geschätzte maximal erreichbare Steigleistung / Steigrate (nicht 
 berücksichtig sind aerodynamischer Widerstand des Multikopters).

 Rotorfläche: die durch alle Rotoren gebildete 
 Grundfläche, wenn senkrecht auf den Kopter geschaut wird. Je höher 
 die Rotorfläche, desto effizienter wird ihr Kopter.

 mit Rotorausfall: Vorhersage über die Steuerbarkeit des 
 Multikopters bei Ausfall eines Motors (r = Anzahl Rotoren):

 [img alt='resistant']Resistent 
 gegen Rotorausfall: der Kopter hat 6 oder mehr Rotoren und das 
 Schweben mit den verbleibenden Motoren ist mit weniger als 80% Gas 
 möglich unter der Annahme, das der gegenüberligende Motor keinen 
 Schubanteil liefert (gleichbedutend mit doppeltem 
 gegenüberliegendem Motorausfall, r-2).
ODER, der Kopter hat 5 
 Rotoren und Schweben mit den verbleibenden Motoren ist mit 66% 
 Gas oder weniger möglich (r-1). 

 [img alt='conrtolable']Ein 
 Rotorausfall ist mit hoher Warscheinlichkeit 
 kontrollierbar für eine umgehende Notlandung. Bei grosser 
 Asymetrie (Gewichtsverteilung oder Wind) ist dennoch ein Kontrollverlust 
 möglich.
Ihr Kopter hat 5 oder mehr Rotoren und Schweben ist 
 mit den verbleibenden Motoren (r-1) mit 66% bis 80% Gas möglich. 

 [img alt='uncontrolable']Ein 
 Rotorausfall führt zu einem Kontrollverlust.
Ihr Kopter hat 4 
 oder weniger Rotoren oder zum Schweben mit den Verbleibenden 
 Motoren (r-1) ist mehr als 80% Gas nötig.
Anmerkung: 
 Dies ist nur eine rechnerische Vorhersage - um 
 Gewissheit darüber zu erlangen deaktivieren Sie einen Motor und 
 versuchen sie sicher zu starten bzw. zu schweben.
Es 
 liegt in der Natur eines Quad- bzw. Tre-Copters, dass ein 
 Rotorausfall unweigerlich zum Absturz führt.

Reichweiten Abschätzung:
Die 
 Reichweiten-Abschätzung ist eine relative Berechnung der zu 
 erwartenden Reichweite (grün) ohne Wind im Flug auf konstanter Höhe. 
 da der Übergangsauftrieb (translational lift) nicht berücksichtigt 
 wird. Sie können typischerweise eine Reichweite zwischen «Reichweite ohne 
 Luftwiderstand» (theoretisches Maximum) und «Reichweite mit 
 Standard-Luftwiderstand» (Annahme basiert auf einer üblichen 
 Kopterform und Cd=1.3) erzielen oder im Idealfall gar mehr. Da die Kopterform start variieren kann, können 
 durch höheren Luftwiderstand bei hoher geschwindigkeit auch geringere Werte erzielt werden. 
 Das ende der Reichweiten-Kurve entspricht der max. 
 Horizontal-Gescheindigkeit.

 Annahme Standard-Luftwiderstand (blau): Die zentrale Plattform ist 
 gerade so gross, dass auf einem symetrischen Rahmen die maximale 
 Propeller-Grösse angebracht werden kann. Die Arme sind 2.5cm/1inch 
 breit und der Kopter ist 10cm/4inch hoch. Is ihr Multikopter 
 grösser, wird die Reigweite und die Höchstgeschwindigkeit (rote 
 Markierung) tiefer ausfallen.

 [img alt='']

 Standard-Luftwiderstand = blaue Fläche

Motorenkennlinie:

 In der Motorgrafik zeigt die Vollgas-Kennlinien mit zunehmendem 
 Strom (Dyno Test). Die maximalwerte sind markiert. Die erwartete
 Motorgehäusetemperatur springt von grün auf rot, sobald 80°C
 überschritten wird. Eine Gehäusetemperatur von über 80°C kann
 den Motor permanent schädigen.

 | 

 | 

 | 
Hints &
 Tips

Too long wire kills your ESC 
 - still #1 cause for burned ESC

...still working on that...

 |  
 | 
Auslegehilfen

Tödliche Kabelverlängerung am Regler - 
 Hauptursache für Reglerversagen

...wir arbeiten noch daran..

 | 

Vortex Ring State 
 (blade stall due downwash)

 During a vertical descent any copter may settle into its own 
 downwash. This may lead to a severe flight condition as the 
 propeller blade may start to stall and the produced lift will drop 
 dramatically and the descent rate cannot be reduced anymore. A total 
 loss of control may be the result. This 
 phenomenon is called Vortex Ring State (VRS).

How to avoid VRS?

The vortex ring state can be completely avoided by descending 
 on flightpaths shallower than 30 degrees (at any speed).

At steep angles (e.g. vertical), the vortex ring wake remains 
 below the copter at slow rates of descent.

Approach your landing site against the wind - tail wind 
 increases the risk to enter the own downwash.

High pitch propellers increase the risk of vortex ring state 
 considerable. (rule of thumb: pitch shall be less than 66% of the 
 prop diameter – the lower the pitch the smaller the risk for VRS)

Recognition and escape VRS
The copter pilot can 
 recognize entering the VRS by a wobbling copter. Immediately 
 start to move in any horizontal direction (e.g. forward) to get out of 
 the vortex ring wake and reduce your rate of descent.

See a demonstration of
 Vortex Ring 
 State (at 2min 25s) at youtube...

 |  
 | 

Wirbelringstadium (Schubverlust durch eigenen 
 Abwind)
Während eines vertikalen Sinkfluges kann jeder Kopter in 
 seinen eigenen Abwind geraten, was zu einem dramatischem Schubverlust 
 führt und der Sinkflug kaum noch gestoppt werden kann. daraus kann ein 
 kompletter Kontrollverlust entstehen. Dieses Phänomen nennt man 
 Wirbelringstaduim oder engl. Vortex Ring State (VRS).

Wie kann man VRS vermeiden?

VRS kann komplett vermieden werden, wenn der Sinkwinkel des 
 Kopters geringer als 30° ist.

Bei steilen Sinkwinkel und geringen Sinkraten bleibt der 
 gefärliche Wirbelring unter dem Kopter.

Fliegen Sie Ihren Landeplatz immer gegen den Wind an - 
 Rückenwind erhöht das Risiko in den eigenen Abwind zu geraten.

Luftschrauben mit hohen Steigungen erhöhen das Risiko deines 
 eintrettenden Wirbelringstaduim. (Faustregel: Die 
 Propeller-Steigung sollte geringer als 66% des Durchmessers - je 
 geringer die Steigung desto kleiner wird das Risiko von 
 Wirbelringstaduim.

Erkennen und Entkommen von VRS
Der Kopterpilot 
 erkennt ein bginnendes Wirbelringstadium durch einen 
 schlingernden/wackelnden Kopter. Leiten Sie unverzüglich 
 eine horizontale Bewegung (z.B. forwärts) ein und verringern Sie die 
 vertikale Sinkrate, damit der Kopter aus dem eigenen Abwind 
 herausfliegt.

Eine eindrückliche Demonstation von
 Vortex Ring 
 State (bei 2min 25s) finden Sie auf youtube...

 | 
 [img alt='']

 |  
 | 
 [img alt='']

 [img alt='']

 Quelle: http://www.copters.com/aero/settling.html

 | 

 | 

hover efficiency - flat vs. coax configuration
most muticopter 
 pilot beleve that a flat setup is about 20-30% more efficent than a coax 
 configuration.
This is true if we do a propeller-based comparison 
 of a given 
 motor-prop combination in flat and coax configuration. BUT this does 
 not compare equal disk area and the better flat efficiency results from the fact the flat 
 configuration has 
 twice the disk area of a coax!

 What if we are talking in terms of frame size?
If we compare 
 coax vs. flat on a given frame size the efficiency 
 is much higher with a coax configuration. Why?

due blade clearance of a flat is less than coax - therefore 
 the flat must use much smaler props.

as coax can use much bigger props. the disk area is about 50% 
 higher than a flat configuration on the same frame size. The 
 higher the disc area the more efficient is hovering.

further more bigger and therefore slower turning props are more 
 efficient.

Tre- and Quad-Fames have a much higher rotor area-fill than Hexa 
 or Octo

 |  
 | 

Schwebe-Effizienz - flache vs. coaxiale Auslegung
Die meisten 
 Multikopterpiloten verfallen dem Trugschluss, dass flache Auslegungen 
 rund 20-30% effizienter sind als coaxiale.
Dies trifft nur zu, wenn wir 
 von einer gebenen Motor-Propeller-Kombination ausgehen und diese als 
 flache bzw. coaxiale Anordnung vermessen. Aber dieser Vergleich 
 basiert nicht auf der gleichen Rotorfläche sondern ist vielmehr das 
 Resultat der doppelten Rotorfläche einer flachen Konfiguration!
Aber wie verhält sich 
 das, wenn wir von einer gegebenen Rahmengrösse ausgehen?
Wen wir 
 nun die beiden Auslegungen basierend auf einer bestehenden 
 Rahmengrösse betrachten, ist die coaxiale Auslegung wesentlich effizienter: Warum?

Der Propeller-Freiraum ist bei der flachen Auslegung geringer. 
 Es müssen kleinere Propeller gewählt werden.

dagegen kann bei einer Coax-Auslegung wesentlich grössere 
 Propeller verwendet werden. Daraus resultiert ca. 50% mehr 
 Rotorfläche!

des Weiteren sind grössere und daruch langsamer drehende 
 Propeller effizienzer.

Y6 Tre- und X8 Quad-Rahmen haben eine bessere 
 Flächenausnützung als Hexa oder Octo

 | 
 [img alt='flat vs. coax rotor area'] 

 same frame size - left coax X8 with large props, right 
 flat Octo with smaller props  (drawing by Robert Lefebvre)

 | 

 | 

max Propeller size with zero tip clearance for symetric frames:

 - for flat Octo: max. Prop Diameter ~ 0.383 x frame size
- for flat 
 Hexa: max. Prop Diameter ~ 0.5 x frame size
- for coax X8: max. 
 Prop Diameter ~ 0.707 x frame size
- for coax Y6: max. Prop 
 Diameter ~ 0.866 x frame size

The size of the frame is defined by the distance of the two 
 opposite motors (X) or double the arm length from center to motor (Y). 

Conclusion: on a given frame optimized Y6 or X8 
 coax configuration has a better efficiency than a flat hexa/octo 
 configuration due higher total disk area. A coax having even a 
 better redundancy against a single engine failure as the disk area 
 stays unchanged as long as the remaining motor can take-over the full 
 load....
The key to best hover efficiency is low copter 
 weight with maximum disk size.

optimizing coax efficency:
Are you using same 
 props on top and bottom? Then you might optimize your efficiency of 
 your coax copter upto ~5%:
Power: The power 
 distribution between upper and lower motor shoul be about 50%.

 Diameter:  a 
 variation on the upper propeller’s diameter has almost no influence in 
 the efficiency of a coaxial propulsion system. Contrarily, increasing 
 the lower propeller’s diameter proved to increase the efficiency of a 
 coaxial system, while decreasing it resulted in a decrease of 
 efficiency of a coaxial system.
Pitch: a variation 
 on the upper propeller’s pitch resulting in a decrease of the 
 efficiency of a coaxial system. A decrease on the lower propeller’s 
 pitch results in a decrease of the efficiency of a coaxial system 
 while an increase on the lower propeller’s pitch results in an 
 increase of the efficiency of a coaxial system.
As a starting point 
 the lower prop should (roughly) be 1.5" higher pitched at same 
 diameter or about 1 inch wider (i.e 14x4.8 and 13x6 / 14x6 as an example).
If that is not 
 possible, the lower prop has to spin faster than the top prop. 
 Otherwise it will just freewheel. And this is also where you loose 
 quite a bit of efficiency dues to more drag when increasing the rpm.

General:
Running en electric Motor below his optimal efficiency current
 results in a faster increase of wast power than running it over this
 point.
PConst: The Propeller Constant
 indicates its degree of  the power absorbed by the prop due
 aerodnamic resistant. In general the thinner a prop blade is the
 lower the Prop Const gets. A typical Prop Const is between min. 1.00
 and 1.15 (max. 2.00). Pconst may be derived from 
 Propeller Data: Pconst 
 ~ 1+CP0

TConst: This value is normaly 1.0. The thrust of 
 some (few) propellers need the be adjusted and will be used for 
 finetuning only.
 |  
 | 

max Propeller-Grösse für symetrieche Rahmen:
- für flachen 
 Octo: max. Prop Durchmesser ~ 0.383 x Rahmengrösse
- für flachen 
 Hexa: max. Prop Durchmesser ~ 0.5 x Rahmengrösse
- für coaxial 
 X8: max. Prop Durchmesser ~ 0.707 x Rahmengrösse
- für coaxial 
 Y6: max. Prop Durchmesser ~ 0.866 x Rahmengrösse

Die Rahmengrösse ist definiert durch die Distanz zwischen den 
 gegenüberliegenden Motoren (X) oder die doppelte Armlänge vom 
 Zentrum zum Motor.

Fazit: Bei gegebenem Rahmen erreichen optimale Y6 und X8 
 Auslegungen (Coax) bessere Wirkungsgrade als flachen 
 Konfiguration bedingt durch die 
 höhere Rotorfläche. Sie haben gar die bessere Redundanz, da bei 
 einem Motorausfall die Rotorfläche unverändert bleibt (solange der 
 verbleibente Motor die gesamte Last übernehmen kann)....

 Der Schlüssel zu bester Schwebe-Effizienz ist ein geringes 
 Koptergewicht mit maximaler Rotorfläche.

Optimierung der Coax Effizienz:
Verwenden Sie 
 zwei gleiche Propeller? Dann können Sie den Wirkungsgrad Ihres 
 Coax-Antrieb bis 5% steigern:
Leistung: DieLast 
 des Motors sollte gleichmässig auf oben und unten verteilt sein.

 Durchmesser: Veränderungen des oberen Props hat kaum 
 einfluss auf die Effizienz. Hingegen wird die Effizienz erhöht mit 
 einem leicht grösseren Prop unten.
Steigung: 
 Veränderungen am oberen Prop führt zu einer schlechteren Effizienz. 
 Verringerung der Steigung am unteren Prop verringert die Effizienz, 
 eine Erhöhung verbessert die Effizienz.
Als 
 Ausgangpunkt verwenden Sie für den unteren Prop eine um ca. 1.5" 
 höhere Steigung bei gleichem oder leicht grösserem Durchmesser (z.B. 13x4.8 and 
 13x6 / 14x6 
 as an example).
Sollte das nicht möglich sein, muss der untere 
 Prop eine höhere Drehzahl haben als der obere - sonst dreht er 
 beinahe im leeren. Meist wird in diesem Bereich am meisten 
 Wirkungsgrad vergeben....

Generell:

Der Betrieb eines Elektromotors unter seinem optimalen
 Wirkungsgrad führt zu einer überproportionalen Zunahme der
 Verlustleistung.

PConst.: Die Propeller Konstante ist ein Mass für
 die Leistungsabsorbtion des Propellers durch seinen aerodynamischen
 Widerstand. Allgemein gesagt: Je dünner ein Propellerblatt ist je
 kleiner fällt seine Konstante aus. Prop Konst liegt zwischen min.
 1.00 und 1.15 (max. 2.00). Pconst kann auch aus
 Propeller 
 Datensammlungen abgeleited werden.: Pconst ~ 1+CP0

TConst: Dieser Wert ist typischerweise 1.0. Die 
 Schubentwicklung vereinzelter Propeller kann damit zur 
 Feinabstimmung angepasst werden.

 | 

 | 

copyright  by Solution for All Markus Müller

 www.ecalc.ch  email: info[at]ecalc.ch
