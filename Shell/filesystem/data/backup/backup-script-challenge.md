3.  If you run the command:

    ~~~
    history | tail -5 > recent.sh
    ~~~

    the last command in the file is the `history` command itself, i.e.,
    the shell has added `history` to the command log before actually
    running it. In fact, the shell *always* adds commands to the log
    before running them. Why do you think it does this?

4.  Joel's `data` directory contains three files: `fructose.dat`,
    `glucose.dat`, and `sucrose.dat`. Explain what a script called
    `example.sh` would do when run as `bash example.sh *.dat` if it
    contained the following lines:

<table>
  <tr>
    <td valign="top">1.</td>
    <td valign="top">
<pre>
echo *.*
</pre>
    </td>
  </tr>
  <tr>
    <td valign="top">2.</td>
    <td valign="top">
<pre>
for filename in $1 $2 $3
do
    cat $filename
done
</pre>
    </td>
  </tr>
  <tr>
    <td valign="top">3.</td>
    <td valign="top">
<pre>
echo $*.dat
</pre>
    </td>
  </tr>
</table>
