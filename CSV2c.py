#!/bin/python

def conversion():
    # File converting from
    with open("TAS.csv","r") as input:
        # File converting to
        with open("TAS.h","w") as output:
            #setup file
            output.write("/*")
            output.write("         Keith's Sweet Header File\n")
            output.write("     Copyright (C) Keith Lynd, 2019.\n")
            output.write("\n")
            output.write("     klynd [at] rocketmail [dot] com\n")
            output.write("            www.headripper.com\n")
            output.write("*\ \n")
            output.write("\n")
            output.write("// inputs list\n")
            output.write("USB_JoystickReport_Input_t Inputs[] = {\n")
            # skip first 3 lines of instruction
            input.readline()
            input.readline()
            input.readline()
            # remove whitespace and put into list called 'frame'
            for line in input:
                line = line.strip()
                frame = [x.strip() for x in line.split(",")]
                outputLine = ""
                stuffToOr = []
                #for each row in csv after
                for press in frame:
                    if press == "Y":
                        stuffToOr += ["0x01"]
                    elif press == "B":
                        stuffToOr += ["0x02"]
                    elif press == "A":
                        stuffToOr += ["0x04"]
                    elif press == "X":
                        stuffToOr += ["0x08"]
                    elif press == "L":
                        stuffToOr += ["0x10"]
                    elif press == "R":
                        stuffToOr += ["0x20"]
                    elif press == "ZL":
                        stuffToOr += ["0x40"]
                    elif press == "ZR":
                        stuffToOr += ["0x80"]
                    elif press == "MINUS":
                        stuffToOr += ["0x100"]
                    elif press == "PLUS":
                        stuffToOr += ["0x200"]
                    elif press == "LCLICK":
                        stuffToOr += ["0x400"]
                    elif press == "RCLICK":
                        stuffToOr += ["0x800"]
                    elif press == "HOME":
                        stuffToOr += ["0x1000"]
                    elif press == "CAPTURE":
                        stuffToOr += ["0x2000"]
                    else:
                        pass
                buttons = 0x00
                for item in stuffToOr:
                    try:
                        buttons = buttons | int( item, base=16)
                    except:
                        pass

                outputLine += hex(buttons) + ","
                outputLine += "HAT_CENTER" + ","
                outputLine += frame[0] + ","
                outputLine += frame[1] + ","
                outputLine += frame[2] + ","
                outputLine += frame[3] + ","
                outputLine += "0"

                output.write("  {" +outputLine + "}" + "\n")
            output.write("}\n")
            output.write("\n")
            output.write("#endif")

def main():
    conversion()

main()