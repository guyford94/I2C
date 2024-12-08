# I2C
Example of using I2C with Pyboard
Protocol between 2 devices when the Pyboard is the slave
The slave receives a message from the master in the form of 3 characters.
And according to the letters it receives, it responds to the master
In addition, information can be sent as digits to update certain predetermined values ​​separated by "*"

| **Master Message** | **Message Explanation**                                      | **Slave Message**   |
|--------------------|--------------------------------------------------------------|---------------------|
| RTT                | Start connection with master                                 | RTR                 |
| INI                | Check of equipment                                           | OK_                 |
| BNG                | Start of session                                             | RDY                 |
| CHK                | Checksum                                                     | Checksum + zeros to complete for 3 characters |
| OK_                | Verify connection                                            | ACK                 |
| ERR                | Error                                                        | ACK                 |
| WFU                | Waiting for confirmation that the update worked             | EWF                 |
| EOS                | End of data transmission                                     | EOS                 |
| END                | End of connection                                            | ACK                 |

