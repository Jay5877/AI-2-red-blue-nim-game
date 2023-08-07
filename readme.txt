-> Name : Jay Shah

-> UTA ID : 1002070971

-> Programming language used : Python 3.10.7

-> Structure of my code: 
   	My entire code is in a single File named red_blue_nim.py
	Then I have wrote 3 functions. 
	1st one is for exploring the possible moves from a given state.
	2nd and 3rd functions are for minimax with alpha beta prunning where only difference is
		3rd is for resource limited or depth limited minimax search.
	After major functions I have class declaration which also have the functions for human move and 
		computer move in itself namely "hmove" and "cmove".
	Following the class initialization is my main nim fucntion where the whole gameplay happens.
	And at the very end is my lines reading commands from terminal/cmd.


-> How to run my code:
	My (.py) file is in zip folder so You need to extract it. Now wherever you extract it
	make sure, that while running the file in CMD pr any terminal the path is set to the location
	where the .py file is.  
	You can call my function using the filename :- red_blue_nim.py
	followed by number of red marble and then the number of blue marbles.
	Then you need to pass the first players command which is as follow
	for computer - "computer"
	for human - "human"
	and at last enter the no of depth upto which you want the minimax search to go.
	Please note:- if no first player will be passed than default player would be computer. 
	But if a wrong input will be given it will exit the code.	
	Command for the depth limited search is set to NONE. And will only become true if, declared in the command line
	arguement by giving the number command. 

	So format of command line arguement for my code is as follow
	
	red_blue_nim.py <num-red> <num-blue> <first-player> <depth>


Thank you!
