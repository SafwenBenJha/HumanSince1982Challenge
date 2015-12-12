#!/bin/bash
#task_slected is variable that allows to check if one of the tasks has been accomplished
task_selected=0
while [ $task_selected = 0 ]
do
	echo -e "Would you like to start task A or task B "
	read  task
	if [ "$task" == "A" -o "$task" == "a" ] ; then
		echo "task A selected."
		mkdir New_Human #create new folder New_Human
		task_selected=1
	else 
		if [ "$task" == "B" -o "$task" == "b" ] ; then
		echo "task B selected."
		rmdir New_Human #delete folder New_Human
		task_selected=1
		else
			echo "Only A or B are accepted"
		fi
	fi
done