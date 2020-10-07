import time
import argparse
my_parser = argparse.ArgumentParser(description='give the mobile number and the sms number')
my_parser.add_argument('mn', metavar='mn',type=str, help='Mobile Number')
my_parser.add_argument('fq', metavar='fq',type=str, help='Numbers Of Sms')
args = my_parser.parse_args()

mn = args.mn
fq = args.fq
time.sleep(10)
with open("ramandahiya.txt","w") as f:
    f.write(f"{mn}{fq}")