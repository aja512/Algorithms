// c++
	void traverse()
	{
	   Node* curr = head ;     // in starting curr points(refer) to head
	   Node* prev = NULL ;     // in starting previous is null
	   // for forward travesal
	   while (curr != NULL)    // while not reached end of list
	   {
		  cout << curr->data << ' ';            // print curr data
		  Node *next = XOR(prev, curr->np_ptr); // to get next node
		  prev = curr ;                         // storing curr as prev
		  curr = next ;                         // storing next as curr
	   }
   
	   cout << endl ;         // only for formattig output
	   // for backward traversal
	   // prev is pointing to last node after first while loop and
	   // curr is NULL after first while loop
		while (prev != NULL)   // till we reach before start of list
	   {
		  cout << prev->data << " ";             // print prev data
		  Node *next = XOR(curr, prev->np_ptr);  // to get next node
		  curr = prev ;                          // storing prev as curr
		  prev = next ;                          // storing next as prev
	   }
	}
