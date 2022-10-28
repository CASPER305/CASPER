#!/bin/bash

#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root/CASPER && sudo python3 CASPER.py

else

echo 'you must be root ! '
echo 'use sudo'

fi
