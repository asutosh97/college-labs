function mul()
{
    echo $(( $1 * $2 ))
}
val1=10
val2=20
echo `mul $val1 $val2`