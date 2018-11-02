
public class JavaBST {
	
	Node root;

	private class Node{
		int val;
		Node left, right;
		
		public Node(int v, Node l, Node r){
			val = v; 
			left = l;
			right = r;
		}
	}
	
	private boolean isEmpty(){
		return (root == null);
	}
	
	public void insert(int v){
		if(isEmpty()){
			root = new Node(v, null, null);
			System.out.println("Inserted root " + v);
		}
		else{
			Node probe = root;
			while(probe != null){
				System.out.print(v + " - Looking at " + probe.val + "...");
				if(v < probe.val){
					System.out.println(" Went left. ");
					if(probe.left == null){
						probe.left = new Node(v, null, null);
						System.out.println("Inserted!");
						return;
					}
					else{
						probe = probe.left;
					}
				}
				else if(v > probe.val){
					System.out.println(" Went right. ");
					if(probe.right == null){
						probe.right = new Node(v, null, null);
						System.out.println("Inserted!");
						return;
					}
					else{
						probe = probe.right;
					}
				}
				else{
					//v already in bst. 
					System.out.println("\n" + v + " already in BST");
					return;
				}
			}
			
		}
	}
	
	public boolean search(int v){
		if(isEmpty()){
			return false;
		}
		else{
			Node probe = root;
			while(probe != null){
				if (v < probe.val){
					probe = probe.left;
				}
				else if (v > probe.val){
					probe = probe.right;
				}
				else{
					return true;
				}
			}
			return false;
		}
		
		
	}
	
	public void rotate(){
		
		
	}
	
	public void delete(){
		
		
	}
}
