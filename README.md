# I2C
Example of using I2C with Pyboard
Protocol between 2 devices when the Pyboard is the slave
The slave receives a message from the master in the form of 3 characters.
And according to the letters it receives, it responds to the master
In addition, information can be sent as digits to update certain predetermined values ​​separated by "*"

Table of use of the protocol
master 		message	Explanation of the message	              	slave massge
RTT		    start connection whit master			                  RTR
INI		    Check of equipment			                          	OK_
BNG	    	Start of session			                            	RDY
CHK		    checksum					                                  checksum + zeros to complete for 3 characters
OK_		    verify connection				                            ACK
ERR		    ERROR				                                	    	ACK
WFU		    Waiting for confirmation that the update worked	    EWF
EOS		    End of data transmission			                      EOS
END		    End of connection				                            ACK
