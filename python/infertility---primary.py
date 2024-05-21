# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"K26..00","system":"readv2"},{"code":"54282.0","system":"readv2"},{"code":"36264.0","system":"readv2"},{"code":"32485.0","system":"readv2"},{"code":"99607.0","system":"readv2"},{"code":"4520.0","system":"readv2"},{"code":"1615.0","system":"readv2"},{"code":"61954.0","system":"readv2"},{"code":"38990.0","system":"readv2"},{"code":"3331.0","system":"readv2"},{"code":"5292.0","system":"readv2"},{"code":"7273.0","system":"readv2"},{"code":"102597.0","system":"readv2"},{"code":"102703.0","system":"readv2"},{"code":"58858.0","system":"readv2"},{"code":"766.0","system":"readv2"},{"code":"N46","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('male-infertility-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["infertility---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["infertility---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["infertility---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
