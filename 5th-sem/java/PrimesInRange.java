 class PrimesInRange
{
	public static void main(String[] args)
	{	
		boolean sieve[] = new boolean[301];	
		for(int i = 1; i <= 300; i++)
		{
			sieve[i] = true;
		}
		
		for(int i = 2; i <= 300; i++)
		{
			if(sieve[i] == true)
			{
				for(int j = 2 * i; j <= 300; j = j + i)
				{
					sieve[j] = false;
				}
			}
		}
		
		for(int i = 200; i <= 300; i++)
		{
			if(sieve[i] == true)
			{
				System.out.println(i);
			}
		}
		
	}
}