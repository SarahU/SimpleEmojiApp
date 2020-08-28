**Run:**

Docker port: 5000

**Test Inputs:**

'3 :thumbsup: -n 2 -s *' - returns '👍*👍*👍*👍*👍*👍'

'THREE :thumbsup:' - returns 'Unknown command: THREE :thumbsup:'

From netcat: echo -n "3 :thumbsup: -n 2 -s *" | netcat -u localhost 5000


**Decisions:**

ANY exceptions caught will return an unknown error. Did not cater for return the type of the error as that as that wasn't requested and a general error is caught but this could be extended to check for the exact problem with the command

Multiple test cases are missing, especially edge cases.

Note, this was written on a Windows machine