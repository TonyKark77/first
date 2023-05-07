<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6897bb;}
.s3 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">time</span>
<span class="s1">password = </span><span class="s2">0</span>
<span class="s1">name = </span><span class="s2">0</span>
<span class="s1">date = </span><span class="s2">0</span>
<span class="s1">pass_to_site = </span><span class="s0">False</span>
<span class="s1">id = </span><span class="s2">0</span>
<span class="s1">tries = </span><span class="s2">3</span>
<span class="s1">counter = </span><span class="s2">0</span>
<span class="s1">tr = </span><span class="s0">True</span>
<span class="s0">while </span><span class="s1">tr:</span>
    <span class="s0">if </span><span class="s1">counter == </span><span class="s2">3</span><span class="s1">:</span>
        <span class="s0">break</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s0">pass</span>
    <span class="s1">a = input(</span><span class="s3">&quot;login or register?&quot;</span><span class="s1">)</span>
    <span class="s0">if </span><span class="s1">a == </span><span class="s3">&quot;login&quot;</span><span class="s1">:</span>
        <span class="s0">while </span><span class="s1">tries :</span>
            <span class="s1">userlog = input(</span><span class="s3">&quot;enter your name &quot;</span><span class="s1">)</span>
            <span class="s0">if </span><span class="s1">userlog == id:</span>
                <span class="s1">pass_to_site = </span><span class="s0">True</span>
                <span class="s1">tries = </span><span class="s2">0</span>
            <span class="s0">else</span><span class="s1">:</span>
                <span class="s1">tries -= </span><span class="s2">1</span>
                <span class="s0">if </span><span class="s1">tries == </span><span class="s2">0</span><span class="s1">:</span>
                    <span class="s1">time.sleep((counter +</span><span class="s2">1</span><span class="s1">)*</span><span class="s2">4</span><span class="s1">)</span>
                    <span class="s1">print((counter +</span><span class="s2">1</span><span class="s1">)*</span><span class="s2">4</span><span class="s1">)</span>
                    <span class="s1">counter += </span><span class="s2">1</span>
                    <span class="s0">if </span><span class="s1">counter == </span><span class="s2">3</span><span class="s1">:</span>
                        <span class="s1">print(</span><span class="s3">&quot;you are banned&quot;</span><span class="s1">)</span>
                        <span class="s0">break</span>
                    <span class="s1">tries = </span><span class="s2">3</span>
    <span class="s0">elif </span><span class="s1">a == </span><span class="s3">&quot;register&quot;</span><span class="s1">:</span>
        <span class="s1">password = input(</span><span class="s3">&quot;enter your password: &quot;</span><span class="s1">)</span>
        <span class="s1">name = input(</span><span class="s3">&quot;enter your name: &quot;</span><span class="s1">)</span>
        <span class="s1">date = input(</span><span class="s3">&quot;enter your date of birth: &quot;</span><span class="s1">)</span>
        <span class="s1">pass_to_site = </span><span class="s0">True</span>
        <span class="s1">save = input(</span><span class="s3">&quot;wanna save your id? y/n?&quot;</span><span class="s1">)</span>
        <span class="s0">if </span><span class="s1">save == </span><span class="s3">&quot;y&quot;</span><span class="s1">:</span>
            <span class="s1">id = name</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s0">pass</span>
    <span class="s0">else</span><span class="s1">:</span>
            <span class="s0">pass</span>
    <span class="s0">if </span><span class="s1">pass_to_site == </span><span class="s0">True</span><span class="s1">:</span>
        <span class="s1">print(</span><span class="s3">&quot;Welcome to your page!&quot;</span><span class="s1">)</span>
        <span class="s1">almfin = int(input(</span><span class="s3">&quot;wanna exit and start again or just exit again? 1:2&quot;</span><span class="s1">))</span>
        <span class="s0">if </span><span class="s1">almfin == </span><span class="s2">1</span><span class="s1">:</span>
            <span class="s1">tr = </span><span class="s0">True</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s0">pass</span>
</pre>
</body>
</html>