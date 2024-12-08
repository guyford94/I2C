# I2C Protocol Example with Pyboard as Slave

This example demonstrates the use of I2C communication between a master device and a Pyboard acting as a slave. The protocol involves the slave receiving messages from the master in the form of 3 characters. Based on the received characters, the slave responds accordingly.

Additionally, the slave can receive numerical values separated by asterisks (`*`) to update predetermined values.

## Protocol Overview

The Pyboard acts as the **slave** in this communication, while the **master** sends messages to it. Here's the table of the protocol:

| **Master Message** | **Message Explanation**                                      | **Slave Response**      |
|--------------------|--------------------------------------------------------------|-------------------------|
| RTT                | Start connection with master                                 | RTR                     |
| INI                | Check of equipment                                           | OK_                     |
| BNG                | Start of session                                             | RDY                     |
| CHK                | Checksum                                                     | Checksum + zeros to complete for 3 characters |
| OK_                | Verify connection                                            | ACK                     |
| ERR                | Error                                                        | ACK                     |
| WFU                | Waiting for confirmation that the update worked             | EWF                     |
| EOS                | End of data transmission                                     | EOS                     |
| END                | End of connection                                            | ACK                     |

## How It Works

1. **Master to Slave**: The master sends a message in the form of 3 characters (e.g., `RTT`, `INI`, etc.) to the Pyboard slave.
2. **Slave Response**: The slave responds to each command based on the received message.
3. **Update Values**: The master can send numerical data in the format of `value*value*value`, where values are separated by an asterisk (`*`). These values are used to update predetermined variables in the slave device.
