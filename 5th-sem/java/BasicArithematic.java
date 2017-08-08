import java.util.*;  
class BasicArithematic
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		System.out.println("a = " + a + " b = " + b);
		System.out.println("a + b = "+ (a + b));
		System.out.println("a - b = "+ (a - b));
		System.out.println("a * b = " + (a * b));
		System.out.println("a / b = " + (a / b));
	}
}