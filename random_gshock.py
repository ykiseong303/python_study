event_list = [
"GWF-A1000BRT-1ADR",
"GM-5600EY-1DR",
"GMW-B5000GD-9DR",
"GMW-B5000D-1DR",
"GMW-B5000G-2DR",
"GW-M5610-1BDR",
"GW-M5610BB-1JF",
"GA-2100-1ADR",
"GA-2100-1A1DR",
"GA-2110ET-8ADR",
"GA-2110ET-2ADR",
"GG-1000-1ADR",
"GG-1000-1A5DR",
"GG-1000-1A3DR",
"SLV-19B-1DR",
"GST-S130BC-1ADR",
"LOV-16C-7DR",
"GST-S130BC-1A3DR",
"GR-B100-1A4DR",
"GR-B100-1A3DR",
"GR-B100-1A2DR",
"GST-B100B-1A4DR",
"GW-5000-1JF",
"GST-B100B-1A3DR",
"GST-B100-1ADR",
"GMW-B5000G-1DR",
"SLV-18B-1DR",
"GMA-S130VC-8ADR",
"LOV-19B-1DR",
"GMA-S130VC-4ADR",
"GMA-B800SC-1A4DR",
"GMA-B800SC-1A2DR",
"GMA-B800SC-9ADR",
"GMA-B800-8ADR",
"GMA-B800-7ADR",
"GD-350-1BDR",
"GBA-800-8ADR",
"GA-400HR-1ADR",
"GA-400GB-1ADR",
"GA-400GB-1A9DR",
"GA-400GB-1A4DR",
"DW-5600BB-1DR",
"GBA-800DG-9ADR",
"GBA-800DG-2ADR",
"GBA-800AT-1ADR",
"GBA-800-3ADR",
"GBA-800-2A2DR",
"GA-110LS-7ADR",
"GA-110LS-1ADR",
"GA-100RS-4ADR",
"GA-100RS-2ADR",
"G-100CU-7ADR",
"DW-5600SC-8DR",
"DW-5600SC-4DR",
"DW-5600SC-2DR",
"DW-5600LU-2DR",
"DW-5600LS-7DR",
"DW-5600LS-2DR",
"DW-5600DN-7DR",
"GW-M5610BC-1DR",
"AWR-M100SDC-1ADR",
"GA-2000SU-1ADR",
"GA-2000S-1ADR",
"GBA-800SF-1ADR",
"GBA-BOOLU-1A1DR",
"GA-2000-1A9DR",
"GA-2000-1A2DR",
"GA-200-1ADR",
"GA-110GB-1ADR",
"GA-110-1BDR",
"DW-9052GBX-1A9DR",
"G-5600E-1DR",
"DW-9052GBX-1A4DR",
"DW-5750E-1DR",
"DW-5750E-1BDR",
"DW-5610SU-8DR",
"DW-5610SU-3DR",
"DW-5600TGA-9DR",
"DW-5600MS-1DR",
"DW-5600BBN-1DR"]

# event_list=["GWF-A1000BRT-1ADR",
# "GM-5600EY-1DR",
# "GMW-B5000GD-9DR",
# "GMW-B5000D-1DR",
# "GMW-B5000G-2DR",
# "DW-5750E-1BDR",
# "DW-5610SU-8DR",
# "DW-5610SU-3DR",
# "DW-5600TGA-9DR",
# "DW-5600MS-1DR",
# "DW-5600BBN-1DR"]

import random

random.shuffle(event_list)
print(event_list)

Winning = random.sample(event_list, 3)
print(Winning)

get_list = []

get_GMW = 0
get_gshock = 0
for x in Winning : 
    if x == "GWF-A1000BRT-1ADR" or x.startswith("GMW-B5000") :
        if x == "GWF-A1000BRT-1ADR" :
            get_list.clear()
            get_list.append(x)
            break
        elif x.startswith("GMW-B5000") and get_GMW == 0:
            get_list.insert(0,x)
            get_GMW += 2
            if get_gshock == 2 :
                get_list.pop()                 
            continue
    elif (get_GMW  + get_gshock) < 3 : 
        get_list.append(x)
        get_gshock += 1 
print(get_list)

