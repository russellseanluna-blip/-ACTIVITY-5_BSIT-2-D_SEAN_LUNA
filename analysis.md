Analysis Questions and Answer
Q1: Why does the linked stack push at the head instead of the tail?
The linked stack uses the head when pushing and popping because these operations can be done quickly in O(1) time.
If the tail were used, the program would have to go through the entire list to locate the node before the last one. 
This would take more time, making the process less efficient. Using the head makes the operations easier and faster.

Q2: Why must the array queue be circular?
A circular queue is important because it allows the array to reuse spaces that become empty after removing elements. 
In a regular linear queue, the front index keeps moving forward, leaving unused spaces that cannot be accessed again. 
This may cause a false overflow, where the queue appears full even though there are still available spaces. 
Using the modulo (%) operator allows the front and rear positions to move back to the beginning of the array, 
making better use of memory while keeping enqueue and dequeue operations efficient at O(1) time.
