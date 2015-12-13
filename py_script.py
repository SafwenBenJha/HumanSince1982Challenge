from subprocess import Popen, PIPE, STDOUT
cmd1 = 'mkdir new_Human1'
cmd2 = 'rmdir new_Human1'
task = raw_input('Would you like to start task A or task B')
if (str(task) == "A" or str(task) =="a"):
	p1 = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
	output = p1.stdout.read()
	print output
	print "done"
#	p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
#	output2 = p1.stdout.read()
#	print output2
else "wrong input"