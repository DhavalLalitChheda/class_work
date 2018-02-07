class Test{
	public static void main(String args[]){
		Double a = new Double("0.05");
		Double c = new Double("3");
		Double b = new Double("0.15");
		int i = Double.compare(a * 3, b);
		if(i == 1){
			System.out.println("B is greater than A");
		
		} else if(i < 0){
			System.out.println("Wrong Answer");
		} else{
			System.out.println("Hi");
		}
	}
}