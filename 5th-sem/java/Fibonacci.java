import java.util.*; 
class Fibonacci
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int a[] =  new int[n];
		a[0] = 0;
		a[1] = 1;
		System.out.println("0");
		System.out.println("1");
		for(int i = 2; i < n; i++)
		{
			a[i] = a[i-1] + a[i-2];
			System.out.println(a[i]);
		}
	}
}