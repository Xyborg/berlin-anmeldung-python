# Berlin Anmeldung Appointments (Python)
This Python script will automatically check for free Anmeldung appointments in Berlin, and find them for you.

The way I created it, it will list free appointments for all the districts, as most of the time is hard to find a free slot. It's up to you then to decide if the Bürgeramt (citizens' office) is too far for you or not.

If you need more information regarding how the Anmeldung works, check the page [The Anmeldung - How to register an address in Berlin](https://allaboutberlin.com/guides/anmeldung-in-english-berlin)

## Usage
    python3 anmeldme.py

### Output

```
xyborg@local anmeldung % python3 anmeldme.py
Getting ready to parse content...

Trying page 1:  https://service.berlin.de/terminvereinbarung/termin/day/
Trying page 2:  https://service.berlin.de/terminvereinbarung/termin/day/1636210348/
15:52:30 > I couldn't find any available termin :(

Trying page 1:  https://service.berlin.de/terminvereinbarung/termin/day/
Trying page 2:  https://service.berlin.de/terminvereinbarung/termin/day/1636210411/
15:53:33 > I couldn't find any available termin :(

Trying page 1:  https://service.berlin.de/terminvereinbarung/termin/day/
Trying page 2:  https://service.berlin.de/terminvereinbarung/termin/day/1636212614/

#######################################################

I found  6  avialable appointments!:

#######################################################

10-11-2021: https://service.berlin.de/terminvereinbarung/termin/time/1636498800/
17-11-2021: https://service.berlin.de/terminvereinbarung/termin/time/1637103600/
24-11-2021: https://service.berlin.de/terminvereinbarung/termin/time/1637708400/
01-12-2021: https://service.berlin.de/terminvereinbarung/termin/time/1638313200/
08-12-2021: https://service.berlin.de/terminvereinbarung/termin/time/1638918000/
15-12-2021: https://service.berlin.de/terminvereinbarung/termin/time/1639522800/

Hurry! Copy the links and book your termin now.
```
