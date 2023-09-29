class Node{
    int elem;
    Node next;
    Node(int e, Node n){
        elem = e;
        next = n;
    }
}

class LinkedList{

    Node head; //instance variable

    LinkedList(int[] a){
        //write your code here
    }

    public void showList(){
        //write your code here
    }

    public boolean isEmpty(){
        //write your code here
        return true;
    }

    public void clear(){
        //write your code here
    }

    public void insert(int newElement){
        //write your code here
    }

    public void insert(int newElement, int index){
        //write your code here
    }

    public Node remove(int deleteKey){
        //write your code here
        return null;
    }

    public LinkedList evenList(){
        //write your code here
        return null;
    }

    public boolean find(int element){
        //write your code here
        return false;
    }

    public void reverseList(){
        //write your code here
    }

    public void sort(){
        //write your code here
    }

    public int sum(){
        //write your code here
        return -1;
    }

    public void rotateKTimes(int k, String direction){
        //write your code here
    }

    //==========================Tester Code==========================//

    public static void main(String[] args) {
        
        //Task-2.1, 2.2 -- Constructor & showList
        System.out.println("//=======Task 2.1, 2.2 -- Constructor & showList=======//");
        int[] a = {10, 20, 30, 40, 50, 60};
        LinkedList l1 = new LinkedList(a);
        l1.showList(); //Should print: 10->20->30->40->50->60

        //Task-2.3 -- isEmpty
        System.out.println("//========Task 2.3 -- isEmpty========//");
        boolean isListEmpty = l1.isEmpty();
        System.out.println(isListEmpty); //Should print: false
        int[] b = null;
        LinkedList l2 = new LinkedList(b);
        isListEmpty = l2.isEmpty();
        System.out.println(isListEmpty); //Should print: true

        //Task-2.4 -- Clear
        System.out.println("//=======Task 2.4 -- Clear =======//");
        System.out.println("Before clearing Linked List");
        l1.showList(); //Should print: 10->20->30->40->50->60
        l1.clear();
        System.out.println("After clearing Linked List");
        l1.showList(); //Should print: Empty List

        //Task-2.5, 2.6 -- Insert
        System.out.println("//=======Task 2.5, 2.6 -- Insert=======//");
        int[] c = {10, 20, 30, 40, 50, 60, 70, 80, 90};
        LinkedList l3 = new LinkedList(c);
        l3.showList(); //Should print: 10->20->30->40->50->60->70->80->90
        l3.insert(100);
        l3.showList(); //Should print: 10->20->30->40->50->60->70->80->90->100
        l3.insert(0, 0);
        l3.showList(); //Should print: 0->10->20->30->40->50->60->70->80->90->100
        l3.insert(110, 5);
        l3.showList(); //Should print: 0->10->20->30->40->110->50->60->70->80->90->100
        l3.insert(120, 12);
        l3.showList(); //Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
        l3.insert(50); //Should print: Key 50 already exists

        //Task-2.7 -- Remove
        System.out.println("//=======Task 2.7 -- Remove=======//");
        l3.showList(); //Should print: 0->10->20->30->40->110->50->60->70->80->90->100->120
        l3.remove(0);
        l3.showList(); //Should print: 10->20->30->40->110->50->60->70->80->90->100->120
        l3.remove(110); 
        l3.showList(); //Should print: 10->20->30->40->50->60->70->80->90->100->120
        l3.remove(120);
        l3.showList(); //Should print: 10->20->30->40->50->60->70->80->90->100
        l3.remove(120); //Should print: Key 120 does not exist

        //Task-2.8 -- EvenList
        System.out.println("//=======Task 2.8 -- EvenList =======//");
        int[] d = {1, 2, 5, 3, 8};
        LinkedList l4 = new LinkedList(d);
        LinkedList l5 = l4.evenList();
        l5.showList(); //Should print: 2->8

        //Task-2.9 -- Find
        System.out.println("//=======Task 2.9 -- Find =======//");
        boolean found = l4.find(5);
        System.out.println(found); //Should print: true
        found = l4.find(4);
        System.out.println(found); //Should print: false

        //Task-2.10 -- Reverse List
        System.out.println("//=======Task 2.10 -- Reverse =======//");
        System.out.print("Before Reverse: ");
        l4.showList(); //Should print: 1->2->5->3->8
        l4.reverseList();
        System.out.print("After Reverse: ");
        l4.showList(); //Should print: 8->3->5->2->1

        //Task-2.11 -- Sort
        System.out.println("//=======Task 2.11 -- Sort =======//");
        System.out.println("Before Sort: ");
        l4.showList(); //Should print: 8->3->5->2->1
        l4.sort();
        System.out.println("After Sort: ");
        l4.showList(); //Should print: 1->2->3->5->8

        //Task-2.12 -- Sum of Elements
        System.out.println("//=======Task 2.12 -- Sum of Elements =======//");
        l4.showList(); //Should print: 1->2->3->5->8
        int total = l4.sum();
        System.out.println("Sum of Elements: " + total);

        //Task-2.13 -- Rotate
        System.out.println("//=======Task 2.13 -- Rotate =======/");
        l4.showList(); //Should print: 1->2->3->5->8
        l4.rotateKTimes(2, "left");
        l4.showList(); //Should print: 3->5->8->1->2
        l4.rotateKTimes(2, "right");
        l4.showList(); //Should print: 1->2->3->5->8
    }

}