import java.util.*; 
class CheckNumberPallindrome
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		
		// reverse the number
		int temp = a;
		int b = 0;
		while(temp != 0)
		{
			b = b * 10 + (temp % 10);
			temp = temp / 10;
		}
		if(a == b)
			System.out.println("yes");
		else
			System.out.println("no");
	}
}