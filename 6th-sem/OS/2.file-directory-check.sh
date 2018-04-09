check_file_folder() {
	if [ -e $filename ] ; then
		if [ -d $filename ] ; then
			echo "$filename is a directory"
		elif [-f $filename] ; then
			echo "$filename is a regular file"
		fi
	else
		echo "$filename is neither a directory nor a regular file"
	fi
}

read -p 'Enter the absolute path of the item to be checked: ' filename
echo `check_file_folder $filename`