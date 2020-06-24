#! /bin/bash
GAMING_TEXT=0
STEP_GAMING=0
STEP_OLD=0
STEP=0
while :
do 
    gn=1
    temp=$(sensors | grep mem: | sed 's/[^0-9]*//g'|  tr -d ' ')
    echo=$((temp=temp/100000000))
    if [ $temp -lt 38 ]
    then
    	STEP=1
    	FAN_PERCENT=10
    elif [ $temp -lt 50 ]
    then
    	STEP=2
    	FAN_PERCENT=20
    elif [ $temp -lt 58 ]
    then
    	STEP_GAMING=1
    	STEP=3
    	FAN_PERCENT=35
    elif [ $temp -lt 70 ]
    then
    	STEP_GAMING=2
    	STEP=4
    	FAN_PERCENT=70
    	gn=5
    	#echo " "
    	#echo " "
    	#echo "Temperature is over $temp Celcius"
    	#echo "I'm going to sleep for $gn seconds"
    elif [ $temp -lt 80 ]
    then
    	STEP_GAMING=3
    	STEP=5
    	FAN_PERCENT=90
    	echo " "
    	echo " "
    	echo "THIS IS NOT NORMAL"
    	echo "Temperature is over $temp Celcius"
    	#echo "I'm going to sleep for $gn seconds"
    	gn=2
    else
    	FAN_PERCENT=100
    	gn=60
    fi
    GAMING_TEXT=$STEP_GAMING
    if [ $STEP_GAMING -gt 0 ]
    then
    	if [ $STEP_OLD -gt $STEP ]
    	then
    	#echo "Gaming Step $STEP_GAMING is active, ignoring Step $STEP"
    	STEP=$((STEP+1))
    	GAMING_TEXT=$((STEP_GAMING))
    	STEP_GAMING=0
    	fi
    fi
    if [ $STEP -eq $STEP_OLD ]
    then
    	true
    else
    	sh ./amdgpu-pro-fans.sh -s $FAN_PERCENT
    	#echo "Level $STEP is using now"
    fi
    now=$(date +"%T")
    echo " #################"
    echo "# Temperature:" $temp "#"
    echo "# Fan speed:  " $FAN_PERCENT "#"
    echo "# Step:       " $STEP       " #  ########## "
    echo "# Gaming Step:" $GAMING_TEXT"  # # "$now" #"
    echo " #################   ########## "
    echo " "
    sleep "$gn"
    STEP_OLD=$((STEP))
done
