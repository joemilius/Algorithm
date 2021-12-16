var mergeTwoLists = function(l1, l2) {
    let dummyHead = new ListNode(0);
    let currentNode = dummyHead; 

    while(l1 !== null && l2 !== null){

        if(l1.val < l2.val){
            currentNode.next = l1;
            l1 = l1.next
        } else {
            currentNode.next = l2
            l2 = l2.next
        }
        console.log(currentNode)
        currentNode = currentNode.next
        console.log(currentNode)
    }

    if(l1 !== null) {
        currentNode.next = l1;
    } else if (l2 !== null) {
        currentNode.next = l2
    }
    console.log(dummyHead)

    return dummyHead.next
}