import os

XX = os.getcwd()
CLAN = str(XX)
cc =CLAN.replace('CASPER', '')

os.system('chmod +x CASPER.sh')
os.system(f'cd {cc} && cp -r CASPER /root')
os.system('mv CASPER.sh /bin/CASPER')

print('Done ... ')
