import java.util.*; 
class CheckPrime
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		boolean flag = true;
		for (int i = 2; i * i <= n; i++)
		{
			if( n % i == 0)
			{
				flag = false;
				break;
			}
		}
		if (flag)
		{
			System.out.println("Prime");
		}
		else
		{
			System.out.println("Not Prime");
		}
	}
}