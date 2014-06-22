digbit
======

Automatic domain generation for BitSquatting

BitSquatting is not new but it’s relatively new. This type of attack relies on a random bit that switches from 0 to 1 or from 1 to 0 inside a RAM. Because of this even though you try to access domain like cnn.com, in fact your computer is requesting ann.com. It’s rare but it happens. It can be caused by a cosmic radiation or overheated memory modules. If You would like to learn more I can recommend [Artem’s](http://dinaburg.org/bitsquatting.html) page.

To make it easier to find a domain that is in a single bit-shift distance (as in Hamming distance) I’ve created a script that is generating all the possibilities.

For example lets search for domains (bit-wise) close to cnn.com. The script output will be:

> snn.com knn.com gnn.com ann.com bnn.com c.n.com cfn.com cjn.com cln.com con.com cnf.com cnj.com cnl.com cno.com cnn.som cnn.kom cnn.gom cnn.aom cnn.bom cnn.cgm cnn.ckm cnn.cmm cnn.cnm cnn.coe cnn.coi cnn.coo cnn.col

To make it easier to check if particular domain is already registered or not, I’ve made a wrapper script that will execute the python script and for each generated domain it will execute command:
	
> `nslookup domain | grep "NXDOMAIN"`

The wrapper script is executed with a single argument that is a domain name. Sample output for twitter.com:

> 4witter.com
dwitter.com  < available
pwitter.com
vwitter.com
uwitter.com
t7itter.com  < available
tgitter.com
tsitter.com
tuitter.com
tvitter.com
twytter.com
twatter.com
twmtter.com
twktter.com
twhtter.com  < available
twi4ter.com
twidter.com  < available
twipter.com  < available
twivter.com  < available
twiuter.com
twit4er.com
twitder.com
twitper.com
twitver.com  < available
twituer.com
twittur.com
twittmr.com  < available
twittar.com
twittgr.com
twittdr.com
twitte2.com  < available
twitteb.com
twittez.com  < available
twittev.com
twittep.com  < available
twittes.com
twitter.som  < available
twitter.kom  < available
twitter.gom  < available
twitter.aom  < available
twitter.bom  < available
twitter.cgm  < available
twitter.ckm  < available
twitter.cmm  < available
twitter.cnm  < available
twitter.coe  < available
twitter.coi  < available
twitter.coo  < available
twitter.col  < available



Some of those reported as available are obviously false-positive since TLDs like kom don’t really exist. I did not removed them because new TLDs are added from time to time and you might as well have a custom domain setup within your LAN.
